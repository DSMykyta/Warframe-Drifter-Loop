// ═══════════════════════════════════════════════════
// ШАБЛОН ДІАЛОГУ — копіюй і заповнюй
// ═══════════════════════════════════════════════════
//
// Файл: dialogues/character/dialogue_name.js
// Після створення: bash generate_manifest.sh


// ═══ ВАРІАНТ 1: TITLES (гравець обирає тему) ═══

DIALOGUE_ENTRIES.push({
  id: "ar_r2_talk_about_sword",   // унікальний ID
  who: "ar",                       // short ID персонажа
  conditions: {
    chemistry_min: ["ar", 35],     // потрібна хімія 35+
    flag_true: ["arthur_intro_done"],
    flag_false: ["ar_sword_talk_done"]
  },
  priority: 40,
  titles: [
    {text: "Розкажи про меч.", label: "ar_sword_story", chemistry: {"ar": 2}},
    {text: "Як ти отримав шрам?", label: "ar_scar_story"},
    {text: "Нічого, забудь.", label: "ar_nevermind"}
  ]
});

registerScript("ar_sword_story", [
  {type: "show", who: "ar"},
  {type: "say", who: "ar", text: "Excalibur. Не оригінал, звісно."},
  {type: "say", who: "ar", text: "Але достатньо гострий щоб різати все що потрібно."},
  {type: "say", who: "mc", text: "Звучить серйозно."},
  {type: "say", who: "ar", text: "Це і є серйозно."},
  {type: "set_flag", flag: "ar_sword_talk_done"},
  {type: "end", text: ""}
]);

registerScript("ar_scar_story", [
  {type: "show", who: "ar"},
  {type: "say", who: "ar", text: "..."},
  {type: "say", who: "ar", text: "Не сьогодні."},
  // НЕ ставимо flag — можна запитати знову
  {type: "end", text: ""}
]);

registerScript("ar_nevermind", [
  {type: "say", who: "ar", text: "Окей."},
  {type: "end", text: ""}
]);


// ═══ ВАРІАНТ 2: FORCED (запускається автоматично) ═══

DIALOGUE_ENTRIES.push({
  id: "el_telepathy_warning",
  who: "el",
  conditions: {
    chemistry_min: ["el", 60],
    flag_true: ["eleanor_intro_done"],
    flag_false: ["el_warning_done"]
  },
  priority: 85,                    // високий — forced
  label: "el_warning_scene"        // label замість titles = forced
});

registerScript("el_warning_scene", [
  {type: "show", who: "el"},
  {type: "telepathy", who: "el", text: "...обережно."},
  {type: "say", who: "el", text: "Я відчуваю щось. Щось недобре."},
  {type: "say", who: "el", text: "Будь уважний сьогодні."},
  {type: "set_flag", flag: "el_warning_done"},
  {type: "end", text: ""}
]);


// ═══ ВАРІАНТ 3: З МЕНЮ ВСЕРЕДИНІ ═══

DIALOGUE_ENTRIES.push({
  id: "lt_coffee_offer",
  who: "lt",
  conditions: {
    flag_true: ["coffee_machine_found"],
    flag_false: ["lt_coffee_accepted"]
  },
  priority: 35,
  repeatable: true,
  titles: [
    {text: "Хочеш каву?", label: "lt_coffee_scene"}
  ]
});

registerScript("lt_coffee_scene", [
  {type: "show", who: "lt"},
  {type: "say", who: "mc", text: "Тримай. Приніс каву."},
  {type: "say", who: "lt", text: "..."},
  {type: "say", who: "lt", text: "Ти серйозно?"},
  {type: "menu", choices: [
    {text: "Так. Ти заслуговуєш.", label: "coffee_kind", chemistry: {"lt": 4}},
    {text: "Просто була зайва.", label: "coffee_casual", chemistry: {"lt": 1}}
  ]},
  {type: "label", id: "coffee_kind"},
  {type: "say", who: "lt", text: "...Дякую. Серйозно."},
  {type: "set_flag", flag: "lt_coffee_accepted"},
  {type: "jump", to: "coffee_end"},
  {type: "label", id: "coffee_casual"},
  {type: "say", who: "lt", text: "Ну, якщо зайва. Не відмовлюсь."},
  {type: "label", id: "coffee_end"},
  {type: "end", text: ""}
]);


// ═══ ВАРІАНТ 4: TIMED EVENT (зникає через N днів) ═══

DIALOGUE_ENTRIES.push({
  id: "am_urgent_request",
  who: "am",
  conditions: {
    flag_true: ["arcade_broken"],
    flag_false: ["arcade_fixed"],
    day_min: 5,
    day_max: 10
  },
  priority: 55,
  expires_in_days: 3,              // зникне через 3 дні
  on_expire: {                     // наслідки якщо пропустив
    chemistry_change: {"am": -5},
    flags_set: ["arcade_expired"],
    gossip_heat: 2
  },
  titles: [
    {text: "Що з автоматом?", label: "am_fix_arcade"}
  ]
});

registerScript("am_fix_arcade", [
  {type: "show", who: "am"},
  {type: "say", who: "am", text: "Нарешті! Допоможи полагодити."},
  {type: "time", minutes: 45},
  {type: "chemistry", who: "am", amount: 5},
  {type: "set_flag", flag: "arcade_fixed"},
  {type: "end", text: ""}
]);
