// ═══════════════════════════════════════════════════
// КЛАВІАТУРНІ СКОРОЧЕННЯ
// ═══════════════════════════════════════════════════
//
// Enter / Space — наступна репліка (advance)
// Ctrl         — skip mode (тримати = пропускати)
// Escape       — закрити overlay / меню

var _skipMode = false;
var _skipTimer = null;

document.addEventListener("keydown", function(e) {
  // Enter або Space — advance
  if (e.key === "Enter" || e.key === " ") {
    e.preventDefault();
    if (typeof advance === "function") advance();
  }

  // Ctrl — skip mode ON
  if (e.key === "Control" && !_skipMode) {
    _skipMode = true;
    _skipTimer = setInterval(function() {
      if (typeof advance === "function") advance();
    }, 80);
  }

  // Escape — закрити overlay
  if (e.key === "Escape") {
    if (typeof hideOverlay === "function") hideOverlay();
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
