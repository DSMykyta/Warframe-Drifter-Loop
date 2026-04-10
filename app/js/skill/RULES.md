# Правила написання контенту

## Що МОЖНА

- Створювати .js файли в `scenes/` і `dialogues/` (будь-яка глибина папок)
- Викликати `registerScript()`, пушати в `DIALOGUE_ENTRIES`, `BANTER_ENTRIES`, `MISSION_DIALOGUE_ENTRIES`, `SPECIAL_MISSION_ENTRIES`, `BONUS_OPTIONS`, `HELP_REQUEST_ENTRIES`, `RAW_THOUGHT_DEFS`
- Використовувати `registerDayHook()` для щоденних перевірок
- Викликати будь-які функції з ENGINE_API.md
- Використовувати всі типи нод діалогу

## Що НЕ МОЖНА

### ID
- **НІКОЛИ** не дублювати ID (dialogue, banter, mission). Рушій попередить в консолі, але це все одно баг.
- Конвенція імен: `{character}_{quest}_{stage}` — наприклад `ar_sword_quest_stage2`

### Флаги
- Не створювати флаги з однаковими іменами в різних файлах для різних цілей
- Конвенція: `{quest_name}_{action}` — наприклад `coffee_quest_started`, `coffee_machine_found`
- Одноденні флаги (скидаються щодня) мають закінчуватись на `_today`

### Скрипти
- Ім'я скрипту = унікальне. Конвенція: `{character}_{context}_{action}`
- **НІКОЛИ** не робити `{type: "jump", to: "same_script"}` де same_script = поточний скрипт. Це вічний цикл.
- Кожен скрипт МУСИТЬ мати `{type: "end"}` в кінці (або `{type: "return"}` для підскриптів)

### Діалоги (say)
- `who: "ar"` — тільки short ID, не "Артур"
- `who: "mc"` — фрази гравця (без плашки імені)
- `who: null` — наратор (курсив)
- Текст — тільки промова. Без емодзі. Без дужок типу "(сміється)".
- Думки гравця → `{type: "think"}`, не say
- Телепатія Елеонор → `{type: "telepathy", who: "el"}`

### Хімія
- Daily cap = 15 на персонажа. Не намагайся дати +50 в одному діалозі — буде обрізано.
- Негативна хімія НЕ обмежена капом.
- `chemistry` в `say` ноді — маленькі бонуси (+1..+3). Великі — через `{type: "chemistry"}` окремо.

### Час
- Розмова = 15 хв (автоматично при кліку на NPC)
- Додатковий час в діалозі через `{type: "time", minutes: N}`
- Контролюй час — гравець має обмежений день

### Пріоритети
- 90-99: критичні сюжетні (не зловживай)
- 70-89: forced квестові
- 50-69: titles з виборами
- 30-49: звичайні
- 10-29: заглушки
- 1-9: banter

### Titles vs Label
- `titles: [...]` — гравець ОБИРАЄ тему. Показує меню привітань.
- `label: "script"` — FORCED. Запускається автоматично при вході в локацію де є NPC.
- НЕ ставити і titles і label одночасно.

### Conditions
- `flag_true` / `flag_false` — масиви рядків
- `chemistry_min` / `chemistry_max` — масив [id, число]
- `day_min` / `day_max` — число (день включно / не включно)
- `rank_min` / `rank_max` — число
- `location` — id локації (динамічна умова)
- `time_min` / `time_max` — хвилини (динамічна умова)

### Файлова структура
```
scenes/
  act1/
    intro.js          ← сюжетні сцени (runScript напряму)
    explore_mall.js
  quests/
    coffee_quest.js   ← квести з хуками
  events/
    pair_events.js    ← banter сцени
  finale/
    finale.js
    finale_lose.js

dialogues/
  arthur/
    rank1/            ← діалоги за рангом хімії
      talk_sword.js
    rank3/
      deep_talk.js
  eleanor/
    rank1/
    rank3/
  stubs/              ← заглушки (fallback)
    arthur/
    eleanor/
```

### Після створення файлу
```bash
cd app/js
bash generate_manifest.sh
```
Це оновить `content.json` і гра підхопить новий файл.
