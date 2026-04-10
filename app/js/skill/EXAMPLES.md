# Приклади контенту — копіюй і адаптуй

## 1. Проста розмова (titles)

```js
// dialogues/arthur/rank1/talk_discipline.js

DIALOGUE_ENTRIES.push({
  id: "ar_r1_discipline",
  who: "ar",
  conditions: {
    flag_true: ["arthur_intro_done"],
    flag_false: ["ar_discipline_done"],
    chemistry_min: ["ar", 15]
  },
  priority: 35,
  titles: [
    {text: "Ти завжди такий суворий?", label: "ar_discipline_talk"}
  ]
});

registerScript("ar_discipline_talk", [
  {type: "show", who: "ar"},
  {type: "say", who: "mc", text: "Ти завжди такий суворий?"},
  {type: "say", who: "ar", text: "Суворий?"},
  {type: "say", who: "ar", text: "Я відповідальний. Є різниця."},
  {type: "say", who: "mc", text: "Яка?"},
  {type: "say", who: "ar", text: "Суворий — карає. Відповідальний — захищає."},
  {type: "chemistry", who: "ar", amount: 2},
  {type: "set_flag", flag: "ar_discipline_done"},
  {type: "end", text: ""}
]);
```

## 2. Forced діалог (автоматичний)

```js
// dialogues/eleanor/rank2/telepathy_event.js

DIALOGUE_ENTRIES.push({
  id: "el_r2_telepathy",
  who: "el",
  conditions: {
    chemistry_min: ["el", 40],
    flag_true: ["eleanor_intro_done"],
    flag_false: ["el_telepathy_event_done"]
  },
  priority: 80,
  label: "el_telepathy_event"
});

registerScript("el_telepathy_event", [
  {type: "show", who: "el"},
  {type: "telepathy", who: "el", text: "Не лякайся. Це я."},
  {type: "say", who: "el", text: "Вибач. Мені потрібно було перевірити."},
  {type: "say", who: "mc", text: "Перевірити що?"},
  {type: "say", who: "el", text: "Що ти не брешеш. Коли говориш що тобі не все одно."},
  {type: "menu", choices: [
    {text: "Мені справді не все одно.", label: "el_honest", chemistry: {"el": 5}},
    {text: "Ти читаєш мої думки?", label: "el_angry"}
  ]},
  {type: "label", id: "el_honest"},
  {type: "say", who: "el", text: "...Знаю. Тепер знаю."},
  {type: "set_flag", flag: "el_telepathy_event_done"},
  {type: "jump", to: "el_tele_end"},
  {type: "label", id: "el_angry"},
  {type: "say", who: "el", text: "Іноді. Не спеціально. Вибач."},
  {type: "set_flag", flag: "el_telepathy_event_done"},
  {type: "label", id: "el_tele_end"},
  {type: "end", text: ""}
]);
```

## 3. Banter (парна NPC сцена)

```js
// scenes/events/am_ao_gaming.js

BANTER_ENTRIES.push({
  id: "banter_am_ao_gaming",
  chars: ["am", "ao"],
  location: "arcade",
  conditions: {
    flag_false: ["banter_gaming_seen"],
    day_min: 3
  },
  priority: 5,
  label: "banter_gaming_scene"
});

registerScript("banter_gaming_scene", [
  {type: "show", who: "am", at: "left"},
  {type: "show", who: "ao", at: "right"},
  {type: "say", who: "am", text: "Аоі! Новий рекорд!"},
  {type: "say", who: "ao", text: "Покажи."},
  {type: "say", who: "ao", text: "...Це мій старий рекорд. Ти його побив на одне очко."},
  {type: "say", who: "am", text: "Рекорд є рекорд!"},
  {type: "set_flag", flag: "banter_gaming_seen"},
  {type: "end", text: ""}
]);
```

## 4. Квест з хуками і місією

```js
// scenes/quests/rooftop_quest.js

// Хук: нагадування
function checkRooftopQuestReminder() {
  if (!getFlag("rooftop_quest_started")) return;
  if (getFlag("rooftop_quest_done")) return;
  if (getFlag("rooftop_reminded")) return;
  if (gameState.time.day >= 10) {
    sendPagerMessage("qu", "Дах. Не забув?");
    setFlag("rooftop_reminded");
  }
}
registerDayHook(checkRooftopQuestReminder);

// Етап 1: Квінсі пропонує
DIALOGUE_ENTRIES.push({
  id: "qu_rooftop_offer",
  who: "qu",
  conditions: {
    chemistry_min: ["qu", 30],
    flag_false: ["rooftop_quest_started"],
    day_min: 5
  },
  priority: 55,
  titles: [
    {text: "Що там на даху?", label: "qu_rooftop_start"}
  ]
});

registerScript("qu_rooftop_start", [
  {type: "show", who: "qu"},
  {type: "say", who: "qu", text: "Дах. Тихо, ніхто не заважає."},
  {type: "say", who: "qu", text: "Приходь ввечері. Покажу дещо."},
  {type: "set_flag", flag: "rooftop_quest_started"},
  {type: "set_flag", flag: "rooftop_unlocked"},
  {type: "end", text: ""}
]);

// Етап 2: Зустріч на даху
DIALOGUE_ENTRIES.push({
  id: "qu_rooftop_meet",
  who: "qu",
  conditions: {
    flag_true: ["rooftop_quest_started"],
    flag_false: ["rooftop_quest_done"],
    location: "rooftop",
    time_min: 1080  // після 18:00
  },
  priority: 75,
  label: "qu_rooftop_scene"
});

registerScript("qu_rooftop_scene", [
  {type: "scene", bg: "bg_rooftop.webp"},
  {type: "show", who: "qu"},
  {type: "say", who: "qu", text: "Тихо тут."},
  {type: "say", who: null, text: "Квінсі дивиться на місто. Мовчить."},
  {type: "say", who: "qu", text: "Іноді... треба просто стояти і дивитись."},
  {type: "say", who: "qu", text: "Без стрільби. Без планів."},
  {type: "chemistry", who: "qu", amount: 5},
  {type: "set_flag", flag: "rooftop_quest_done"},
  {type: "addInsight", id: "quincy_peace", text: "Квінсі шукає тишу. Не тільки ціль."},
  {type: "end", text: ""}
]);

// Квестова місія
SPECIAL_MISSION_ENTRIES.push({
  id: "rooftop_sniper_mission",
  name: "СНАЙПЕРСЬКА ПОЗИЦІЯ",
  level: 4,
  reward: 400,
  rep: 7,
  partner: "qu",
  partner_count: 1,
  label: "rooftop_mission_dlg",
  conditions: {
    flag_true: ["rooftop_quest_done"],
    flag_false: ["rooftop_mission_done"]
  },
  chance: 100
});

registerScript("rooftop_mission_dlg", [
  {type: "show", who: "qu"},
  {type: "say", who: "qu", text: "Бачиш ту точку?"},
  {type: "say", who: "qu", text: "Один постріл. Одна можливість."},
  {type: "say", who: "mc", text: "Ти впевнений?"},
  {type: "say", who: "qu", text: "Завжди."},
  {type: "set_flag", flag: "rooftop_mission_done"},
  {type: "end", text: ""}
]);
```

## 5. Романтична гілка

```js
// dialogues/aoi/rank5/confession.js

DIALOGUE_ENTRIES.push({
  id: "ao_confession",
  who: "ao",
  conditions: {
    chemistry_min: ["ao", 160],
    flag_true: ["aoi_trusts"],
    flag_false: ["ao_confession_done"],
    dating: null  // не зустрічається ні з ким
  },
  priority: 95,
  label: "ao_confession_scene"
});

registerScript("ao_confession_scene", [
  {type: "scene", bg: "bg_rooftop.webp"},
  {type: "show", who: "ao"},
  {type: "play", channel: "music", file: "romantic_theme.mp3", loop: true, fadein: 2000},
  {type: "say", who: "ao", text: "Можна... поговорити?"},
  {type: "say", who: "ao", text: "Не про місії. Не про мол."},
  {type: "say", who: "ao", text: "Про нас."},
  {type: "menu", choices: [
    {text: "Я теж хотів поговорити.", label: "ao_yes"},
    {text: "Про що саме?", label: "ao_what"},
    {text: "Аоі, ми друзі.", label: "ao_friend"}
  ]},
  {type: "label", id: "ao_yes"},
  {type: "say", who: "ao", text: "Правда?"},
  {type: "say", who: "mc", text: "Правда."},
  {type: "say", who: "ao", text: "Тоді... давай спробуємо."},
  {type: "set_flag", flag: "ao_confession_done"},
  // startDating викликається в хуку нижче
  {type: "end", text: ""},
  {type: "label", id: "ao_what"},
  {type: "say", who: "ao", text: "Ти знаєш про що."},
  {type: "jump", to: "ao_yes"},
  {type: "label", id: "ao_friend"},
  {type: "say", who: "ao", text: "...Окей. Друзі. Добре."},
  {type: "set_flag", flag: "ao_confession_done"},
  {type: "set_flag", flag: "ao_friendzoned"},
  {type: "end", text: ""}
]);

// Хук: якщо гравець погодився — почати романс
var _aoConfCheck = setInterval(function() {
  if (getFlag("ao_confession_done") && !getFlag("ao_friendzoned") && !getFlag("ao_dating_set")) {
    startDating("ao");
    setFlag("ao_dating_set");
    addJournalEntry("Ми з Аоі тепер разом.", "romance");
    clearInterval(_aoConfCheck);
  }
}, 500);
```
