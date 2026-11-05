// ═══════════════════════════════════════════════════
// ЛОКАЦІЇ
// ═══════════════════════════════════════════════════
//
// 5 типів:
//   standard  — звичайна, з'єднана з молом
//   adjacent  — доступна тільки через батьківську (parent)
//   paired    — дві секції одного місця, перехід 0 хв
//   locked    — видно на карті із замочком, треба unlock_flag
//   hidden    — не видно поки нема unlock_flag
//
// 2 поверхи: floor 1 і floor 2
//
// Дані завантажуються з locations.csv

var LOCATIONS = {};

registerState("location", {
  current: "backroom",
});

// Завантажити локації з CSV
function loadLocations(callback) {
  loadCSV("data/locations.csv", function(rows) {
    for (var i = 0; i < rows.length; i++) {
      var r = rows[i];
      LOCATIONS[r.id] = {
        id: r.id,
        name: r.name,
        floor: parseInt(r.floor),
        type: r.type,
        parent: r.parent || null,
        connects: r.connects ? r.connects.split(";") : [],
        unlock_flag: r.unlock_flag || null,
      };
    }
    if (callback) callback();
  });
}

// Чи локація доступна?
function isAccessible(id) {
  var loc = LOCATIONS[id];
  if (!loc) return false;
  if (loc.type === "hidden" && loc.unlock_flag && !getFlag(loc.unlock_flag)) return false;
  if (loc.type === "locked" && loc.unlock_flag && !getFlag(loc.unlock_flag)) return false;
  return true;
}

// Чи локація видна на карті?
function isVisible(id) {
  var loc = LOCATIONS[id];
  if (!loc) return false;
  if (loc.type === "hidden" && loc.unlock_flag && !getFlag(loc.unlock_flag)) return false;
  if (loc.type === "adjacent") return false;
  return true;
}

// Вартість переміщення в хвилинах
function travelCost(from, to) {
  if (from === to) return 0;
  if (!isAccessible(to)) return -1;
  var locTo = LOCATIONS[to];
  // Суміжна — тільки з батьківської
  if (locTo && locTo.type === "adjacent") {
    if (locTo.parent === from) return 5;
    return 15;
  }
  // Поєднані — 0 хв
  var locFrom = LOCATIONS[from];
  if (locFrom && locTo) {
    if (locFrom.connects.indexOf(to) >= 0 && locTo.connects.indexOf(from) >= 0) {
      // Обидві вказують одна на одну — paired
      if (locFrom.type !== "standard" || locTo.type !== "standard") return 0;
    }
  }
  // Сусідні (мол↔точка) — 5 хв
  if (from === "mall" || to === "mall") return 5;
  // Все інше — через мол — 10 хв
  return 10;
}

// Переміститись
function travelTo(destination) {
  if (!isAccessible(destination)) return false;
  var cost = travelCost(gameState.location.current, destination);
  if (cost < 0) return false;
  if (cost > 0) advanceTime(cost);
  gameState.location.current = destination;
  autoSave();
  return true;
}

// Назва поточної локації
function currentLocationName() {
  var loc = LOCATIONS[gameState.location.current];
  return loc ? loc.name : "???";
}

// Список доступних локацій з поточної
function getReachableLocations() {
  var result = [];
  for (var id in LOCATIONS) {
    if (id === gameState.location.current) continue;
    if (!isVisible(id)) continue;
    if (!isAccessible(id)) {
      // Закрита — показати із замочком
      result.push({ id: id, name: LOCATIONS[id].name, locked: true, floor: LOCATIONS[id].floor });
    } else {
      result.push({ id: id, name: LOCATIONS[id].name, locked: false, floor: LOCATIONS[id].floor });
    }
  }
  return result;
}

// Локації по поверхах
function getLocationsByFloor(floor) {
  return getReachableLocations().filter(function(l) { return l.floor === floor; });
}
