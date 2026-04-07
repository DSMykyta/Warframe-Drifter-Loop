// ═══════════════════════════════════════════════════
// UI ЛОКАЦІЇ
// ═══════════════════════════════════════════════════
//
// Показує: фон, HUD, спрайти NPC, дії.
// Клік на NPC → запуск діалогу (dispatcher → stubs → generic).
// Клік на КАРТА → overlay.
// Клік на СПАТИ → nextDay (тільки в бекрумі).
// Клік на МІСІЇ → overlay.

function showLocation() {
  // Сховати діалог і вибір
  var dlg = document.querySelector(".dialogue");
  if (dlg) dlg.style.display = "none";
  var choices = document.querySelector(".choices");
  if (choices) choices.style.display = "none";

  // Прибрати старі спрайти
  clearSprites();

  // Фон локації
  var locId = gameState.location.current;
  var bg = document.querySelector(".game-bg");
  if (bg) _setLocationBg(bg, locId);

  // HUD
  showHUD();
  updateHUD();

  // Пейджер
  if (typeof showPager === "function") showPager();
  if (typeof updatePagerScreen === "function") updatePagerScreen();

  // Спрайти NPC
  showSprites(locId);

  // Перевірити forced діалог при вході в локацію
  if (typeof checkForcedDialogue === "function") {
    var forced = checkForcedDialogue(locId);
    if (forced && forced.label && SCRIPTS[forced.label]) {
      hideHUD();
      if (typeof hidePager === "function") hidePager();
      if (typeof markDialogueSeen === "function") markDialogueSeen(forced.id);
      runScript(forced.label);
      return;
    }
  }

  // Перевірити banter (парні сцени NPC)
  if (typeof getBanter === "function") {
    var banter = getBanter(locId);
    if (banter && banter.label && SCRIPTS[banter.label]) {
      hideHUD();
      if (typeof hidePager === "function") hidePager();
      runScript(banter.label);
      return;
    }
  }

  // NPC і дії
  showLocationUI();
}


// ─── СПРАЙТИ NPC ───

function showSprites(locId) {
  var container = document.getElementById("sprites-container");
  if (!container) return;
  container.innerHTML = "";

  var charsHere = getCharsHere(locId);
  var positions = getPositions(charsHere.length);

  charsHere.forEach(function(ch, i) {
    var spritePath = "assets/sprites/" + (ch.sprite || ch.short) + "/knee-test.png";
    var wrapper = document.createElement("div");
    wrapper.className = "sprite-wrapper clickable";
    wrapper.style.left = positions[i] + "%";
    wrapper.alt = ch.name;
    wrapper.setAttribute("data-name", ch.name);

    var img = document.createElement("img");
    img.className = "sprite-img";
    img.src = spritePath;
    img.alt = ch.name;
    img.onerror = function() { this.parentElement.style.display = "none"; };

    wrapper.appendChild(img);
    wrapper.addEventListener("click", function(e) {
      e.stopPropagation();
      _talkToNPC(ch);
    });
    container.appendChild(wrapper);
  });
}

function clearSprites() {
  if (typeof clearSceneSprites === "function") clearSceneSprites();
  var container = document.getElementById("sprites-container");
  if (container) container.innerHTML = "";
}


// ─── ВИЗНАЧИТИ ХТО ТУТ (triggers + fallback на home) ───

function getCharsHere(locId) {
  var result = [];
  var seen = {};

  // Спробувати trigger систему
  try {
    if (typeof getCharsAt === "function") {
      var charNames = getCharsAt(locId);
      for (var i = 0; i < charNames.length; i++) {
        for (var short in CAST) {
          if (CAST[short].name === charNames[i] && !seen[short]) {
            seen[short] = true;
            result.push(CAST[short]);
            break;
          }
        }
      }
    }
  } catch (e) {
    console.error("[getCharsHere] trigger error:", e);
  }

  // Fallback: home location
  if (result.length === 0) {
    for (var s in CAST) {
      var ch = CAST[s];
      if (ch.home === locId && !seen[s]) {
        result.push(ch);
      }
    }
  }

  return result;
}


// Позиції спрайтів по центру
function getPositions(count) {
  if (count === 0) return [];
  if (count === 1) return [50];
  if (count === 2) return [30, 70];
  if (count === 3) return [20, 50, 80];
  if (count === 4) return [15, 38, 62, 85];
  if (count === 5) return [10, 30, 50, 70, 90];
  return [10, 25, 40, 55, 70, 85];
}


// ─── UI ЛОКАЦІЇ: кнопки дій ───

function showLocationUI() {
  var locId = gameState.location.current;
  var locName = currentLocationName();
  var time = getTimeString();
  var day = gameState.time.day;

  var choicesEl = document.querySelector(".choices");
  var left = document.querySelector(".choices-left");
  var list = document.querySelector(".choices-list");

  left.innerHTML = "";
  list.innerHTML = "";

  // NPC кнопки НЕ потрібні — спрайти самі клікабельні (showSprites).
  // Підсвітити спрайти з діалогом (зірочка над головою)
  var charsHere = getCharsHere(locId);
  var container = document.getElementById("sprites-container");
  if (container) {
    var sprites = container.querySelectorAll(".sprite-wrapper");
    for (var si = 0; si < sprites.length; si++) {
      var spriteName = sprites[si].getAttribute("data-name");
      var hasSpecial = false;
      if (typeof getActiveDialogue === "function") {
        hasSpecial = getActiveDialogue(spriteName) !== null;
      }
      if (hasSpecial) {
        sprites[si].classList.add("has-dialogue");
      }
    }
  }

  // Місії (тільки в гаражі)
  if (locId === "garage" && gameState.missions && gameState.missions.list && gameState.missions.list.length > 0) {
    var btnMissions = document.createElement("button");
    btnMissions.className = "choice-btn";
    btnMissions.textContent = "МІСІЇ (" + gameState.missions.list.length + ")";
    btnMissions.addEventListener("click", function(e) {
      e.stopPropagation();
      showOverlay("missions");
    });
    list.appendChild(btnMissions);
  }

  // Магазин (мол або магазин одягу)
  if (locId === "mall" || locId === "clothing_shop") {
    var btnShop = document.createElement("button");
    btnShop.className = "choice-btn";
    btnShop.textContent = "МАГАЗИН";
    btnShop.addEventListener("click", function(e) {
      e.stopPropagation();
      showOverlay("shop");
    });
    list.appendChild(btnShop);
  }

  // Кавомашина (кафе, футкорт)
  if (locId === "cafe" || locId === "cafe_balcony" || locId === "foodcourt") {
    var btnCoffee = document.createElement("button");
    btnCoffee.className = "choice-btn";
    btnCoffee.textContent = "КАВОМАШИНА";
    btnCoffee.addEventListener("click", function(e) {
      e.stopPropagation();
      if (!getFlag("coffee_machine_found")) setFlag("coffee_machine_found");
      showOverlay("coffee");
    });
    list.appendChild(btnCoffee);
  }

  // Спати (тільки в бекрумі)
  if (locId === "backroom") {
    var btnSleep = document.createElement("button");
    btnSleep.className = "choice-btn";
    btnSleep.textContent = "СПАТИ";
    btnSleep.addEventListener("click", function(e) {
      e.stopPropagation();
      _goToSleep();
    });
    list.appendChild(btnSleep);
  }

  choicesEl.style.display = "flex";

  // Кнопка КАРТА — зліва внизу (тільки якщо карту знайдено)
  if (getFlag("has_map")) {
    _showMapButton();
  }
}


// ─── КНОПКА КАРТИ (зліва внизу) ───

function _showMapButton() {
  _hideMapButton();
  var btn = document.createElement("button");
  btn.id = "map-btn-fixed";
  btn.className = "map-btn-fixed";
  btn.textContent = "КАРТА";
  btn.addEventListener("click", function(e) {
    e.stopPropagation();
    showOverlay("map");
  });
  document.getElementById("game-screen").appendChild(btn);
}

function _hideMapButton() {
  var old = document.getElementById("map-btn-fixed");
  if (old) old.remove();
}


// ─── РОЗМОВА З NPC ───

function _talkToNPC(ch) {
  var name = ch.name;

  // Позначити що говорили сьогодні
  if (typeof markTalkedToday === "function") markTalkedToday(name);
  if (typeof resetInteraction === "function") resetInteraction(name);
  if (typeof addChemistry === "function") addChemistry(name, 1);
  advanceTime(15);

  // Шукаємо діалог (повертає entry або null)
  var entry = null;
  if (typeof getDialogue === "function") {
    entry = getDialogue(name);
  }

  // ═══ TITLES: меню привітань ═══
  if (entry && entry.titles && entry.titles.length > 0) {
    _showTitlesMenu(entry);
    return;
  }

  // ═══ LABEL (forced): запустити напряму ═══
  if (entry && entry.label && SCRIPTS[entry.label]) {
    _hideForDialogue();
    if (typeof markDialogueSeen === "function") markDialogueSeen(entry.id);
    runScript(entry.label);
    return;
  }

  // Fallback: stub
  _hideForDialogue();
  var stubLabel = _findRandomStub(name);
  if (stubLabel && SCRIPTS[stubLabel]) {
    runScript(stubLabel);
    return;
  }
  if (SCRIPTS["generic_stub"]) {
    runScript("generic_stub");
  } else {
    _returnToLocation();
  }
}


// ─── Сховати UI для діалогу ───
function _hideForDialogue() {
  var choicesEl = document.querySelector(".choices");
  if (choicesEl) choicesEl.style.display = "none";
  _hideMapButton();
  hideHUD();
  if (typeof hidePager === "function") hidePager();
}


// ─── TITLES: показати привітання як меню ───
function _showTitlesMenu(entry) {
  var list = document.querySelector(".choices-list");
  if (!list) return;
  list.innerHTML = "";

  // Бонусні опції (напр. "Хай, бро" від Квінсі)
  if (typeof BONUS_OPTIONS !== "undefined") {
    for (var b = 0; b < BONUS_OPTIONS.length; b++) {
      var bo = BONUS_OPTIONS[b];
      if (bo.who !== entry.who) continue;
      if (bo.once && getFlag(bo.id + "_used")) continue;
      if (!checkStableConditions(bo.conditions || {})) continue;
      (function(bonus) {
        var btn = document.createElement("button");
        btn.className = "choice-btn";
        btn.textContent = bonus.text;
        btn.addEventListener("click", function(e) {
          e.stopPropagation();
          _hideForDialogue();
          if (bonus.once) setFlag(bonus.id + "_used");
          if (typeof markDialogueSeen === "function") markDialogueSeen(entry.id);
          runScript(bonus.label);
        });
        list.appendChild(btn);
      })(bo);
    }
  }

  // Основні привітання
  for (var i = 0; i < entry.titles.length; i++) {
    (function(title) {
      var btn = document.createElement("button");
      btn.className = "choice-btn";
      btn.textContent = title.text;
      btn.addEventListener("click", function(e) {
        e.stopPropagation();
        _hideForDialogue();
        if (typeof markDialogueSeen === "function") markDialogueSeen(entry.id);
        if (title.chemistry) {
          for (var cn in title.chemistry) addChemistry(cn, title.chemistry[cn]);
        }
        if (title.flag) setFlag(title.flag);
        runScript(title.label);
      });
      list.appendChild(btn);
    })(entry.titles[i]);
  }
}


// Знайти випадковий stub для NPC за іменем
function _findRandomStub(name) {
  var prefix = "stub_" + name + "_";
  var candidates = [];

  for (var key in SCRIPTS) {
    if (key.indexOf(prefix) === 0) {
      candidates.push(key);
    }
  }

  if (candidates.length === 0) return null;
  return candidates[Math.floor(Math.random() * candidates.length)];
}


// ─── СОН ───

function _goToSleep() {
  var choicesEl = document.querySelector(".choices");
  choicesEl.style.display = "none";
  _hideMapButton();
  hideHUD();
  if (typeof hidePager === "function") hidePager();

  // Перевірити кінець гри (день 31)
  if (gameState.time.day >= 31) {
    var bg = document.querySelector(".game-bg");
    if (bg) bg.style.background = "#000";

    // Зберегти persistent дані
    var victory = (typeof checkAllFriends === "function") && checkAllFriends();
    if (typeof onLoopEnd === "function") onLoopEnd(victory);

    // Запустити фінальну сцену
    if (victory && SCRIPTS["finale_victory"]) {
      hideHUD();
      if (typeof hidePager === "function") hidePager();
      runScript("finale_victory");
    } else if (!victory && SCRIPTS["finale_defeat"]) {
      hideHUD();
      if (typeof hidePager === "function") hidePager();
      runScript("finale_defeat");
    } else {
      // Fallback якщо скрипти не завантажені
      var dlg = document.querySelector(".dialogue");
      var nameEl = document.querySelector(".say-name");
      var textEl = document.querySelector(".say-text");
      if (dlg) dlg.style.display = "flex";
      if (nameEl) nameEl.style.visibility = "hidden";
      if (textEl) {
        textEl.className = "say-text narrator";
        textEl.textContent = victory
          ? "День 31. Реактор стабілізований. Петля розірвана."
          : "День 31. Петля замикається. Кінець... цього разу.";
      }
    }
    return;
  }

  // Сцена сну — чорний екран
  var bg2 = document.querySelector(".game-bg");
  if (bg2) bg2.style.background = "#000";

  var dlg2 = document.querySelector(".dialogue");
  var nameEl2 = document.querySelector(".say-name");
  var textEl2 = document.querySelector(".say-text");
  if (dlg2) dlg2.style.display = "flex";
  if (nameEl2) nameEl2.style.visibility = "hidden";
  if (textEl2) {
    textEl2.className = "say-text narrator";
    textEl2.textContent = "...";
  }

  // Виконати nextDay після паузи
  setTimeout(function() {
    nextDay();

    if (textEl2) {
      textEl2.textContent = "День " + gameState.time.day + ". " + getTimeString() + ".";
    }

    // Клік — повернутись до гри
    var _sleepHandler = function() {
      document.getElementById("game-screen").removeEventListener("click", _sleepHandler);
      if (dlg2) dlg2.style.display = "none";
      _returnToLocation();
    };

    // Затримка перед слуханням кліків
    setTimeout(function() {
      document.getElementById("game-screen").addEventListener("click", _sleepHandler);
    }, 500);
  }, 1000);
}


// ─── ПОМІЧНА ФУНКЦІЯ: встановити фон з fallback на jpg/webp ───

// ─── BG_OVERRIDES: фонові зміни на основі прапорців ───

var BG_OVERRIDES = {
  "coffee_machine_found": {"cafe": "bg_cafe_coffee"}
};

function _getOverrideBg(locId) {
  for (var flag in BG_OVERRIDES) {
    if (BG_OVERRIDES[flag][locId] && getFlag(flag)) {
      return BG_OVERRIDES[flag][locId];
    }
  }
  return null;
}


function _setLocationBg(bgEl, locId) {
  // Перевірити оверрайди
  var override = _getOverrideBg(locId);
  var basePath = override
    ? "assets/backgrounds/" + override
    : "assets/backgrounds/bg_" + locId;
  var img = new Image();
  img.onload = function() {
    bgEl.style.background = "url('" + basePath + ".webp') center/cover no-repeat";
  };
  img.onerror = function() {
    var img2 = new Image();
    img2.onload = function() {
      bgEl.style.background = "url('" + basePath + ".png') center/cover no-repeat";
    };
    img2.onerror = function() {
      var img3 = new Image();
      img3.onload = function() {
        bgEl.style.background = "url('" + basePath + ".jpg') center/cover no-repeat";
      };
      img3.onerror = function() {
        bgEl.style.background = "#111";
      };
      img3.src = basePath + ".jpg";
    };
    img2.src = basePath + ".png";
  };
  img.src = basePath + ".webp";
}
