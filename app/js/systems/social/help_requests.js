// ═══════════════════════════════════════════════════
// ЗАПИТИ ДОПОМОГИ ЧЕРЕЗ ПЕЙДЖЕР
// ═══════════════════════════════════════════════════
//
// Порт з help_requests.rpy
//
// NPC надсилають запити допомоги на пейджер.
// Один запит на день. 30% шанс кожен. 45 хв, +100 крон, +4 хімія.

// Масив запитів допомоги (сцени можуть додавати свої)
var HELP_REQUEST_ENTRIES = [
  {
    id: "lettie_help_meds",
    who: "\u041b\u0435\u0442\u0442\u0456",   // Летті
    conditions: {
      flag_false: ["helped_lettie_today"],
      chemistry_min: ["\u041b\u0435\u0442\u0442\u0456", 10],
      time_min: 600,
      time_max: 1320
    },
    chance: 30,
    message: "\u041f\u043e\u0442\u0440\u0456\u0431\u043d\u0430 \u0434\u043e\u043f\u043e\u043c\u043e\u0433\u0430 \u0437 \u043c\u0435\u0434\u0438\u043a\u0430\u043c\u0435\u043d\u0442\u0430\u043c\u0438. \u0417\u0430\u0439\u0434\u0435\u0448?",
    // Потрібна допомога з медикаментами. Зайдеш?
    location: "medbay"
  },
  {
    id: "amir_help_arcade",
    who: "\u0410\u043c\u0456\u0440",    // Амір
    conditions: {
      flag_false: ["helped_amir_today"],
      chemistry_min: ["\u0410\u043c\u0456\u0440", 10],
      time_min: 600,
      time_max: 1320
    },
    chance: 30,
    message: "\u0410\u0412\u0422\u041e\u041c\u0410\u0422 \u0417\u041d\u041e\u0412 \u0417\u041b\u0410\u041c\u0410\u0412\u0421\u042f \u0434\u043e\u043f\u043e\u043c\u043e\u0436\u0438\u0438\u0438\u0438\u0438",
    // АВТОМАТ ЗНОВ ЗЛАМАВСЯ допоможиииии
    location: "arcade"
  },
  {
    id: "arthur_help_reports",
    who: "\u0410\u0440\u0442\u0443\u0440",   // Артур
    conditions: {
      flag_false: ["helped_arthur_today"],
      chemistry_min: ["\u0410\u0440\u0442\u0443\u0440", 10],
      time_min: 600,
      time_max: 1320
    },
    chance: 30,
    message: "\u0417\u0432\u0456\u0442\u0438 \u0441\u0430\u043c\u0456 \u0441\u0435\u0431\u0435 \u043d\u0435 \u0440\u043e\u0437\u0431\u0435\u0440\u0443\u0442\u044c. \u0412\u0456\u043b\u044c\u043d\u0438\u0439?",
    // Звіти самі себе не розберуть. Вільний?
    location: "info_desk"
  },
  {
    id: "aoi_help_records",
    who: "\u0410\u043e\u0456",     // Аоі
    conditions: {
      flag_false: ["helped_aoi_today"],
      chemistry_min: ["\u0410\u043e\u0456", 10],
      time_min: 600,
      time_max: 1320
    },
    chance: 30,
    message: "\u0414\u043e\u043f\u043e\u043c\u043e\u0436\u0435\u0448 \u0441\u043a\u043b\u0430\u0441\u0442\u0438 \u043f\u043b\u0430\u0442\u0456\u0432\u043a\u0438?",
    // Допоможеш скласти платівки?
    location: "music_shop"
  },
  {
    id: "quincy_help_range",
    who: "\u041a\u0432\u0456\u043d\u0441\u0456",  // Квінсі
    conditions: {
      flag_false: ["helped_quincy_today"],
      chemistry_min: ["\u041a\u0432\u0456\u043d\u0441\u0456", 10],
      time_min: 600,
      time_max: 1320
    },
    chance: 30,
    message: "range needs cleaning. u in or what",
    location: "range"
  },
  {
    id: "eleanor_help_notes",
    who: "\u0415\u043b\u0435\u043e\u043d\u043e\u0440", // Елеонор
    conditions: {
      flag_false: ["helped_eleanor_today"],
      chemistry_min: ["\u0415\u043b\u0435\u043e\u043d\u043e\u0440", 10],
      time_min: 600,
      time_max: 1320
    },
    chance: 30,
    message: "\u041c\u0430\u044e \u0437\u0430\u043f\u0438\u0441\u0438 \u044f\u043a\u0456 \u0442\u0440\u0435\u0431\u0430 \u0441\u0438\u0441\u0442\u0435\u043c\u0430\u0442\u0438\u0437\u0443\u0432\u0430\u0442\u0438.",
    // Маю записи які треба систематизувати.
    location: "furniture"
  }
];


// Перевіряє чи є eligible help request. Повертає запис або null.
function checkHelpRequests() {
  // Один запит на день
  if (getFlag("helped_someone_today")) return null;

  for (var i = 0; i < HELP_REQUEST_ENTRIES.length; i++) {
    var entry = HELP_REQUEST_ENTRIES[i];
    var conds = entry.conditions || {};

    // Перевірити chemistry_min
    if (conds.chemistry_min) {
      var cmName = conds.chemistry_min[0];
      var cmVal = conds.chemistry_min[1];
      if ((gameState.chemistry.values[cmName] || 0) < cmVal) continue;
    }

    // Перевірити flag_false
    if (conds.flag_false) {
      var skip = false;
      for (var f = 0; f < conds.flag_false.length; f++) {
        if (getFlag(conds.flag_false[f])) {
          skip = true;
          break;
        }
      }
      if (skip) continue;
    }

    // Перевірити час
    if (conds.time_min !== undefined && gameState.time.minutes < conds.time_min) continue;
    if (conds.time_max !== undefined && gameState.time.minutes >= conds.time_max) continue;

    // Chance
    var ch = entry.chance || 30;
    if ((Math.floor(Math.random() * 100) + 1) <= ch) {
      return entry;
    }
  }

  return null;
}


// Виконує запит допомоги.
// Баланс v2: 45 хв, +100 крон, +4 хімія.
function executeHelpRequest(entry) {
  var who = entry.who;
  var loc = entry.location || "mall";

  // Переміщення
  gameState.location.current = loc;
  advanceTime(45);

  // Нагороди
  addMoney(100);
  addChemistry(who, 4);
  resetInteraction(who);

  // Флаги
  setFlag("helped_" + charFlag(who) + "_today");
  setFlag("helped_someone_today");
}
