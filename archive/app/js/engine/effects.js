// ═══════════════════════════════════════════════════
// ЕКРАННІ ЕФЕКТИ — shake, flash, tint
// ═══════════════════════════════════════════════════
//
// Використання в скриптах:
// { type: "effect", name: "shake", intensity: 10, duration: 500 }
// { type: "effect", name: "flash", color: "#fff", duration: 300 }
// { type: "effect", name: "tint", color: "#f00", opacity: 0.3, duration: 1000 }

function applyEffect(name, params, callback) {
  switch (name) {
    case "shake":
      _effectShake(params.intensity || 10, params.duration || 500, callback);
      break;
    case "flash":
      _effectFlash(params.color || "#fff", params.duration || 300, callback);
      break;
    case "tint":
      _effectTint(params.color || "#000", params.opacity || 0.5, params.duration || 1000, callback);
      break;
    default:
      if (callback) callback();
  }
}

// ─── SHAKE: тремтіння екрану ───
function _effectShake(intensity, duration, callback) {
  var bg = document.querySelector(".game-bg");
  if (!bg) { if (callback) callback(); return; }

  var start = Date.now();
  var origTransform = bg.style.transform || "";

  var shakeInterval = setInterval(function() {
    var elapsed = Date.now() - start;
    if (elapsed >= duration) {
      clearInterval(shakeInterval);
      bg.style.transform = origTransform;
      if (callback) callback();
      return;
    }
    // Зменшувати інтенсивність з часом
    var factor = 1 - (elapsed / duration);
    var x = (Math.random() * 2 - 1) * intensity * factor;
    var y = (Math.random() * 2 - 1) * intensity * factor;
    bg.style.transform = "translate(" + x + "px, " + y + "px)";
  }, 16); // ~60fps
}

// ─── FLASH: спалах кольору ───
function _effectFlash(color, duration, callback) {
  var overlay = _getEffectOverlay();
  overlay.style.background = color;
  overlay.style.opacity = "1";
  overlay.style.display = "block";
  overlay.style.transition = "opacity " + duration + "ms ease-out";

  // Запустити анімацію fade-out
  requestAnimationFrame(function() {
    overlay.style.opacity = "0";
  });

  setTimeout(function() {
    overlay.style.display = "none";
    overlay.style.transition = "";
    if (callback) callback();
  }, duration);
}

// ─── TINT: затінення кольором ───
function _effectTint(color, opacity, duration, callback) {
  var overlay = _getEffectOverlay();
  overlay.style.background = color;
  overlay.style.opacity = "0";
  overlay.style.display = "block";
  overlay.style.transition = "opacity " + (duration / 2) + "ms ease";

  // Fade in
  requestAnimationFrame(function() {
    overlay.style.opacity = String(opacity);
  });

  // Тримати, потім fade out
  setTimeout(function() {
    overlay.style.opacity = "0";
    setTimeout(function() {
      overlay.style.display = "none";
      overlay.style.transition = "";
      if (callback) callback();
    }, duration / 2);
  }, duration / 2);
}

// ─── ДОПОМІЖНЕ: overlay елемент ───
function _getEffectOverlay() {
  var el = document.getElementById("effect-overlay");
  if (!el) {
    el = document.createElement("div");
    el.id = "effect-overlay";
    el.style.cssText = "position:absolute;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:95;display:none;";
    var gameScreen = document.getElementById("game-screen");
    if (gameScreen) gameScreen.appendChild(el);
  }
  return el;
}
