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
    id: "thought_team_dynamics",
    requires: ["arthur_leads", "amir_tech", "quincy_sniper"],
    text: "Артур командує, Амір технічно забезпечує, Квінсі прикриває. Троє людей — три рівні бою. Разом вони працюють як механізм.",
    connection: "team_combat_synergy"
  },
  {
    id: "thought_lettie_warmth",
    requires: ["quincy_sniper", "lettie_medic"],
    text: "Летті ховає емоції за сарказмом. Квінсі — за тролінгом. Вони обоє дбають, але не можуть це показати відкрито.",
    connection: "masks_of_care"
  },
  {
    id: "thought_aoi_patience",
    requires: ["aoi_logistics", "hex_exists"],
    text: "Аоі спостерігає, чекає, аналізує. Її терпіння — не слабкість, а зброя. Вона бачить те, що інші пропускають.",
    connection: "aoi_strategic_patience"
  },
  {
    id: "thought_arthur_leadership",
    requires: ["arthur_leads", "hex_exists"],
    text: "Артур лідирує не наказами, а турботою. Це не просто командир — це людина, яка тримає групу разом.",
    connection: "arthur_true_leader"
  },
  {
    id: "thought_trust_circle",
    requires: ["arthur_leads", "aoi_logistics"],
    text: "Довіра в цьому загоні будується не словами, а мовчанням. Хто витримує тишу поруч — той свій.",
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

  // Знайти текст думки перед видаленням
  var thoughtText = "...";
  for (var t = 0; t < gameState.insights.raw_thoughts.length; t++) {
    if (gameState.insights.raw_thoughts[t].id === thoughtId) {
      thoughtText = gameState.insights.raw_thoughts[t].text;
      break;
    }
  }

  // Видалити з необдуманих
  var remaining = [];
  for (var i = 0; i < gameState.insights.raw_thoughts.length; i++) {
    if (gameState.insights.raw_thoughts[i].id !== thoughtId) {
      remaining.push(gameState.insights.raw_thoughts[i]);
    }
  }
  gameState.insights.raw_thoughts = remaining;

  // Додати в лог як зв'язок (з реальним текстом)
  gameState.insights.log.push({
    id: thoughtId,
    text: thoughtText,
    day: gameState.time.day,
    type: "connection"
  });

  // Записати в щоденник
  addJournalEntry(thoughtText, "insight");
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
