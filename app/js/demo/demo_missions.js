// ═══════════════════════════════════════════════════
// ДЕМО: МІСІЇ, ТРАВМИ, ЕВАКУАЦІЯ, РАНГ, ПОДАРУНКИ
// ═══════════════════════════════════════════════════

// ─── СПЕЦІАЛЬНА МІСІЯ (condition-based) ───
SPECIAL_MISSION_ENTRIES.push({
  id: "demo_special_mission",
  name: "ОПЕРАЦІЯ: ДЕМО-ТЕСТ",
  level: 3,
  reward: 500,
  rep: 10,
  partner: "ar",
  partner2: "lt",
  partner_count: 2,
  label: "demo_special_mission_dialogue",
  conditions: {
    flag_true: ["demo_engine_passed"],
    flag_false: ["demo_special_done"]
  },
  chance: 100
});

registerScript("demo_special_mission_dialogue", [
  {type: "show", who: "ar", at: "left"},
  {type: "show", who: "lt", at: "right"},
  {type: "say", who: "ar", text: "Спецоперація. Втрьох."},
  {type: "say", who: "lt", text: "Якщо хтось поранеться — я тут. Летті на місії = 0% травм."},
  {type: "say", who: null, text: "(Летті присутня → імунітет до травм + лікування всіх стаків.)"},
  {type: "set_flag", flag: "demo_special_done"},
  {type: "end", text: ""}
]);


// ─── МІСІЙНИЙ ДІАЛОГ НАПАРНИКА ───
MISSION_DIALOGUE_ENTRIES.push({
  id: "demo_mission_dialogue_am",
  who: "am",
  conditions: {},
  priority: 10,
  chance: 100,
  label: "demo_mission_am_talk"
});

registerScript("demo_mission_am_talk", [
  {type: "say", who: "am", text: "Ну що, погнали? Я взяв свої іграшки."},
  {type: "say", who: null, text: "(Місійний діалог напарника перед результатом.)"},
  {type: "end", text: ""}
]);


// ─── ТЕСТ ПОДАРУНКІВ: діалог з кнопкою подарунка ───
DIALOGUE_ENTRIES.push({
  id: "demo_gift_test",
  who: "ao",
  conditions: {
    flag_true: ["demo_engine_passed"],
    flag_false: ["demo_gift_done"]
  },
  priority: 25,
  titles: [
    {text: "Подарувати щось", label: "demo_gift_scene"},
    {text: "Просто привіт", label: "demo_ao_hi"}
  ]
});

registerScript("demo_ao_hi", [
  {type: "say", who: "ao", text: "Привіт."},
  {type: "end", text: ""}
]);

registerScript("demo_gift_scene", [
  {type: "say", who: null, text: "Обери подарунок для Аоі:"},
  {type: "menu", choices: [
    {text: "Навушники (улюблений, +12)", label: "demo_gift_loved"},
    {text: "Тостер (образливий, -5)", label: "demo_gift_offensive"},
    {text: "Аптечка (нейтральний, +1)", label: "demo_gift_neutral"}
  ]},

  {type: "label", id: "demo_gift_loved"},
  {type: "say", who: null, text: "(Даруємо wireless_headphones Аоі. Очікуємо +12 хімії.)"},
  {type: "set_flag", flag: "demo_gift_done"},
  {type: "end", text: ""},

  {type: "label", id: "demo_gift_offensive"},
  {type: "say", who: null, text: "(Даруємо toaster Аоі. Очікуємо -5 хімії + плітка.)"},
  {type: "set_flag", flag: "demo_gift_done"},
  {type: "end", text: ""},

  {type: "label", id: "demo_gift_neutral"},
  {type: "say", who: null, text: "(Даруємо medical_kit Аоі. Очікуємо +1 хімії.)"},
  {type: "set_flag", flag: "demo_gift_done"},
  {type: "end", text: ""}
]);

// Хуки для реальних подарунків
var _demoGiftCheck = setInterval(function() {
  if (!getFlag("demo_gift_done")) return;
  if (getFlag("demo_gift_applied")) return;

  if (getFlag("demo_gift_done") && typeof giveGift === "function") {
    // Визначити який подарунок обрали за флагами
    // giveGift автоматично обробить — тут просто для логу
    setFlag("demo_gift_applied");
    clearInterval(_demoGiftCheck);
  }
}, 1000);


// ─── ТЕСТ ТРАВМ: 3 стаки → евакуація ───
DIALOGUE_ENTRIES.push({
  id: "demo_evacuation_test",
  who: "ar",
  conditions: {
    flag_true: ["demo_injury_done"],
    flag_false: ["demo_evac_done"]
  },
  priority: 60,
  titles: [
    {text: "Тест евакуації (3 стаки Артуру)", label: "demo_evac_scene"},
    {text: "Тест emergency skip (3 стаки гравцю)", label: "demo_emergency_scene"}
  ]
});

registerScript("demo_evac_scene", [
  {type: "say", who: null, text: "Додаємо Артуру 2 стаки (вже 1 є). Разом = 3 = критичний стан."},
  {type: "say", who: null, text: "Артур піде в recovery_room на 2 дні. Зникне з локацій."},
  {type: "set_flag", flag: "demo_evac_done"},
  {type: "end", text: ""}
]);

registerScript("demo_emergency_scene", [
  {type: "say", who: null, text: "Додаємо гравцю 3 стаки. Emergency skip = пропуск 2 днів."},
  {type: "say", who: null, text: "Прокинешся в медвідділі. Обіцянки не штрафуються."},
  {type: "set_flag", flag: "demo_emergency_done"},
  {type: "end", text: ""}
]);

// Хуки евакуації
var _demoEvacCheck = setInterval(function() {
  if (getFlag("demo_evac_done") && !getFlag("demo_evac_applied")) {
    addInjuryStack("ar");
    addInjuryStack("ar"); // тепер 3 стаки (1 вже був)
    setFlag("demo_evac_applied");
    clearInterval(_demoEvacCheck);
  }
}, 500);

var _demoEmergencyCheck = setInterval(function() {
  if (getFlag("demo_emergency_done") && !getFlag("demo_emergency_applied")) {
    addInjuryStack("player");
    addInjuryStack("player");
    addInjuryStack("player");
    if (typeof emergencySkip === "function") emergencySkip(2);
    setFlag("demo_emergency_applied");
    showLocation();
    clearInterval(_demoEmergencyCheck);
  }
}, 500);


// ─── ТЕСТ RANK-UP ───
DIALOGUE_ENTRIES.push({
  id: "demo_rankup_test",
  who: "ar",
  conditions: {
    flag_true: ["demo_engine_passed"],
    flag_false: ["demo_rankup_done"]
  },
  priority: 15,
  titles: [
    {text: "Тест рангу (дати 300 реп)", label: "demo_rankup_scene"}
  ]
});

registerScript("demo_rankup_scene", [
  {type: "say", who: null, text: "Додаємо 300 репутації. Має пройти rank 1→2→3→4→5→6."},
  {type: "say", who: null, text: "Ранг 3 відкриває бар. Ранг 4 — місії рівня 6."},
  {type: "set_flag", flag: "demo_rankup_done"},
  {type: "end", text: ""}
]);

var _demoRankCheck = setInterval(function() {
  if (getFlag("demo_rankup_done") && !getFlag("demo_rankup_applied")) {
    if (typeof addHexRep === "function") addHexRep(300);
    // Проганяємо tryRankUp кілька разів
    for (var i = 0; i < 6; i++) {
      if (typeof tryRankUp === "function") tryRankUp();
    }
    setFlag("demo_rankup_applied");
    clearInterval(_demoRankCheck);
  }
}, 500);


// ─── ТЕСТ DAILY CAP ───
DIALOGUE_ENTRIES.push({
  id: "demo_dailycap_test",
  who: "lt",
  conditions: {
    flag_true: ["demo_engine_passed"],
    flag_false: ["demo_cap_done"]
  },
  priority: 10,
  titles: [
    {text: "Тест daily cap (спам хімію)", label: "demo_cap_scene"}
  ]
});

registerScript("demo_cap_scene", [
  {type: "say", who: null, text: "Додаємо Летті +100 хімії. Daily cap = 15. Має додати тільки 15."},
  {type: "chemistry", who: "lt", amount: 100},
  {type: "say", who: null, text: "Перевір toast — має бути менше 100."},
  {type: "set_flag", flag: "demo_cap_done"},
  {type: "end", text: ""}
]);


// ─── ТЕСТ DECAY (через сон) ───
DIALOGUE_ENTRIES.push({
  id: "demo_decay_test",
  who: "el",
  conditions: {
    flag_true: ["demo_engine_passed"],
    flag_false: ["demo_decay_done"]
  },
  priority: 10,
  titles: [
    {text: "Тест decay (поспи 10 днів)", label: "demo_decay_scene"}
  ]
});

registerScript("demo_decay_scene", [
  {type: "say", who: null, text: "Після 7+ днів без контакту хімія падає. Поспи 10 днів підряд."},
  {type: "say", who: null, text: "В консолі перевір: gameState.chemistry.values — має зменшитись."},
  {type: "set_flag", flag: "demo_decay_done"},
  {type: "end", text: ""}
]);


// ─── ТЕСТ ФІНАЛУ: день 31 ───
DIALOGUE_ENTRIES.push({
  id: "demo_finale_test",
  who: "ar",
  conditions: {
    flag_true: ["demo_engine_passed"],
    flag_false: ["demo_finale_done"]
  },
  priority: 5,
  titles: [
    {text: "Тест перемоги (день 31, всі 120+)", label: "demo_victory_scene"},
    {text: "Тест поразки (день 31, не всі 120+)", label: "demo_defeat_scene"}
  ]
});

registerScript("demo_victory_scene", [
  {type: "say", who: null, text: "Ставимо день 30, хімію 120 всім. Йди спати → фінал перемоги."},
  {type: "set_flag", flag: "demo_finale_victory"},
  {type: "set_flag", flag: "demo_finale_done"},
  {type: "end", text: ""}
]);

registerScript("demo_defeat_scene", [
  {type: "say", who: null, text: "Ставимо день 30, хімію 50. Йди спати → фінал поразки."},
  {type: "set_flag", flag: "demo_finale_defeat"},
  {type: "set_flag", flag: "demo_finale_done"},
  {type: "end", text: ""}
]);

var _demoFinaleCheck = setInterval(function() {
  if (getFlag("demo_finale_victory") && !getFlag("demo_finale_set")) {
    gameState.time.day = 30;
    for (var k in CAST) {
      gameState.chemistry.values[k] = 120;
    }
    setFlag("demo_finale_set");
    setFlag("day30_warning_done"); // пропустити попередження
    clearInterval(_demoFinaleCheck);
  }
  if (getFlag("demo_finale_defeat") && !getFlag("demo_finale_set")) {
    gameState.time.day = 30;
    for (var k2 in CAST) {
      gameState.chemistry.values[k2] = 50;
    }
    setFlag("demo_finale_set");
    setFlag("day30_warning_done");
    clearInterval(_demoFinaleCheck);
  }
}, 500);


// ─── ТЕСТ NEGLECT (5 днів без місій) ───
DIALOGUE_ENTRIES.push({
  id: "demo_neglect_test",
  who: "el",
  conditions: {
    flag_true: ["demo_engine_passed"],
    flag_false: ["demo_neglect_done"]
  },
  priority: 10,
  titles: [
    {text: "Тест neglect (5 днів без місій)", label: "demo_neglect_scene"}
  ]
});

registerScript("demo_neglect_scene", [
  {type: "say", who: null, text: "Ставимо days_without_mission = 5. При наступному nextDay — штраф всім."},
  {type: "say", who: null, text: "І зявиться аварійна місія в гаражі."},
  {type: "set_flag", flag: "demo_neglect_done"},
  {type: "end", text: ""}
]);

var _demoNeglectCheck = setInterval(function() {
  if (getFlag("demo_neglect_done") && !getFlag("demo_neglect_applied")) {
    gameState.missions.days_without_mission = 5;
    setFlag("demo_neglect_applied");
    clearInterval(_demoNeglectCheck);
  }
}, 500);


// ─── ТЕСТ BROKEN PROMISE ───
DIALOGUE_ENTRIES.push({
  id: "demo_broken_promise",
  who: "qu",
  conditions: {
    flag_true: ["demo_promise_created"],
    flag_false: ["demo_broken_test_done"]
  },
  priority: 10,
  titles: [
    {text: "Тест зламаної обіцянки (не прийти)", label: "demo_broken_scene"}
  ]
});

registerScript("demo_broken_scene", [
  {type: "say", who: null, text: "Створюємо обіцянку на сьогодні яку НЕ виконаємо. При nextDay → -5 хімії."},
  {type: "set_flag", flag: "demo_broken_test_done"},
  {type: "end", text: ""}
]);

var _demoBrokenCheck = setInterval(function() {
  if (getFlag("demo_broken_test_done") && !getFlag("demo_broken_applied")) {
    createPromise("el", "furniture", 100, 200, gameState.time.day, null);
    setFlag("demo_broken_applied");
    clearInterval(_demoBrokenCheck);
  }
}, 500);


// ─── EXPIRED EVENT TEST ───
DIALOGUE_ENTRIES.push({
  id: "demo_expired_event",
  who: "am",
  conditions: {
    flag_true: ["demo_engine_passed"],
    flag_false: ["demo_expired_taken"]
  },
  priority: 35,
  expires_in_days: 1,
  on_expire: {
    chemistry_change: {"am": -5},
    flags_set: ["demo_event_expired"],
    gossip_heat: 3
  },
  titles: [
    {text: "Терміновий івент (1 день)", label: "demo_expired_take"}
  ]
});

registerScript("demo_expired_take", [
  {type: "say", who: "am", text: "Ти встиг. Добре. Цей діалог зник би через 1 день."},
  {type: "say", who: null, text: "Якщо пропустити — через 1 день Амір -5 хімії + 3 gossip heat."},
  {type: "set_flag", flag: "demo_expired_taken"},
  {type: "end", text: ""}
]);
