# CONTENT GUIDE — Як створювати контент для Drifter Loop

Цей документ — рецепт. Описує формати, шаблони і правила для створення діалогів, івентів, гілок.

---

## 1. ТИПИ КОНТЕНТУ І КУДИ КЛАСТИ

| Тип | Реєстрація | Папка | Приклад файлу |
|-----|-----------|-------|---------------|
| Діалог з персонажем | `DIALOGUE_ENTRIES` | `game/dialogues/{char}/` | `arthur_rank1_convo1.rpy` |
| Milestone (хімія 60/120) | `DIALOGUE_ENTRIES` | `game/dialogues/{char}/` | `arthur_trust_milestone.rpy` |
| Групова сцена | `DIALOGUE_ENTRIES` | `game/events/group/` | `bar_night.rpy` |
| Парний banter | `BANTER_ENTRIES` | `game/events/pairs/` | `amir_aoi_arcade.rpy` |
| Місійний діалог | `MISSION_DIALOGUE_ENTRIES` | `game/events/missions/` | `arthur_mission_1.rpy` |
| Місійний івент | `MISSION_DIALOGUE_ENTRIES` | `game/events/missions/` | `metro_jacket_event.rpy` |
| Awareness (патерни) | `DIALOGUE_ENTRIES` | `game/events/awareness/` | `spending_time_arthur.rpy` |
| Gift reaction | `DIALOGUE_ENTRIES` | `game/events/gifts/` | `arthur_gift_reactions.rpy` |
| Обіцянка | `DIALOGUE_ENTRIES` | `game/dialogues/{char}/` | `arthur_drinks_invite.rpy` |
| Stub (заглушка) | Автоматично через `STUB_TOPICS` | `game/stubs/` | `arthur_stubs.rpy` |
| **Динамічна опція** | `BONUS_OPTIONS` | `game/events/` або `game/dialogues/` | `arthur_metro_jacket_react.rpy` |

---

## 2. ШАБЛОН: ЗВИЧАЙНИЙ ДІАЛОГ

Кожен діалог починається з **меню** — без вступних реплік NPC.
Гравець клікає на персонажа і одразу бачить варіанти що сказати.

Диспетчер обирає ОДИН eligible діалог → його `titles` розгортаються
в меню разом з бонусними опціями, подарунком і "незважай".

`show`, `talked_today`, `dialogue_begin/end` — викликаються автоматично
в `location_loop`, НЕ в самому діалозі.

```renpy
# game/dialogues/{char}/{char}_{topic}.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "{char}_{topic}",
        "who": "Артур",
        "conditions": {
            "flag_false": ["{char}_{topic}_done"],
            "chemistry_min": ("Артур", 10),
        },
        "priority": 50,
        "chance": 100,
        # titles = список кортежів (текст_в_меню, label_гілки)
        # Кожен кортеж = один пункт меню при взаємодії з NPC
        "titles": [
            ("Привіт, як справи?", "{char}_{topic}_casual"),
            ("Слухай, є питання.", "{char}_{topic}_serious"),
            ("Чо робиш?", "{char}_{topic}_observe"),
        ],
    })

# Кожна гілка — окремий label. Викликається напряму з меню.
# show/dialogue_begin/talked_today — вже зроблені location_loop.

label {char}_{topic}_casual:
    mc "Привіт, як справи?"

    ar "Нормально. Ти щось хотів?"

    menu:
        "Та просто перепитати.":
            ar "Хм. Ну добре."
            $ add_chemistry("Артур", 2)

        "Хотів поговорити серйозно.":
            ar "Серйозно — це як?"
            $ add_chemistry("Артур", 4)

    # Кінцевий блок — НЕ ПОТРІБЕН в гілках!
    # seen_dialogues і set_flag — робить location_loop автоматично.
    return

label {char}_{topic}_serious:
    mc "Слухай, є одне питання."
    # ... діалог ...
    return

label {char}_{topic}_observe:
    mc "Чо робиш?"
    # ... діалог ...
    return
```

### ЩО РОБИТЬ LOCATION_LOOP АВТОМАТИЧНО (не треба писати в діалозі):

```python
# ДО діалогу:
$ store.talked_today.add(name)
$ reset_interaction(name)
$ dialogue_begin()              # ховає HUD, скидає лічильник
show {char} at char_center

# ПІСЛЯ return з гілки:
$ dialogue_end()                # списує час, показує HUD
$ store.seen_dialogues.add(id)
$ set_flag(id + "_done")
hide {char}
```

### TITLES — ПРАВИЛА НАПИСАННЯ:

**Titles = перші фрази Дрифтера.** Натуральні, як початок реальної розмови.

| Добре | Погано |
|---|---|
| "Привіт" | "Розкажи мені про свій бойовий досвід" |
| "Як справи?" | "Елеонор, як ти стала журналісткою?" |
| "Слухай, можу питання?" | "Що ти думаєш про філософію смерті?" |
| "Нудьгуєш?" | "Летті, що привело тебе до Хьольванії?" |
| "Чо як, старий?" | "Квінсі, яка твоя проблема з Артуром?" |

Кожна гілка починається з `mc "..."` — Дрифтер озвучує те що вибрав гравець,
потім NPC відповідає. Далі — звичайний діалог з menu всередині.

### КЛЮЧОВІ ВІДМІННОСТІ ВІД СТАРОГО ФОРМАТУ:

| Було (старе) | Стало |
|---|---|
| `"label": "arthur_convo1"` | `"titles": [("Привіт", "branch_label"), ...]` — titles замість label |
| `label` з вступними NPC репліками перед menu | Гілки одразу — menu це ПЕРШЕ що бачить гравець |
| `show`, `dialogue_begin`, `talked_today` в діалозі | Автоматично в `location_loop` — НЕ писати в діалозі |
| `seen_dialogues.add()`, `set_flag("_done")` в діалозі | Автоматично в `location_loop` — НЕ писати в діалозі |
| `$ advance_time(5)` після кожної репліки | Автоматично через `dialogue_begin/end` (3 хв/репліка) |
| `$ chemistry["Артур"] += 3` | `$ add_chemistry("Артур", 2)` — через daily cap |
| `"flag_true": ["arthur_intro_done"]` | **Не потрібно** — інтро гарантоване системою |
| `"flag_true": ["prev_convo_done"]` | `"chemistry_min": ("Артур", N)` — плоска система |

### ПРАВИЛА:

1. **НЕ** використовуй `advance_time()` — автолічильник
2. **НЕ** використовуй `chemistry[...] +=` — тільки `add_chemistry()`
3. **НЕ** пиши `show`/`hide`/`dialogue_begin`/`dialogue_end` — робить location_loop
4. **НЕ** пиши `seen_dialogues.add()`/`set_flag("_done")` — робить location_loop
5. **НЕ** створюй ланцюжки через `flag_true` — використовуй `chemistry_min`
6. **НЕ** перевіряй `_intro_done` — гарантоване
7. **НЕ** пиши вступні NPC репліки перед першим menu — menu йде ПЕРШЕ
8. Гілки закінчуються `return` — все інше автоматичне

---

## 3. УМОВИ (CONDITIONS) — ПЛОСКА СИСТЕМА

Діалоги з'являються на основі **стану світу**, не послідовності:

### Стабільні (перевіряються раз на день):

| Ключ | Формат | Опис |
|------|--------|------|
| `chemistry_min` | `("Артур", 10)` | Хімія >= значення |
| `chemistry_max` | `("Артур", 90)` | Хімія < значення |
| `flag_true` | `["flag1", "flag2"]` | Всі флаги True |
| `flag_false` | `["flag1"]` | Всі флаги False |
| `rank_min` | `2` | Ранг Гексу >= |
| `rank_max` | `4` | Ранг Гексу < |
| `day_min` | `10` | День >= |
| `day_max` | `25` | День < |
| `dating` | `None` або `"Артур"` | Поточний партнер |
| `persistent` | `"loop_count"` | Persistent > 0 (для NG+) |

### Динамічні (перевіряються при кожному get_dialogue):

| Ключ | Формат | Опис |
|------|--------|------|
| `time_from` | `1140` | Хвилини >= (19:00 = 1140) |
| `time_to` | `1320` | Хвилини < (22:00 = 1320) |
| `location` | `"bar"` | Гравець в цій локації |
| `chars_at_location` | `["Артур", "Летті"]` | Ці NPC в поточній локації |
| `mission_partner` | `"Квінсі"` | Тільки під час місії з цим NPC |

### Приклад: як діалоги відкриваються природно

```python
# Rank 1 convos (хімія 0-18):
convo1: chemistry_min 0    # одразу після інтро (інтро має priority 90, тому йде першим)
convo2: chemistry_min 5    # після 1-2 взаємодій
convo3: chemistry_min 10   # після кількох розмов/подарунків
convo4: chemistry_min 18   # потрібна цілеспрямована увага

# Rank 2 convos (хімія 20-45):
convo1: chemistry_min 20, rank_min 2
convo2: chemistry_min 28, rank_min 2
...
```

---

## 4. ХІМІЯ — BALANCE V2 ЗНАЧЕННЯ

### Скільки давати:

| Тип вибору | add_chemistry | Коли |
|---|---|---|
| Стандартний добрий | `+2` | Більшість правильних виборів |
| Відмінний/рідкісний | `+4` | Ключові моменти, глибоке розуміння персонажа |
| Поганий/образливий | `-2` | Невдалий жарт, нечутливість |
| Негативний | `-5` | Порушення довіри, зрада |

### Пороги хімії:

| Очки | Ранг | Що відкриває |
|------|------|-------------|
| 0-14 | Нейтрально | Rank 1 convos |
| 15-34 | Привітно | Якорні діалоги |
| 35-59 | Подобається | Глибші теми |
| 60-89 | Довіра | Trust milestone |
| 90-119 | Близько | Особисті теми |
| 120-159 | Друзі | Friends milestone, фінал |
| 160+ | Кохання | Romance confession |

---

## 5. ШАБЛОН: МІСІЙНИЙ ІВЕНТ

Відбувається під час місії. Реєструється в `MISSION_DIALOGUE_ENTRIES`.
Час рахується місією, тому `dialogue_begin/end` **не потрібні**.

```renpy
# game/events/missions/{event_name}.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "{event_name}",
        "who": "Артур",                          # Хто напарник
        "conditions": {
            "flag_false": ["{event_name}_done"],
            "chemistry_min": ("Артур", 30),
            "chemistry_min": ("Аоі", 30),        # Якщо потрібні 2 NPC
        },
        "priority": 50,
        "chance": 75,                             # 75% шанс тригера
        "label": "{event_name}",
    })

label {event_name}:
    # Місійний діалог — БЕЗ dialogue_begin/end, БЕЗ advance_time
    ar "Репліка під час місії."
    mc "Відповідь."

    menu:
        "Варіант 1":
            $ add_chemistry("Артур", 2)
        "Варіант 2":
            $ set_flag("some_flag")

    $ store.seen_dialogues.add("{event_name}")
    $ set_flag("{event_name}_done")
    return
```

---

## 6. ДИНАМІЧНІ ОПЦІЇ (BONUS_OPTIONS)

**Це найважливіша нова система.** Будь-який діалог може отримати додаткову опцію
в меню на основі стану світу — без зміни основного файлу діалогу.

### Як це працює:

1. Окремий файл реєструє `BONUS_OPTIONS.append(...)` з умовами
2. В будь-якому діалозі з цим NPC, якщо умова виконана — опція з'являється
3. Опція може залежати від: флагів, хімії, поточного одягу NPC, інвентарю

### Спосіб 1: Через `if` в menu (найпростіший)

```renpy
menu:
    "Звичайна опція 1":
        jump branch_1
    "Звичайна опція 2":
        jump branch_2
    "О! Це та куртка з метро!" if store.flags.get("arthur_has_metro_jacket") and store.current_outfits.get("Артур") == "metro_jacket":
        call arthur_metro_jacket_react
```

**Коли використовувати:** Коли бонусна опція потрібна в конкретному діалозі.

### Спосіб 2: Через BONUS_OPTIONS реєстр (для cross-file опцій)

```renpy
# game/events/missions/metro_jacket_react.rpy

init python:
    BONUS_OPTIONS.append({
        "id": "arthur_metro_jacket_comment",
        "who": "Артур",
        "text": "О! Зачекай, це що та куртка з метро?",
        "label": "arthur_metro_jacket_react",
        "conditions": {
            "flag_true": ["arthur_has_metro_jacket"],
        },
        "outfit_check": ("Артур", "metro_jacket"),  # тільки коли одягнений
        "once": True,                                 # зникає після використання
    })

label arthur_metro_jacket_react:
    # Ця гілка викликається через call — повертається назад
    ar "Що, бачиш щось знайоме?"
    mc "Це ж та куртка! З тієї станції метро."
    ar "...Може."

    menu:
        "Тобі йде.":
            ar "Дякую."
            $ add_chemistry("Артур", 4)
        "Вона ж була в смітті!":
            ar "Вона була на ЛАВЦІ. Це різні речі."
            $ add_chemistry("Артур", 2)

    $ mark_bonus_used("arthur_metro_jacket_comment")
    return
```

**Коли використовувати:** Коли опція має з'являтися в БУДЬ-ЯКОМУ діалозі з NPC,
а не в конкретному. Наприклад: NPC одягнув нову річ — гравець може прокоментувати
при будь-якій наступній розмові.

### Як вбудувати BONUS_OPTIONS в діалоги:

```renpy
label some_dialogue:
    show arthur at char_center
    $ dialogue_begin()

    ar "Привіт."

    # Основне меню
    $ _bonus = get_bonus_options("Артур")

    menu:
        "Звичайна опція 1":
            jump branch_1
        "Звичайна опція 2":
            jump branch_2

    # Якщо є бонусні опції — друге меню після основного
    if _bonus:
        menu:
            "Ще дещо..." if True:
                pass
        # Або показати кожну бонусну опцію
        for _opt in _bonus:
            # В Ren'Py немає dynamic menu items в for loop,
            # тому використовуй if-перевірки (див. Спосіб 1)
            pass

    $ dialogue_end()
    ...
```

**На практиці Спосіб 1 (`if` в menu) — найнадійніший і найчистіший.**
Спосіб 2 корисний для трекінгу і аналітики, але показ в меню все одно
через `if` в конкретних діалогах.

---

## 7. ПРІОРИТЕТИ

| Діапазон | Тип контенту |
|----------|-------------|
| 90-99 | Інтро, milestone, критичні (day30 warning) |
| 80-89 | Trauma, confession, healing |
| 70-79 | Групові сцени, важливі ланцюжки |
| 60-69 | Глибокі діалоги, обіцянки |
| 50-59 | Якорні діалоги (перша розмова кожного рангу) |
| 40-49 | NG+ гілки, другорядні |
| 1-10 | Awareness, патерни |

---

## 8. ПЕРСОНАЖІ

| Ім'я (кирилиця) | Тег діалогу | show ім'я | Домашня локація |
|-----------------|-------------|-----------|-----------------|
| Артур | `ar` | `arthur` | `security_desk` |
| Елеонор | `el` | `eleanor` | `furniture` |
| Летті | `le` | `lettie` | `medbay` |
| Амір | `am` | `amir` | `arcade` |
| Аоі | `ao` | `aoi` | `music_shop` |
| Квінсі | `qu` | `quince` | `range` |
| Дріфтер (MC) | `mc` | — | `backroom` |

---

## 9. ЛОКАЦІЇ

| ID | Назва |
|----|-------|
| `mall` | Мол Гьольванії |
| `info_desk` | Інфо-острівець |
| `security_desk` | Стійка охорони |
| `arcade` | Аркади |
| `music_shop` | Музичний магазин |
| `furniture` | Магазин меблів |
| `range` | Тир |
| `medbay` | Медвідділ |
| `bar` | Бар |
| `foodcourt` | Футкорт |
| `comp_club` | Комп'ютерний клуб |
| `garage` | Гараж |
| `backroom` | Бекрум |
| `rooftop` | Дах |
| `balcony` | Балкон 2-го поверху |
| `cafe` | Кав'ярня |
| `cafe_balcony` | Біля кав'ярні (2 поверх) |
| `utility` | Підсобка |
| `warehouse` | Склад |

---

## 10. ДОСТУПНІ ФУНКЦІЇ

### В кожному діалозі:
```python
$ store.talked_today.add("Артур")          # На початку
$ dialogue_begin()                          # Скидає лічильник, ховає HUD
$ dialogue_end()                            # Списує час, показує HUD
$ store.seen_dialogues.add("dialogue_id")   # В кінці
$ set_flag("dialogue_id_done")             # В кінці
```

### Хімія (тільки через add_chemistry!):
```python
$ add_chemistry("Артур", 2)                # Добрий вибір (+2)
$ add_chemistry("Артур", 4)                # Відмінний вибір (+4)
$ add_chemistry("Артур", -2)               # Поганий вибір (штрафи без cap)
```

### Флаги, інсайти, записи:
```python
$ set_flag("якийсь_флаг")
$ add_insight("id", "Текст факту")
$ add_journal_entry("Текст.", "conversation")
$ add_gossip("fact_name", ["Артур"], spread_delay=2)
$ create_promise("Артур", "bar", 1200, 1320, store.day + 1, "label")
```

### Одяг (clothing.rpy):
```python
$ set_outfit("Артур", "shirtless")         # Примусово змінити одяг
$ pick_outfit("Артур")                     # Рандомний з пулу
$ refresh_all_outfits()                    # Перевибрати одяг всім NPC
```

### Бонусні опції (bonus_options.rpy):
```python
$ get_bonus_options("Артур")               # Отримати eligible опції
$ mark_bonus_used("option_id")             # Позначити як використану
```

---

## 11. ЧЕКЛИСТ ПЕРЕД КОМІТОМ

- [ ] Файл має `init python:` з `DIALOGUE_ENTRIES.append()`
- [ ] Conditions: `flag_false` для цього діалогу + `chemistry_min`
- [ ] **НЕ** використовується `advance_time()` — є `dialogue_begin()`/`dialogue_end()`
- [ ] **НЕ** використовується `chemistry[...] +=` — тільки `add_chemistry()`
- [ ] **НЕ** перевіряється `_intro_done` в conditions
- [ ] **НЕ** створено ланцюжок через `flag_true: ["prev_done"]`
- [ ] `store.seen_dialogues.add()` і `set_flag("_done")` в кінці
- [ ] Новий флаг додано в `FLAGS_REGISTRY.md`
