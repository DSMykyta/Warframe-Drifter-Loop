// ═══════════════════════════════════════════════════
// СПРАЙТИ В СЦЕНІ — show/hide/position
// ═══════════════════════════════════════════════════
//
// Керує спрайтами персонажів на екрані.
// Використовується рушієм діалогів (dialogue.js).

var _sceneSprites = {};  // { "Артур": {charData, position, zorder} }

// Стандартні позиції (як в Ren'Py)
var SPRITE_POSITIONS = {
  "left":          15,
  "far_left":       5,
  "center_left":   30,
  "center":        50,
  "center_right":  70,
  "right":         85,
  "far_right":     95
};

// Знайти персонажа за short або name
function _resolveChar(who) {
  if (!who) return null;
  if (CAST[who]) return CAST[who];
  for (var s in CAST) {
    if (CAST[s].name === who) return CAST[s];
  }
  return null;
}

// Показати спрайт на екрані
function showSceneSprite(name, position, zorder) {
  var charData = _resolveChar(name);
  if (!charData || !charData.sprite) return;

  var pos = SPRITE_POSITIONS[position] || SPRITE_POSITIONS["center"];
  if (typeof position === "number") pos = position;

  _sceneSprites[charData.name] = {
    charData: charData,
    position: pos,
    zorder: zorder || 0
  };
  renderSceneSprites(null);
}

// Сховати спрайт
function hideSceneSprite(name) {
  var charData = _resolveChar(name);
  if (charData) {
    delete _sceneSprites[charData.name];
  } else {
    delete _sceneSprites[name];
  }
  renderSceneSprites(null);
}

// Очистити всіх
function clearSceneSprites() {
  _sceneSprites = {};
  var container = document.getElementById("sprites-container");
  if (container) container.innerHTML = "";
}

// Відрендерити всіх спрайтів
function renderSceneSprites(speakerName) {
  var container = document.getElementById("sprites-container");
  if (!container) return;
  container.innerHTML = "";

  var entries = [];
  for (var name in _sceneSprites) {
    entries.push(_sceneSprites[name]);
  }
  entries.sort(function(a, b) { return a.zorder - b.zorder; });

  for (var i = 0; i < entries.length; i++) {
    var entry = entries[i];
    var ch = entry.charData;
    var img = document.createElement("img");
    img.className = "sprite";
    img.src = "assets/sprites/" + ch.sprite + "/knee-test.png";
    img.style.left = entry.position + "%";
    img.style.zIndex = 5 + entry.zorder;
    img.alt = ch.name;

    // Більший zorder = ближче до камери = більший спрайт
    if (entry.zorder > 0) {
      var scale = 1 + (entry.zorder * 0.1);
      img.style.height = (80 * scale) + "%";
    }

    if (speakerName && ch.name !== speakerName) {
      img.style.filter = "brightness(0.5)";
      img.style.transition = "filter 0.3s ease";
    } else if (speakerName) {
      img.style.filter = "brightness(1)";
      img.style.transition = "filter 0.3s ease";
    }

    img.onerror = function() { this.style.display = "none"; };
    container.appendChild(img);
  }
}

// Auto-add: якщо персонаж говорить але його нема на сцені — додати
function ensureSpeakerVisible(who) {
  var charData = _resolveChar(who);
  if (!charData) return null;

  if (_sceneSprites[charData.name]) {
    renderSceneSprites(charData.name);
    return charData.name;
  }

  var count = Object.keys(_sceneSprites).length;
  var autoPositions = ["center", "left", "right", "center_left", "center_right", "far_left", "far_right"];
  var pos = autoPositions[count] || "center";

  _sceneSprites[charData.name] = {
    charData: charData,
    position: SPRITE_POSITIONS[pos],
    zorder: count
  };
  renderSceneSprites(charData.name);
  return charData.name;
}
