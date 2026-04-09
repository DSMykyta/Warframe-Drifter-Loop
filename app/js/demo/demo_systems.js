// ═══════════════════════════════════════════════════
// ДЕМО: ТЕСТ ІГРОВИХ СИСТЕМ
// ═══════════════════════════════════════════════════
//
// Реєструє діалоги, banter, forced, titles,
// gifts, coffee, promises, gossip, injuries, romance
// для перевірки ВСІХ систем через гру.

// ─── DIALOGUE ENTRY: titles (меню привітань) ───
DIALOGUE_ENTRIES.push({
  id: "demo_arthur_titles",
  who: "ar",
  conditions: { flag_true: ["demo_engine_passed"] },
  priority: 50,
  repeatable: true,
  titles: [
    {text: "Привіт, Артуре.", label: "demo_ar_greet", chemistry: {"ar": 2}},
    {text: "Як справи?", label: "demo_ar_howru"},
    {text: "Тренуєшся?", label: "demo_ar_train", flag: "demo_asked_train"}
  ]
});

registerScript("demo_ar_greet", [
  {type: "say", who: "ar", text: "Привіт. Все тихо."},
  {type: "end", text: ""}
]);

registerScript("demo_ar_howru", [
  {type: "say", who: "ar", text: "Нормально. Звіти, меч, рутина."},
  {type: "say", who: "ar", text: "А ти?"},
  {type: "menu", choices: [
    {text: "Теж нормально.", label: "demo_ar_fine"},
    {text: "Краще б спав.", label: "demo_ar_tired"}
  ]},
  {type: "label", id: "demo_ar_fine"},
  {type: "say", who: "ar", text: "Добре."},
  {type: "jump", to: "demo_ar_end"},
  {type: "label", id: "demo_ar_tired"},
  {type: "say", who: "ar", text: "Сон — розкіш. Знаю."},
  {type: "label", id: "demo_ar_end"},
  {type: "end", text: ""}
]);

registerScript("demo_ar_train", [
  {type: "say", who: "ar", text: "Щодня. Без винятків."},
  {type: "end", text: ""}
]);


// ─── DIALOGUE ENTRY: forced (label без titles) ───
DIALOGUE_ENTRIES.push({
  id: "demo_forced_eleanor",
  who: "el",
  conditions: {
    flag_true: ["demo_engine_passed"],
    flag_false: ["demo_forced_done"]
  },
  priority: 90,
  label: "demo_forced_el"
});

registerScript("demo_forced_el", [
  {type: "show", who: "el"},
  {type: "telepathy", who: "el", text: "...чуєш мене?"},
  {type: "say", who: "el", text: "Це forced діалог. Спрацював автоматично при вході в локацію."},
  {type: "set_flag", flag: "demo_forced_done"},
  {type: "end", text: ""}
]);


// ─── BANTER ENTRY: парна сцена ───
BANTER_ENTRIES.push({
  id: "demo_banter_am_ao",
  chars: ["am", "ao"],
  location: "arcade",
  conditions: { flag_false: ["demo_banter_seen"] },
  priority: 5,
  label: "demo_banter_scene"
});

registerScript("demo_banter_scene", [
  {type: "show", who: "am", at: "left"},
  {type: "show", who: "ao", at: "right"},
  {type: "say", who: "am", text: "Аоі, глянь який скор."},
  {type: "say", who: "ao", text: "Не рахується. Ти жульничав."},
  {type: "say", who: "am", text: "Це стратегія!"},
  {type: "set_flag", flag: "demo_banter_seen"},
  {type: "end", text: ""}
]);


// ─── PROMISE: Квінсі на даху о 14:00 ───
// Створюється при розмові з Квінсі
DIALOGUE_ENTRIES.push({
  id: "demo_quincy_promise",
  who: "qu",
  conditions: {
    flag_true: ["demo_engine_passed"],
    flag_false: ["demo_promise_created"]
  },
  priority: 40,
  label: "demo_qu_promise"
});

registerScript("demo_qu_promise", [
  {type: "say", who: "qu", text: "Прийди на дах о другій. Треба поговорити."},
  {type: "set_flag", flag: "demo_promise_created"},
  {type: "end", text: ""}
]);

// Хук для створення обіцянки при demo_promise_created
var _demoPromiseCheck = setInterval(function() {
  if (getFlag("demo_promise_created") && !getFlag("demo_promise_added")) {
    createPromise("qu", "rooftop", 840, 960, gameState.time.day, "demo_qu_rooftop");
    setFlag("demo_promise_added");
    clearInterval(_demoPromiseCheck);
  }
}, 1000);

registerScript("demo_qu_rooftop", [
  {type: "say", who: "qu", text: "Прийшов. Добре."},
  {type: "say", who: "qu", text: "Нічого. Просто хотів перевірити що ти тримаєш слово."},
  {type: "chemistry", who: "qu", amount: 5},
  {type: "end", text: ""}
]);


// ─── GOSSIP: тестова плітка ───
// Створюється при виборі "флірт"
DIALOGUE_ENTRIES.push({
  id: "demo_lettie_gossip",
  who: "lt",
  conditions: {
    flag_true: ["demo_engine_passed"],
    flag_false: ["demo_gossip_started"]
  },
  priority: 30,
  titles: [
    {text: "Як пацієнти?", label: "demo_lt_patients"},
    {text: "Флірт (тест пліток)", label: "demo_lt_flirt", flag: "demo_flirted_lettie"}
  ]
});

registerScript("demo_lt_patients", [
  {type: "say", who: "lt", text: "Живі. На жаль."},
  {type: "end", text: ""}
]);

registerScript("demo_lt_flirt", [
  {type: "say", who: "mc", text: "Ти сьогодні... добре виглядаєш."},
  {type: "say", who: "lt", text: "...Серйозно? Я три дні не спала."},
  {type: "set_flag", flag: "demo_gossip_started"},
  {type: "end", text: ""}
]);


// ─── INSIGHT: тест думок ───
// Додається після forced діалогу Елеонор
var _demoInsightCheck = setInterval(function() {
  if (getFlag("demo_forced_done") && !getFlag("demo_insights_added")) {
    if (typeof addInsight === "function") {
      addInsight("demo_fact_1", "Елеонор може говорити в думках. Телепатія.");
      addInsight("demo_fact_2", "Артур тренується щодня. Дисципліна.");
    }
    setFlag("demo_insights_added");
    clearInterval(_demoInsightCheck);
  }
}, 1000);


// ─── HELP REQUEST: тест ───
HELP_REQUEST_ENTRIES.push({
  id: "demo_help_aoi",
  who: "ao",
  conditions: {
    flag_true: ["demo_engine_passed"],
    flag_false: ["helped_aoi_today"],
    time_min: 600,
    time_max: 1320
  },
  chance: 100,  // 100% для демо
  message: "Допоможи перенести платівки?",
  location: "music_shop"
});


// ─── COFFEE GIVE SCENE ───
registerScript("coffee_give_scene", [
  {type: "say", who: null, text: "Тримай. Приніс каву."},
  {type: "say", who: null, text: "(Реакція NPC на каву залежить від уподобань.)"},
  {type: "end", text: ""}
]);


// ─── INJURY TEST: додати травму для перевірки ───
DIALOGUE_ENTRIES.push({
  id: "demo_injury_test",
  who: "ar",
  conditions: {
    flag_true: ["demo_engine_passed"],
    flag_false: ["demo_injury_done"]
  },
  priority: 20,
  titles: [
    {text: "Тест травми", label: "demo_injury_scene"}
  ]
});

registerScript("demo_injury_scene", [
  {type: "say", who: "ar", text: "Тренування. Іноді боляче."},
  {type: "say", who: null, text: "(Додаємо 1 стак травми Артуру для тесту.)"},
  {type: "set_flag", flag: "demo_injury_done"},
  {type: "end", text: ""}
]);

// Хук для травми
var _demoInjuryCheck = setInterval(function() {
  if (getFlag("demo_injury_done") && !getFlag("demo_injury_applied")) {
    if (typeof addInjuryStack === "function") addInjuryStack("ar");
    setFlag("demo_injury_applied");
    clearInterval(_demoInjuryCheck);
  }
}, 1000);


// ─── ROMANCE TEST: високу хімію для тесту ───
DIALOGUE_ENTRIES.push({
  id: "demo_romance_test",
  who: "ao",
  conditions: {
    flag_true: ["demo_engine_passed"],
    chemistry_min: ["ao", 160],
    flag_false: ["demo_romance_done"]
  },
  priority: 95,
  label: "demo_romance_scene"
});

registerScript("demo_romance_scene", [
  {type: "say", who: "ao", text: "...Знаєш, з тобою легко."},
  {type: "menu", choices: [
    {text: "Мені теж.", label: "demo_romance_yes"},
    {text: "Дякую.", label: "demo_romance_no"}
  ]},
  {type: "label", id: "demo_romance_yes"},
  {type: "say", who: "ao", text: "Тоді... давай спробуємо."},
  {type: "set_flag", flag: "demo_romance_done"},
  {type: "end", text: ""},
  {type: "label", id: "demo_romance_no"},
  {type: "say", who: "ao", text: "...Окей."},
  {type: "set_flag", flag: "demo_romance_done"},
  {type: "end", text: ""}
]);

// Хук для romance
var _demoRomanceCheck = setInterval(function() {
  if (getFlag("demo_romance_done") && !getFlag("demo_romance_applied")) {
    if (typeof startDating === "function") startDating("ao");
    setFlag("demo_romance_applied");
    clearInterval(_demoRomanceCheck);
  }
}, 1000);
