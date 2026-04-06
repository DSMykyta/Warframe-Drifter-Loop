// ═══════════════════════════════════════════════════
// ЛОКАЦІЇ + ТРИГЕРНИЙ РУХ ПЕРСОНАЖІВ
// ═════════════════════════════════════��═════════════
//
// Порт з triggers.rpy
//
// Система визначає де кожен NPC знаходиться в конкретний момент.
// Пріоритети: тригер (скрипт) > обіцянка > дім.
// Якщо два NPC хочуть бути в одній локації без парного контенту —
// NPC з нижчим пріоритетом залишається вдома.

// ═══ ГРАФ ЛОКАЦІЙ ═══

var LOCATION_GRAPH = {
  "mall":       ["info_desk","security_desk","arcade","music_shop","furniture",
                 "range","medbay","bar","foodcourt","comp_club","garage",
                 "rooftop","balcony","cafe","cafe_balcony",
                 "utility","warehouse","backroom","clothing_shop",
                 "cinema","gym","billiard","barbershop","photo_studio",
                 "laundry","parking","wc","pharmacy","room_2",
                 "video_rental","electronics","jewelry","bookshop"],
  "info_desk":      ["mall"],
  "security_desk":  ["mall", "security_room"],
  "security_room":  ["security_desk"],
  "arcade":         ["mall"],
  "music_shop":     ["mall"],
  "furniture":      ["mall"],
  "range":          ["mall"],
  "medbay":         ["mall", "recovery_room"],
  "recovery_room":  ["medbay"],
  "bar":            ["mall"],
  "foodcourt":      ["mall"],
  "comp_club":      ["mall"],
  "garage":         ["mall"],
  "backroom":       ["mall"],
  "rooftop":        ["mall"],
  "balcony":        ["mall"],
  "cafe":           ["mall", "cafe_balcony"],
  "cafe_balcony":   ["mall", "cafe"],
  "utility":        ["mall"],
  "warehouse":      ["mall"],
  "clothing_shop":  ["mall"],
  "cinema":         ["mall"],
  "gym":            ["mall"],
  "billiard":       ["mall"],
  "barbershop":     ["mall"],
  "photo_studio":   ["mall"],
  "laundry":        ["mall"],
  "parking":        ["mall"],
  "wc":             ["mall"],
  "pharmacy":       ["mall"],
  "room_2":         ["mall"],
  "video_rental":   ["mall"],
  "electronics":    ["mall"],
  "jewelry":        ["mall"],
  "bookshop":       ["mall"]
};

// Українські назви
var LOCATION_NAMES = {
  "mall":           "\u041c\u043e\u043b \u0413\u044c\u043e\u043b\u044c\u0432\u0430\u043d\u0456\u0457",
  "info_desk":      "\u0406\u043d\u0444\u043e-\u043e\u0441\u0442\u0440\u0456\u0432\u0435\u0446\u044c",
  "security_desk":  "\u0421\u0442\u0456\u0439\u043a\u0430 \u043e\u0445\u043e\u0440\u043e\u043d\u0438",
  "security_room":  "\u041a\u0456\u043c\u043d\u0430\u0442\u0430 \u043e\u0445\u043e\u0440\u043e\u043d\u0438",
  "arcade":         "\u0410\u0440\u043a\u0430\u0434\u0438",
  "music_shop":     "\u041c\u0443\u0437\u0438\u0447\u043d\u0438\u0439 \u043c\u0430\u0433\u0430\u0437\u0438\u043d",
  "furniture":      "\u041c\u0430\u0433\u0430\u0437\u0438\u043d \u043c\u0435\u0431\u043b\u0456\u0432",
  "range":          "\u0422\u0438\u0440",
  "medbay":         "\u041c\u0435\u0434\u0432\u0456\u0434\u0434\u0456\u043b",
  "bar":            "\u0411\u0430\u0440",
  "foodcourt":      "\u0424\u0443\u0442\u043a\u043e\u0440\u0442",
  "comp_club":      "\u041a\u043e\u043c\u043f'\u044e\u0442\u0435\u0440\u043d\u0438\u0439 \u043a\u043b\u0443\u0431",
  "garage":         "\u0413\u0430\u0440\u0430\u0436",
  "backroom":       "\u0411\u0435\u043a\u0440\u0443\u043c",
  "rooftop":        "\u0414\u0430\u0445",
  "balcony":        "\u0411\u0430\u043b\u043a\u043e\u043d 2-\u0433\u043e \u043f\u043e\u0432\u0435\u0440\u0445\u0443",
  "cafe":           "\u041a\u0430\u0432'\u044f\u0440\u043d\u044f",
  "cafe_balcony":   "\u0411\u0456\u043b\u044f \u043a\u0430\u0432'\u044f\u0440\u043d\u0456 (2 \u043f\u043e\u0432\u0435\u0440\u0445)",
  "utility":        "\u041f\u0456\u0434\u0441\u043e\u0431\u043a\u0430",
  "warehouse":      "\u0421\u043a\u043b\u0430\u0434",
  "clothing_shop":  "\u041c\u0430\u0433\u0430\u0437\u0438\u043d \u043e\u0434\u044f\u0433\u0443",
  "recovery_room":  "\u041f\u0430\u043b\u0430\u0442\u0430",
  "cinema":         "\u041a\u0456\u043d\u043e\u0442\u0435\u0430\u0442\u0440",
  "gym":            "\u0421\u043f\u043e\u0440\u0442\u0437\u0430\u043b",
  "billiard":       "\u0411\u0456\u043b\u044c\u044f\u0440\u0434\u043d\u0430",
  "barbershop":     "\u041f\u0435\u0440\u0443\u043a\u0430\u0440\u043d\u044f",
  "photo_studio":   "\u0424\u043e\u0442\u043e\u0441\u0442\u0443\u0434\u0456\u044f",
  "laundry":        "\u041f\u0440\u0430\u043b\u044c\u043d\u044f",
  "parking":        "\u041f\u0430\u0440\u043a\u043e\u0432\u043a\u0430",
  "wc":             "\u0412\u0431\u0438\u0440\u0430\u043b\u044c\u043d\u044f",
  "pharmacy":       "\u0410\u043f\u0442\u0435\u043a\u0430",
  "room_2":         "\u041a\u0456\u043c\u043d\u0430\u0442\u0430 2",
  "video_rental":   "\u0412\u0456\u0434\u0435\u043e\u043f\u0440\u043e\u043a\u0430\u0442",
  "electronics":    "\u0415\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u0456\u043a\u0430 / \u0442\u0435\u0445\u043d\u0456\u043a\u0430",
  "jewelry":        "\u042e\u0432\u0435\u043b\u0456\u0440\u043d\u0438\u0439",
  "bookshop":       "\u041a\u043d\u0438\u0433\u0430\u0440\u043d\u044f"
};

// Домашні локації (заповнюються з CAST)
var HOME_LOCATIONS = {};

// Суміжні локації: дочірня -> батьківська
var ADJACENT_LOCATIONS = {
  "security_room": "security_desk",
  "recovery_room": "medbay"
};

// Поєднані локації (миттєвий перехід)
var PAIRED_LOCATIONS = [
  ["cafe", "cafe_balcony"],
  ["cafe_balcony", "cafe"]
];

// Закриті локації: id -> флаг для відкриття
var LOCKED_LOCATIONS = {
  "garage": "garage_unlocked",
  "recovery_room": "recovery_room_never_unlocked"
};

// Приховані локації: id -> флаг для появи
var HIDDEN_LOCATIONS = {
  "bar":            "syndicate_rank_3",
  "rooftop":        "rooftop_unlocked",
  "security_room":  "security_room_unlocked",
  "warehouse":      "warehouse_unlocked",
  "utility":        "utility_unlocked",
  "comp_club":      "comp_club_unlocked",
  "balcony":        "balcony_unlocked",
  "cinema":         "cinema_unlocked",
  "gym":            "gym_unlocked",
  "billiard":       "billiard_unlocked",
  "barbershop":     "barbershop_unlocked",
  "photo_studio":   "photo_studio_unlocked",
  "laundry":        "laundry_unlocked",
  "parking":        "parking_unlocked",
  "wc":             "wc_unlocked",
  "pharmacy":       "pharmacy_unlocked",
  "room_2":         "room_2_unlocked",
  "video_rental":   "video_rental_unlocked",
  "electronics":    "electronics_unlocked",
  "jewelry":        "jewelry_unlocked",
  "bookshop":       "bookshop_unlocked",
  "cafe":           "cafe_unlocked",
  "cafe_balcony":   "cafe_balcony_unlocked"
};


// ═══ ТРИГЕРИ ПЕРЕМІЩЕННЯ ═══
// Масив об'єктів: {id, chars, location, condition}
// condition — функція що повертає true/false

var LOCATION_TRIGGERS = [
  // День 1: всі в молі до кінця інтро
  {
    id: "day_1_all_mall",
    chars: [], // заповниться після завантаження CAST
    location: "mall",
    condition: function() {
      return gameState.time.day === 1 && !getFlag("intro_done");
    }
  },

  // Вечірній збір у барі (після 20:00)
  {
    id: "group_event_bar",
    chars: [],
    location: "bar",
    condition: function() {
      return getFlag("group_bar_tonight_active") && gameState.time.minutes >= 1200;
    }
  },

  // Артур на даху після сварки з Елеонор
  {
    id: "arthur_rooftop_fight",
    chars: ["\u0410\u0440\u0442\u0443\u0440"],
    location: "rooftop",
    condition: function() {
      return getFlag("arthur_eleanor_fight_active") && !getFlag("arthur_fight_resolved");
    }
  },

  // Елеонор в бекрумі після сварки
  {
    id: "eleanor_backroom_fight",
    chars: ["\u0415\u043b\u0435\u043e\u043d\u043e\u0440"],
    location: "backroom",
    condition: function() {
      return getFlag("arthur_eleanor_fight_active") && !getFlag("arthur_fight_resolved");
    }
  },

  // Травмовані NPC (1-2 стаки) — в медвідділі
  {id: "arthur_injured_medbay",  chars: ["\u0410\u0440\u0442\u0443\u0440"],  location: "medbay",
    condition: function() { return getInjuryStacks("\u0410\u0440\u0442\u0443\u0440") >= 1 && !isNpcInRecovery("\u0410\u0440\u0442\u0443\u0440"); }},
  {id: "eleanor_injured_medbay", chars: ["\u0415\u043b\u0435\u043e\u043d\u043e\u0440"], location: "medbay",
    condition: function() { return getInjuryStacks("\u0415\u043b\u0435\u043e\u043d\u043e\u0440") >= 1 && !isNpcInRecovery("\u0415\u043b\u0435\u043e\u043d\u043e\u0440"); }},
  {id: "amir_injured_medbay",    chars: ["\u0410\u043c\u0456\u0440"],    location: "medbay",
    condition: function() { return getInjuryStacks("\u0410\u043c\u0456\u0440") >= 1 && !isNpcInRecovery("\u0410\u043c\u0456\u0440"); }},
  {id: "aoi_injured_medbay",     chars: ["\u0410\u043e\u0456"],     location: "medbay",
    condition: function() { return getInjuryStacks("\u0410\u043e\u0456") >= 1 && !isNpcInRecovery("\u0410\u043e\u0456"); }},
  {id: "quincy_injured_medbay",  chars: ["\u041a\u0432\u0456\u043d\u0441\u0456"],  location: "medbay",
    condition: function() { return getInjuryStacks("\u041a\u0432\u0456\u043d\u0441\u0456") >= 1 && !isNpcInRecovery("\u041a\u0432\u0456\u043d\u0441\u0456"); }},

  // Критично травмовані (3 стаки) — в палаті
  {id: "arthur_recovery",  chars: ["\u0410\u0440\u0442\u0443\u0440"],  location: "recovery_room",
    condition: function() { return isNpcInRecovery("\u0410\u0440\u0442\u0443\u0440"); }},
  {id: "eleanor_recovery", chars: ["\u0415\u043b\u0435\u043e\u043d\u043e\u0440"], location: "recovery_room",
    condition: function() { return isNpcInRecovery("\u0415\u043b\u0435\u043e\u043d\u043e\u0440"); }},
  {id: "amir_recovery",    chars: ["\u0410\u043c\u0456\u0440"],    location: "recovery_room",
    condition: function() { return isNpcInRecovery("\u0410\u043c\u0456\u0440"); }},
  {id: "aoi_recovery",     chars: ["\u0410\u043e\u0456"],     location: "recovery_room",
    condition: function() { return isNpcInRecovery("\u0410\u043e\u0456"); }},
  {id: "quincy_recovery",  chars: ["\u041a\u0432\u0456\u043d\u0441\u0456"],  location: "recovery_room",
    condition: function() { return isNpcInRecovery("\u041a\u0432\u0456\u043d\u0441\u0456"); }},

  // Аоі шукає інгредієнти на футкорті
  {
    id: "aoi_foodcourt",
    chars: ["\u0410\u043e\u0456"],
    location: "foodcourt",
    condition: function() { return getFlag("aoi_ingredients_active"); }
  },

  // Квінсі злий — пішов на дах
  {
    id: "quincy_rooftop_angry",
    chars: ["\u041a\u0432\u0456\u043d\u0441\u0456"],
    location: "rooftop",
    condition: function() { return getFlag("quincy_angry_active"); }
  },

  // Обідній час: Амір на футкорті
  {
    id: "lunch_foodcourt",
    chars: ["\u0410\u043c\u0456\u0440"],
    location: "foodcourt",
    condition: function() {
      return gameState.time.minutes >= 720 && gameState.time.minutes < 840 && gameState.time.day > 1;
    }
  }
];


// Ініціалізувати домашні локації та chars для масових тригерів.
// Викликається після завантаження CAST.
function initTriggerData() {
  var castKeys = Object.keys(CAST);
  var allNames = [];
  for (var i = 0; i < castKeys.length; i++) {
    var name = CAST[castKeys[i]].name;
    allNames.push(name);
    // HOME_LOCATIONS заповнюється з CAST
    // (data.home має бути визначений в c() або завантажений)
  }

  // Заповнити chars для масових тригерів (день 1, бар)
  for (var t = 0; t < LOCATION_TRIGGERS.length; t++) {
    var trig = LOCATION_TRIGGERS[t];
    if (trig.id === "day_1_all_mall" || trig.id === "group_event_bar") {
      trig.chars = allNames.slice();
    }
  }
}


// ═══ ДОПОМІЖНІ ФУНКЦІЇ ЛОКАЦІЙ ═══

function _isPaired(locA, locB) {
  for (var i = 0; i < PAIRED_LOCATIONS.length; i++) {
    if (PAIRED_LOCATIONS[i][0] === locA && PAIRED_LOCATIONS[i][1] === locB) return true;
  }
  return false;
}

function _isLocked(loc) {
  var flag = LOCKED_LOCATIONS[loc];
  if (!flag) return false;
  return !getFlag(flag);
}

function _isHidden(loc) {
  var flag = HIDDEN_LOCATIONS[loc];
  if (!flag) return false;
  return !getFlag(flag);
}

function _isTriggersAccessible(loc) {
  return !_isLocked(loc) && !_isHidden(loc);
}


// ═══ ОБІЦЯНКИ ЯК ТРИГЕРИ ═══

function _checkPromiseLocation(name) {
  var promises = gameState.promises.list;
  for (var i = 0; i < promises.length; i++) {
    var p = promises[i];
    if (p.who === name && p.day === gameState.time.day) {
      if (gameState.time.minutes >= p.from_min && gameState.time.minutes < p.to_min) {
        return p.where;
      }
    }
  }
  return null;
}


// ═══ СУМІСНІСТЬ В ЛОКАЦІЇ ═══

function _isScriptedTogether(names, location) {
  for (var i = LOCATION_TRIGGERS.length - 1; i >= 0; i--) {
    var trig = LOCATION_TRIGGERS[i];
    if (trig.location !== location) continue;
    if (trig.chars.length < 2) continue;
    if (!trig.condition()) continue;
    var allIn = true;
    for (var n = 0; n < names.length; n++) {
      if (trig.chars.indexOf(names[n]) < 0) { allIn = false; break; }
    }
    if (allIn) return true;
  }
  return false;
}

function _hasPairContent(nameA, nameB, location) {
  for (var i = 0; i < BANTER_ENTRIES.length; i++) {
    var entry = BANTER_ENTRIES[i];
    if (gameState.dispatcher.seen_dialogues.indexOf(entry.id) >= 0) continue;
    var entryLoc = entry.location !== undefined ? entry.location : null;
    if (entryLoc !== null && entryLoc !== location) continue;
    if (entry.chars && entry.chars.length === 2) {
      if (entry.chars.indexOf(nameA) >= 0 && entry.chars.indexOf(nameB) >= 0) {
        var conds = entry.conditions || {};
        if (checkStableConditions(conds)) return true;
      }
    }
  }
  return false;
}

function _hasPromiseAt(name, location) {
  var promises = gameState.promises.list;
  for (var i = 0; i < promises.length; i++) {
    var p = promises[i];
    if (p.who === name && p.day === gameState.time.day) {
      if (gameState.time.minutes >= p.from_min && gameState.time.minutes < p.to_min) {
        if (p.where === location) return true;
      }
    }
  }
  return false;
}

function _locationPriority(name, location) {
  // 3 = дім, 2 = скриптовий тригер, 1 = обіцянка, 0 = інший тригер
  if (HOME_LOCATIONS[name] === location) return 3;

  for (var i = LOCATION_TRIGGERS.length - 1; i >= 0; i--) {
    var trig = LOCATION_TRIGGERS[i];
    if (trig.chars.indexOf(name) >= 0 && trig.location === location && trig.condition()) {
      if (trig.chars.length >= 2) return 2;
      return 0;
    }
  }

  if (_hasPromiseAt(name, location)) return 1;
  return 0;
}


// ═══ ГОЛОВНА ФУНКЦІЯ: ДЕ ПЕРСОНАЖ? ═══

// Визначає бажану локацію без перевірки зайнятості
function _getRawLocation(name) {
  if (isNpcAbsent(name)) return null;
  if (isNight()) return null;

  // Тригери (останній — найпріоритетніший)
  for (var i = LOCATION_TRIGGERS.length - 1; i >= 0; i--) {
    var trig = LOCATION_TRIGGERS[i];
    if (trig.chars.indexOf(name) >= 0 && trig.condition()) {
      return trig.location;
    }
  }

  // Обіцянка
  var promiseLoc = _checkPromiseLocation(name);
  if (promiseLoc) return promiseLoc;

  // Дім
  return HOME_LOCATIONS[name] || "mall";
}


// Визначає поточну локацію персонажа з урахуванням конфліктів.
function getCharLocation(name) {
  var loc = _getRawLocation(name);
  if (loc === null) return null;

  var home = HOME_LOCATIONS[name] || "mall";
  if (loc === home) return loc;

  // Хто ще хоче бути в цій локації?
  var allNames = Object.keys(CAST);
  var others = [];
  for (var i = 0; i < allNames.length; i++) {
    var otherName = CAST[allNames[i]].name;
    if (otherName !== name && _getRawLocation(otherName) === loc) {
      others.push(otherName);
    }
  }
  if (others.length === 0) return loc;

  // Скриптовий тригер зібрав разом — ок
  if (_isScriptedTogether([name].concat(others), loc)) return loc;

  // Є парний контент — ок
  for (var j = 0; j < others.length; j++) {
    if (_hasPairContent(name, others[j], loc)) return loc;
  }

  // Обіцянки привели обох — ок
  if (_hasPromiseAt(name, loc)) {
    for (var k = 0; k < others.length; k++) {
      if (_hasPromiseAt(others[k], loc)) return loc;
    }
  }

  // Конфлікт: хто має вищий пріоритет — той залишається
  var myPri = _locationPriority(name, loc);
  var maxOtherPri = 0;
  for (var m = 0; m < others.length; m++) {
    var otherPri = _locationPriority(others[m], loc);
    if (otherPri > maxOtherPri) maxOtherPri = otherPri;
  }
  if (myPri >= maxOtherPri) return loc;

  return home;
}


// Повертає список персонажів у локації
function getCharsAt(location) {
  if (isNight()) return [];
  var result = [];
  var allNames = Object.keys(CAST);
  for (var i = 0; i < allNames.length; i++) {
    var name = CAST[allNames[i]].name;
    if (getCharLocation(name) === location) {
      result.push(name);
    }
  }
  return result;
}
