// ═══════════════════════════════════════════════════
// НАЛАШТУВАННЯ — музика, звуки, текст, авто
// ═══════════════════════════════════════════════════

var SETTINGS_KEY = "drifter_settings";

var settings = {
  musicVolume: 80,
  sfxVolume: 80,
  textSpeed: 50,
  autoAdvance: false,
  autoDelay: 3000,
  skipReadOnly: false,
  textboxOpacity: 70
};

var _targetMusicVolume = 0.5;
var _targetSfxVolume = 1.0;

function loadSettings() {
  try {
    var raw = localStorage.getItem(SETTINGS_KEY);
    if (raw) {
      var saved = JSON.parse(raw);
      for (var key in saved) {
        if (key in settings) settings[key] = saved[key];
      }
    }
  } catch(e) {}
  applySettings();
}

function saveSettings() {
  localStorage.setItem(SETTINGS_KEY, JSON.stringify(settings));
}

function applySettings() {
  // Гучність музики: 0-100 → 0.0-1.0
  _targetMusicVolume = settings.musicVolume / 100;
  if (_musicEl) _musicEl.volume = _targetMusicVolume;

  // Гучність звуків: 0-100 → 0.0-1.0
  _targetSfxVolume = settings.sfxVolume / 100;

  // Швидкість тексту: 0=повільно(60ms), 50=нормально(32ms), 100=швидко(5ms)
  TEXT_SPEED_MS = Math.round(60 - (settings.textSpeed / 100) * 55);

  // Прозорість текстового блоку
  document.documentElement.style.setProperty("--textbox-opacity", (settings.textboxOpacity / 100).toFixed(2));
}

// Ініціалізація слайдерів
function _initSettingsUI() {
  var musicSlider = document.getElementById("setting-music");
  var sfxSlider = document.getElementById("setting-sfx");
  var speedSlider = document.getElementById("setting-textspeed");
  var autoToggle = document.getElementById("setting-auto");

  if (musicSlider) {
    musicSlider.value = settings.musicVolume;
    musicSlider.addEventListener("input", function() {
      settings.musicVolume = parseInt(this.value);
      applySettings();
      saveSettings();
    });
  }

  if (sfxSlider) {
    sfxSlider.value = settings.sfxVolume;
    sfxSlider.addEventListener("input", function() {
      settings.sfxVolume = parseInt(this.value);
      applySettings();
      saveSettings();
    });
  }

  if (speedSlider) {
    speedSlider.value = settings.textSpeed;
    speedSlider.addEventListener("input", function() {
      settings.textSpeed = parseInt(this.value);
      applySettings();
      saveSettings();
    });
  }

  if (autoToggle) {
    if (settings.autoAdvance) autoToggle.classList.add("active");
    autoToggle.addEventListener("click", function() {
      this.classList.toggle("active");
      settings.autoAdvance = this.classList.contains("active");
      saveSettings();
    });
  }

  // Fullscreen toggle
  var fsToggle = document.getElementById("setting-fullscreen");
  if (fsToggle) {
    if (document.fullscreenElement) fsToggle.classList.add("active");
    fsToggle.addEventListener("click", function() {
      this.classList.toggle("active");
      toggleFullscreen();
    });
  }

  // Textbox opacity
  var opacitySlider = document.getElementById("setting-textbox-opacity");
  if (opacitySlider) {
    opacitySlider.value = settings.textboxOpacity;
    opacitySlider.addEventListener("input", function() {
      settings.textboxOpacity = parseInt(this.value);
      applySettings();
      saveSettings();
    });
  }

  // Skip mode toggle (read-only vs all)
  var skipModeToggle = document.getElementById("setting-skipmode");
  var skipModeHint = document.getElementById("skipmode-hint");
  if (skipModeToggle) {
    if (settings.skipReadOnly) skipModeToggle.classList.add("active");
    if (skipModeHint) skipModeHint.textContent = settings.skipReadOnly ? "Тільки прочитане" : "Пропускати все";
    skipModeToggle.addEventListener("click", function() {
      this.classList.toggle("active");
      settings.skipReadOnly = this.classList.contains("active");
      if (skipModeHint) skipModeHint.textContent = settings.skipReadOnly ? "Тільки прочитане" : "Пропускати все";
      saveSettings();
    });
  }
}

// Fullscreen API
function toggleFullscreen() {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen().catch(function() {});
  } else {
    document.exitFullscreen().catch(function() {});
  }
}

// Автозапуск
loadSettings();
document.addEventListener("DOMContentLoaded", _initSettingsUI);
