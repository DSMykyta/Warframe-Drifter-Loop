// ═══════════════════════════════════════════════════
// ШАБЛОН КВЕСТУ — копіюй і заповнюй
// ═══════════════════════════════════════════════════
//
// Файл: scenes/quest_name.js
// Після створення: bash generate_manifest.sh
//
// Квест складається з:
// 1. Хуки для nextDay() — перевірки прогресу
// 2. DIALOGUE_ENTRIES — діалоги NPC (titles або forced)
// 3. registerScript() — самі скрипти
// 4. SPECIAL_MISSION_ENTRIES — квестові місії (якщо є)
// 5. BONUS_OPTIONS — додаткові опції (якщо є)


// ═══ ХУКИ ═══
// Функції що запускаються кожен новий день.
// Перевіряють прогрес і запускають наступні етапи.

function checkMyQuestStage1() {
  if (!getFlag("my_quest_started")) return;
  if (getFlag("my_quest_stage1_done")) return;
  // Якщо минуло 3 дні — нагадати через пейджер
  if (gameState.time.day - (gameState.flags.data["my_quest_started_day"] || 0) >= 3) {
    sendPagerMessage("ar", "Не забув про ту справу?");
    setFlag("my_quest_stage1_reminded");
  }
}

function checkMyQuestStage2() {
  if (!getFlag("my_quest_stage1_done")) return;
  if (getFlag("my_quest_complete")) return;
  // Автоматично завершити якщо умова
  if (getFlag("special_item_found")) {
    setFlag("my_quest_complete");
    addJournalEntry("Квест завершено.", "event");
  }
}

// Реєстрація хуків
registerDayHook(checkMyQuestStage1);
registerDayHook(checkMyQuestStage2);


// ═══ ДІАЛОГИ ═══

// Етап 1: Артур пропонує квест (titles — гравець обирає)
DIALOGUE_ENTRIES.push({
  id: "my_quest_offer",
  who: "ar",
  conditions: {
    flag_true: ["intro_done"],
    flag_false: ["my_quest_started"],
    day_min: 3,
    chemistry_min: ["ar", 15]
  },
  priority: 60,
  titles: [
    {text: "Про що хотів поговорити?", label: "my_quest_accept"},
    {text: "Потім.", label: "my_quest_decline"}
  ]
});

registerScript("my_quest_accept", [
  {type: "show", who: "ar"},
  {type: "say", who: "ar", text: "Є справа. Потрібна допомога."},
  {type: "say", who: "ar", text: "На складі щось цікаве. Перевіриш?"},
  {type: "menu", choices: [
    {text: "Звісно.", label: "quest_yes", chemistry: {"ar": 3}},
    {text: "Що саме?", label: "quest_details"}
  ]},
  {type: "label", id: "quest_details"},
  {type: "say", who: "ar", text: "Не впевнений. Тому і питаю."},
  {type: "label", id: "quest_yes"},
  {type: "say", who: "ar", text: "Добре. Подивись коли будеш на складі."},
  {type: "set_flag", flag: "my_quest_started"},
  {type: "end", text: ""}
]);

registerScript("my_quest_decline", [
  {type: "say", who: "ar", text: "Окей. Не поспішаю."},
  {type: "end", text: ""}
]);


// Етап 2: Forced діалог (label — запускається автоматично при вході в локацію)
DIALOGUE_ENTRIES.push({
  id: "my_quest_find",
  who: "am",  // Амір на складі
  conditions: {
    flag_true: ["my_quest_started"],
    flag_false: ["my_quest_stage1_done"],
    location: "warehouse"
  },
  priority: 80,
  label: "my_quest_find_scene"
});

registerScript("my_quest_find_scene", [
  {type: "scene", bg: "bg_warehouse.webp", text: "СКЛАД"},
  {type: "show", who: "am"},
  {type: "say", who: "am", text: "О. Ти теж тут."},
  {type: "say", who: "am", text: "Глянь що я знайшов."},
  {type: "say", who: null, text: "Амір показує стару коробку з деталями."},
  {type: "chemistry", who: "am", amount: 2},
  {type: "set_flag", flag: "my_quest_stage1_done"},
  {type: "set_flag", flag: "special_item_found"},
  {type: "end", text: ""}
]);


// Етап 3: Групова сцена (Banter)
BANTER_ENTRIES.push({
  id: "my_quest_group",
  chars: ["ar", "am"],
  location: "backroom",
  conditions: {
    flag_true: ["my_quest_stage1_done"],
    flag_false: ["my_quest_group_seen"]
  },
  priority: 8,
  label: "my_quest_group_scene"
});

registerScript("my_quest_group_scene", [
  {type: "show", who: "ar", at: "left"},
  {type: "show", who: "am", at: "right"},
  {type: "say", who: "ar", text: "Амір сказав ти знайшов деталі."},
  {type: "say", who: "am", text: "Ага. На складі. Купа цікавого."},
  {type: "say", who: "ar", text: "Добре."},
  {type: "set_flag", flag: "my_quest_group_seen"},
  {type: "end", text: ""}
]);


// ═══ КВЕСТОВА МІСІЯ (якщо потрібна) ═══

SPECIAL_MISSION_ENTRIES.push({
  id: "my_quest_mission",
  name: "ОПЕРАЦІЯ: МОЙ КВЕСТ",
  level: 3,
  reward: 300,
  rep: 5,
  partner: "ar",
  partner_count: 1,
  label: "my_quest_mission_dialogue",
  conditions: {
    flag_true: ["my_quest_stage1_done"],
    flag_false: ["my_quest_mission_done"]
  },
  chance: 100
});

registerScript("my_quest_mission_dialogue", [
  {type: "show", who: "ar"},
  {type: "say", who: "ar", text: "Готовий? Це може бути небезпечно."},
  {type: "say", who: "mc", text: "Завжди готовий."},
  {type: "set_flag", flag: "my_quest_mission_done"},
  {type: "end", text: ""}
]);


// ═══ БОНУСНА ОПЦІЯ (якщо потрібна) ═══

BONUS_OPTIONS.push({
  id: "my_quest_special_option",
  who: "ar",
  text: "Показати знахідку зі складу",
  label: "my_quest_show_item",
  conditions: {
    flag_true: ["special_item_found"],
    flag_false: ["my_quest_complete"]
  },
  once: true
});

registerScript("my_quest_show_item", [
  {type: "say", who: "ar", text: "Що це?"},
  {type: "say", who: "mc", text: "Знайшов на складі. Тримай."},
  {type: "say", who: "ar", text: "...Дякую."},
  {type: "chemistry", who: "ar", amount: 5},
  {type: "set_flag", flag: "my_quest_complete"},
  {type: "end", text: ""}
]);
