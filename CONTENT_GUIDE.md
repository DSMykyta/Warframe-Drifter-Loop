# CONTENT GUIDE — Як створювати контент для Drifter Loop

Цей документ — рецепт. Описує формати, шаблони і правила для створення діалогів, івентів, гілок.

---

## 1. ТИПИ КОНТЕНТУ І КУДИ КЛАСТИ

| Тип | Реєстрація | Папка | Приклад файлу |
|-----|-----------|-------|---------------|
| Діалог з персонажем | `DIALOGUE_ENTRIES` | `game/dialogues/{char}/` | `arthur_about_team.rpy` |
| Milestone (хімія 60/120) | `DIALOGUE_ENTRIES` | `game/dialogues/{char}/` | `arthur_trust_milestone.rpy` |
| Групова сцена | `DIALOGUE_ENTRIES` | `game/events/group/` | `bar_night.rpy` |
| Парний banter | `BANTER_ENTRIES` | `game/events/pairs/` | `amir_aoi_arcade.rpy` |
| Місійний міні-діалог | `MISSION_DIALOGUE_ENTRIES` | `game/events/missions/` | `arthur_mission_1.rpy` |
| Awareness (патерни) | `DIALOGUE_ENTRIES` | `game/events/awareness/` | `spending_time_arthur.rpy` |
| Gift reaction | `DIALOGUE_ENTRIES` | `game/events/gifts/` | `arthur_gift_reactions.rpy` |
| Обіцянка | `DIALOGUE_ENTRIES` | `game/dialogues/{char}/` | `arthur_drinks_invite.rpy` |
| Stub (заглушка) | Автоматично через `STUB_TOPICS` | `game/stubs/` | `arthur_stubs.rpy` |

---

## 2. ШАБЛОН: ЗВИЧАЙНИЙ ДІАЛОГ

```renpy
# game/dialogues/{char}/{char}_{topic}.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "{char}_{topic}",            # Унікальний ID
        "who": "Артур",                     # Кирилицею, як в CAST
        "conditions": {                     # Коли доступний (див. секцію 5)
            "flag_true": ["arthur_intro_done"],
            "flag_false": ["{char}_{topic}_done"],
            "chemistry_min": ("Артур", 30),
        },
        "priority": 50,                    # Чим вище — тим раніше спрацює (див. секцію 6)
        "chance": 100,                      # % шанс що спрацює
        "label": "{char}_{topic}",
    })

label {char}_{topic}:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    ar "Репліка NPC."
    $ advance_time(5)

    mc "Відповідь гравця."
    $ advance_time(5)

    menu:
        "Варіант 1":
            $ advance_time(5)
            ar "Реакція на варіант 1."
            $ advance_time(5)
            $ chemistry["Артур"] += 3       # Якщо є вплив
            $ set_flag("якийсь_флаг")       # Якщо відкриває щось

        "Варіант 2":
            $ advance_time(5)
            ar "Реакція на варіант 2."
            $ advance_time(5)

    # ОБОВ'ЯЗКОВИЙ БЛОК ЗАКРИТТЯ:
    $ store.seen_dialogues.add("{char}_{topic}")
    $ set_flag("{char}_{topic}_done")
    $ add_insight("insight_id", "Текст факту для шафи думок.")  # опціонально
    $ add_journal_entry("Запис в щоденник.", "conversation")     # опціонально

    hide arthur
    return
```

---

## 3. ШАБЛОН: ГРУПОВА СЦЕНА

```renpy
# game/events/group/{scene_name}.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "{scene_name}",
        "who": "Артур",                     # Хто ініціює (для daily_deck)
        "conditions": {
            "flag_true": ["arthur_intro_done", "lettie_intro_done"],
            "flag_false": ["{scene_name}_done"],
            "chars_at_location": ["Артур", "Летті"],  # Обидва мають бути тут
            "time_from": 1140,              # Після 19:00 (опціонально)
        },
        "priority": 70,
        "chance": 50,
        "label": "{scene_name}",
    })

label {scene_name}:
    $ store.talked_today.add("Артур")
    $ store.talked_today.add("Летті")

    show arthur at left
    show lettie at right

    ar "Репліка."
    $ advance_time(5)
    le "Репліка."
    $ advance_time(5)

    # ... діалог ...

    $ chemistry["Артур"] += 3
    $ chemistry["Летті"] += 3
    $ store.seen_dialogues.add("{scene_name}")
    $ set_flag("{scene_name}_done")

    hide arthur
    hide lettie
    return
```

---

## 4. ШАБЛОН: ПАРНИЙ BANTER

Banter = фонова сценка при вході в локацію. Не вибирається гравцем — просто відбувається.

```renpy
# game/events/pairs/{pair_name}.rpy

init python:
    BANTER_ENTRIES.append({
        "id": "{pair_name}",
        "location": "comp_club",            # Де відбувається (None = будь-де)
        "chars": ["Аоі", "Амір"],           # Обидва мають бути в локації
        "conditions": {
            "flag_true": ["aoi_intro_done", "amir_intro_done"],
            "flag_false": ["{pair_name}_seen"],
        },
        "label": "{pair_name}",
    })

label {pair_name}:
    show aoi at left
    show amir at right

    am "Репліка."
    $ advance_time(5)
    ao "Репліка."
    $ advance_time(5)

    $ set_flag("{pair_name}_seen")
    $ store.seen_dialogues.add("{pair_name}")

    hide aoi
    hide amir
    return
```

**Одиночний banter** (текстовий, без label):

```python
BANTER_ENTRIES.append({
    "id": "quincy_troll_comment",
    "who": "Квінсі",                        # Одиночний — "who" замість "chars"
    "conditions": {
        "flag_true": ["quincy_intro_done"],
        "flag_false": ["quincy_troll_seen"],
    },
    "location": None,                        # Будь-де
    "text": "nice moves m8",                 # Текст без label
})
```

---

## 5. УМОВИ (CONDITIONS)

### Стабільні (перевіряються раз на день при build_daily_deck):

| Ключ | Формат | Опис |
|------|--------|------|
| `chemistry_min` | `("Артур", 60)` | Хімія >= значення |
| `chemistry_max` | `("Артур", 90)` | Хімія < значення |
| `flag_true` | `["flag1", "flag2"]` | Всі флаги True |
| `flag_false` | `["flag1"]` | Всі флаги False (ще не ставились) |
| `rank_min` | `2` | Ранг Гексу >= |
| `rank_max` | `4` | Ранг Гексу < |
| `day_min` | `10` | День >= |
| `day_max` | `25` | День < |
| `dating` | `None` або `"Артур"` | Поточний партнер |
| `persistent` | `"loop_count"` | Persistent змінна > 0 (для NG+) |

### Динамічні (перевіряються при кожному get_dialogue):

| Ключ | Формат | Опис |
|------|--------|------|
| `time_from` | `1140` | Хвилини >= (19:00 = 1140) |
| `time_to` | `1320` | Хвилини < (22:00 = 1320) |
| `location` | `"bar"` | Гравець в цій локації |
| `chars_at_location` | `["Артур", "Летті"]` | Ці NPC в поточній локації гравця |
| `mission_partner` | `"Квінсі"` | Тільки під час місії з цим NPC |

### Додаткові (для спец. контенту):

| Ключ | Формат | Опис |
|------|--------|------|
| `expires_in_days` | `3` | Діалог доступний N днів після появи в deck (потім зникає) |
| `on_expire` | `"label_name"` | Label що викликається коли діалог протух (опціонально) |
| `tag` | `"heavy_lore"` | Cooldown-тег: діалоги з однаковим тегом не повторюються в один день |

**Примітка:** Диспетчер також розуміє `time_min`/`time_max` — це синоніми `time_from`/`time_to`. Для нового контенту використовуй `time_from`/`time_to`.

---

## 6. ПРІОРИТЕТИ

| Діапазон | Тип контенту |
|----------|-------------|
| 90-99 | Інтро, milestone, критичні (day30 warning) |
| 80-89 | Trauma, confession, healing |
| 70-79 | Групові сцени, важливі ланцюжки |
| 60-69 | Глибокі діалоги, обіцянки |
| 50-59 | Якорні діалоги (стандартні) |
| 40-49 | NG+ гілки |
| 1-10 | Awareness, патерни |

Якщо пріоритет однаковий — випадковий вибір з найвищих.

---

## 7. ШАБЛОН: МІСІЙНИЙ ДІАЛОГ

Відбувається під час місії. Без `advance_time()`. Реєструється в **MISSION_DIALOGUE_ENTRIES** (не DIALOGUE_ENTRIES).

```renpy
# game/events/missions/{char}_mission_{N}.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "{char}_mission_{N}",
        "who": "Артур",
        "conditions": {
            "flag_true": ["arthur_intro_done"],
        },
        "priority": 50,
        "label": "{char}_mission_{N}",
    })

label {char}_mission_{N}:
    ar "Репліка під час місії."
    mc "Відповідь."
    ar "Ще репліка."
    return
```

---

## 8. ШАБЛОН: ОБІЦЯНКА

Діалог створює обіцянку → наступного дня NPC чекає → гравець приходить або ні.

```renpy
# В діалозі-запрошенні:
$ create_promise("Артур", "bar", 1200, 1320, store.day + 1, "arthur_bar_meeting")
# Хто, де, з якої хвилини, до якої, якого дня, label зустрічі

# Label зустрічі (в тому ж файлі):
label arthur_bar_meeting:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    ar "Прийшов. Добре."
    $ advance_time(5)
    # ... діалог зустрічі ...

    $ chemistry["Артур"] += 5
    $ set_flag("arthur_bar_meeting_done")
    $ fulfill_promise(store.promises[-1] if store.promises else None)

    hide arthur
    return
```

Якщо гравець не прийде — `check_broken_promises()` в next_day дає -5 хімії.

---

## 9. ШАБЛОН: STUB (ЗАГЛУШКА)

Коли нема eligible діалогів — диспетчер дає stub. Не потребує реєстрації в DIALOGUE_ENTRIES.
Теми визначені в `STUB_TOPICS` (dispatcher.rpy). Label = `stub_{Ім'я}_{тема}`.

```renpy
# game/stubs/{char}_stubs.rpy

label stub_Артур_cooking:
    show arthur at char_center
    ar "Сьогодні готую рагу. Якщо знайду картоплю."
    $ advance_time(5)
    ar "Якщо ні — знову консерви."
    $ advance_time(5)
    hide arthur
    return
```

---

## 10. ІМЕНУВАННЯ І РЕЄСТР ФЛАГІВ

### Іменування

Повні правила — `NAMING_CONVENTIONS.md`. Коротко:

- Флаг: `{хто}_{що}_{стан}` — `arthur_cooking_done`, `intro_stayed_silent`, `pair_arthur_quincy_seen`
- Файл: `{char}_{тема}.rpy` — збігається з label і ID
- Label = ID = ім'я файлу: `arthur_cooking` всюди

### Реєстр

Кожен `set_flag()` **обов'язково** додається в `FLAGS_REGISTRY.md`.

Для кожного флагу вказати:
- **Флаг** — назва
- **Файл** — де ставиться (`set_flag()`)
- **Контекст** — що сталося в грі
- **Використовується** — де цей флаг є в `flag_true`/`flag_false` як тригер. Якщо поки ніде — `—`

Перед створенням нового діалогу — перевір реєстр. Якщо потрібен флаг з іншого діалогу, знайди його в реєстрі щоб дізнатися точну назву і контекст.

---

## 11. ДОСТУПНІ ФУНКЦІЇ

### Обов'язкові в кожному діалозі:
```python
$ store.talked_today.add("Артур")          # На початку
$ advance_time(5)                           # Після кожної репліки (5 хв)
$ store.seen_dialogues.add("dialogue_id")   # В кінці
$ set_flag("dialogue_id_done")             # В кінці
```

### Опціональні:
```python
$ chemistry["Артур"] += 5                   # Змінити хімію
$ chemistry["Артур"] -= 3                   # Зменшити хімію
$ set_flag("якийсь_флаг")                  # Поставити флаг (для умов інших діалогів)
$ add_insight("id", "Текст факту")         # Факт в шафу думок
$ add_journal_entry("Текст.", "тип")       # Запис в щоденник
$ add_gossip("Артур", "flirt", "Аоі")     # Додати плітку
$ create_promise("Хто", "де", from, to, day, "label")  # Обіцянка
$ start_dating("Артур")                    # Почати романс (chemistry >= 160)
$ add_injury_stack("player")               # Травма гравцю
$ add_injury_stack("Артур")                # Травма NPC
```

### Типи journal_entry:
`"conversation"`, `"mission"`, `"promise"`, `"insight"`, `"romance"`, `"milestone"`, `"event"`, `"lore"`

---

## 12. ПЕРСОНАЖІ

| Ім'я (кирилиця) | Тег діалогу | show ім'я | Домашня локація |
|-----------------|-------------|-----------|-----------------|
| Артур | `ar` | `arthur` | `info_desk` |
| Елеонор | `el` | `eleanor` | `furniture` |
| Летті | `le` | `lettie` | `medbay` |
| Амір | `am` | `amir` | `arcade` |
| Аоі | `ao` | `aoi` | `music_shop` |
| Квінсі | `qu` | `quince` | `range` |
| Дріфтер (MC) | `mc` | — | `backroom` |

### Позиції на екрані:
```renpy
show arthur at char_center    # Один персонаж — по центру
show arthur at left           # Двоє — лівий
show lettie at right          # Двоє — правий
```

---

## 13. ЛОКАЦІЇ

| ID | Назва | Суміжні |
|----|-------|---------|
| `mall` | Мол Гьольванії | Всі точки |
| `info_desk` | Інфостійка | mall, info_room |
| `info_room` | Кімната за стійкою | info_desk |
| `arcade` | Аркади | mall |
| `music_shop` | Музичний магазин | mall |
| `furniture` | Магазин меблів | mall |
| `range` | Тир | mall |
| `medbay` | Медвідділ | mall |
| `bar` | Бар | mall |
| `foodcourt` | Футкорт | mall |
| `comp_club` | Комп'ютерний клуб | mall, garage |
| `garage` | Гараж | comp_club |
| `backroom` | Бекрум | mall |
| `rooftop` | Дах | mall |

Переміщення: сусідні = 5 хв, через мол = 10 хв.

---

## 14. ХІМІЯ (ТІРИ)

| Очки | Ранг | Що відкриває |
|------|------|-------------|
| 0-14 | Нейтрально | Інтро |
| 15-34 | Привітно | Якорні |
| 35-59 | Подобається | Більше якорних |
| 60-89 | Довіра | Trust milestone, глибокі |
| 90-119 | Близько | Ланцюжки |
| 120-159 | Друзі | Friends milestone, фінал |
| 160+ | Кохання | Romance confession |

---

## 15. ЧАС

- Гравець прокидається о **08:00** (480 хв)
- Після **24:00** (1440 хв) — ніч, NPC зникають
- Кожна репліка = `advance_time(5)` (5 хв)
- Місія = рівень × 60 хв
- Подарунок = 10 хв
- Переміщення = 5 або 10 хв

**Конвертація:** 19:00 = 1140, 20:00 = 1200, 21:00 = 1260, 22:00 = 1320

---

## 16. ЛАНЦЮЖКИ ЧЕРЕЗ ФЛАГИ

Діалог A ставить флаг → Діалог B вимагає цей флаг:

```
arthur_intro → flag: arthur_intro_done
  → arthur_about_team (flag_true: arthur_intro_done) → flag: arthur_about_team_done
    → arthur_cooking (flag_true: arthur_about_team_done) → flag: arthur_cooking_done
      → arthur_drinks_invite (flag_true: arthur_cooking_done, chemistry_min: 30)
```

Кожен наступний діалог вимагає `flag_true` від попереднього + можливо `chemistry_min`.

---

## 17. ШАБЛОН: ТРАВМА/INJURY КОНТЕНТ

Травми — важлива ігрова механіка. Стаки (1-3) додаються через місії або сюжетно. Діалоги можуть реагувати на стан травм.

### Діалог-реакція на травму NPC:

```renpy
# game/dialogues/{char}/{char}_injured_reaction.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "{char}_injured_reaction",
        "who": "Летті",                         # Хто говорить
        "conditions": {
            "flag_true": ["lettie_intro_done"],
            "flag_false": ["{char}_injured_reaction_done"],
        },
        "priority": 80,                          # Високий — травма важлива
        "chance": 100,
        "label": "{char}_injured_reaction",
    })

label {char}_injured_reaction:
    show lettie at char_center
    $ store.talked_today.add("Летті")

    le "Як ти? Бачила, що місія пішла не за планом."
    $ advance_time(5)

    # Перевірка стану гравця:
    if get_injury_stacks("player") >= 2:
        le "Ти маєш відпочити. Серйозно."
        $ advance_time(5)
    elif get_injury_stacks("player") >= 1:
        le "Нічого страшного, але обережніше."
        $ advance_time(5)

    $ store.seen_dialogues.add("{char}_injured_reaction")
    $ set_flag("{char}_injured_reaction_done")
    hide lettie
    return
```

### Banter при травмі:

```python
BANTER_ENTRIES.append({
    "id": "amir_sees_injured_player",
    "who": "Амір",
    "location": None,
    "conditions": {
        "flag_true": ["amir_intro_done"],
    },
    # У коді get_banter() перевірить get_injury_stacks("player") >= 1
    "text": "Ого, ти виглядаєш потрепано. Все ок?",
})
```

### Доступні функції для травм:

```python
$ add_injury_stack("player")               # Додати стак гравцю
$ add_injury_stack("Артур")                # Додати стак NPC
$ get_injury_stacks("player")              # Поточні стаки (0-3)
$ get_injury_stacks("Артур")               # Стаки NPC
$ is_npc_absent("Артур")                   # True якщо 3 стаки (NPC відсутній)
$ is_npc_mission_eligible("Артур")         # True якщо < 2 стаків
```

### Правила травм:

- **1 стак:** NPC ходить, але +10% шанс нової травми при місії
- **2 стаки:** NPC не доступний як напарник для місій
- **3 стаки:** NPC повністю відсутній (переміщується в medbay)
- **Зцілення:** Стак зникає через 1 повний день без нових травм (день 12 отримав → день 13 ще є → день 14 зник)
- **Летті як напарник:** Шанс травм = 0%
- **Повторна місія:** +10% шанс за кожну повторну місію з тим самим напарником за день

---

## 18. ПРОТУХАЮЧІ ІВЕНТИ

Деякі діалоги мають дедлайн — вікно можливості:

```python
DIALOGUE_ENTRIES.append({
    "id": "arthur_limited_offer",
    "who": "Артур",
    "conditions": {
        "flag_true": ["arthur_cooking_done"],
        "flag_false": ["arthur_limited_offer_done"],
        "day_min": 10,
    },
    "priority": 60,
    "expires_in_days": 3,                    # Зникає через 3 дні після появи в deck
    "on_expire": "arthur_limited_expired",   # Опціонально: label при протуханні
    "label": "arthur_limited_offer",
})
```

Якщо є `on_expire` — label викликається автоматично в `next_day()`. Використовуй для наслідків пропущеного діалогу (NPC розчарований, плітки, зміна хімії).

---

## 19. COOLDOWN ТЕГИ

Для контролю щільності контенту. Діалоги з однаковим `tag` не обираються більше 1 разу/день:

```python
DIALOGUE_ENTRIES.append({
    "id": "arthur_deep_lore_1",
    "who": "Артур",
    "conditions": { ... },
    "priority": 60,
    "tag": "heavy_lore",                     # Один heavy_lore на день
    "label": "arthur_deep_lore_1",
})
```

Теги відстежуються в `tags_used_today` (скидається кожен день). Корисні теги:
- `heavy_lore` — глибока лор-інформація
- `emotional` — емоційно тяжкі сцени
- `flirt` — флірт-опції

---

## 20. ПРИКЛАД: ПОВНИЙ ОПИС → ФАЙЛ

**Опис:** "Амір після місії рівня 4+ скаржиться на болі в руках, Летті пропонує допомогу, гравець вибирає — підтримати Аміра чи пожартувати."

**Що робити:**

1. Файл: `game/dialogues/amir/amir_hand_pain.rpy`
2. Реєстрація в `DIALOGUE_ENTRIES`
3. Conditions: `flag_true: [amir_intro_done, lettie_intro_done]`, `flag_false: [amir_hand_pain_done]`, `chemistry_min: (Амір, 35)`, `chars_at_location: [Летті]`
4. Label з діалогом, menu, закриттям

---

## 21. РОЗБІЖНОСТІ З ARCHITECTURE.md

ARCHITECTURE.md — дизайн-документ (ідея). Цей CONTENT_GUIDE відображає **реальний код**.

| Тема | Architecture каже | Код/Guide каже | Правий |
|------|------------------|---------------|--------|
| Час у conditions | `time_min`/`time_max` | `time_from`/`time_to` (диспетчер розуміє обидва) | Код — обидва працюють, для нового контенту `time_from`/`time_to` |
| Місійні діалоги | `DIALOGUE_ENTRIES` з `mission_partner` | Окремий `MISSION_DIALOGUE_ENTRIES` | Код — окремий пул логічніший |
| Show name Квінсі | Не уточнює | `quince` (show), `quincy` (flags/files) | Код — два різних імені для різних контекстів |
