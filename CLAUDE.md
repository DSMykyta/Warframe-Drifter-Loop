# Warframe: Drifter Loop — Контекст для Claude

## Що це
Кастомна HTML/JS візуальна новела. Діалогова система — flat entries з умовами (як Hades), не branching tree. Гра працює на web, APK, EXE однаково. Пріоритет — тачскрін.

## Архітектура

### Файлова структура
```
app/
  index.html          — SPA entry point, 1920x1080 viewport з CSS scale
  css/                — base, game, hud, menu, screens
  data/               — characters.csv, locations.csv, pager_messages.csv
  assets/             — sprites/, backgrounds/, audio/, icons/, pager/
  js/
    engine/           — state, dialogue, sprites, audio, transitions, effects, keyboard, loader, seen, preloader
    systems/
      core/           — time, money, flags, rank, decay, day, save, persistent
      social/         — chemistry, romance, gossip, promises, gifts, coffee, help_requests
      combat/         — missions, injuries
      world/          — locations/triggers, dispatcher, clothing, bonus_options, insights
      items/          — inventory
    ui/               — screens, hud, location, overlays, pager, backlog, gallery, loadscreen, settings, quickmenu, questtree, confirm
    scenes/           — intro, explore_mall, stubs, coffee_quest, pair_events, finale, finale_lose
    dialogues/        — *_intro.js (6 файлів) + stubs/ (30 файлів)
    demo/             — demo_init, demo_dialogues, demo_systems, demo_missions (ТЕСТ, зараз активний)
```

### Ключові принципи
1. **Short ID скрізь** — внутрішні ключі = ar, el, lt, am, ao, qu. `charName(id)` для display. `charFlag(id)` для flag names (arthur, eleanor...).
2. **Новий персонаж = рядок в characters.csv** — все інше автоматично (gossip routes, coffee prefs, daily flags, chemistry, triggers).
3. **Ніяких правих кліків, контекстних меню, hover-only інтерактивів** — тільки touch-friendly.
4. **Один клас `.sprite`** — і для scene (діалоги) і для location (локація). `dialogue-mode` на контейнері збільшує.
5. **`_enterDialogueMode()`** — єдина точка входу в діалоговий стан (ховає HUD, збільшує спрайти, блокує кліки).

### Діалоговий рушій (dialogue.js)
Типи нод: show, hide, scene, bg, say, menu, label, jump, call, return, with, play, stop, telepathy, think, set_flag, if, chemistry, time, pager, pager_request, wait_pager, effect, end.

`execute(pc)` — switch по типу ноди. `advance()` — наступна нода (клік/тап).

### Диспетчер (dispatcher.js)
- `DIALOGUE_ENTRIES` — з titles (меню) або label (forced)
- `BANTER_ENTRIES` — парні NPC сцени
- `MISSION_DIALOGUE_ENTRIES` — діалоги напарників на місіях
- Daily deck — фільтрується раз на день по stable conditions, dynamic перевіряються при кожному запиті
- Priority → chance → random — алгоритм вибору

### Ігровий цикл (game.js)
`startNewGame()` → intro → explore_mall → location loop.
`onSceneEnd()` — перевіряє після-intro, victory, defeat, pending mission, повертає до локації.
`nextDay()` в day.js — 15 кроків: penalty → day++ → resets → promises → neglect → decay → injuries → flags → missions → rank → events → deck → gossip → coffee hooks → autosave.

### Екран місії (overlays.js)
`_selectMission` → fade → `_executeMission`:
1. Loading spinner 4 сек (іконка в правому нижньому куті)
2. Якщо є місійний діалог → івент → ще 4 сек loading
3. `_showMissionReport` — чорний екран з "МІСІЮ ВИКОНАНО/ПРОВАЛЕНО", анімація чисел репутації/грошей
4. Клік → назад до гаражу

### Save/Load (save.js)
`SAVE_VERSION = 2`. Міграція v1→v2 конвертує кириличні ключі в short ID. `_syncDialogueToState()` / `_syncStateToDialogue()` для збереження позиції в діалозі.

### Persistent (persistent.js)
`localStorage["drifter_persistent"]` — loop_count, completed, all_friends, cg_unlocked, endings_seen, insights_log, previous_journal, romanced. Живе між петлями (NG+).

## Демо режим
Зараз активний. Сцени закоментовані в index.html, демо-файли підключені. Щоб повернути гру — див. `app/js/demo/README.md`.

## Відомі рішення
- Флаги = повні латинські імена (dating_arthur, helped_lettie_today)
- Внутрішні ключі = short ID (ar, el, lt, am, ao, qu)
- GOSSIP_ROUTES, COFFEE_PREFERENCES генеруються з CAST metadata
- Daily flags генеруються динамічно з CAST
- `charFlag(id)` читає CAST[id].flag_name замість hardcoded map
- `.sprite` — єдиний клас для всіх спрайтів (location + scene)
- `_enterDialogueMode()` — єдина точка входу

## Що не чіпати
- Кирилиця в text полях (display) — це нормально
- Коментарі з кирилицею — теж ок
- Структура CSV файлів — автолоадер парсить їх
