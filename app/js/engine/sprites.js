// ═══════════════════════════════════════════════════
// СПРАЙТИ В СЦЕНІ — show/hide/position
// ═══════════════════════════════════════════════════
//
// Логіка розміщення як в Ren'Py:
//
// 1 персонаж  → центр
// 2 персонажі → рівномірно (зліва направо за порядком show)
// 3 персонажі → якщо є zorder — вищий zorder в центрі
// N персонажів → рівномірно, непарні — 7 слотів (центр зайнятий),
//                парні — 6 слотів (рівномірно)
//
// zorder визначає шар (хто поверх кого).
// Без zorder = 0. Вищий zorder = ближче до гравця.
// При однаковому zorder — хто першим show, той пріоритетніший.

var _sceneSprites = {};   // { "Артур": {charData, zorder, order} }
var _showOrder = 0;       // лічильник порядку show

// Стандартні слоти для N персонажів
// Непарні: 7 слотів з центральним
// Парні: 6 слотів рівномірно
function _calcPositions(count) {
  if (count === 0) return [];
  if (count === 1) return [50];
  if (count === 2) return [35, 65];
  if (count === 3) return [20, 50, 80];
  if (count === 4) return [15, 38, 62, 85];
  if (count === 5) return [10, 30, 50, 70, 90];
  if (count === 6) return [8, 24, 40, 60, 76, 92];
  // 7+
  var positions = [];
  for (var i = 0; i < count; i++) {
    positions.push(5 + (90 * i / (count - 1)));
  }
  return positions;
}

// Сортувати персонажів для розміщення:
// Вищий zorder → центр, нижчий → краї
function _sortForPlacement(entries) {
  // Спочатку сортуємо за zorder (desc), потім за order (asc)
  var sorted = entries.slice().sort(function(a, b) {
    if (b.zorder !== a.zorder) return b.zorder - a.zorder;
    return a.order - b.order;
  });

  // Розмістити: найвищий zorder → центральна позиція
  // Решта — від центру до країв
  var count = sorted.length;
  var positions = _calcPositions(count);
  var result = new Array(count);

  // Центральний індекс
  var centerIdx = Math.floor(count / 2);

  // Заповнення: [0] → центр, [1] → ліво від центру, [2] → право, ...
  var placed = [];
  placed[centerIdx] = sorted[0]; // Найвищий zorder в центр

  var leftIdx = centerIdx - 1;
  var rightIdx = centerIdx + 1;

  for (var i = 1; i < sorted.length; i++) {
    if (i % 2 === 1 && leftIdx >= 0) {
      placed[leftIdx] = sorted[i];
      leftIdx--;
    } else if (rightIdx < count) {
      placed[rightIdx] = sorted[i];
      rightIdx++;
    } else if (leftIdx >= 0) {
      placed[leftIdx] = sorted[i];
      leftIdx--;
    }
  }

  // Присвоїти позиції
  for (var j = 0; j < count; j++) {
    if (placed[j]) {
      placed[j].position = positions[j];
    }
  }

  return placed.filter(function(x) { return !!x; });
}


// ═══ ПУБЛІЧНІ ФУНКЦІЇ ═══

function _resolveChar(who) {
  if (!who) return null;
  if (CAST[who]) return CAST[who];
  for (var s in CAST) {
    if (CAST[s].name === who) return CAST[s];
  }
  return null;
}

// show: додати персонажа на сцену
function showSceneSprite(name, at, zorder) {
  var charData = _resolveChar(name);
  if (!charData || !charData.sprite) return;

  _sceneSprites[charData.name] = {
    charData: charData,
    zorder: zorder || 0,
    order: _showOrder++,
    position: 50  // тимчасово, перерахується в render
  };
  renderSceneSprites(null);
}

// hide: прибрати персонажа
function hideSceneSprite(name) {
  var charData = _resolveChar(name);
  if (charData) {
    delete _sceneSprites[charData.name];
  } else {
    delete _sceneSprites[name];
  }
  renderSceneSprites(null);
}

// scene change: очистити всіх
function clearSceneSprites() {
  _sceneSprites = {};
  _showOrder = 0;
  var container = document.getElementById("sprites-container");
  if (container) container.innerHTML = "";
}

// Відрендерити спрайти на екрані
function renderSceneSprites(speakerName) {
  var container = document.getElementById("sprites-container");
  if (!container) return;
  container.innerHTML = "";

  var entries = [];
  for (var name in _sceneSprites) {
    entries.push(_sceneSprites[name]);
  }
  if (entries.length === 0) return;

  // Розрахувати позиції
  var placed = _sortForPlacement(entries);

  // Сортувати для рендеру за zorder (нижчий рендериться першим = позаду)
  placed.sort(function(a, b) { return a.zorder - b.zorder; });

  for (var i = 0; i < placed.length; i++) {
    var entry = placed[i];
    var ch = entry.charData;
    var img = document.createElement("img");
    img.className = "sprite";
    img.src = "assets/sprites/" + ch.sprite + "/knee-test.png";
    img.style.left = entry.position + "%";
    img.style.zIndex = 5 + entry.zorder;
    img.alt = ch.name;

    // Затемнити тих хто не говорить
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

// Auto-add: якщо персонаж говорить але його нема на сцені — додати з zorder 0
function ensureSpeakerVisible(who) {
  var charData = _resolveChar(who);
  if (!charData) return null;

  // Вже на сцені — тільки підсвітити
  if (_sceneSprites[charData.name]) {
    renderSceneSprites(charData.name);
    return charData.name;
  }

  // Додати з zorder 0
  _sceneSprites[charData.name] = {
    charData: charData,
    zorder: 0,
    order: _showOrder++,
    position: 50
  };
  renderSceneSprites(charData.name);
  return charData.name;
}
