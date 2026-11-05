// ═══════════════════════════════════════════════════
// КЛАВІАТУРНІ СКОРОЧЕННЯ + МИША
// ═══════════════════════════════════════════════════
//
// Enter / Space — наступна репліка (advance)
// Ctrl          — skip mode (тримати = пропускати)
// Escape        — закрити overlay / меню
// L             — відкрити історію (бекло́г)
// H             — сховати/показати UI
// Wheel Down    — advance
// Wheel Up      — відкрити бекло́г
// Right-click   — контекстне меню

var _skipMode = false;
var _skipTimer = null;

// Перевірка: чи ми зараз на ігровому екрані?
function _isGameActive() {
  var gs = document.getElementById("game-screen");
  return gs && gs.style.display !== "none";
}

document.addEventListener("keydown", function(e) {
  // F11 — повний екран (працює завжди)
  if (e.key === "F11") {
    e.preventDefault();
    if (typeof toggleFullscreen === "function") toggleFullscreen();
    return;
  }

  // F1 — довідка по клавішах (працює завжди)
  if (e.key === "F1") {
    e.preventDefault();
    if (typeof showHelpOverlay === "function") showHelpOverlay();
    return;
  }

  // Escape — закрити overlay / бекло́г (працює завжди)
  if (e.key === "Escape") {
    // Довідка
    if (typeof _helpOverlay !== "undefined" && _helpOverlay) {
      _helpOverlay.remove();
      _helpOverlay = null;
      return;
    }
    // Підтвердження
    if (typeof _confirmOverlay !== "undefined" && _confirmOverlay) {
      _confirmOverlay.remove();
      _confirmOverlay = null;
      return;
    }
    // Спочатку бекло́г
    var backlog = document.getElementById("overlay-backlog");
    if (backlog && backlog.style.display === "flex") {
      if (typeof hideBacklog === "function") hideBacklog();
      return;
    }
    if (typeof hideOverlay === "function") hideOverlay();
    return;
  }

  // Решта клавіш працюють ТІЛЬКИ на ігровому екрані
  if (!_isGameActive()) return;

  // F5 — швидке збереження
  if (e.key === "F5") {
    e.preventDefault();
    if (typeof quickSave === "function") quickSave();
    return;
  }

  // F9 — швидке завантаження
  if (e.key === "F9") {
    e.preventDefault();
    if (typeof quickLoad === "function") quickLoad();
    return;
  }

  // Tab — toggle skip mode
  if (e.key === "Tab") {
    e.preventDefault();
    if (typeof _qmSkip === "function") _qmSkip();
    return;
  }

  // PageUp — бекло́г (відкрити або скролити вгору)
  if (e.key === "PageUp") {
    e.preventDefault();
    var backlogUp = document.getElementById("overlay-backlog");
    if (backlogUp && backlogUp.style.display === "flex") {
      var mainUp = backlogUp.querySelector("main");
      if (mainUp) mainUp.scrollTop -= 300;
    } else {
      if (typeof showBacklog === "function") showBacklog();
    }
    return;
  }

  // PageDown — скролити бекло́г вниз
  if (e.key === "PageDown") {
    e.preventDefault();
    var backlogDown = document.getElementById("overlay-backlog");
    if (backlogDown && backlogDown.style.display === "flex") {
      var mainDown = backlogDown.querySelector("main");
      if (mainDown) mainDown.scrollTop += 300;
    }
    return;
  }

  // Arrow keys — навігація виборів
  if (e.key === "ArrowUp" || e.key === "ArrowDown") {
    var choicesEl = document.querySelector(".choices");
    if (choicesEl && choicesEl.style.display === "flex") {
      e.preventDefault();
      var btns = choicesEl.querySelectorAll(".choice-btn:not(.locked-choice)");
      if (btns.length === 0) return;
      var current = choicesEl.querySelector(".choice-focused");
      var idx = -1;
      for (var ci = 0; ci < btns.length; ci++) {
        if (btns[ci] === current) { idx = ci; break; }
      }
      if (e.key === "ArrowDown") idx = (idx + 1) % btns.length;
      else idx = (idx - 1 + btns.length) % btns.length;
      if (current) current.classList.remove("choice-focused");
      btns[idx].classList.add("choice-focused");
      return;
    }
  }

  // Enter або Space — advance (або натиснути обраний вибір)
  if (e.key === "Enter" || e.key === " ") {
    e.preventDefault();
    var choicesEnter = document.querySelector(".choices");
    if (choicesEnter && choicesEnter.style.display === "flex") {
      var focused = choicesEnter.querySelector(".choice-focused");
      if (focused) { focused.click(); return; }
    }
    if (typeof advance === "function") advance();
  }

  // Ctrl — skip mode ON
  if (e.key === "Control" && !_skipMode) {
    _skipMode = true;
    _skipTimer = setInterval(function() {
      if (typeof advance === "function") {
        // Перевірка skip-read-only
        if (typeof canSkipCurrentNode === "function" && !canSkipCurrentNode()) {
          _skipMode = false;
          if (_skipTimer) { clearInterval(_skipTimer); _skipTimer = null; }
          return;
        }
        advance();
      }
    }, 80);
  }

  // L — бекло́г
  if (e.key === "l" || e.key === "L") {
    if (typeof showBacklog === "function") showBacklog();
  }

  // H — сховати UI
  if (e.key === "h" || e.key === "H") {
    if (typeof _qmHide === "function") _qmHide();
  }
});

document.addEventListener("keyup", function(e) {
  // Ctrl — skip mode OFF
  if (e.key === "Control") {
    _skipMode = false;
    if (_skipTimer) {
      clearInterval(_skipTimer);
      _skipTimer = null;
    }
  }
});

// ═══ КОЛЕСО МИШІ ═══
document.addEventListener("wheel", function(e) {
  // Тільки коли діалог активний на game-screen
  if (!_isGameActive()) return;
  if (typeof currentScript === "undefined" || !currentScript) return;

  // Ігноруємо якщо overlay відкритий
  var gameScreen = document.getElementById("game-screen");
  var overlays = gameScreen.querySelectorAll(".overlay");
  for (var i = 0; i < overlays.length; i++) {
    if (overlays[i].style.display === "flex") return;
  }
  // Ігноруємо якщо бекло́г відкритий
  var backlog = document.getElementById("overlay-backlog");
  if (backlog && backlog.style.display === "flex") return;

  if (e.deltaY > 0) {
    // Wheel down — advance
    if (typeof advance === "function") advance();
  } else if (e.deltaY < 0) {
    // Wheel up — бекло́г
    if (typeof showBacklog === "function") showBacklog();
  }
}, { passive: true });

// Заблокувати контекстне меню браузера на game-screen
document.addEventListener("contextmenu", function(e) {
  var gameScreen = document.getElementById("game-screen");
  if (gameScreen && gameScreen.style.display !== "none") {
    e.preventDefault();
  }
});



// ═══ ДОВІДКА ПО КЛАВІШАХ ═══

var _helpOverlay = null;

function showHelpOverlay() {
  if (_helpOverlay) { _helpOverlay.remove(); _helpOverlay = null; return; }

  var keys = [
    ["Enter / Space / Click", "Наступна репліка"],
    ["Ctrl (тримати)", "Пропуск тексту"],
    ["Tab", "Увімк./вимк. пропуск"],
    ["Escape", "Закрити меню / overlay"],
    ["L", "Текстова історія (бекло\u0301г)"],
    ["H", "Сховати / показати UI"],
    ["F1", "Ця довідка"],
    ["F5", "Швидке збереження"],
    ["F9", "Швидке завантаження"],
    ["F11", "Повний екран"],
    ["PageUp / PageDown", "Гортати історію"],
    ["\u2191 \u2193 + Enter", "Навігація виборів"],
    ["Колесо вниз", "Наступна репліка"],
    ["Колесо вгору", "Текстова історія"]
  ];

  _helpOverlay = document.createElement("div");
  _helpOverlay.id = "help-overlay";

  var box = '<div class="help-box"><div class="help-title">Керування</div>';
  for (var i = 0; i < keys.length; i++) {
    box += '<div class="help-row"><span class="help-key">' + keys[i][0] + '</span><span class="help-desc">' + keys[i][1] + '</span></div>';
  }
  box += '<button class="help-close">ЗАКРИТИ</button></div>';
  _helpOverlay.innerHTML = box;

  _helpOverlay.querySelector(".help-close").addEventListener("click", function() {
    _helpOverlay.remove();
    _helpOverlay = null;
  });

  document.getElementById("viewport").appendChild(_helpOverlay);
}
