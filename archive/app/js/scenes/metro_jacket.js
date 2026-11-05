// ═══════════════════════════════════════════════════
// МІСІЙНИЙ ІВЕНТ: Куртка зі станції метро
// ═══════════════════════════════════════════════════
//
// Порт з game/events/missions/metro_jacket_event.rpy
//
// Тригер: місія з Артуром, rank 3+, chemistry 30+.
// Аоі знаходить куртку. Гравець вибирає кому віддати.

MISSION_DIALOGUE_ENTRIES.push({
  id: "metro_jacket_event",
  who: "ar",
  conditions: {
    flag_false: ["metro_jacket_event_done"],
    chemistry_min: ["ar", 30],
    rank_min: 3
  },
  priority: 60,
  chance: 75,
  label: "metro_jacket_event"
});

// Бонусна опція: коментар про куртку
if (typeof BONUS_OPTIONS !== "undefined") {
  BONUS_OPTIONS.push({
    id: "arthur_metro_jacket_comment",
    who: "ar",
    text: "О! Зачекай, це що та куртка з метро?",
    label: "arthur_metro_jacket_react",
    conditions: {
      flag_true: ["arthur_has_metro_jacket"],
      flag_false: ["arthur_metro_jacket_comment_done"]
    },
    once: true
  });
}


// ─── Сцена місії ───

registerScript("metro_jacket_event", [
  {type: "say", who: "ao", text: "Зачекайте."},
  {type: "say", who: "ao", text: "Там на лавці... бачите?"},
  {type: "say", who: "ar", text: "Аоі, ми на місії."},
  {type: "say", who: "ao", text: "Та зачекай ти! Подивись — куртка. Ціла. Навіть чиста."},
  {type: "say", who: null, text: "Шкіряна. І виглядає непогано."},
  {type: "say", who: "ar", text: "Це сміття. Можемо рухатись далі?"},
  {type: "say", who: "ao", text: "Це НЕ сміття, Артуре. Це вінтаж."},
  {type: "say", who: "ar", text: "Вінтаж. На зараженій станції метро."},
  {type: "say", who: "ao", text: "Найкращі знахідки — в найгірших місцях!"},
  {type: "menu", choices: [
    {text: "Заберу собі. Непогана куртка.", label: "metro_jacket_take"},
    {text: "Та ні, залиш. Невідомо що на ній.", label: "metro_jacket_leave"},
    {text: "Артуре, може тобі? В твоєму стилі.", label: "metro_jacket_arthur"}
  ]}
]);

registerScript("metro_jacket_take", [
  {type: "say", who: "ao", text: "О! Тобі точно піде!"},
  {type: "say", who: "ar", text: "Як хочеш. Рухаємось."},
  {type: "set_flag", flag: "drifter_has_metro_jacket"},
  {type: "set_flag", flag: "metro_jacket_event_done"},
  {type: "chemistry", who: "ao", amount: 2},
  {type: "end"}
]);

registerScript("metro_jacket_leave", [
  {type: "say", who: "ao", text: "Ех... Ти правий, напевно."},
  {type: "say", who: "ar", text: "Розумне рішення."},
  {type: "set_flag", flag: "arthur_has_metro_jacket"},
  {type: "set_flag", flag: "metro_jacket_event_done"},
  {type: "chemistry", who: "ar", amount: 2},
  {type: "end"}
]);

registerScript("metro_jacket_arthur", [
  {type: "say", who: "ar", text: "Моя? Я не збираю речі з..."},
  {type: "say", who: "ao", text: "Артуре. Подивись на неї. Серйозно."},
  {type: "say", who: "ar", text: "...Добре. Але тільки тому що Аоі не замовкне."},
  {type: "say", who: "ao", text: "Він її взяв! Перемога!"},
  {type: "set_flag", flag: "arthur_has_metro_jacket"},
  {type: "set_flag", flag: "arthur_took_jacket_openly"},
  {type: "set_flag", flag: "metro_jacket_event_done"},
  {type: "chemistry", who: "ar", amount: 4},
  {type: "chemistry", who: "ao", amount: 2},
  {type: "end"}
]);


// ─── Бонусна сцена: реакція на куртку ───

registerScript("arthur_metro_jacket_react", [
  {type: "say", who: "ar", text: "Що?"},
  {type: "say", who: null, text: "«Куртка. Та, зі станції метро.»"},
  {type: "menu", choices: [
    {text: "Тобі йде. Серйозно.", label: "metro_jacket_react_nice"},
    {text: "Аоі була права — вінтаж тобі пасує.", label: "metro_jacket_react_aoi"}
  ]}
]);

registerScript("metro_jacket_react_nice", [
  {type: "say", who: "ar", text: "...Дякую."},
  {type: "set_flag", flag: "arthur_metro_jacket_comment_done"},
  {type: "chemistry", who: "ar", amount: 4},
  {type: "end"}
]);

registerScript("metro_jacket_react_aoi", [
  {type: "say", who: "ar", text: "Скажи їй це, і вона не замовкне тиждень."},
  {type: "say", who: "ar", text: "Але... так. Може вона не зовсім помилилась."},
  {type: "set_flag", flag: "arthur_metro_jacket_comment_done"},
  {type: "chemistry", who: "ar", amount: 2},
  {type: "chemistry", who: "ao", amount: 2},
  {type: "end"}
]);
