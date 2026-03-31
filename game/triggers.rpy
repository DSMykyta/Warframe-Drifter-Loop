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
        "Артур":   "info_desk",
        "Аоі":     "music_shop",
        "Амір":    "arcade",
        "Квінсі":  "range",
        "Летті":   "medbay",
        "Елеонор": "furniture",
    }

    # ═══ ГРАФ ЛОКАЦІЙ ═══
    # Кожна точка → список суміжних. Мол — центр.

    LOCATION_GRAPH = {
        "mall":       [
            "info_desk", "arcade", "music_shop", "furniture",
            "range", "medbay", "bar", "foodcourt", "comp_club",
            "backroom", "rooftop",
        ],
        "info_desk":  ["mall", "info_counter"],
        "info_counter":  ["info_desk"],
        "arcade":     ["mall"],
        "music_shop": ["mall"],
        "furniture":  ["mall"],
        "range":      ["mall"],
        "medbay":     ["mall"],
        "bar":        ["mall"],
        "foodcourt":  ["mall"],
        "comp_club":  ["mall", "garage"],
        "garage":     ["comp_club"],
        "backroom":   ["mall"],
        "rooftop":    ["mall"],
        "balcony":    ["mall"],
        "cafe":       ["mall"],
        "cafe_balcony": ["cafe", "balcony"],
        "utility":    ["mall"],
        "warehouse":  ["mall"],
    }

    # ═══ УКРАЇНСЬКІ НАЗВИ ═══

    LOCATION_NAMES = {
        "mall":       "Мол Гьольванії",
        "info_desk":  "Інфо-острівець",
        "info_counter":  "Інфостійка",
        "arcade":     "Аркади",
        "music_shop": "Музичний магазин",
        "furniture":  "Магазин меблів",
        "range":      "Тир",
        "medbay":     "Медвідділ",
        "bar":        "Бар",
        "foodcourt":  "Футкорт",
        "comp_club":  "Комп'ютерний клуб",
        "garage":     "Гараж",
        "backroom":   "Бекрум",
        "rooftop":    "Дах",
        "balcony":    "Балкон 2-го поверху",
        "cafe":       "Кав'ярня",
        "cafe_balcony": "Біля кав'ярні (2 поверх)",
        "utility":    "Підсобка",
        "warehouse":  "Склад",
    }

    # ═══ СУБ-ЛОКАЦІЇ ═══

    SUB_LOCATIONS = {
        "info_desk": "info_counter",
        "info_counter": "info_desk",
        "comp_club": "garage",
        "garage":    "comp_club",
    }

    def is_sub(loc_a, loc_b):
        """Перевіряє чи одна локація є суб-локацією іншої."""
        return SUB_LOCATIONS.get(loc_a) == loc_b

    # ═══ ВАРТІСТЬ ПЕРЕМІЩЕННЯ ═══

    def travel_cost(from_loc, to_loc):
        """Повертає вартість переміщення в хвилинах.
        0 = та сама локація, 5 = сусідні, 10 = через мол."""
        if from_loc == to_loc:
            return 0
        # Сусідні (включаючи мол↔точка і суб-локації)
        if to_loc in LOCATION_GRAPH.get(from_loc, []):
            return 5
        # Все інше — через мол (точка↔точка)
        return 10

    def travel_to(destination):
        """Переміщує гравця до локації. Витрачає час."""
        cost = travel_cost(store.current_location, destination)
        if cost > 0:
            advance_time(cost)
        store.current_location = destination

    # ═══ ПОЗИЦІЇ НА КАРТІ (для UI) ═══

    MAP_POSITIONS = {
        "mall":       (960, 540),
        "info_desk":  (1400, 300),
        "info_counter":  (1600, 200),
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
        "rooftop":    (960, 150),
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
            "condition": lambda: get_injury_stacks("Артур") >= 1,
        },
        {
            "id": "eleanor_injured_medbay", "chars": ["Елеонор"],
            "location": "medbay",
            "condition": lambda: get_injury_stacks("Елеонор") >= 1,
        },
        {
            "id": "amir_injured_medbay", "chars": ["Амір"],
            "location": "medbay",
            "condition": lambda: get_injury_stacks("Амір") >= 1,
        },
        {
            "id": "aoi_injured_medbay", "chars": ["Аоі"],
            "location": "medbay",
            "condition": lambda: get_injury_stacks("Аоі") >= 1,
        },
        {
            "id": "quincy_injured_medbay", "chars": ["Квінсі"],
            "location": "medbay",
            "condition": lambda: get_injury_stacks("Квінсі") >= 1,
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
