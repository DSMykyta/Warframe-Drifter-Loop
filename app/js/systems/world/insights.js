// ═══════════════════════════════════════════════════
// ШАФА ДУМОК (INSIGHTS) + ЩОДЕННИК
// ═══════════════════════════════════════════════════
//
// Порт з dispatcher.rpy (секція INSIGHTS + JOURNAL)
//
// Два типи записів:
// 1. Факти (add_insight) — миттєві, від діалогів
// 2. Зв'язки (raw_thoughts) — потребують 2+ факти + 30 хв "обдумування"
//
// Щоденник — окремий лог подій/записів Дріфтера.

// Зв'язки — потребують 2+ факти для появи, потім 30 хв "обдумування"
var RAW_THOUGHT_DEFS = [
  {
    id: "thought_arthur_leadership",
    requires: ["arthur_leader", "arthur_cooks_for_team"],
    text: "\u0410\u0440\u0442\u0443\u0440 \u043b\u0456\u0434\u0438\u0440\u0443\u0454 \u043d\u0435 \u043d\u0430\u043a\u0430\u0437\u0430\u043c\u0438, \u0430 \u0442\u0443\u0440\u0431\u043e\u0442\u043e\u044e. \u0413\u043e\u0442\u0443\u0454 \u0434\u043b\u044f \u0432\u0441\u0456\u0445, \u0431\u0435\u0440\u0435 \u0432\u0456\u0434\u043f\u043e\u0432\u0456\u0434\u0430\u043b\u044c\u043d\u0456\u0441\u0442\u044c. \u0426\u0435 \u043d\u0435 \u043f\u0440\u043e\u0441\u0442\u043e \u043a\u043e\u043c\u0430\u043d\u0434\u0438\u0440 \u2014 \u0446\u0435 \u043b\u044e\u0434\u0438\u043d\u0430, \u044f\u043a\u0430 \u0442\u0440\u0438\u043c\u0430\u0454 \u0433\u0440\u0443\u043f\u0443 \u0440\u0430\u0437\u043e\u043c.",
    // Артур лідирує не наказами, а турботою...
    connection: "arthur_true_leader"
  },
  {
    id: "thought_lettie_warmth",
    requires: ["quincy_sniper", "lettie_cares"],
    text: "\u041b\u0435\u0442\u0442\u0456 \u0445\u043e\u0432\u0430\u0454 \u0435\u043c\u043e\u0446\u0456\u0457 \u0437\u0430 \u0441\u0430\u0440\u043a\u0430\u0437\u043c\u043e\u043c. \u041a\u0432\u0456\u043d\u0441\u0456 \u2014 \u0437\u0430 \u0442\u0440\u043e\u043b\u0456\u043d\u0433\u043e\u043c. \u0412\u043e\u043d\u0438 \u043e\u0431\u043e\u0454 \u0434\u0431\u0430\u044e\u0442\u044c, \u0430\u043b\u0435 \u043d\u0435 \u043c\u043e\u0436\u0443\u0442\u044c \u0446\u0435 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u0438 \u0432\u0456\u0434\u043a\u0440\u0438\u0442\u043e.",
    // Летті ховає емоції за сарказмом...
    connection: "masks_of_care"
  },
  {
    id: "thought_aoi_patience",
    requires: ["aoi_observer", "aoi_silence"],
    text: "\u0410\u043e\u0456 \u0441\u043f\u043e\u0441\u0442\u0435\u0440\u0456\u0433\u0430\u0454, \u0447\u0435\u043a\u0430\u0454, \u0430\u043d\u0430\u043b\u0456\u0437\u0443\u0454. \u0407\u0457 \u0442\u0435\u0440\u043f\u0456\u043d\u043d\u044f \u2014 \u043d\u0435 \u0441\u043b\u0430\u0431\u043a\u0456\u0441\u0442\u044c, \u0430 \u0437\u0431\u0440\u043e\u044f. \u0412\u043e\u043d\u0430 \u0431\u0430\u0447\u0438\u0442\u044c \u0442\u0435, \u0449\u043e \u0456\u043d\u0448\u0456 \u043f\u0440\u043e\u043f\u0443\u0441\u043a\u0430\u044e\u0442\u044c.",
    // Аоі спостерігає, чекає, аналізує...
    connection: "aoi_strategic_patience"
  },
  {
    id: "thought_team_dynamics",
    requires: ["arthur_leader", "amir_tech", "quincy_sniper"],
    text: "\u0410\u0440\u0442\u0443\u0440 \u043a\u043e\u043c\u0430\u043d\u0434\u0443\u0454, \u0410\u043c\u0456\u0440 \u0442\u0435\u0445\u043d\u0456\u0447\u043d\u043e \u0437\u0430\u0431\u0435\u0437\u043f\u0435\u0447\u0443\u0454, \u041a\u0432\u0456\u043d\u0441\u0456 \u043f\u0440\u0438\u043a\u0440\u0438\u0432\u0430\u0454. \u0422\u0440\u043e\u0454 \u043b\u044e\u0434\u0435\u0439 \u2014 \u0442\u0440\u0438 \u0440\u0456\u0432\u043d\u0456 \u0431\u043e\u044e. \u0420\u0430\u0437\u043e\u043c \u0432\u043e\u043d\u0438 \u043f\u0440\u0430\u0446\u044e\u044e\u0442\u044c \u044f\u043a \u043c\u0435\u0445\u0430\u043d\u0456\u0437\u043c.",
    // Артур командує, Амір технічно забезпечує...
    connection: "team_combat_synergy"
  },
  {
    id: "thought_trust_circle",
    requires: ["arthur_trust", "aoi_silence"],
    text: "\u0414\u043e\u0432\u0456\u0440\u0430 \u0432 \u0446\u044c\u043e\u043c\u0443 \u0437\u0430\u0433\u043e\u043d\u0456 \u0431\u0443\u0434\u0443\u0454\u0442\u044c\u0441\u044f \u043d\u0435 \u0441\u043b\u043e\u0432\u0430\u043c\u0438, \u0430 \u043c\u043e\u0432\u0447\u0430\u043d\u043d\u044f\u043c. \u0425\u0442\u043e \u0432\u0438\u0442\u0440\u0438\u043c\u0443\u0454 \u0442\u0438\u0448\u0443 \u043f\u043e\u0440\u0443\u0447 \u2014 \u0442\u043e\u0439 \u0441\u0432\u0456\u0439.",
    // Довіра в цьому загоні будується не словами, а мовчанням...
    connection: "trust_through_silence"
  }
];


registerState("insights", {
  log: [],            // [{id, text, day, type}, ...] — побачені факти і зв'язки
  raw_thoughts: [],   // [{id, text, requires, connection}, ...] — необдумані зв'язки
  journal: []         // [{day, text, type}, ...] — щоденник Дріфтера
});


// Додає простий факт в Шафу Думок. Миттєвий.
function addInsight(id, text) {
  setFlag(id);
  gameState.insights.log.push({
    id: id,
    text: text,
    day: gameState.time.day,
    type: "fact"
  });
  checkRawThoughts();
}


// Перевіряє чи зібрані факти для нових зв'язків.
function checkRawThoughts() {
  for (var i = 0; i < RAW_THOUGHT_DEFS.length; i++) {
    var rt = RAW_THOUGHT_DEFS[i];

    // Вже є в необдуманих?
    var alreadyQueued = false;
    for (var j = 0; j < gameState.insights.raw_thoughts.length; j++) {
      if (gameState.insights.raw_thoughts[j].id === rt.id) {
        alreadyQueued = true;
        break;
      }
    }
    if (alreadyQueued) continue;

    // Вже осмислений?
    if (getFlag(rt.id)) continue;

    // Всі вимоги виконані?
    var allMet = true;
    for (var r = 0; r < rt.requires.length; r++) {
      if (!getFlag(rt.requires[r])) {
        allMet = false;
        break;
      }
    }

    if (allMet) {
      // Додати копію в необдумані
      gameState.insights.raw_thoughts.push({
        id: rt.id,
        text: rt.text,
        requires: rt.requires.slice(),
        connection: rt.connection
      });
    }
  }
}


// Осмислити сиру думку. Витрачає 30 хв. Активує флаг.
function contemplate(thoughtId) {
  advanceTime(30);
  setFlag(thoughtId);

  // Видалити з необдуманих
  var remaining = [];
  for (var i = 0; i < gameState.insights.raw_thoughts.length; i++) {
    if (gameState.insights.raw_thoughts[i].id !== thoughtId) {
      remaining.push(gameState.insights.raw_thoughts[i]);
    }
  }
  gameState.insights.raw_thoughts = remaining;

  // Додати в лог як зв'язок
  gameState.insights.log.push({
    id: thoughtId,
    text: "...",
    day: gameState.time.day,
    type: "connection"
  });
}


// Чи є необдумані зв'язки
function hasRawThoughts() {
  return gameState.insights.raw_thoughts.length > 0;
}


// ═══════════════════════════════════════════════
// ЩОДЕННИК
// ═══════════════════════════════════════════════

// Додає запис в щоденник Дріфтера.
function addJournalEntry(text, entryType) {
  if (!entryType) entryType = "note";
  gameState.insights.journal.push({
    day: gameState.time.day,
    text: text,
    type: entryType
  });
}
