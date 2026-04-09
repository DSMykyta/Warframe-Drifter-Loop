// ═══════════════════════════════════════════════════
// SEEN — трекінг прочитаних діалогових нод
// ═══════════════════════════════════════════════════
//
// Зберігає set прочитаних нод (scriptName:pc) в localStorage.
// Використовується для skip-read-only режиму.

var SEEN_KEY = "drifter_seen";
var SEEN_NODES = {};
var _seenDirty = false;

// Завантажити з localStorage
(function() {
  try {
    var raw = localStorage.getItem(SEEN_KEY);
    if (raw) SEEN_NODES = JSON.parse(raw);
  } catch(e) {
    SEEN_NODES = {};
  }
})();

// Позначити ноду як прочитану
function markSeen(scriptName, index) {
  if (!scriptName) return;
  var key = scriptName + ":" + index;
  if (!SEEN_NODES[key]) {
    SEEN_NODES[key] = 1;
    _seenDirty = true;
  }
}

// Перевірити чи нода прочитана
function isSeen(scriptName, index) {
  if (!scriptName) return false;
  return SEEN_NODES[scriptName + ":" + index] === 1;
}

// Зберегти в localStorage (дебаунс — раз на 2 секунди)
var _seenSaveTimer = null;
function _scheduleSaveSeen() {
  if (_seenSaveTimer) return;
  _seenSaveTimer = setTimeout(function() {
    _seenSaveTimer = null;
    if (_seenDirty) {
      localStorage.setItem(SEEN_KEY, JSON.stringify(SEEN_NODES));
      _seenDirty = false;
    }
  }, 2000);
}

// Зберегти негайно (при виході)
function saveSeen() {
  if (_seenDirty) {
    localStorage.setItem(SEEN_KEY, JSON.stringify(SEEN_NODES));
    _seenDirty = false;
  }
}

// Зберігати перед закриттям вкладки
window.addEventListener("beforeunload", saveSeen);
