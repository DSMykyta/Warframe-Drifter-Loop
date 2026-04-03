# game/triggers.rpy
# ═══════════════════════════════════════════════════
# ЛОКАЦІЇ + ТРИГЕРНИЙ РУХ ПЕРСОНАЖІВ
# ═══════════════════════════════════════════════════


# ═══ СИСТЕМА ЛОКАЦІЙ — граф-зірка з центром на молі ═══

init -5 python:

    # ═══ СПИСОК ПЕРСОНАЖІВ ═══

    CAST = ["Артур", "Елеонор", "Летті", "Амір", "Аоі", "Квінсі"]

    # ═══ ДОМАШНІ ЛОКАЦІЇ ═══

    HOME_LOCATIONS = {
        "Артур":   "security_desk",
        "Аоі":     "music_shop",
        "Амір":    "arcade",
        "Квінсі":  "range",
        "Летті":   "medbay",
        "Елеонор": "furniture",
    }

    # ═══════════════════════════════════════════════════
    # 5 ТИПІВ ЛОКАЦІЙ
    # ═══════════════════════════════════════════════════
    #
    # 1. ЛОКАЦІЯ (звичайна)
    #    Окрема точка на карті, з'єднана з молом.
    #    Мол → локація = 5 хв, локація → інша локація = 10 хв (через мол).
    #    Приклад: music_shop, arcade, range
    #
    # 2. СУМІЖНА ЛОКАЦІЯ
    #    Доступна ЛИШЕ через батьківську локацію, не з молу напряму.
    #    Батьківська → суміжна = 5 хв. Мол → суміжна = 10 хв (мол→батьківська→суміжна).
    #    Приклад: security_room (лише через security_desk)
    #
    # 3. ПОЄДНАНІ ЛОКАЦІЇ
    #    Дві секції одного місця. Перехід між ними = 0 хв (миттєво).
    #    Обидві доступні з молу окремо.
    #    Приклад: cafe ↔ cafe_balcony
    #
    # 4. ЗАКРИТА ЛОКАЦІЯ
    #    Видно на карті із замочком, але не можна увійти поки нема прапорця.
    #    Після відкриття працює як звичайна локація.
    #    Приклад: backroom (потрібен ключ/дозвіл)
    #
    # 5. ПРИХОВАНА ЛОКАЦІЯ
    #    Не видно на карті взагалі, поки не виконана умова.
    #    Після відкриття з'являється на карті і працює як звичайна локація.
    #    Приклад: bar (з'являється на syndicate rank 3)
    # ═══════════════════════════════════════════════════

    # ═══ ГРАФ ЛОКАЦІЙ ═══

    LOCATION_GRAPH = {
        "mall":       [
            "info_desk", "security_desk", "arcade", "music_shop", "furniture",
            "range", "medbay", "bar", "foodcourt", "comp_club", "garage",
            "rooftop", "balcony", "cafe", "cafe_balcony",
            "utility", "warehouse", "backroom", "clothing_shop",
        ],
        "info_desk":      ["mall"],
        "security_desk":  ["mall", "security_room"],
        "security_room":  ["security_desk"],
        "arcade":         ["mall"],
        "music_shop":     ["mall"],
        "furniture":      ["mall"],
        "range":          ["mall"],
        "medbay":         ["mall", "recovery_room"],
        "recovery_room":  ["medbay"],
        "bar":            ["mall"],
        "foodcourt":      ["mall"],
        "comp_club":      ["mall"],
        "garage":         ["mall"],
        "backroom":       ["mall"],
        "rooftop":        ["mall"],
        "balcony":        ["mall"],
        "cafe":           ["mall", "cafe_balcony"],
        "cafe_balcony":   ["mall", "cafe"],
        "utility":        ["mall"],
        "warehouse":      ["mall"],
        "clothing_shop":  ["mall"],
    }

    # ═══ УКРАЇНСЬКІ НАЗВИ ═══

    LOCATION_NAMES = {
        "mall":           "Мол Гьольванії",
        "info_desk":      "Інфо-острівець",
        "security_desk":  "Стійка охорони",
        "security_room":  "Кімната охорони",
        "arcade":         "Аркади",
        "music_shop":     "Музичний магазин",
        "furniture":      "Магазин меблів",
        "range":          "Тир",
        "medbay":         "Медвідділ",
        "bar":            "Бар",
        "foodcourt":      "Футкорт",
        "comp_club":      "Комп'ютерний клуб",
        "garage":         "Гараж",
        "backroom":       "Бекрум",
        "rooftop":        "Дах",
        "balcony":        "Балкон 2-го поверху",
        "cafe":           "Кав'ярня",
        "cafe_balcony":   "Біля кав'ярні (2 поверх)",
        "utility":        "Підсобка",
        "warehouse":      "Склад",
        "clothing_shop":  "Магазин одягу",
        "recovery_room":  "Палата",
    }

    # ═══ СУМІЖНІ ЛОКАЦІЇ ═══
    # Дочірня → батьківська. Дочірня доступна ЛИШЕ через батьківську.
    ADJACENT_LOCATIONS = {
        "security_room": "security_desk",
        "recovery_room": "medbay",
    }

    # ═══ ПОЄДНАНІ ЛОКАЦІЇ ═══
    # Секції одного місця. Перехід = 0 хв.
    PAIRED_LOCATIONS = {
        ("cafe", "cafe_balcony"),
        ("cafe_balcony", "cafe"),
    }

    # ═══ ЗАКРИТІ ЛОКАЦІЇ ═══
    # Видно на карті (із замочком), але не можна увійти.
    # Локація → прапорець для відкриття.
    LOCKED_LOCATIONS = {
        "garage": "garage_unlocked",
        "recovery_room": "recovery_room_never_unlocked",  # завжди закрита для гравця
    }

    # ═══ ПРИХОВАНІ ЛОКАЦІЇ ═══
    # Не видно на карті взагалі, поки нема прапорця.
    # Після відкриття — звичайна локація.
    HIDDEN_LOCATIONS = {
        "bar":            "syndicate_rank_3",
        "rooftop":        "rooftop_unlocked",
        "security_room":  "security_room_unlocked",
        "warehouse":      "warehouse_unlocked",
        "utility":        "utility_unlocked",
        "cafe":           "cafe_unlocked",
        "cafe_balcony":   "cafe_balcony_unlocked",
        "clothing_shop":  "clothing_shop_unlocked",
    }

    def is_locked(loc):
        """Перевіряє чи локація закрита (замочок на карті)."""
        flag = LOCKED_LOCATIONS.get(loc)
        if flag is None:
            return False
        return not store.flags.get(flag)

    def is_hidden(loc):
        """Перевіряє чи локація прихована (не видно на карті)."""
        flag = HIDDEN_LOCATIONS.get(loc)
        if flag is None:
            return False
        return not store.flags.get(flag)

    def is_accessible(loc):
        """Перевіряє чи можна увійти в локацію."""
        return not is_locked(loc) and not is_hidden(loc)

    def is_adjacent(loc):
        """Перевіряє чи локація є суміжною (доступна лише через батьківську)."""
        return loc in ADJACENT_LOCATIONS

    def get_parent(loc):
        """Повертає батьківську локацію для суміжної, або None."""
        return ADJACENT_LOCATIONS.get(loc)

    def is_paired(loc_a, loc_b):
        """Перевіряє чи дві локації є секціями одного місця."""
        return (loc_a, loc_b) in PAIRED_LOCATIONS

    # ═══ ВАРТІСТЬ ПЕРЕМІЩЕННЯ ═══

    def travel_cost(from_loc, to_loc):
        """Повертає вартість переміщення в хвилинах.
        0 = та сама або поєднані, 5 = сусідні/суміжні, 10 = через мол.
        -1 = неможливо (закрита або прихована)."""
        if from_loc == to_loc:
            return 0
        if not is_accessible(to_loc):
            return -1
        if (from_loc, to_loc) in PAIRED_LOCATIONS:
            return 0
        # Суміжна — лише з батьківської
        if to_loc in ADJACENT_LOCATIONS:
            if ADJACENT_LOCATIONS[to_loc] == from_loc:
                return 5
            # Не з батьківської — через мол + батьківську
            return 15
        # Сусідні (мол↔точка)
        if to_loc in LOCATION_GRAPH.get(from_loc, []):
            return 5
        # Все інше — через мол
        return 10

    def travel_to(destination):
        """Переміщує гравця до локації. Витрачає час."""
        if not is_accessible(destination):
            return
        cost = travel_cost(store.current_location, destination)
        if cost > 0:
            advance_time(cost)
        store.current_location = destination
        # Зміна локації скидає пейджер на статус
        if store.pager_mode == "message":
            store.pager_mode = "status"
        # Автозбереження при зміні локації
        renpy.save("auto-1", "День {} — {}".format(store.day, LOCATION_NAMES.get(destination, destination)))

    # ═══ ПОЗИЦІЇ НА КАРТІ (для UI) ═══

    MAP_POSITIONS = {
        "mall":       (960, 540),
        "info_desk":  (1400, 300),
        "security_desk":  (1600, 200),
        "security_room":  (1750, 150),
        "arcade":     (400, 400),
        "music_shop": (600, 300),
        "furniture":  (1200, 700),
        "range":      (300, 600),
        "medbay":     (500, 700),
        "bar":        (800, 800),
        "foodcourt":  (1100, 400),
        "comp_club":  (1400, 600),
        "garage":     (1600, 700),
        "backroom":   (200, 300),
        "rooftop":        (960, 150),
        "clothing_shop":  (300, 400),
    }


# ═══ ТРИГЕРНИЙ РУХ ПЕРСОНАЖІВ ═══

init -4 python:

    # ═══ ТРИГЕРИ ПЕРЕМІЩЕННЯ ═══
    # chars = список персонажів яких стосується
    # location = куди переміщує
    # condition = lambda що повертає True/False

    LOCATION_TRIGGERS = [
        # День 1: всі в молі ТІЛЬКИ до кінця інтро (допит на футкорті)
        # Після інтро — розходяться по HOME_LOCATIONS
        {
            "id": "day_1_all_mall",
            "chars": ["Артур", "Елеонор", "Летті", "Амір", "Аоі", "Квінсі"],
            "location": "mall",
            "condition": lambda: store.day == 1 and not store.flags.get("intro_done"),
        },

        # Вечірній збір у барі (після 20:00, якщо є тригер)
        {
            "id": "group_event_bar",
            "chars": ["Артур", "Елеонор", "Летті", "Амір", "Аоі", "Квінсі"],
            "location": "bar",
            "condition": lambda: store.flags.get("group_bar_tonight_active") and store.minutes >= 1200,
        },

        # Артур на даху після сварки з Елеонор
        {
            "id": "arthur_rooftop_fight",
            "chars": ["Артур"],
            "location": "rooftop",
            "condition": lambda: store.flags.get("arthur_eleanor_fight_active") and not store.flags.get("arthur_fight_resolved"),
        },

        # Елеонор в бекрумі після сварки
        {
            "id": "eleanor_backroom_fight",
            "chars": ["Елеонор"],
            "location": "backroom",
            "condition": lambda: store.flags.get("arthur_eleanor_fight_active") and not store.flags.get("arthur_fight_resolved"),
        },

        # Травмовані NPC (1-2 стаки) — в медвідділі у Летті
        {
            "id": "arthur_injured_medbay", "chars": ["Артур"],
            "location": "medbay",
            "condition": lambda: get_injury_stacks("Артур") >= 1 and not is_npc_in_recovery("Артур"),
        },
        {
            "id": "eleanor_injured_medbay", "chars": ["Елеонор"],
            "location": "medbay",
            "condition": lambda: get_injury_stacks("Елеонор") >= 1 and not is_npc_in_recovery("Елеонор"),
        },
        {
            "id": "amir_injured_medbay", "chars": ["Амір"],
            "location": "medbay",
            "condition": lambda: get_injury_stacks("Амір") >= 1 and not is_npc_in_recovery("Амір"),
        },
        {
            "id": "aoi_injured_medbay", "chars": ["Аоі"],
            "location": "medbay",
            "condition": lambda: get_injury_stacks("Аоі") >= 1 and not is_npc_in_recovery("Аоі"),
        },
        {
            "id": "quincy_injured_medbay", "chars": ["Квінсі"],
            "location": "medbay",
            "condition": lambda: get_injury_stacks("Квінсі") >= 1 and not is_npc_in_recovery("Квінсі"),
        },

        # Критично травмовані (3 стаки) — в палаті, без свідомості
        {
            "id": "arthur_recovery", "chars": ["Артур"],
            "location": "recovery_room",
            "condition": lambda: is_npc_in_recovery("Артур"),
        },
        {
            "id": "eleanor_recovery", "chars": ["Елеонор"],
            "location": "recovery_room",
            "condition": lambda: is_npc_in_recovery("Елеонор"),
        },
        {
            "id": "amir_recovery", "chars": ["Амір"],
            "location": "recovery_room",
            "condition": lambda: is_npc_in_recovery("Амір"),
        },
        {
            "id": "aoi_recovery", "chars": ["Аоі"],
            "location": "recovery_room",
            "condition": lambda: is_npc_in_recovery("Аоі"),
        },
        {
            "id": "quincy_recovery", "chars": ["Квінсі"],
            "location": "recovery_room",
            "condition": lambda: is_npc_in_recovery("Квінсі"),
        },

        # Аоі шукає інгредієнти на футкорті
        {
            "id": "aoi_foodcourt",
            "chars": ["Аоі"],
            "location": "foodcourt",
            "condition": lambda: store.flags.get("aoi_ingredients_active"),
        },

        # Квінсі злий — пішов на дах
        {
            "id": "quincy_rooftop_angry",
            "chars": ["Квінсі"],
            "location": "rooftop",
            "condition": lambda: store.flags.get("quincy_angry_active"),
        },

        # Обідній час: рандомний персонаж на футкорті
        {
            "id": "lunch_foodcourt",
            "chars": ["Амір"],  # Амір найчастіше обідає
            "location": "foodcourt",
            "condition": lambda: store.minutes >= 720 and store.minutes < 840 and store.day > 1,
        },
    ]


    # ═══ ОБІЦЯНКИ ЯК ТРИГЕРИ ═══

    def _check_promise_location(name):
        """Перевіряє чи персонаж має бути на місці обіцянки."""
        for p in store.promises:
            if p["who"] == name and p["day"] == store.day:
                if store.minutes >= p["from_min"] and store.minutes < p["to_min"]:
                    return p["where"]
        return None


    # ═══ ГОЛОВНА ФУНКЦІЯ: ДЕ ПЕРСОНАЖ? ═══

    def get_char_location(name):
        """Визначає поточну локацію персонажа.
        Пріоритет: absent (3 стаки) → ніч → тригери → обіцянки → домашня."""
        # 3 стаки травм = повністю відсутній
        if is_npc_absent(name):
            return None

        # Після 24:00 всі зникли
        if is_night():
            return None

        # Перевірити тригери (пріоритет від останнього)
        for trigger in reversed(LOCATION_TRIGGERS):
            if name in trigger["chars"]:
                if trigger["condition"]():
                    return trigger["location"]

        # Перевірити обіцянки
        promise_loc = _check_promise_location(name)
        if promise_loc:
            return promise_loc

        # Домашня локація
        return HOME_LOCATIONS.get(name, "mall")


    def get_chars_at(location):
        """Повертає список персонажів у локації. Порожній після 24:00."""
        if is_night():
            return []
        return [n for n in CAST if get_char_location(n) == location]
