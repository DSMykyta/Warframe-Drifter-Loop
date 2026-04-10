// ═══════════════════════════════════════════════════
// ДІАЛОГОВИЙ РУШІЙ — ЯДРО
// ═══════════════════════════════════════════════════
//
// Виконує масив команд по черзі. Гравець клікає — наступна.
// Спрайти  → sprites.js
// Аудіо    → audio.js
// Переходи → transitions.js

var SCRIPTS = {};
var currentScript = null;
var pc = 0;
var callStack = [];
var typing = false;
var _typeTimer = null;
var _fullText = "";
var _waitingForPager = false;
var _waitPagerLabels = null;
var _inputLocked = false;
var _executeDepth = 0;
var _MAX_EXECUTE_DEPTH = 500;
var TEXT_SPEED_MS = 22;

// ═══ СТАН ДІАЛОГУ ДЛЯ SAVE/LOAD ═══

registerState("dialogue_engine", {
  scriptName: null,
  pc: 0,
  callStack: [],
  sceneSprites: {},
  showOrder: 0,
  currentMusic: null,
  currentBg: null,
  afterIntro: false,
  afterExplore: false,
  waitingForPager: false,
  waitPagerLabels: null
});

// Зворотній пошук ключа SCRIPTS за масивом
function _findScriptName(scriptRef) {
  if (!scriptRef) return null;
  for (var key in SCRIPTS) {
    if (SCRIPTS[key] === scriptRef) return key;
  }
  return null;
}

// Синхронізувати глобальні змінні → gameState (перед save)
function _syncDialogueToState() {
  var ds = gameState.dialogue_engine;
  ds.scriptName = _findScriptName(currentScript);
  ds.pc = pc;
  // callStack: конвертувати посилання на масиви в імена
  ds.callStack = callStack.map(function(entry) {
    return { scriptName: _findScriptName(entry.script), pc: entry.pc };
  });
  // sceneSprites: зберегти тільки серіалізовані дані
  ds.sceneSprites = {};
  for (var name in _sceneSprites) {
    var s = _sceneSprites[name];
    ds.sceneSprites[name] = {
      short: s.charData ? s.charData.short : null,
      zorder: s.zorder,
      order: s.order
    };
  }
  ds.showOrder = _showOrder;
  ds.currentMusic = _currentMusic;
  // Зберегти поточний фон
  var bgEl = document.querySelector(".game-bg");
  if (bgEl) {
    var bgStyle = bgEl.style.background;
    ds.currentBg = bgStyle || null;
  }
  ds.afterIntro = _afterIntro;
  ds.afterExplore = _afterExplore;
  ds.waitingForPager = _waitingForPager;
  ds.waitPagerLabels = _waitPagerLabels;
}

// Відновити глобальні змінні з gameState (після load)
function _syncStateToDialogue() {
  var ds = gameState.dialogue_engine;
  // Відновити скрипт
  if (ds.scriptName && SCRIPTS[ds.scriptName]) {
    currentScript = SCRIPTS[ds.scriptName];
    pc = ds.pc || 0;
  } else {
    currentScript = null;
    pc = 0;
  }
  // Відновити callStack
  callStack = (ds.callStack || []).map(function(entry) {
    return { script: SCRIPTS[entry.scriptName] || null, pc: entry.pc };
  }).filter(function(entry) { return entry.script !== null; });
  // Відновити спрайти
  _sceneSprites = {};
  _showOrder = ds.showOrder || 0;
  for (var name in (ds.sceneSprites || {})) {
    var saved = ds.sceneSprites[name];
    var charData = _resolveChar(saved.short);
    if (charData) {
      _sceneSprites[name] = {
        charData: charData,
        zorder: saved.zorder || 0,
        order: saved.order || 0,
        position: 50
      };
    }
  }
  if (Object.keys(_sceneSprites).length > 0) {
    renderSceneSprites(null);
  }
  // Відновити фон
  if (ds.currentBg) {
    var bgEl = document.querySelector(".game-bg");
    if (bgEl) bgEl.style.background = ds.currentBg;
  }
  // Відновити музику
  if (ds.currentMusic && typeof playAudio === "function") {
    playAudio("music", ds.currentMusic, true, 500);
  }
  // Відновити flow flags
  _afterIntro = ds.afterIntro || false;
  _afterExplore = ds.afterExplore || false;
  _waitingForPager = ds.waitingForPager || false;
  _waitPagerLabels = ds.waitPagerLabels || null;
}

// Скинути діалоговий стан (при поверненні до локації)
function _clearDialogueState() {
  gameState.dialogue_engine.scriptName = null;
  gameState.dialogue_engine.pc = 0;
  gameState.dialogue_engine.callStack = [];
  gameState.dialogue_engine.sceneSprites = {};
  gameState.dialogue_engine.showOrder = 0;
  gameState.dialogue_engine.afterIntro = false;
  gameState.dialogue_engine.afterExplore = false;
  gameState.dialogue_engine.waitingForPager = false;
  gameState.dialogue_engine.waitPagerLabels = null;
}


// ═══ РЕЄСТРАЦІЯ ТА ЗАПУСК ═══

function registerScript(name, nodes) {
  if (SCRIPTS[name]) {
    console.warn("[registerScript] Overwriting existing script: " + name);
  }
  SCRIPTS[name] = nodes;
  nodes._labels = {};
  nodes.forEach(function(node, i) {
    if (node.type === "label") nodes._labels[node.id] = i;
  });
}

function runScript(name) {
  if (!SCRIPTS[name]) return;
  currentScript = SCRIPTS[name];
  pc = 0;
  callStack = [];
  _sceneSprites = {};
  execute(pc);
}


// ═══ ДРУК ПО БУКВАХ ═══

function typewrite(text, el) {
  clearInterval(_typeTimer);
  _fullText = text;
  typing = true;
  _hideContinueIndicator();
  var i = 0;
  el.textContent = "";
  _typeTimer = setInterval(function() {
    i++;
    if (i >= text.length) {
      el.textContent = text;
      typing = false;
      clearInterval(_typeTimer);
      _showContinueIndicator();
    } else {
      el.textContent = text.slice(0, i);
    }
  }, TEXT_SPEED_MS);
}

function skipType() {
  clearInterval(_typeTimer);
  var el = document.querySelector(".say-text");
  if (el) el.textContent = _fullText;
  typing = false;
  _showContinueIndicator();
}

function _showContinueIndicator() {
  var ind = document.querySelector(".say-continue");
  if (ind) ind.classList.add("visible");
}

function _hideContinueIndicator() {
  var ind = document.querySelector(".say-continue");
  if (ind) ind.classList.remove("visible");
}


// ═══ ВИКОНАННЯ КОМАНД ═══

function execute(index) {
  _executeDepth++;
  if (_executeDepth > _MAX_EXECUTE_DEPTH) {
    console.error("[dialogue] Max recursion depth reached at index " + index + ". Possible infinite loop.");
    _executeDepth = 0;
    _inputLocked = false;
    currentScript = null;
    onSceneEnd();
    return;
  }
  if (!currentScript) return;
  if (index >= currentScript.length) {
    if (callStack.length > 0) {
      var ret = callStack.pop();
      currentScript = ret.script;
      pc = ret.pc;
      execute(pc);
      return;
    }
    return;
  }

  var node = currentScript[index];

  try {
  switch (node.type) {

    // ─── show: показати спрайт ───
    case "show":
      showSceneSprite(node.who, node.at || "center", node.zorder || 0);
      pc = index + 1; execute(pc); break;

    // ─── hide: сховати спрайт ───
    case "hide":
      hideSceneSprite(node.who);
      pc = index + 1; execute(pc); break;

    // ─── scene: змінити фон + очистити спрайти ───
    case "scene":
      clearSceneSprites();
      var bgS = document.querySelector(".game-bg");
      if (bgS) {
        if (node.bg === "bg_black.png" || node.bg === "black") {
          bgS.style.background = "#000";
        } else {
          bgS.style.background = "url('assets/backgrounds/" + node.bg + "') center/cover no-repeat";
        }
      }
      if (node.text) {
        var title = document.querySelector(".scene-title");
        if (title) {
          _inputLocked = true;
          title.querySelector("span").textContent = node.text;
          title.classList.add("visible");
          setTimeout(function() {
            title.classList.remove("visible");
            setTimeout(function() { _inputLocked = false; pc = index + 1; execute(pc); }, 600);
          }, 2000);
        }
      } else {
        pc = index + 1; execute(pc);
      }
      break;

    // ─── say: діалог ───
    case "say":
      // Прелоадити наступні ассети (look-ahead)
      if (typeof preloadScriptAssets === "function") {
        preloadScriptAssets(currentScript, index + 1);
      }
      // Трекінг прочитаних нод
      if (typeof markSeen === "function") {
        markSeen(_findScriptName(currentScript), index);
        if (typeof _scheduleSaveSeen === "function") _scheduleSaveSeen();
      }
      var nameEl = document.querySelector(".say-name");
      var textEl = document.querySelector(".say-text");
      var dlg = document.querySelector(".dialogue");
      if (dlg) dlg.style.display = "flex";

      if (node.who === "mc") {
        // Гравець — без плашки з іменем
        highlightSpeaker(null);
        nameEl.style.visibility = "hidden";
        nameEl.removeAttribute("data-char");
        textEl.className = "say-text";
      } else if (node.who) {
        ensureSpeakerVisible(node.who);
        nameEl.style.visibility = "visible";
        nameEl.textContent = charName(node.who);
        // Встановити data-char для кольору імені
        var _charShort = CAST[node.who] ? node.who : null;
        if (!_charShort) {
          for (var _cs in CAST) { if (CAST[_cs].name === node.who) { _charShort = _cs; break; } }
        }
        nameEl.setAttribute("data-char", _charShort || "");
        textEl.className = "say-text";
      } else {
        highlightSpeaker(null);
        nameEl.style.visibility = "hidden";
        nameEl.removeAttribute("data-char");
        textEl.className = "say-text narrator";
      }
      typewrite(node.text, textEl);
      if (typeof pushToHistory === "function") pushToHistory(node.who, node.text, "say");
      if (node.flag) setFlag(node.flag);
      if (node.chemistry) {
        for (var n in node.chemistry) addChemistry(n, node.chemistry[n]);
      }
      if (node.time) advanceTime(node.time);
      // Авто-режим: запланувати advance після завершення typewrite
      if (typeof _autoMode !== "undefined" && _autoMode && typeof _tryAutoAdvance === "function") {
        _tryAutoAdvance();
      }
      break;

    // ─── menu: вибір ───
    case "menu":
      _hideContinueIndicator();
      var dlg2 = document.querySelector(".dialogue");
      if (dlg2) dlg2.style.display = "none";
      var choices = document.querySelector(".choices");
      var list = document.querySelector(".choices-list");
      list.innerHTML = "";
      node.choices.forEach(function(ch) {
        var isLocked = false;
        if (ch.condition) {
          if (ch.condition.flag && !getFlag(ch.condition.flag)) isLocked = true;
          if (ch.condition.flag_false && getFlag(ch.condition.flag_false)) isLocked = true;
        }
        // Показати заблоковані вибори (сірими), замість ховання
        var btn = document.createElement("button");
        var isSeen = ch.flag && getFlag(ch.flag);
        btn.className = "choice-btn" + (ch.bonus ? " bonus" : "") +
          (isSeen ? " seen-choice" : "") +
          (isLocked ? " locked-choice" : "");
        btn.textContent = isLocked ? ch.text : ch.text;
        if (isLocked) {
          list.appendChild(btn);
          return; // Не додаємо click handler
        }
        btn.addEventListener("click", function(e) {
          e.stopPropagation();
          if (typeof pushToHistory === "function") pushToHistory(null, "\u25b8 " + ch.text, "choice");
          if (ch.flag) setFlag(ch.flag);
          if (ch.chemistry) {
            for (var cn in ch.chemistry) addChemistry(cn, ch.chemistry[cn]);
          }
          choices.style.display = "none";
          if (ch.label) {
            var t = currentScript._labels[ch.label];
            if (t !== undefined) {
              pc = t + 1; execute(pc);
            } else if (SCRIPTS[ch.label]) {
              currentScript = SCRIPTS[ch.label];
              pc = 0;
              execute(pc);
            } else {
              pc++; execute(pc);
            }
          } else {
            pc++; execute(pc);
          }
          // Відновити auto-advance після вибору
          if (typeof _autoMode !== "undefined" && _autoMode && typeof _tryAutoAdvance === "function") {
            setTimeout(_tryAutoAdvance, 200);
          }
        });
        list.appendChild(btn);
      });
      choices.style.display = "flex";
      break;

    // ─── flow control ───
    case "label":
      pc = index + 1; execute(pc); break;

    case "jump":
      var jt = currentScript._labels[node.to];
      if (jt !== undefined) {
        pc = jt + 1; execute(pc);
      } else if (SCRIPTS[node.to]) {
        currentScript = SCRIPTS[node.to];
        pc = 0;
        execute(pc);
      }
      break;

    case "call":
      callStack.push({ script: currentScript, pc: index + 1 });
      if (node.script) {
        currentScript = SCRIPTS[node.script];
        pc = 0;
        if (node.to) {
          var ct = currentScript._labels[node.to];
          if (ct !== undefined) pc = ct + 1;
        }
      } else {
        var lt2 = currentScript._labels[node.to];
        if (lt2 !== undefined) pc = lt2 + 1;
      }
      execute(pc);
      break;

    case "return":
      if (callStack.length > 0) {
        var r = callStack.pop();
        currentScript = r.script;
        pc = r.pc;
        execute(pc);
      }
      break;

    // ─── with: transition ───
    case "with":
      applyTransition(node.transition || "dissolve", node.duration || 500, function() {
        pc = index + 1; execute(pc);
      });
      break;

    // ─── play/stop: audio ───
    case "play":
      playAudio(node.channel || "sound", node.file, node.loop, node.fadein);
      pc = index + 1; execute(pc); break;

    case "stop":
      stopAudio(node.channel || "music", node.fadeout);
      pc = index + 1; execute(pc); break;

    // ─── telepathy/think ───
    case "telepathy":
      if (typeof markSeen === "function") { markSeen(_findScriptName(currentScript), index); if (typeof _scheduleSaveSeen === "function") _scheduleSaveSeen(); }
      var dlg3 = document.querySelector(".dialogue");
      if (dlg3) dlg3.style.display = "none";
      var tel = document.querySelector(".telepathy-overlay");
      tel.innerHTML = "";
      tel.className = "telepathy-overlay shaking";
      for (var ti = 0; ti < node.text.length; ti++) {
        var span = document.createElement("span");
        span.textContent = node.text[ti];
        span.className = "telepathy-char";
        span.style.animationDelay = (Math.random() * 2).toFixed(2) + "s";
        tel.appendChild(span);
      }
      tel.style.display = "flex";
      if (typeof pushToHistory === "function") pushToHistory(node.who || "Елеонор", node.text, "telepathy");
      break;

    case "think":
      if (typeof markSeen === "function") { markSeen(_findScriptName(currentScript), index); if (typeof _scheduleSaveSeen === "function") _scheduleSaveSeen(); }
      var dlg4 = document.querySelector(".dialogue");
      if (dlg4) dlg4.style.display = "none";
      var think = document.querySelector(".telepathy-overlay");
      think.className = "telepathy-overlay thinking";
      think.textContent = "";
      think.style.display = "flex";
      typewrite(node.text, think);
      if (typeof pushToHistory === "function") pushToHistory(null, node.text, "think");
      break;

    // ─── game state ───
    case "set_flag":
      setFlag(node.flag, node.value !== undefined ? node.value : true);
      pc = index + 1; execute(pc); break;

    case "if":
      var cond = false;
      if (node.flag) cond = getFlag(node.flag);
      if (node.flag_false) cond = !getFlag(node.flag_false);
      if (node.loop_restart) cond = isLoopRestart();
      if (node.first_loop) cond = !isLoopRestart();
      if (node.has_save) cond = typeof hasSaveData === "function" && hasSaveData();
      if (node.chemistry_min) {
        cond = (gameState.chemistry.values[node.chemistry_min[0]] || 0) >= node.chemistry_min[1];
      }
      if (cond && node.jump) {
        var it = currentScript._labels[node.jump];
        if (it !== undefined) { pc = it + 1; execute(pc); break; }
      }
      if (!cond && node.else_jump) {
        var et = currentScript._labels[node.else_jump];
        if (et !== undefined) { pc = et + 1; execute(pc); break; }
      }
      pc = index + 1; execute(pc); break;

    case "chemistry":
      if (node.values) {
        for (var cn2 in node.values) addChemistry(cn2, node.values[cn2]);
      } else if (node.who) {
        addChemistry(node.who, node.amount || 0);
      }
      pc = index + 1; execute(pc); break;

    case "time":
      advanceTime(node.minutes);
      pc = index + 1; execute(pc); break;

    case "pager":
      if (typeof sendPagerMessage === "function") {
        sendPagerMessage(node.who || "", node.text || "");
      }
      pc = index + 1; execute(pc); break;

    case "pager_request":
      if (typeof sendPagerRequest === "function") {
        sendPagerRequest(node.who || "", node.text || "", node.accept || null, node.decline || null);
      }
      pc = index + 1; execute(pc); break;

    case "wait_pager":
      // Пауза — чекаємо натискання кнопки пейджера
      _waitingForPager = true;
      _waitPagerLabels = {
        left: node.left || null,
        center: node.center || null,
        right: node.right || null
      };
      break;

    case "bg":
      var gbg = document.querySelector(".game-bg");
      if (gbg) {
        if (node.file === "bg_black.png" || node.file === "black") {
          gbg.style.background = "#000";
        } else {
          gbg.style.background = "url('assets/backgrounds/" + node.file + "') center/cover no-repeat";
        }
      }
      pc = index + 1; execute(pc); break;

    case "end":
      var nameE = document.querySelector(".say-name");
      var textE = document.querySelector(".say-text");
      var dlgE = document.querySelector(".dialogue");
      if (dlgE) dlgE.style.display = "flex";
      if (nameE) nameE.style.visibility = "hidden";
      if (textE) {
        textE.className = "say-text narrator";
        textE.textContent = node.text || "";
      }
      break;

    // ─── effect: екранні ефекти ───
    case "effect":
      if (typeof applyEffect === "function") {
        _inputLocked = true;
        applyEffect(node.name, node, function() {
          _inputLocked = false;
          pc = index + 1; execute(pc);
        });
      } else {
        pc = index + 1; execute(pc);
      }
      break;

    default:
      pc = index + 1; execute(pc);
  }
  } catch(e) {
    var scriptName = _findScriptName(currentScript) || "unknown";
    console.error("[dialogue execute] Error at " + scriptName + ":" + index, e);
    _inputLocked = false;
    if (typeof showToast === "function") showToast("Помилка в сцені, пропущено крок", "error");
    pc = index + 1;
    execute(pc);
  }
}


// ═══ КЛІК — НАСТУПНА КОМАНДА ═══

// Перевірка чи можна пропустити поточну ноду (для skip-read-only)
function canSkipCurrentNode() {
  if (!currentScript) return false;
  // Якщо skip-read-only вимкнений — пропускаємо все
  if (!settings || !settings.skipReadOnly) return true;
  // Перевіряємо чи нода прочитана
  var scriptName = _findScriptName(currentScript);
  if (typeof isSeen === "function" && isSeen(scriptName, pc)) return true;
  return false;
}

function advance() {
  _executeDepth = 0;
  if (_inputLocked) return;
  if (!currentScript) return;
  if (_waitingForPager) return; // Чекаємо кнопку пейджера
  var choices = document.querySelector(".choices");
  if (choices && choices.style.display === "flex") return;
  var title = document.querySelector(".scene-title");
  if (title && title.classList.contains("visible")) return;
  var tel = document.querySelector(".telepathy-overlay");
  if (tel && tel.style.display === "flex") { tel.style.display = "none"; }
  if (typing) { skipType(); return; }

  if (currentScript[pc] && currentScript[pc].type === "end" && !currentScript[pc].text) {
    // Кінець сцени — текст порожній, фінальний клік
    currentScript = null;
    clearSceneSprites();
    onSceneEnd();
    return;
  }

  pc++;
  execute(pc);
}


// Викликається з pager.js коли гравець натиснув кнопку під час wait_pager
function onPagerButton(button) {
  if (!_waitingForPager) return;
  _waitingForPager = false;

  var labelId = _waitPagerLabels ? _waitPagerLabels[button] : null;
  _waitPagerLabels = null;

  if (labelId && currentScript && currentScript._labels[labelId] !== undefined) {
    pc = currentScript._labels[labelId];
    execute(pc);
  } else {
    pc++;
    execute(pc);
  }
}
