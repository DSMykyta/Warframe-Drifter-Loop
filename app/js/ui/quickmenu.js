// ═══════════════════════════════════════════════════
// QUICK MENU — панель під час діалогу
// ═══════════════════════════════════════════════════
//
// [ЗБЕРЕГТИ] [ЗАВАНТАЖИТИ] [ІСТОРІЯ] [АВТО] [ПРОПУСК] [СХОВАТИ]

var _autoMode = false;
var _autoTimer = null;
var _skipToggle = false;
var _skipToggleTimer = null;
var _uiHidden = false;

function _createQuickMenu() {
  var qm = document.getElementById("quick-menu");
  if (qm) return; // вже створено

  qm = document.createElement("div");
  qm.id = "quick-menu";
  qm.style.display = "none";

  var buttons = [
    { id: "qm-save",    text: "ЗБЕРЕГТИ",     action: _qmSave,     tip: "Швидке збереження" },
    { id: "qm-load",    text: "ЗАВАНТАЖИТИ",   action: _qmLoad,     tip: "Екран завантаження" },
    { id: "qm-log",     text: "ІСТОРІЯ",      action: _qmLog,      tip: "Текстова історія" },
    { id: "qm-auto",    text: "АВТО",         action: _qmAuto,     tip: "Автопрокрутка тексту" },
    { id: "qm-skip",    text: "ПРОПУСК",      action: _qmSkip,     tip: "Пропуск тексту" },
    { id: "qm-settings",text: "НАЛАШТУВАННЯ",  action: function() { showScreen("settings-screen"); }, tip: "Налаштування" },
    { id: "qm-menu",    text: "МЕНЮ",         action: function() {
      if (typeof confirmDialog === "function") {
        confirmDialog("Повернутись до головного меню?", function() { autoSave(); showScreen("main-menu"); });
      } else { autoSave(); showScreen("main-menu"); }
    }, tip: "Головне меню" }
  ];

  for (var i = 0; i < buttons.length; i++) {
    var btn = document.createElement("button");
    btn.className = "qm-btn";
    btn.id = buttons[i].id;
    btn.textContent = buttons[i].text;
    if (buttons[i].tip) btn.title = buttons[i].tip;
    btn.addEventListener("click", (function(action) {
      return function(e) { e.stopPropagation(); action(); };
    })(buttons[i].action));
    qm.appendChild(btn);
  }

  var gameScreen = document.getElementById("game-screen");
  if (gameScreen) gameScreen.appendChild(qm);
}

function showQuickMenu() {
  var qm = document.getElementById("quick-menu");
  if (qm && !_uiHidden) qm.style.display = "flex";
}

function hideQuickMenu() {
  var qm = document.getElementById("quick-menu");
  if (qm) qm.style.display = "none";
}

// ═══ КНОПКИ ═══

function _qmSave() {
  var slot = findFreeSlot();
  if (slot) {
    save(slot, "День " + gameState.time.day + " / " + getTimeString());
    if (typeof showToast === "function") showToast("Збережено (слот " + slot + ")", "save");
  } else {
    if (typeof confirmDialog === "function") {
      confirmDialog("Всі слоти зайняті. Перезаписати автозбереження?", function() { autoSave(); });
    } else {
      autoSave();
    }
  }
}

function _qmLoad() {
  // Зберегти й повернутись в меню завантаження
  autoSave();
  showScreen("load-screen");
  renderLoadScreen();
}

function _qmLog() {
  if (typeof showBacklog === "function") showBacklog();
}

function _qmAuto() {
  _autoMode = !_autoMode;
  var btn = document.getElementById("qm-auto");
  if (btn) btn.classList.toggle("qm-active", _autoMode);

  if (_autoMode) {
    _disableSkipToggle();
    _showModeIndicator("\u25b6 АВТО");
    _tryAutoAdvance();
  } else {
    _cancelAutoTimer();
    _hideModeIndicator();
  }
}

function _qmSkip() {
  _skipToggle = !_skipToggle;
  var btn = document.getElementById("qm-skip");
  if (btn) btn.classList.toggle("qm-active", _skipToggle);

  if (_skipToggle) {
    _disableAutoMode();
    _showModeIndicator("\u25b6\u25b6 \u041f\u0420\u041e\u041f\u0423\u0421\u041a");
    _skipToggleTimer = setInterval(function() {
      if (typeof advance === "function") {
        // Перевірка skip-read-only
        if (typeof canSkipCurrentNode === "function" && !canSkipCurrentNode()) {
          _disableSkipToggle();
          return;
        }
        advance();
      }
    }, 80);
  } else {
    _disableSkipToggle();
  }
}

function _qmHide() {
  _uiHidden = !_uiHidden;
  var dlg = document.querySelector(".dialogue");
  var qm = document.getElementById("quick-menu");
  var hud = document.querySelector(".hud");

  if (_uiHidden) {
    if (dlg) dlg.style.visibility = "hidden";
    if (qm) qm.style.display = "none";
    if (hud) hud.style.visibility = "hidden";
    // Клік для повернення
    document.getElementById("game-screen").addEventListener("click", _unhideUI, { once: true });
  } else {
    _unhideUI();
  }
}

function _unhideUI() {
  _uiHidden = false;
  var dlg = document.querySelector(".dialogue");
  var qm = document.getElementById("quick-menu");
  var hud = document.querySelector(".hud");
  if (dlg && dlg.style.display === "flex") dlg.style.visibility = "visible";
  if (qm) qm.style.display = "flex";
  if (hud) hud.style.visibility = "visible";
}

// ═══ AUTO MODE ═══

var _autoTypingCheck = null;

function _tryAutoAdvance() {
  if (!_autoMode) return;
  if (_autoTypingCheck) { clearInterval(_autoTypingCheck); _autoTypingCheck = null; }
  if (typing) {
    _autoTypingCheck = setInterval(function() {
      if (!typing) {
        clearInterval(_autoTypingCheck);
        _autoTypingCheck = null;
        _scheduleAutoAdvance();
      }
    }, 100);
  } else {
    _scheduleAutoAdvance();
  }
}

function _scheduleAutoAdvance() {
  if (!_autoMode) return;
  var delay = (settings && settings.autoDelay) ? settings.autoDelay : 3000;
  _autoTimer = setTimeout(function() {
    if (_autoMode && typeof advance === "function") {
      advance();
      // Продовжити ланцюг, якщо все ще в режимі авто
      setTimeout(_tryAutoAdvance, 100);
    }
  }, delay);
}

function _cancelAutoTimer() {
  if (_autoTimer) { clearTimeout(_autoTimer); _autoTimer = null; }
}

function _disableAutoMode() {
  if (_autoTypingCheck) { clearInterval(_autoTypingCheck); _autoTypingCheck = null; }
  _autoMode = false;
  _cancelAutoTimer();
  var btn = document.getElementById("qm-auto");
  if (btn) btn.classList.remove("qm-active");
  if (!_skipToggle) _hideModeIndicator();
}

function _disableSkipToggle() {
  _skipToggle = false;
  if (_skipToggleTimer) { clearInterval(_skipToggleTimer); _skipToggleTimer = null; }
  var btn = document.getElementById("qm-skip");
  if (btn) btn.classList.remove("qm-active");
  if (!_autoMode) _hideModeIndicator();
}

// ═══ MODE INDICATOR ═══

function _showModeIndicator(text) {
  var ind = document.getElementById("mode-indicator");
  if (!ind) {
    ind = document.createElement("div");
    ind.id = "mode-indicator";
    var gs = document.getElementById("game-screen");
    if (gs) gs.appendChild(ind);
  }
  ind.textContent = text;
  ind.style.display = "block";
}

function _hideModeIndicator() {
  var ind = document.getElementById("mode-indicator");
  if (ind) ind.style.display = "none";
}

// Показувати quick menu коли діалог відображається
var _qmObserver = null;
var _qmObservedElement = null;
function _watchDialogueVisibility() {
  var dlg = document.querySelector(".dialogue");
  if (!dlg) return;

  // Якщо вже спостерігаємо цей самий елемент — не створювати новий
  if (_qmObserver && _qmObservedElement === dlg) return;

  // Відключити попередній спостерігач
  if (_qmObserver) {
    _qmObserver.disconnect();
    _qmObserver = null;
  }

  _qmObservedElement = dlg;
  _qmObserver = new MutationObserver(function() {
    if (dlg.style.display === "flex") {
      showQuickMenu();
    } else {
      hideQuickMenu();
    }
  });
  _qmObserver.observe(dlg, { attributes: true, attributeFilter: ["style"] });
}

// Ініціалізація
document.addEventListener("DOMContentLoaded", function() {
  _createQuickMenu();
  // Затримка — чекаємо поки dialogue element з'явиться
  setTimeout(_watchDialogueVisibility, 500);
});
