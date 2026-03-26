# game/scenes/finale_win.rpy
# ═══════════════════════════════════════════════
# ФІНАЛ: ПЕРЕМОГА
# ═══════════════════════════════════════════════

init -5 python:

    def check_all_friends():
        """Перевіряє чи всі 6 персонажів на рівні Друзі (120+)."""
        for name in CAST:
            if store.chemistry.get(name, 0) < 120:
                return False
        return True

    def check_finale_trigger():
        """Перевіряє чи настав фінал (день 31)."""
        return store.day >= 31


# ═══════════════════════════════════════════════
# ПЕРЕВІРКА В КІНЦІ ДНЯ 30
# ═══════════════════════════════════════════════

init python:
    DIALOGUE_ENTRIES.append({
        "id": "day30_warning",
        "who": "Артур",
        "conditions": {
            "day_min": 30,
            "day_max": 31,
            "flag_false": ["day30_warning_done"],
        },
        "priority": 99,
        "chance": 100,
        "label": "day30_warning",
    })

label day30_warning:
    show arthur at char_center

    ar "Завтра — Новий Рік. Реактор."
    $ advance_time(5)

    ar "Якщо ми не готові... якщо ми не довіряємо одне одному повністю..."
    $ advance_time(5)

    ar "Не буде другого шансу."
    $ advance_time(5)

    $ set_flag("day30_warning_done")
    $ store.seen_dialogues.add("day30_warning")

    hide arthur
    return


# ═══════════════════════════════════════════════
# ПЕРЕМОГА
# ═══════════════════════════════════════════════

label finale_victory:
    scene black
    pause 1.0

    "День 31. Новий Рік. Реактор."
    pause 1.0

    "Гекс стоїть разом. Усі шестеро. І ти."
    pause 1.0

    show arthur at left
    ar "Ми готові."
    $ advance_time(5)

    show eleanor at right
    el "Я бачу в них впевненість. Справжню."
    $ advance_time(5)

    hide arthur
    hide eleanor

    show lettie at left
    le "Якщо хтось поранеться — я тут. Але краще б ніхто не поранився."
    $ advance_time(5)

    show amir at right
    am "Системи стабільні. Реактор під контролем. Наскільки це можливо."
    $ advance_time(5)

    hide lettie
    hide amir

    show aoi at left
    ao "Тисяча журавликів. Бажання — щоб ми всі вижили."
    $ advance_time(5)

    show quince at right
    qu "Менше слів. Більше дій. Погнали."
    $ advance_time(5)

    hide aoi
    hide quince

    scene black
    pause 1.0

    "Реактор. Серце Гьольванії. Тисячі тонн нестабільної енергії."
    pause 1.0

    "Але Гекс працює як єдиний організм. Кожен знає свою роль."
    pause 1.0

    "Артур координує. Елеонор сканує. Летті підтримує. Амір контролює системи."
    pause 0.5
    "Аоі знаходить слабке місце. Квінсі робить один точний постріл."
    pause 1.0

    "Реактор стабілізований."
    pause 1.0

    "Петля — розірвана."
    pause 2.0

    scene black
    "..."
    pause 1.0

    "Ви стоїте на даху молу. Перше січня 2000 року."
    pause 1.0

    "Перший ранок без петлі."
    pause 1.0

    show arthur at char_center
    ar "Ми зробили це."
    $ advance_time(5)

    mc "Разом."
    $ advance_time(5)

    ar "Разом."
    $ advance_time(5)

    if store.dating:
        $ _partner = store.dating
        "Ти дивишся на [_partner]. І знаєш — це тільки початок."

    hide arthur

    # Зберегти persistent
    $ persistent.completed = True
    $ persistent.all_friends = True
    if store.dating:
        $ _partner_key = "romanced_" + store.dating.lower()
        $ setattr(persistent, _partner_key, True)

    scene black
    pause 2.0

    "WARFRAME: DRIFTER LOOP"
    pause 1.0
    "Кінець."
    pause 1.0
    "...Або початок?"
    pause 2.0

    return


# ═══════════════════════════════════════════════
# ПЕРЕВІРКА НА ДЕНЬ 31 (виклик з next_day)
# ═══════════════════════════════════════════════

label check_day31:
    if store.day >= 31:
        if check_all_friends():
            call finale_victory
        else:
            call finale_defeat
        # Після фіналу — повернення до головного меню або restart
        $ MainMenu(confirm=False)()
    return
