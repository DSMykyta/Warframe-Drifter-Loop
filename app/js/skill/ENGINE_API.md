# API Рушія — Довідник для написання контенту

## Персонажі (short ID)

| ID | Ім'я | Flag Name | Дім | Кава |
|----|------|-----------|-----|------|
| ar | Артур | arthur | security_desk | coffee_espresso |
| el | Елеонор | eleanor | furniture | coffee_latte |
| lt | Летті | lettie | medbay | coffee_latte |
| am | Амір | amir | arcade | coffee_espresso |
| ao | Аоі | aoi | music_shop | coffee_cocoa |
| qu | Квінсі | quincy | range | coffee_black |

`charName("ar")` → "Артур" (для display)
`charFlag("ar")` → "arthur" (для флагів)

---

## Типи нод діалогу

### say — репліка
```js
{type: "say", who: "ar", text: "Щодня. Без винятків."}
// who: "ar"/"el"/... = NPC, "mc" = гравець, null = наратор
// Опціонально: flag, chemistry: {"ar": 3}, time: 30
```

### menu — вибір
```js
{type: "menu", choices: [
  {text: "Згоден", label: "yes_branch", chemistry: {"ar": 2}},
  {text: "Ні", label: "no_branch"},
  {text: "Заблоковано", label: "locked", condition: {flag: "need_this_flag"}},
  {text: "Бонус", label: "bonus", bonus: true}
]}
```

### show / hide — спрайти
```js
{type: "show", who: "ar", at: "center", zorder: 1}
{type: "hide", who: "ar"}
```

### scene / bg — фони
```js
{type: "scene", bg: "bg_arcade.webp", text: "НАЗВА СЦЕНИ"}  // очищає спрайти
{type: "bg", file: "bg_arcade.webp"}  // тільки фон, спрайти залишаються
```

### label / jump / call / return — flow
```js
{type: "label", id: "my_section"}
{type: "jump", to: "my_section"}       // або ім'я скрипту
{type: "call", script: "other_script"} // повернеться через return
{type: "return"}
```

### if — умова
```js
{type: "if", flag: "has_pager", jump: "pager_yes", else_jump: "pager_no"}
{type: "if", chemistry_min: ["ar", 120], jump: "friends"}
{type: "if", flag_false: "intro_done", jump: "not_ready"}
{type: "if", first_loop: true, jump: "first_time"}
```

### set_flag / chemistry / time
```js
{type: "set_flag", flag: "quest_started"}
{type: "chemistry", who: "ar", amount: 5}
{type: "chemistry", values: {"ar": 3, "el": -2}}
{type: "time", minutes: 30}
```

### telepathy / think
```js
{type: "telepathy", who: "el", text: "...чуєш мене?"}  // трясучийся текст
{type: "think", text: "Треба подумати."}                 // курсив
```

### pager
```js
{type: "pager", who: "lt", text: "Зайди в медвідділ."}
{type: "pager_request", who: "am", text: "Допоможи?", accept: "help_yes", decline: "help_no"}
{type: "wait_pager", left: "accept_label", right: "decline_label"}
```

### effect / transition
```js
{type: "effect", name: "shake", intensity: 15, duration: 500}
{type: "effect", name: "flash", color: "#fff", duration: 300}
{type: "effect", name: "tint", color: "#f00", opacity: 0.3, duration: 800}
{type: "with", transition: "fade", duration: 600}
{type: "with", transition: "dissolve", duration: 500}
```

### play / stop — аудіо
```js
{type: "play", channel: "music", file: "theme.mp3", loop: true, fadein: 1000}
{type: "stop", channel: "music", fadeout: 1000}
{type: "play", channel: "sound", file: "door.mp3"}
```

### end — кінець
```js
{type: "end", text: ""}  // порожній = вихід при кліку
{type: "end", text: "Кінець розділу."}  // показує текст
```

---

## Реєстрація контенту

### DIALOGUE_ENTRIES — діалоги NPC
```js
DIALOGUE_ENTRIES.push({
  id: "unique_id",           // УНІКАЛЬНИЙ
  who: "ar",                 // short ID
  conditions: {              // коли доступний
    flag_true: ["intro_done"],
    flag_false: ["quest_done"],
    chemistry_min: ["ar", 60],
    day_min: 5,
    rank_min: 2
  },
  priority: 50,              // вищий = першим перевіряється
  chance: 100,               // % шанс (1-100)
  repeatable: false,         // чи можна повторити

  // ОДИН з двох:
  label: "script_name",      // forced — запускається автоматично
  // АБО
  titles: [                  // titles — гравець обирає
    {text: "Привіт", label: "greet_script", chemistry: {"ar": 2}},
    {text: "Як справи?", label: "howru_script"}
  ]
});
```

### BANTER_ENTRIES — парні сцени NPC
```js
BANTER_ENTRIES.push({
  id: "unique_id",
  chars: ["am", "ao"],       // хто бере участь
  location: "arcade",        // де (null = будь-де)
  conditions: {flag_false: ["banter_seen"]},
  priority: 5,
  label: "banter_script"
});
```

### MISSION_DIALOGUE_ENTRIES — діалог на місії
```js
MISSION_DIALOGUE_ENTRIES.push({
  id: "unique_id",
  who: "am",                 // напарник
  conditions: {},
  priority: 10,
  chance: 100,
  label: "mission_talk_script"
});
```

### SPECIAL_MISSION_ENTRIES — квестові місії
```js
SPECIAL_MISSION_ENTRIES.push({
  id: "unique_id",
  name: "НАЗВА МІСІЇ",
  level: 3,
  reward: 500,
  rep: 10,
  partner: "ar",
  partner2: "lt",            // опціонально
  partner_count: 2,
  label: "mission_dialogue",
  conditions: {flag_true: ["quest_stage_3"]},
  chance: 100
});
```

### BONUS_OPTIONS — додаткові опції в меню
```js
BONUS_OPTIONS.push({
  id: "unique_id",
  who: "ar",
  text: "Тримай подарунок.",
  label: "gift_scene",
  conditions: {flag_true: ["has_gift"]},
  once: true                 // зникає після використання
});
```

### HELP_REQUEST_ENTRIES — запити допомоги
```js
HELP_REQUEST_ENTRIES.push({
  id: "unique_id",
  who: "ao",
  conditions: {
    flag_false: ["helped_aoi_today"],
    chemistry_min: ["ao", 10],
    time_min: 600,
    time_max: 1320
  },
  chance: 30,
  message: "Допоможи?",
  location: "music_shop"
});
```

### RAW_THOUGHT_DEFS — зв'язки думок
```js
RAW_THOUGHT_DEFS.push({
  id: "thought_my_connection",
  requires: ["fact_id_1", "fact_id_2"],
  text: "Текст осмислення...",
  connection: "connection_flag_name"
});
```

---

## Хуки

### registerDayHook — виконується при nextDay()
```js
function myQuestDailyCheck() {
  if (!getFlag("quest_stage_1")) return;
  if (getFlag("quest_stage_2")) return;
  // логіка...
}
registerDayHook(myQuestDailyCheck);
```

---

## Корисні функції

| Функція | Що робить |
|---------|-----------|
| `setFlag("name")` | Встановити флаг |
| `getFlag("name")` | Прочитати флаг |
| `clearFlag("name")` | Скинути флаг |
| `addChemistry("ar", 5)` | +5 хімії Артуру (cap 15/день) |
| `addMoney(100)` | +100 крон |
| `spendMoney(50)` | -50 крон (повертає false якщо мало) |
| `advanceTime(30)` | +30 хвилин |
| `addHexRep(5)` | +5 репутації |
| `addInsight("id", "text")` | Додати факт в думки |
| `addJournalEntry("text", "event")` | Запис в щоденник |
| `addGossip("fact", ["ar"], 2)` | Створити плітку |
| `createPromise("ar", "loc", 600, 720, 5, "label")` | Обіцянка зустрічі |
| `sendPagerMessage("ar", "text")` | Повідомлення на пейджер |
| `charName("ar")` | → "Артур" |
| `charFlag("ar")` | → "arthur" |
| `startDating("ar")` | Почати романс (потрібно chem ≥ 160) |
| `breakUp("ar")` | Розірвати (-30 хімії) |

---

## Умови (conditions)

### Стабільні (раз на день)
| Поле | Формат | Приклад |
|------|--------|---------|
| `flag_true` | ["flag1", "flag2"] | Всі мають бути true |
| `flag_false` | ["flag1"] | Всі мають бути false |
| `chemistry_min` | ["ar", 60] | Хімія ≥ 60 |
| `chemistry_max` | ["ar", 120] | Хімія < 120 |
| `rank_min` | 2 | Ранг ≥ 2 |
| `rank_max` | 4 | Ранг < 4 |
| `day_min` | 5 | День ≥ 5 |
| `day_max` | 15 | День < 15 |
| `dating` | "ar" або null | Зустрічається з |

### Динамічні (при кожному запиті)
| Поле | Формат | Приклад |
|------|--------|---------|
| `time_min` | 600 | Час ≥ 10:00 |
| `time_max` | 1320 | Час < 22:00 |
| `location` | "arcade" | Гравець тут |
| `talked_today` | true/false | + who |
| `chars_at_location` | ["ar", "el"] | Всі тут |

---

## Пріоритети (рекомендовано)

| Діапазон | Тип контенту |
|----------|-------------|
| 90-99 | Критичні сюжетні (фінал, день 30) |
| 70-89 | Forced квестові діалоги |
| 50-69 | Titles з виборами |
| 30-49 | Звичайні розмови |
| 10-29 | Заглушки, дрібниці |
| 1-9 | Banter, фон |
