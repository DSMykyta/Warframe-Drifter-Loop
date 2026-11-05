// ═══════════════════════════════════════════════════
// ПРЕЛОАДЕР АССЕТІВ
// ═══════════════════════════════════════════════════
//
// Завантажує зображення заздалегідь для плавного відображення.

var _assetCache = {};
var _assetCacheKeys = [];
var _CACHE_MAX = 200;

function _evictOldestAsset() {
  if (_assetCacheKeys.length > _CACHE_MAX) {
    var oldest = _assetCacheKeys.shift();
    delete _assetCache[oldest];
  }
}

function preloadImage(src) {
  if (_assetCache[src]) return;
  var img = new Image();
  img.src = src;
  _assetCache[src] = img;
  _assetCacheKeys.push(src);
  _evictOldestAsset();
}

// Прелоадити всі спрайти персонажів
function preloadCharacterSprites() {
  for (var short in CAST) {
    var ch = CAST[short];
    if (ch.sprite) {
      preloadImage("assets/sprites/" + ch.sprite + "/knee-test.png");
    }
  }
}

// Прелоадити фони сусідніх локацій (webp → png → jpg fallback)
function preloadNearbyBackgrounds(currentLoc) {
  if (typeof LOCATION_GRAPH === "undefined") return;
  var neighbors = LOCATION_GRAPH[currentLoc];
  if (!neighbors) return;
  for (var i = 0; i < neighbors.length; i++) {
    _preloadBgWithFallback("assets/backgrounds/bg_" + neighbors[i]);
  }
}

function _preloadBgWithFallback(basePath) {
  if (_assetCache[basePath]) return;
  var img = new Image();
  img.onload = function() { _assetCache[basePath] = img; _assetCacheKeys.push(basePath); _evictOldestAsset(); };
  img.onerror = function() {
    var img2 = new Image();
    img2.onload = function() { _assetCache[basePath] = img2; _assetCacheKeys.push(basePath); _evictOldestAsset(); };
    img2.onerror = function() {
      var img3 = new Image();
      img3.onload = function() { _assetCache[basePath] = img3; _assetCacheKeys.push(basePath); _evictOldestAsset(); };
      img3.src = basePath + ".jpg";
    };
    img2.src = basePath + ".png";
  };
  img.src = basePath + ".webp";
}

// Прелоадити ассети зі скрипту (look-ahead)
function preloadScriptAssets(script, fromPc) {
  if (!script) return;
  var ahead = Math.min(fromPc + 20, script.length);
  for (var i = fromPc; i < ahead; i++) {
    var node = script[i];
    if (!node) continue;
    if (node.type === "scene" && node.bg) {
      preloadImage("assets/backgrounds/" + node.bg);
    }
    if (node.type === "show" && node.who) {
      var ch = _resolveChar(node.who);
      if (ch && ch.sprite) {
        preloadImage("assets/sprites/" + ch.sprite + "/knee-test.png");
      }
    }
    if (node.type === "bg" && node.file) {
      preloadImage("assets/backgrounds/" + node.file);
    }
  }
}
