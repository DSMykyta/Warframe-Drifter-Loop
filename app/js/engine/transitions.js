// ═══════════════════════════════════════════════════
// TRANSITIONS — переходи між сценами
// ═══════════════════════════════════════════════════
//
// dissolve — плавне затемнення/появлення
// fade     — затемнення до чорного і назад

function applyTransition(type, duration, callback) {
  var bg = document.querySelector(".game-bg");
  if (!bg) { if (callback) callback(); return; }

  duration = duration || 500;

  if (type === "dissolve" || type === "fade") {
    bg.style.transition = "opacity " + duration + "ms ease";
    bg.style.opacity = "0";
    setTimeout(function() {
      bg.style.opacity = "1";
      setTimeout(function() {
        bg.style.transition = "";
        if (callback) callback();
      }, duration);
    }, duration);
  } else {
    if (callback) callback();
  }
}
