// ═══════════════════════════════════════════════════
// СИСТЕМА ЗБЕРЕЖЕННЯ
// ═══════════════════════════════════════════════════
//
// Механізм як в Ren'Py (loadsave.py):
// Серіалізує весь gameState автоматично — всі зареєстровані системи.

var SAVE_PREFIX = "drifter_";
var MAX_SLOTS = 20;
var SAVE_VERSION = 2;

function save(slot, description) {
  // Синхронізувати діалоговий стан перед збереженням
  if (typeof _syncDialogueToState === "function") _syncDialogueToState();
  var data = serializeState();
  data._meta = {
    _save_name: description || "",
    _ctime: Date.now(),
    _version: SAVE_VERSION,
    _game_day: gameState.time.day,
    _game_time: gameState.time.minutes,
    _game_location: gameState.location.current,
    _game_hex_rep: gameState.rank ? gameState.rank.hex_rep : 0,
    _game_money: gameState.money ? gameState.money.amount : 0
  };
  try {
    localStorage.setItem(SAVE_PREFIX + slot, JSON.stringify(data));
  } catch(e) {
    if (typeof showToast === "function") showToast("Сховище переповнене. Видаліть старі збереження.", "error");
    return false;
  }
  return true;
}

function load(slot) {
  var raw = localStorage.getItem(SAVE_PREFIX + slot);
  if (!raw) return false;
  try {
    var data = JSON.parse(raw);
  } catch(e) {
    console.error("[save] Corrupted save in slot " + slot, e);
    if (typeof showToast === "function") showToast("Збереження пошкоджене", "error");
    deleteSave(slot);
    return false;
  }
  var meta = data._meta || {};
  delete data._meta;
  // Міграція старих saves
  _migrateSave(data, meta._version || 0);
  deserializeState(data);
  // Очистити бекло́г при завантаженні (нова сесія)
  if (typeof _textHistory !== "undefined") _textHistory = [];
  // Відновити діалоговий стан після завантаження
  if (typeof _syncStateToDialogue === "function") _syncStateToDialogue();
  return true;
}

// Міграція saves між версіями
function _migrateSave(data, fromVersion) {
  if (fromVersion < 1) {
    // v0 → v1: додати dialogue_engine якщо відсутній
    if (!data.dialogue_engine) {
      data.dialogue_engine = {
        scriptName: null, pc: 0, callStack: [],
        sceneSprites: {}, showOrder: 0,
        currentMusic: null, currentBg: null,
        afterIntro: false, afterExplore: false,
        waitingForPager: false, waitPagerLabels: null
      };
    }
  }
  if (fromVersion < 2) {
    // v1 → v2: конвертувати кириличні ключі персонажів в short ID
    var _nameMap = {
      "\u0410\u0440\u0442\u0443\u0440": "ar", "\u0415\u043b\u0435\u043e\u043d\u043e\u0440": "el",
      "\u041b\u0435\u0442\u0442\u0456": "lt", "\u0410\u043c\u0456\u0440": "am",
      "\u0410\u043e\u0456": "ao", "\u041a\u0432\u0456\u043d\u0441\u0456": "qu"
    };
    function _migrateKeys(obj) {
      if (!obj) return;
      for (var k in _nameMap) {
        if (obj[k] !== undefined) { obj[_nameMap[k]] = obj[k]; delete obj[k]; }
      }
    }
    function _migrateArray(arr) {
      if (!arr) return;
      for (var i = 0; i < arr.length; i++) {
        if (_nameMap[arr[i]]) arr[i] = _nameMap[arr[i]];
      }
    }
    if (data.chemistry) { _migrateKeys(data.chemistry.values); _migrateKeys(data.chemistry.gainedToday); }
    if (data.dispatcher) {
      _migrateKeys(data.dispatcher.daily_deck);
      _migrateArray(data.dispatcher.talked_today);
      _migrateKeys(data.dispatcher.stub_pools);
      _migrateKeys(data.dispatcher.tags_used_today);
    }
    if (data.decay) _migrateKeys(data.decay.days_since_interaction);
    if (data.gifts) _migrateArray(data.gifts.gifted_today);
    if (data.missions) _migrateKeys(data.missions.missions_today_with);
    if (data.injuries) {
      _migrateKeys(data.injuries.stacks);
      _migrateKeys(data.injuries.day_gained);
      _migrateKeys(data.injuries.recovery_until);
    }
    if (data.romance && _nameMap[data.romance.dating]) {
      data.romance.dating = _nameMap[data.romance.dating];
    }
    if (data.promises && data.promises.list) {
      for (var _pi = 0; _pi < data.promises.list.length; _pi++) {
        var _pw = data.promises.list[_pi].who;
        if (_nameMap[_pw]) data.promises.list[_pi].who = _nameMap[_pw];
      }
    }
  }
}

function autoSave() {
  save("auto", "День " + gameState.time.day);
}

function quickSave() {
  var desc = "День " + gameState.time.day + " / " + (typeof getTimeString === "function" ? getTimeString() : "");
  if (save("quick", desc)) {
    if (typeof showToast === "function") showToast("Швидке збереження", "save");
  }
}

function quickLoad() {
  var raw = localStorage.getItem(SAVE_PREFIX + "quick");
  if (!raw) {
    if (typeof showToast === "function") showToast("Немає швидкого збереження", "error");
    return;
  }
  if (typeof confirmDialog === "function") {
    confirmDialog("Швидке завантаження? Незбережений прогрес буде втрачено.", function() {
      if (typeof _disableAutoMode === "function") _disableAutoMode();
      if (typeof _disableSkipToggle === "function") _disableSkipToggle();
      if (typeof _textHistory !== "undefined") _textHistory = [];
      if (load("quick")) {
        showScreen("game-screen");
        if (gameState.dialogue_engine && gameState.dialogue_engine.scriptName && currentScript) {
          showHUD(); updateHUD();
          if (typeof showPager === "function") showPager();
          execute(pc);
        } else {
          showLocation();
        }
      }
    });
  }
}

function getLatestSave() {
  var saves = listSaves();
  if (saves.length === 0) return null;
  var latest = saves[0];
  for (var i = 1; i < saves.length; i++) {
    if ((saves[i].meta._ctime || 0) > (latest.meta._ctime || 0)) {
      latest = saves[i];
    }
  }
  return latest;
}

// ═══ TOAST СПОВІЩЕННЯ ═══
function showToast(message, type) {
  var container = document.getElementById("toast-container");
  if (!container) return;
  var toast = document.createElement("div");
  toast.className = "toast" + (type ? " toast-" + type : "");
  toast.textContent = message;
  container.appendChild(toast);
  setTimeout(function() { if (toast.parentNode) toast.remove(); }, 3200);
}

function deleteSave(slot) {
  localStorage.removeItem(SAVE_PREFIX + slot);
}

function listSaves() {
  var saves = [];
  var slots = ["auto", "quick"];
  for (var j = 1; j <= MAX_SLOTS; j++) slots.push(j);
  for (var s = 0; s < slots.length; s++) {
    var raw = localStorage.getItem(SAVE_PREFIX + slots[s]);
    if (raw) {
      try {
        saves.push({ slot: slots[s], meta: JSON.parse(raw)._meta || {} });
      } catch(e) {
        console.warn("[save] Corrupted save in slot " + slots[s]);
      }
    }
  }
  return saves;
}

// Аліас для dialogue.js (if node.has_save)
function hasSaveData() { return hasSaves(); }

function hasSaves() {
  if (localStorage.getItem(SAVE_PREFIX + "auto")) return true;
  if (localStorage.getItem(SAVE_PREFIX + "quick")) return true;
  for (var i = 1; i <= MAX_SLOTS; i++) {
    if (localStorage.getItem(SAVE_PREFIX + i)) return true;
  }
  return false;
}

function findFreeSlot() {
  for (var i = 1; i <= MAX_SLOTS; i++) {
    if (!localStorage.getItem(SAVE_PREFIX + i)) return i;
  }
  return null;
}
