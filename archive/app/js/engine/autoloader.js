// ═══════════════════════════════════════════════════
// АВТОЗАВАНТАЖУВАЧ КОНТЕНТУ
// ═══════════════════════════════════════════════════
//
// Читає content.json → завантажує ВСІ .js файли з scenes/ і dialogues/.
// Кожен файл сам реєструє себе через registerScript() / DIALOGUE_ENTRIES.push().
//
// Щоб додати новий контент:
//   1. Створи .js файл в js/scenes/ або js/dialogues/ (будь-яка вкладеність)
//   2. Запусти: node generate_manifest.js (або вручну додай в content.json)
//   3. Готово — гра підхопить автоматично
//
// content.json — масив шляхів відносно js/:
//   ["scenes/intro.js", "dialogues/stubs/arthur/stub_r1_talk1_sword.js"]

var _contentManifest = [];
var _contentLoaded = 0;
var _contentTotal = 0;

function loadContentManifest(callback) {
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "js/content.json", true);
  xhr.onload = function() {
    if (xhr.status === 200) {
      try {
        _contentManifest = JSON.parse(xhr.responseText);
      } catch(e) {
        console.error("[autoloader] Bad manifest:", e);
        _contentManifest = [];
      }
    } else {
      console.warn("[autoloader] No content.json found, skipping auto-load");
      _contentManifest = [];
    }
    _loadContentFiles(callback);
  };
  xhr.onerror = function() {
    console.warn("[autoloader] Failed to fetch manifest");
    if (callback) callback();
  };
  xhr.send();
}

// Зворотна сумісність
var loadDialogueManifest = loadContentManifest;

function _loadContentFiles(callback) {
  _contentTotal = _contentManifest.length;
  _contentLoaded = 0;

  if (_contentTotal === 0) {
    console.log("[autoloader] No content files in manifest");
    if (callback) callback();
    return;
  }

  console.log("[autoloader] Loading " + _contentTotal + " content files...");

  function _loadNext() {
    if (_contentLoaded >= _contentTotal) {
      console.log("[autoloader] All " + _contentTotal + " files loaded");
      if (callback) callback();
      return;
    }
    var script = document.createElement("script");
    script.src = "js/" + _contentManifest[_contentLoaded] + "?v=" + Date.now();
    script.onload = function() {
      _contentLoaded++;
      _loadNext();
    };
    script.onerror = function() {
      console.error("[autoloader] FAILED:", _contentManifest[_contentLoaded]);
      _contentLoaded++;
      _loadNext();
    };
    document.head.appendChild(script);
  }
  _loadNext();
}
