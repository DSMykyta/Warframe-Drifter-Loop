// ═══════════════════════════════════════════════════
// РУШІЙ
// ═══════════════════════════════════════════════════
//
// Дві частини:
// 1. Стан гри — системи реєструють свої дані
// 2. Персонажі — реєструються з characters.js
//
// Все зберігається і завантажується автоматично.


// ─── СТАН ГРИ ───

var gameState = {};
var _stateDefaults = {};

function registerState(name, defaults) {
  _stateDefaults[name] = JSON.parse(JSON.stringify(defaults));
  gameState[name] = JSON.parse(JSON.stringify(defaults));
}

function resetState() {
  for (var name in _stateDefaults) {
    gameState[name] = JSON.parse(JSON.stringify(_stateDefaults[name]));
  }
}

function serializeState() {
  return JSON.parse(JSON.stringify(gameState));
}

function deserializeState(data) {
  for (var name in data) {
    if (name in gameState) {
      gameState[name] = data[name];
    }
  }
}


// ─── ПЕРСОНАЖІ ───

var CAST = {};          // "ar" → { short: "ar", name: "Артур", full: "Артур Найтінгейл", abilities: [...] }
var CAST_BY_NAME = {};  // "Артур" → те саме

//                c(short, name, full, missions, romance, telepathy)
function c(short, name, full, missions, romance, telepathy) {
  var data = {
    short: short,
    name: name,
    full: full,
    missions: missions,
    romance: romance,
    telepathy: telepathy,
  };
  CAST[short] = data;
  CAST_BY_NAME[name] = data;

  // Якщо має хімію — додати автоматично
  if ((missions || romance) && gameState.chemistry) {
    gameState.chemistry.values[name] = gameState.chemistry.values[name] || 0;
    gameState.chemistry.gainedToday[name] = gameState.chemistry.gainedToday[name] || 0;
  }
}

// Отримати ім'я для діалогу за скороченням
function charName(short) {
  return CAST[short] ? CAST[short].name : short;
}

// Перевірити чи персонаж має здатність
function charCan(short, ability) {
  return CAST[short] && CAST[short][ability];
}

// Список всіх хто має здатність
function charsWith(ability) {
  var result = [];
  for (var short in CAST) {
    if (CAST[short][ability]) result.push(CAST[short].name);
  }
  return result;
}
