// ═══════════════════════════════════════════════════
// МЕНЕДЖЕР МІСІЙ ТА НАГОРОД
// ═══════════════════════════════════════════════════
//
// Порт з missions.rpy
//
// Пул напарників спільний — кожен NPC може бути на ОДНІЙ місії.
// Парна місія забирає 2 з пулу.
// Місія 5 = ранг 2+, місія 6 = ранг 4+.
// Спеціальні місії — condition-based, як DIALOGUE_ENTRIES.

// Назви місій (випадковий вибір)
var MISSION_NAMES_POOL = [
  "\u0422\u0438\u0445\u0435 \u043f\u0440\u043e\u043d\u0438\u043a\u043d\u0435\u043d\u043d\u044f",        // Тихе проникнення
  "\u0420\u043e\u0437\u0432\u0456\u0434\u043a\u0430 \u0442\u0435\u0440\u0438\u0442\u043e\u0440\u0456\u0457",  // Розвідка території
  "\u0421\u0443\u043f\u0440\u043e\u0432\u0456\u0434 \u043a\u0430\u0440\u0430\u0432\u0430\u043d\u0443",  // Супровід каравану
  "\u0420\u044f\u0442\u0443\u0432\u0430\u043b\u044c\u043d\u0430 \u043e\u043f\u0435\u0440\u0430\u0446\u0456\u044f", // Рятувальна операція
  "\u0417\u043b\u0430\u043c \u0432\u043e\u0440\u043e\u0436\u043e\u0457 \u0441\u0438\u0441\u0442\u0435\u043c\u0438", // Злам ворожої системи
  "\u0417\u043d\u0435\u0448\u043a\u043e\u0434\u0436\u0435\u043d\u043d\u044f \u0431\u043e\u043c\u0431\u0438",       // Знешкодження бомби
  "\u0417\u0430\u0445\u0438\u0441\u0442 \u0440\u0443\u0431\u0435\u0436\u0456\u0432",     // Захист рубежів
  "\u041d\u0456\u0447\u043d\u0438\u0439 \u043f\u0430\u0442\u0440\u0443\u043b\u044c",     // Нічний патруль
  "\u0421\u0430\u0431\u043e\u0442\u0430\u0436",                          // Саботаж
  "\u041f\u0435\u0440\u0435\u0445\u043e\u043f\u043b\u0435\u043d\u043d\u044f \u0434\u0430\u043d\u0438\u0445"  // Перехоплення даних
];


// Нагороди за рівнем місії
var MISSION_REWARDS = {
  1: {reward: 120, rep: 2},
  2: {reward: 200, rep: 3},
  3: {reward: 300, rep: 5},
  4: {reward: 420, rep: 7},
  5: {reward: 550, rep: 9},
  6: {reward: 700, rep: 12}
};


// Мінімальний ранг для місії
var MISSION_RANK_REQ = {
  1: 1,
  2: 1,
  3: 1,
  4: 1,
  5: 2,   // відкривається на ранзі 2
  6: 4    // відкривається на ранзі 4
};


// Спеціальні місії — condition-based (сцени заповнюють)
var SPECIAL_MISSION_ENTRIES = [];


registerState("missions", {
  list: [],                    // масив місій на сьогодні
  days_without_mission: 0,     // лічильник днів без місій
  selected: 0,                 // індекс обраної місії
  current_partner: null,       // напарник на поточній місії
  current_partner2: null,      // другий напарник (парна місія)
  missions_today_with: {}      // {"Артур": 2, ...} — скільки місій з ким сьогодні
});


// Перемішати масив (Fisher-Yates)
function _shuffleArray(arr) {
  var copy = arr.slice();
  for (var i = copy.length - 1; i > 0; i--) {
    var j = Math.floor(Math.random() * (i + 1));
    var tmp = copy[i];
    copy[i] = copy[j];
    copy[j] = tmp;
  }
  return copy;
}


// Повертає список eligible спеціальних місій
function getSpecialMissions() {
  var result = [];
  for (var i = 0; i < SPECIAL_MISSION_ENTRIES.length; i++) {
    var entry = SPECIAL_MISSION_ENTRIES[i];
    if (gameState.dispatcher.seen_dialogues.indexOf(entry.id) >= 0) continue;
    var conds = entry.conditions || {};
    if (!checkStableConditions(conds)) continue;

    // Chance
    var ch = entry.chance !== undefined ? entry.chance : 100;
    if (ch < 100 && (Math.floor(Math.random() * 100) + 1) > ch) continue;

    result.push(entry);
  }
  return result;
}


// Генерує місії на день.
// Пріоритет: квестові спецмісії -> звичайні -> аварійна.
// Пул напарників спільний.
function generateMissions() {
  var names = _shuffleArray(MISSION_NAMES_POOL);

  // Пул напарників (без тих хто в палаті — 3 стаки)
  var allNames = Object.keys(CAST);
  var pool = [];
  for (var pi = 0; pi < allNames.length; pi++) {
    var castName = allNames[pi];
    if (!isNpcInRecovery(castName)) {
      pool.push(castName);
    }
  }
  pool = _shuffleArray(pool);

  gameState.missions.list = [];

  // ═══ 1. СПЕЦМІСІЇ ПЕРШИМИ — квест має пріоритет ═══
  var specials = getSpecialMissions();
  for (var si = 0; si < specials.length; si++) {
    var special = specials[si];
    var spPartner = special.partner || null;
    var spPartner2 = special.partner2 || null;

    // Забрати напарників спецмісії з пулу
    if (spPartner) {
      var spIdx = pool.indexOf(spPartner);
      if (spIdx >= 0) pool.splice(spIdx, 1);
    }
    if (spPartner2) {
      var sp2Idx = pool.indexOf(spPartner2);
      if (sp2Idx >= 0) pool.splice(sp2Idx, 1);
    }

    gameState.missions.list.push({
      name: special.name || "\u0421\u041f\u0415\u0426\u041e\u041f\u0415\u0420\u0410\u0426\u0406\u042f", // СПЕЦОПЕРАЦІЯ
      level: special.level || 3,
      reward: special.reward || 0,
      rep: special.rep || 0,
      partner: spPartner,
      partner2: spPartner2,
      partner_count: special.partner_count || 0,
      is_special: true,
      special_id: special.id,
      special_label: special.label || null
    });
  }

  // ═══ 2. ЗВИЧАЙНІ МІСІЇ — по рівнях ═══
  var maxLevel = 6;
  for (var lvl = 1; lvl <= maxLevel; lvl++) {
    var mr = MISSION_REWARDS[lvl] || {reward: 100 * lvl, rep: lvl};
    var mName = names[(lvl - 1) % names.length];

    // Перевірка рангу
    var rankReq = MISSION_RANK_REQ[lvl] || 1;
    if (gameState.rank.syndicate_rank < rankReq) continue;

    // Напарник з пулу (забирається!)
    var partner = null;
    if (pool.length > 0) {
      partner = pool.shift();
    }

    var mission = {
      name: mName,
      level: lvl,
      reward: mr.reward,
      rep: mr.rep,
      partner: partner,
      partner2: null,
      partner_count: partner ? 1 : 0
    };

    // 15% шанс на парну місію (рівень 3+, є напарник, є ще хтось в пулі)
    if (partner && lvl >= 3 && pool.length > 0) {
      if ((Math.floor(Math.random() * 100) + 1) <= 15) {
        mission.partner2 = pool.shift();
        mission.partner_count = 2;
        mission.name = mission.name + " [\u041f\u0410\u0420\u041d\u0410]"; // [ПАРНА]
      }
    }

    gameState.missions.list.push(mission);
  }

  // Зберегти пул для подальшого оновлення слотів
  gameState.missions._remainingPool = pool.slice();

  // ═══ 3. АВАРІЙНА МІСІЯ — якщо neglect критичний ═══
  if (gameState.missions.days_without_mission >= 5) {
    // Перший персонаж з касту як напарник
    var firstKey = Object.keys(CAST)[0];
    var redemptionPartner = firstKey ? firstKey : null;

    gameState.missions.list.push({
      name: "\u0410\u0412\u0410\u0420\u0406\u0419\u041d\u0410 \u041e\u041f\u0415\u0420\u0410\u0426\u0406\u042f", // АВАРІЙНА ОПЕРАЦІЯ
      level: 4,
      reward: 0,
      rep: 0,
      partner: redemptionPartner,
      partner2: null,
      partner_count: redemptionPartner ? 1 : 0,
      is_redemption: true
    });
  }
}


// Оновити слот після виконання місії — нова назва, новий напарник.
// Слот залишається, місія не зникає.
function refreshMissionSlot(index) {
  var mission = gameState.missions.list[index];
  if (!mission) return;

  // Спецмісії не оновлюються — видаляються
  if (mission.is_special || mission.is_redemption) {
    gameState.missions.list.splice(index, 1);
    return;
  }

  // Нова назва
  var names = _shuffleArray(MISSION_NAMES_POOL);
  mission.name = names[0];

  // Повернути старого напарника в пул
  var pool = gameState.missions._remainingPool || [];
  if (mission.partner) pool.push(mission.partner);
  if (mission.partner2) pool.push(mission.partner2);
  pool = _shuffleArray(pool);

  // Новий напарник з пулу
  mission.partner = pool.length > 0 ? pool.shift() : null;
  mission.partner2 = null;
  mission.partner_count = mission.partner ? 1 : 0;

  // 15% парна (рівень 3+)
  if (mission.partner && mission.level >= 3 && pool.length > 0) {
    if (Math.floor(Math.random() * 100) + 1 <= 15) {
      mission.partner2 = pool.shift();
      mission.partner_count = 2;
      if (mission.name.indexOf("[ПАРНА]") < 0) {
        mission.name += " [ПАРНА]";
      }
    }
  }

  gameState.missions._remainingPool = pool;
}
