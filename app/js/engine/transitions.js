// ═══════════════════════════════════════════════════
// TRANSITIONS — переходи між сценами
// ═══════════════════════════════════════════════════
//
// dissolve — crossfade (плавна заміна зображення)
// fade     — затемнення до чорного і назад
// wipe     — горизонтальне зсування (clip-path)
// slide    — зсув зліва/справа
// pixelate — пікселізація через blur

function applyTransition(type, duration, callback) {
  var bg = document.querySelector(".game-bg");
  if (!bg) { if (callback) callback(); return; }

  duration = duration || 500;

  // Миттєвий перехід під час skip mode
  if ((typeof _skipMode !== "undefined" && _skipMode) ||
      (typeof _skipToggle !== "undefined" && _skipToggle)) {
    if (callback) callback();
    return;
  }

  _inputLocked = true;

  // Safety timeout — скинути lock якщо transition "завис"
  var safetyTimer = setTimeout(function() {
    _inputLocked = false;
  }, Math.max(duration * 3, 10000));

  function _unlock() {
    clearTimeout(safetyTimer);
    _inputLocked = false;
  }

  try {
    switch (type) {

      // Dissolve — crossfade: зберегти старий стан, плавно з'явити новий
      case "dissolve":
        bg.style.transition = "opacity " + duration + "ms ease";
        bg.style.opacity = "0";
        setTimeout(function() {
          try {
            bg.style.transition = "";
            bg.style.opacity = "0";
            if (callback) callback();
            requestAnimationFrame(function() {
              bg.style.transition = "opacity " + duration + "ms ease";
              bg.style.opacity = "1";
              setTimeout(function() {
                bg.style.transition = "";
                _unlock();
              }, duration);
            });
          } catch(e) { console.error("[transition dissolve]", e); _unlock(); }
        }, duration);
        return; // callback вже викликаний всередині

      // Fade — через чорний екран (callback коли екран чорний)
      case "fade":
        bg.style.transition = "opacity " + (duration / 2) + "ms ease";
        bg.style.opacity = "0";
        setTimeout(function() {
          try {
            // Екран чорний — змінити контент зараз
            if (callback) callback();
            // Fade in з новим контентом
            requestAnimationFrame(function() {
              bg.style.transition = "opacity " + (duration / 2) + "ms ease";
              bg.style.opacity = "1";
              setTimeout(function() {
                bg.style.transition = "";
                _unlock();
              }, duration / 2);
            });
          } catch(e) { console.error("[transition fade]", e); _unlock(); if (callback) callback(); }
        }, duration / 2);
        break;

      // Wipe — горизонтальне розкриття через clip-path
      case "wipe":
        bg.style.transition = "clip-path " + duration + "ms ease-in-out";
        bg.style.clipPath = "inset(0 100% 0 0)";
        setTimeout(function() {
          try {
            bg.style.clipPath = "inset(0 0 0 0)";
            setTimeout(function() {
              bg.style.transition = "";
              bg.style.clipPath = "";
              _unlock();
              if (callback) callback();
            }, duration);
          } catch(e) { console.error("[transition wipe]", e); _unlock(); if (callback) callback(); }
        }, 50);
        break;

      // Slide — зсув вліво
      case "slide":
        bg.style.transition = "transform " + (duration / 2) + "ms ease-in";
        bg.style.transform = "translateX(-100%)";
        setTimeout(function() {
          try {
            bg.style.transition = "";
            bg.style.transform = "translateX(100%)";
            requestAnimationFrame(function() {
              bg.style.transition = "transform " + (duration / 2) + "ms ease-out";
              bg.style.transform = "translateX(0)";
              setTimeout(function() {
                bg.style.transition = "";
                bg.style.transform = "";
                _unlock();
                if (callback) callback();
              }, duration / 2);
            });
          } catch(e) { console.error("[transition slide]", e); _unlock(); if (callback) callback(); }
        }, duration / 2);
        break;

      // Pixelate — blur ефект
      case "pixelate":
        bg.style.transition = "filter " + (duration / 2) + "ms ease";
        bg.style.filter = "blur(20px)";
        setTimeout(function() {
          try {
            bg.style.filter = "blur(0)";
            bg.style.transition = "filter " + (duration / 2) + "ms ease";
            setTimeout(function() {
              bg.style.transition = "";
              bg.style.filter = "";
              _unlock();
              if (callback) callback();
            }, duration / 2);
          } catch(e) { console.error("[transition pixelate]", e); _unlock(); if (callback) callback(); }
        }, duration / 2);
        break;

      // Невідомий тип — без переходу
      default:
        _unlock();
        if (callback) callback();
    }
  } catch(e) {
    console.error("[applyTransition]", e);
    _unlock();
    if (callback) callback();
  }
}
