// ═══════════════════════════════════════════════════
// АУДІО — музика, звуки, голос
// ═══════════════════════════════════════════════════
//
// Канали: music (циклічна), sound (одноразовий), voice (одноразовий)

var _currentMusic = null;
var _musicEl = null;
var _soundEl = null;

function playAudio(channel, file, loop, fadein) {
  if (channel === "music") {
    if (_musicEl) { _musicEl.pause(); _musicEl = null; }
    _musicEl = new Audio("assets/audio/" + file);
    _musicEl.loop = loop !== false;
    _musicEl.volume = 0;
    _musicEl.play().catch(function(){});
    var targetVol = 0.5;
    var fadeTime = fadein || 1000;
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
    _soundEl = new Audio("assets/audio/" + file);
    _soundEl.play().catch(function(){});
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
