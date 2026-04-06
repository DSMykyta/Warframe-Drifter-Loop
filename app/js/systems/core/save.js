// ═══════════════════════════════════════════════════
// СИСТЕМА ЗБЕРЕЖЕННЯ
// ═══════════════════════════════════════════════════
//
// Механізм як в Ren'Py (loadsave.py):
// Серіалізує весь gameState автоматично — всі зареєстровані системи.

var SAVE_PREFIX = "drifter_";
var MAX_SLOTS = 20;

function save(slot, description) {
  var data = serializeState();
  data._meta = {
    _save_name: description || "",
    _ctime: Date.now(),
    _game_day: gameState.time.day,
    _game_time: gameState.time.minutes,
    _game_location: gameState.location.current,
    _game_hex_rep: gameState.rank ? gameState.rank.hex_rep : 0,
    _game_money: gameState.money ? gameState.money.amount : 0
  };
  localStorage.setItem(SAVE_PREFIX + slot, JSON.stringify(data));
  return true;
}

function load(slot) {
  var raw = localStorage.getItem(SAVE_PREFIX + slot);
  if (!raw) return false;
  var data = JSON.parse(raw);
  delete data._meta;
  deserializeState(data);
  return true;
}

function autoSave() {
  save("auto", "День " + gameState.time.day);
}

function deleteSave(slot) {
  localStorage.removeItem(SAVE_PREFIX + slot);
}

function listSaves() {
  var saves = [];
  var autoRaw = localStorage.getItem(SAVE_PREFIX + "auto");
  if (autoRaw) {
    saves.push({ slot: "auto", meta: JSON.parse(autoRaw)._meta || {} });
  }
  for (var i = 1; i <= MAX_SLOTS; i++) {
    var raw = localStorage.getItem(SAVE_PREFIX + i);
    if (raw) {
      saves.push({ slot: i, meta: JSON.parse(raw)._meta || {} });
    }
  }
  return saves;
}

function hasSaves() {
  if (localStorage.getItem(SAVE_PREFIX + "auto")) return true;
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
