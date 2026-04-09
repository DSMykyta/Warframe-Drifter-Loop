// ═══════════════════════════════════════════════════
// АВТОЗАВАНТАЖУВАЧ ДІАЛОГІВ
// ═══════════════════════════════════════════════════
//
// Читає dialogues.json → завантажує всі .js файли з папки dialogues/.
// Кожен файл сам реєструє себе через DIALOGUE_ENTRIES.push() і registerScript().
//
// Щоб додати новий діалог:
//   1. Створи .js файл в js/dialogues/ (будь-яка вкладеність)
//   2. Запусти generate_manifest.bat (або вручну додай в dialogues.json)
//   3. Готово — гра підхопить автоматично
//
// dialogues.json — масив відносних шляхів:
//   ["stubs/arthur/stub_r0_talk1_weather.js", "intros/arthur_intro.js"]

var _dialogueManifest = [];
var _dialoguesLoaded = 0;
var _dialoguesTotal = 0;

function loadDialogueManifest(callback) {
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "js/dialogues/dialogues.json", true);
  xhr.onload = function() {
    if (xhr.status === 200) {
      try {
        _dialogueManifest = JSON.parse(xhr.responseText);
      } catch(e) {
        console.error("[autoloader] Bad manifest:", e);
        _dialogueManifest = [];
      }
    } else {
      console.warn("[autoloader] No manifest found, skipping auto-load");
      _dialogueManifest = [];
    }
    _loadDialogueFiles(callback);
  };
  xhr.onerror = function() {
    console.warn("[autoloader] Failed to fetch manifest");
    if (callback) callback();
  };
  xhr.send();
}

function _loadDialogueFiles(callback) {
  _dialoguesTotal = _dialogueManifest.length;
  _dialoguesLoaded = 0;

  if (_dialoguesTotal === 0) {
    console.log("[autoloader] No dialogue files in manifest");
    if (callback) callback();
    return;
  }

  console.log("[autoloader] Loading " + _dialoguesTotal + " dialogue files...");

  for (var i = 0; i < _dialogueManifest.length; i++) {
    var script = document.createElement("script");
    script.src = "js/dialogues/" + _dialogueManifest[i] + "?v=" + Date.now();
    script.onload = function() {
      _dialoguesLoaded++;
      if (_dialoguesLoaded >= _dialoguesTotal) {
        console.log("[autoloader] All " + _dialoguesTotal + " dialogues loaded");
        if (callback) callback();
      }
    };
    script.onerror = function() {
      console.warn("[autoloader] Failed to load:", this.src);
      _dialoguesLoaded++;
      if (_dialoguesLoaded >= _dialoguesTotal) {
        if (callback) callback();
      }
    };
    document.head.appendChild(script);
  }
}
