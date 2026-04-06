// ═══════════════════════════════════════════════════
// ОВЕРЛЕЇ — карта, щоденник, інвентар, думки, місії, магазин, кава
// ═══════════════════════════════════════════════════
//
// Оверлеї відображаються поверх ігрового екрану.
// Відкриття — ховає HUD. Закриття — повертає HUD.
// Кожен оверлей має свою функцію рендеру.

var _currentOverlay = null;

// Усі доступні оверлеї
var OVERLAYS = ["map", "journal", "inventory", "insights", "missions", "shop", "coffee"];


// ─── ПОКАЗАТИ ОВЕРЛЕЙ ───

function showOverlay(name) {
  // Сховати попередній, якщо є
  hideOverlay();

  var el = document.getElementById("overlay-" + name);
  if (!el) return;

  _currentOverlay = name;
  hideHUD();

  // Рендер вмісту
  var renderers = {
    "map": renderMap,
    "journal": renderJournal,
    "inventory": renderInventory,
    "insights": renderInsights,
    "missions": renderMissions,
    "shop": renderShop,
    "coffee": renderCoffee
  };

  if (renderers[name]) renderers[name]();

  el.classList.add("visible");

  // Друкувати заголовок
  var h1 = el.querySelector("h1");
  if (h1) titleTypeIn(h1);
}


// ─── СХОВАТИ ОВЕРЛЕЙ ───

function hideOverlay() {
  if (!_currentOverlay) return;

  var el = document.getElementById("overlay-" + _currentOverlay);
  if (el) {
    var h1 = el.querySelector("h1");
    if (h1 && h1.getAttribute("data-word")) {
      titleTypeOut(h1, function() {
        el.classList.remove("visible");
      });
    } else {
      el.classList.remove("visible");
    }
  }

  _currentOverlay = null;
  showHUD();
  updateHUD();
}


// ═══════════════════════════════════════════════════
// РЕНДЕР: КАРТА
// ═══════════════════════════════════════════════════

var _mapFloor = 1;

function renderMap() {
  _mapFloor = LOCATIONS[gameState.location.current] ?
    LOCATIONS[gameState.location.current].floor : 1;
  _renderMapFloor();
}

function switchMapFloor(floor) {
  _mapFloor = floor;
  _renderMapFloor();
}

function _renderMapFloor() {
  var main = document.querySelector("#overlay-map main");
  if (!main) return;

  // Таби поверхів
  var html = '<div class="map-tabs">';
  html += '<button class="map-tab' + (_mapFloor === 1 ? ' active' : '') + '" onclick="switchMapFloor(1)">ПОВЕРХ 1</button>';
  html += '<button class="map-tab' + (_mapFloor === 2 ? ' active' : '') + '" onclick="switchMapFloor(2)">ПОВЕРХ 2</button>';
  html += '</div>';

  // Креслення
  html += '<div class="map-blueprint">';

  // Розташування кімнат на кресленні (вручну задані координати)
  var layout = _getMapLayout(_mapFloor);

  for (var i = 0; i < layout.length; i++) {
    var room = layout[i];
    var loc = LOCATIONS[room.id];
    if (!loc) continue;

    // Перевірка видимості
    if (!isVisible(room.id) && room.id !== gameState.location.current) continue;

    var isCurrent = (room.id === gameState.location.current);
    var isLocked = !isAccessible(room.id);

    var classes = "map-room";
    if (isCurrent) classes += " current";
    if (isLocked) classes += " locked";

    var onclick = isLocked ? "" :
      ' onclick="_mapTravelTo(\'' + room.id + '\')"';

    html += '<div class="' + classes + '" style="' +
      'left:' + room.x + 'px;top:' + room.y + 'px;' +
      'width:' + room.w + 'px;height:' + room.h + 'px;"' +
      onclick + '>' +
      loc.name + '</div>';
  }

  html += '</div>';

  main.innerHTML = html;
}


// Переміститися з карти
function _mapTravelTo(locId) {
  if (!isAccessible(locId)) return;
  travelTo(locId);
  hideOverlay();
  showLocation();
}


// Розташування кімнат — блупрінт
function _getMapLayout(floor) {
  if (floor === 1) {
    return [
      // Мол — центральний хол
      {id: "mall",           x: 440, y: 220, w: 260, h: 160},

      // Ліва частина
      {id: "info_desk",      x: 100, y: 220, w: 180, h: 80},
      {id: "security_desk",  x: 100, y: 320, w: 180, h: 80},
      {id: "security_room",  x: 100, y: 420, w: 180, h: 80},

      // Верх
      {id: "arcade",         x: 440, y: 60,  w: 260, h: 120},

      // Права частина
      {id: "range",          x: 860, y: 220, w: 180, h: 80},
      {id: "foodcourt",      x: 440, y: 420, w: 260, h: 100},

      // Низ
      {id: "garage",         x: 860, y: 420, w: 180, h: 100},

      // Приховані (з'являються за прогресом)
      {id: "bar",            x: 860, y: 60,  w: 180, h: 120},
      {id: "cinema",         x: 100, y: 60,  w: 180, h: 120},
      {id: "gym",            x: 100, y: 520, w: 180, h: 70},
      {id: "billiard",       x: 310, y: 520, w: 160, h: 70},
      {id: "barbershop",     x: 730, y: 60,  w: 120, h: 70},
      {id: "photo_studio",   x: 730, y: 150, w: 120, h: 70},
      {id: "laundry",        x: 500, y: 520, w: 160, h: 70},
      {id: "parking",        x: 860, y: 320, w: 180, h: 80},
      {id: "wc",             x: 730, y: 340, w: 100, h: 60}
    ];
  }

  // Поверх 2
  return [
    // Центр — бекрум
    {id: "backroom",       x: 440, y: 220, w: 260, h: 160},

    // Ліва частина
    {id: "music_shop",     x: 100, y: 60,  w: 180, h: 100},
    {id: "furniture",      x: 100, y: 180, w: 180, h: 100},
    {id: "clothing_shop",  x: 100, y: 300, w: 180, h: 100},

    // Права частина
    {id: "medbay",         x: 860, y: 60,  w: 180, h: 100},
    {id: "recovery_room",  x: 860, y: 180, w: 180, h: 80},

    // Верх
    {id: "cafe",           x: 440, y: 60,  w: 180, h: 120},
    {id: "cafe_balcony",   x: 640, y: 60,  w: 140, h: 120},

    // Низ
    {id: "comp_club",      x: 440, y: 420, w: 200, h: 100},
    {id: "rooftop",        x: 680, y: 420, w: 180, h: 100},
    {id: "balcony",        x: 860, y: 280, w: 180, h: 100},

    // Приховані
    {id: "utility",        x: 100, y: 420, w: 160, h: 80},
    {id: "warehouse",      x: 280, y: 420, w: 140, h: 80},
    {id: "pharmacy",       x: 730, y: 220, w: 110, h: 80},
    {id: "video_rental",   x: 730, y: 320, w: 110, h: 80},
    {id: "electronics",    x: 310, y: 160, w: 110, h: 80},
    {id: "jewelry",        x: 310, y: 260, w: 110, h: 80},
    {id: "bookshop",       x: 310, y: 360, w: 110, h: 80}
  ];
}


// ═══════════════════════════════════════════════════
// РЕНДЕР: ЩОДЕННИК
// ═══════════════════════════════════════════════════

function renderJournal() {
  var main = document.querySelector("#overlay-journal main");
  if (!main) return;

  var entries = gameState.insights.journal;

  if (!entries || entries.length === 0) {
    main.innerHTML = '<div class="journal-empty">Щоденник порожній. Записи з\'являться під час гри.</div>';
    return;
  }

  // Групувати за днями (з найновішого)
  var byDay = {};
  for (var i = 0; i < entries.length; i++) {
    var day = entries[i].day;
    if (!byDay[day]) byDay[day] = [];
    byDay[day].push(entries[i]);
  }

  // Сортувати дні від найновішого
  var days = Object.keys(byDay).sort(function(a, b) { return b - a; });

  var html = '<div class="journal-list">';

  for (var d = 0; d < days.length; d++) {
    var dayNum = days[d];
    var dayEntries = byDay[dayNum];

    html += '<div class="journal-day">';
    html += '<div class="journal-day-header">День ' + dayNum + '</div>';

    for (var e = 0; e < dayEntries.length; e++) {
      var entry = dayEntries[e];
      var typeClass = entry.type ? " type-" + entry.type : "";
      html += '<div class="journal-entry' + typeClass + '">' +
        _escapeHtml(entry.text) + '</div>';
    }

    html += '</div>';
  }

  html += '</div>';
  main.innerHTML = html;
}


// ═══════════════════════════════════════════════════
// РЕНДЕР: ІНВЕНТАР
// ═══════════════════════════════════════════════════

function renderInventory() {
  var main = document.querySelector("#overlay-inventory main");
  if (!main) return;

  var items = gameState.inventory.items;
  var keys = Object.keys(items);

  if (keys.length === 0) {
    main.innerHTML = '<div class="inventory-grid"><div class="inventory-empty">Інвентар порожній.</div></div>';
    return;
  }

  var html = '<div class="inventory-grid">';

  for (var i = 0; i < keys.length; i++) {
    var id = keys[i];
    var qty = items[id];
    var name = getItemName(id);

    html += '<div class="inventory-item">';
    html += '<div class="inventory-item-name">' + _escapeHtml(name) + '</div>';
    html += '<div class="inventory-item-qty">x' + qty + '</div>';
    html += '</div>';
  }

  html += '</div>';
  main.innerHTML = html;
}


// ═══════════════════════════════════════════════════
// РЕНДЕР: ШАФА ДУМОК
// ═══════════════════════════════════════════════════

function renderInsights() {
  var main = document.querySelector("#overlay-insights main");
  if (!main) return;

  var log = gameState.insights.log;
  var raw = gameState.insights.raw_thoughts;

  if ((!log || log.length === 0) && (!raw || raw.length === 0)) {
    main.innerHTML = '<div class="insights-empty">Шафа думок порожня. Спілкуйтесь з людьми — факти з\'являться.</div>';
    return;
  }

  var html = '<div class="insights-section">';

  // Необдумані зв'язки (зверху — потребують дії)
  if (raw && raw.length > 0) {
    html += '<div class="insights-group">';
    html += '<div class="insights-group-title">Необдумані зв\'язки</div>';

    for (var r = 0; r < raw.length; r++) {
      var thought = raw[r];
      html += '<div class="raw-thought" onclick="_contemplateThought(\'' +
        thought.id + '\')">';
      html += _escapeHtml(thought.text);
      html += '<div class="raw-thought-hint">Натисни щоб обдумати (30 хв)</div>';
      html += '</div>';
    }

    html += '</div>';
  }

  // Факти і зв'язки
  if (log && log.length > 0) {
    // Розділити на факти і зв'язки
    var facts = [];
    var connections = [];

    for (var i = 0; i < log.length; i++) {
      if (log[i].type === "connection") {
        connections.push(log[i]);
      } else {
        facts.push(log[i]);
      }
    }

    // Зв'язки
    if (connections.length > 0) {
      html += '<div class="insights-group">';
      html += '<div class="insights-group-title">Зв\'язки</div>';
      for (var c = 0; c < connections.length; c++) {
        html += '<div class="insight-item type-connection">' +
          _escapeHtml(connections[c].text) + '</div>';
      }
      html += '</div>';
    }

    // Факти
    if (facts.length > 0) {
      html += '<div class="insights-group">';
      html += '<div class="insights-group-title">Факти</div>';
      for (var f = facts.length - 1; f >= 0; f--) {
        html += '<div class="insight-item type-fact">' +
          _escapeHtml(facts[f].text) +
          ' <span style="color:rgba(255,255,255,0.2);font-size:12px;">День ' +
          facts[f].day + '</span></div>';
      }
      html += '</div>';
    }
  }

  html += '</div>';
  main.innerHTML = html;
}


// Обдумати зв'язок
function _contemplateThought(thoughtId) {
  contemplate(thoughtId);
  renderInsights(); // Перемалювати
  updateHUD();
}


// ═══════════════════════════════════════════════════
// РЕНДЕР: МІСІЇ
// ═══════════════════════════════════════════════════

function renderMissions() {
  var main = document.querySelector("#overlay-missions main");
  if (!main) return;

  var missions = gameState.missions.list;

  // Генерувати місії якщо пусто
  if ((!missions || missions.length === 0) && typeof generateMissions === "function") {
    generateMissions();
    missions = gameState.missions.list;
  }

  if (!missions || missions.length === 0) {
    main.innerHTML = '<div class="missions-empty">Сьогодні немає доступних місій.</div>';
    return;
  }

  var html = '<div class="missions-list">';

  for (var i = 0; i < missions.length; i++) {
    var m = missions[i];

    var cardClass = "mission-card";
    if (m.is_special) cardClass += " special";
    if (m.is_redemption) cardClass += " redemption";

    html += '<div class="' + cardClass + '" onclick="_selectMission(' + i + ')">';
    html += '<div class="mission-info">';
    html += '<div class="mission-name">' + _escapeHtml(m.name) + '</div>';
    html += '<div class="mission-meta">';
    html += '<span class="mission-meta-level">Рівень ' + m.level + '</span>';

    if (m.partner) {
      var partners = m.partner;
      if (m.partner2) partners += ', ' + m.partner2;
      html += '<span class="mission-meta-partner">Напарник: ' + _escapeHtml(partners) + '</span>';
    }

    html += '</div></div>';

    html += '<div class="mission-reward">';
    if (m.reward > 0) {
      html += '<div class="mission-reward-money">' + m.reward + ' крон</div>';
    }
    if (m.rep > 0) {
      html += '<div class="mission-reward-rep">+' + m.rep + ' реп.</div>';
    }
    html += '</div>';

    html += '</div>';
  }

  html += '</div>';
  main.innerHTML = html;
}


// Обрати та виконати місію
function _selectMission(index) {
  var missions = gameState.missions.list;
  if (!missions || index < 0 || index >= missions.length) return;

  var m = missions[index];
  gameState.missions.selected = index;

  // Закрити оверлей
  hideOverlay();
  hideHUD();
  if (typeof hidePager === "function") hidePager();

  // Запустити виконання місії
  _executeMission(m, index);
}


// Виконати місію: час, нагороди, травми, результат
function _executeMission(m, index) {
  // Час на місію: 60-120 хв залежно від рівня
  var missionTime = 60 + (m.level * 10);
  advanceTime(missionTime);

  // Партнер
  var partner = m.partner || null;
  var partner2 = m.partner2 || null;

  // Записати що ходили на місію з цим NPC
  if (partner) {
    gameState.missions.missions_today_with[partner] =
      (gameState.missions.missions_today_with[partner] || 0) + 1;
    gameState.missions.current_partner = partner;
  }
  if (partner2) {
    gameState.missions.missions_today_with[partner2] =
      (gameState.missions.missions_today_with[partner2] || 0) + 1;
    gameState.missions.current_partner2 = partner2;
  }

  // Кидок на травму
  var injuryResult = null;
  var injuryMessages = [];
  if (typeof rollMissionInjury === "function") {
    injuryResult = rollMissionInjury(m.level, partner, partner2);
    if (injuryResult && typeof applyMissionInjuries === "function") {
      var applied = applyMissionInjuries(injuryResult, partner, partner2);
      injuryMessages = applied.messages || [];
    }
  }

  // Нагороди
  if (m.reward > 0) addMoney(m.reward);
  if (m.rep > 0 && typeof addHexRep === "function") addHexRep(m.rep);

  // Хімія з партнером (+3 за місію)
  if (partner) {
    addChemistry(partner, 3);
    if (typeof resetInteraction === "function") resetInteraction(partner);
  }
  if (partner2) {
    addChemistry(partner2, 2);
    if (typeof resetInteraction === "function") resetInteraction(partner2);
  }

  // Скинути лічильник днів без місій
  if (typeof onMissionComplete === "function") onMissionComplete();

  // Видалити виконану місію зі списку
  gameState.missions.list.splice(index, 1);

  // Щоденник
  var journalText = "Місія: " + m.name + ". Рівень " + m.level + ".";
  if (m.reward > 0) journalText += " +" + m.reward + " крон.";
  if (m.rep > 0) journalText += " +" + m.rep + " реп.";
  if (typeof addJournalEntry === "function") addJournalEntry(journalText, "mission");

  // Показати результат місії
  _showMissionResult(m, injuryMessages);
}


// Показати результат місії як діалог
function _showMissionResult(m, injuryMessages) {
  var resultLines = [];
  resultLines.push("Місія завершена: " + m.name);

  if (m.reward > 0) resultLines.push("Нагорода: " + m.reward + " крон");
  if (m.rep > 0) resultLines.push("Репутація: +" + m.rep);

  // Травми
  for (var i = 0; i < injuryMessages.length; i++) {
    resultLines.push(injuryMessages[i]);
  }

  if (injuryMessages.length === 0) {
    resultLines.push("Без травм.");
  }

  // Побудувати тимчасовий скрипт для показу результату
  var nodes = [];
  for (var j = 0; j < resultLines.length; j++) {
    nodes.push({ type: "say", who: null, text: resultLines[j] });
  }
  nodes.push({ type: "end", text: "" });

  registerScript("_mission_result_temp", nodes);
  runScript("_mission_result_temp");
}


// ═══════════════════════════════════════════════════
// РЕНДЕР: МАГАЗИН
// ═══════════════════════════════════════════════════

var _shopCategory = "gift";

function renderShop() {
  _renderShopCategory(_shopCategory);
}

function switchShopCategory(cat) {
  _shopCategory = cat;
  _renderShopCategory(cat);
}

function _renderShopCategory(cat) {
  var main = document.querySelector("#overlay-shop main");
  if (!main) return;

  var categories = [
    {id: "gift",       label: "ПОДАРУНКИ"},
    {id: "decor",      label: "ДЕКОР"},
    {id: "consumable", label: "ВИТРАТНИКИ"},
    {id: "info",       label: "ІНФОРМАЦІЯ"}
  ];

  // Баланс
  var html = '<div class="shop-balance">Баланс: ' +
    gameState.money.amount + ' крон</div>';

  // Таби категорій
  html += '<div class="shop-tabs">';
  for (var t = 0; t < categories.length; t++) {
    var c = categories[t];
    html += '<button class="shop-tab' + (cat === c.id ? ' active' : '') +
      '" onclick="switchShopCategory(\'' + c.id + '\')">' + c.label + '</button>';
  }
  html += '</div>';

  // Сітка товарів
  var items = getCatalogByCategory(cat);

  html += '<div class="shop-grid">';

  for (var i = 0; i < items.length; i++) {
    var item = items[i];
    var owned = getItemCount(item.id) > 0;
    var canAfford = gameState.money.amount >= item.price;

    var itemClass = "shop-item";
    if (owned && (cat === "decor" || cat === "info")) itemClass += " owned";
    if (!canAfford && !owned) itemClass += " cant-afford";

    var onclick = (owned && (cat === "decor" || cat === "info")) ? "" :
      ' onclick="_shopBuyItem(\'' + item.id + '\')"';

    html += '<div class="' + itemClass + '"' + onclick + '>';
    html += '<div class="shop-item-name">' + _escapeHtml(item.name) + '</div>';
    html += '<div class="shop-item-price">' + item.price + ' крон</div>';

    if (owned && (cat === "decor" || cat === "info")) {
      html += '<div class="shop-item-owned">Придбано</div>';
    }

    html += '</div>';
  }

  html += '</div>';
  main.innerHTML = html;
}


// Купити предмет через магазин
function _shopBuyItem(itemId) {
  if (buyItem(itemId)) {
    _renderShopCategory(_shopCategory); // Перемалювати
    updateHUD();
  }
}


// ═══════════════════════════════════════════════════
// РЕНДЕР: КАВОМАШИНА
// ═══════════════════════════════════════════════════

function renderCoffee() {
  var main = document.querySelector("#overlay-coffee main");
  if (!main) return;

  var coffees = getAvailableCoffees();

  // Баланс
  var html = '<div class="coffee-balance">Баланс: ' +
    gameState.money.amount + ' крон</div>';

  // Список напоїв для покупки
  html += '<div class="coffee-menu">';

  for (var i = 0; i < coffees.length; i++) {
    var c = coffees[i];
    var canAfford = gameState.money.amount >= c.price;
    var itemClass = "coffee-item";
    if (!canAfford) itemClass += " cant-afford";

    html += '<div class="' + itemClass + '" onclick="_coffeeBuy(\'' + c.id + '\')">';
    html += '<div class="coffee-info">';
    html += '<div class="coffee-name">' + _escapeHtml(c.name) + '</div>';
    html += '<div class="coffee-desc">' + _escapeHtml(c.desc) + '</div>';
    html += '</div>';
    html += '<div class="coffee-price">' + c.price + ' крон</div>';
    html += '</div>';
  }

  html += '</div>';

  // Кава в інвентарі
  var coffeeList = getCoffeeList();
  if (coffeeList.length > 0) {
    html += '<div class="coffee-inventory">';
    html += '<div class="coffee-inventory-title">В інвентарі</div>';

    for (var j = 0; j < coffeeList.length; j++) {
      html += '<div class="coffee-inv-item">';
      html += '<span>' + _escapeHtml(coffeeList[j].name) + '</span>';
      html += '<span class="coffee-inv-qty">x' + coffeeList[j].qty + '</span>';
      html += '</div>';
    }

    html += '</div>';
  }

  main.innerHTML = html;
}


// Купити каву
function _coffeeBuy(coffeeId) {
  if (buyCoffee(coffeeId)) {
    renderCoffee(); // Перемалювати
    updateHUD();
  }
}


// ═══════════════════════════════════════════════════
// УТИЛІТИ
// ═══════════════════════════════════════════════════

// Екранування HTML
function _escapeHtml(text) {
  if (!text) return '';
  return String(text)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
