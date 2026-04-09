// ═══════════════════════════════════════════════════
// АУДІО — музика, звуки, голос
// ═══════════════════════════════════════════════════
//
// Канали: music (циклічна), sound (одноразовий), voice (одноразовий)
// SFX пул для одночасних звуків. Crossfade для музики.

var _currentMusic = null;
var _musicEl = null;
var _sfxPool = [];
var _sfxPoolSize = 8;

function playAudio(channel, file, loop, fadein) {
  if (channel === "music") {
    var targetVol = (typeof _targetMusicVolume !== "undefined") ? _targetMusicVolume : 0.5;
    var fadeTime = fadein || 1000;

    // Crossfade: fade out старої музики паралельно з fade in нової
    if (_musicEl) {
      var oldEl = _musicEl;
      var oldSteps = 20;
      var oldStepVol = oldEl.volume / oldSteps;
      var oldStepTime = fadeTime / oldSteps;
      var oldFade = setInterval(function() {
        oldEl.volume = Math.max(0, oldEl.volume - oldStepVol);
        if (oldEl.volume <= 0) { oldEl.pause(); clearInterval(oldFade); }
      }, oldStepTime);
    }

    _musicEl = new Audio("assets/audio/" + file);
    _musicEl.loop = loop !== false;
    _musicEl.volume = 0;
    _musicEl.play().catch(function(){});
    var steps = 20;
    var stepVol = targetVol / steps;
    var stepTime = fadeTime / steps;
    var vol = 0;
    var fadeInterval = setInterval(function() {
      vol += stepVol;
      if (vol >= targetVol) { _musicEl.volume = targetVol; clearInterval(fadeInterval); }
      else if (_musicEl) { _musicEl.volume = vol; }
      else { clearInterval(fadeInterval); }
    }, stepTime);
    _currentMusic = file;
  } else {
    // SFX пул — знайти вільний елемент або створити новий
    var sfx = null;
    for (var i = 0; i < _sfxPool.length; i++) {
      if (_sfxPool[i].ended || _sfxPool[i].paused) {
        sfx = _sfxPool[i];
        break;
      }
    }
    if (!sfx) {
      if (_sfxPool.length < _sfxPoolSize) {
        sfx = new Audio();
        _sfxPool.push(sfx);
      } else {
        // Перевикористати найстаріший
        sfx = _sfxPool[0];
        sfx.pause();
      }
    }
    sfx.src = "assets/audio/" + file;
    sfx.volume = (typeof _targetSfxVolume !== "undefined") ? _targetSfxVolume : 1.0;
    sfx.play().catch(function(){});
  }
}

function stopAudio(channel, fadeout) {
  if (channel === "music" && _musicEl) {
    var el = _musicEl;
    var fadeTime = fadeout || 1000;
    var steps = 20;
    var stepVol = el.volume / steps;
    var stepTime = fadeTime / steps;
    var fadeInterval = setInterval(function() {
      el.volume = Math.max(0, el.volume - stepVol);
      if (el.volume <= 0) { el.pause(); clearInterval(fadeInterval); }
    }, stepTime);
    _musicEl = null;
    _currentMusic = null;
  }
}
