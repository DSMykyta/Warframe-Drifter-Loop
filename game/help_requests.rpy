# game/help_requests.rpy
# ═══════════════════════════════════════════════════
# ЗАПИТИ ДОПОМОГИ ЧЕРЕЗ ПЕЙДЖЕР
# ═══════════════════════════════════════════════════

init python:

    # Реєстрація запитів
    HELP_REQUEST_ENTRIES.append({
        "id": "lettie_help_meds",
        "who": "Летті",
        "conditions": {
            "flag_false": ["helped_lettie_today"],
            "chemistry_min": ("Летті", 10),
            "time_min": 600,
            "time_max": 1320,
        },
        "chance": 30,
        "message": "Потрібна допомога з медикаментами. Зайдеш?",
        "location": "medbay",
    })

    HELP_REQUEST_ENTRIES.append({
        "id": "amir_help_arcade",
        "who": "Амір",
        "conditions": {
            "flag_false": ["helped_amir_today"],
            "chemistry_min": ("Амір", 10),
            "time_min": 600,
            "time_max": 1320,
        },
        "chance": 30,
        "message": "АВТОМАТ ЗНОВ ЗЛАМАВСЯ допоможиииии",
        "location": "arcade",
    })

    HELP_REQUEST_ENTRIES.append({
        "id": "arthur_help_reports",
        "who": "Артур",
        "conditions": {
            "flag_false": ["helped_arthur_today"],
            "chemistry_min": ("Артур", 10),
            "time_min": 600,
            "time_max": 1320,
        },
        "chance": 30,
        "message": "Звіти самі себе не розберуть. Вільний?",
        "location": "info_desk",
    })

    HELP_REQUEST_ENTRIES.append({
        "id": "aoi_help_records",
        "who": "Аоі",
        "conditions": {
            "flag_false": ["helped_aoi_today"],
            "chemistry_min": ("Аоі", 10),
            "time_min": 600,
            "time_max": 1320,
        },
        "chance": 30,
        "message": "Допоможеш скласти платівки?",
        "location": "music_shop",
    })

    HELP_REQUEST_ENTRIES.append({
        "id": "quincy_help_range",
        "who": "Квінсі",
        "conditions": {
            "flag_false": ["helped_quincy_today"],
            "chemistry_min": ("Квінсі", 10),
            "time_min": 600,
            "time_max": 1320,
        },
        "chance": 30,
        "message": "range needs cleaning. u in or what",
        "location": "range",
    })

    HELP_REQUEST_ENTRIES.append({
        "id": "eleanor_help_notes",
        "who": "Елеонор",
        "conditions": {
            "flag_false": ["helped_eleanor_today"],
            "chemistry_min": ("Елеонор", 10),
            "time_min": 600,
            "time_max": 1320,
        },
        "chance": 30,
        "message": "Маю записи які треба систематизувати.",
        "location": "furniture",
    })

    # ═══ Перевірка та виконання ═══

    def check_help_requests():
        """Перевіряє чи є eligible help request. Повертає запис або None."""
        if store.flags.get("helped_someone_today"):
            return None  # один запит на день

        for entry in HELP_REQUEST_ENTRIES:
            conds = entry.get("conditions", {})
            # Перевірити chemistry_min
            if "chemistry_min" in conds:
                name, val = conds["chemistry_min"]
                if store.chemistry.get(name, 0) < val:
                    continue
            # Перевірити flag_false
            if "flag_false" in conds:
                skip = False
                for f in conds["flag_false"]:
                    if store.flags.get(f):
                        skip = True
                        break
                if skip:
                    continue
            # Перевірити час
            if "time_min" in conds and store.minutes < conds["time_min"]:
                continue
            if "time_max" in conds and store.minutes >= conds["time_max"]:
                continue
            # Chance
            ch = entry.get("chance", 30)
            if renpy.random.randint(1, 100) <= ch:
                return entry

        return None

    def execute_help_request(entry):
        """Виконує запит допомоги. Баланс v2: 45 хв, +100 крон, +4 хімія."""
        who = entry["who"]
        loc = entry.get("location", "mall")

        # Переміщення
        store.current_location = loc
        advance_time(45)

        # Нагороди
        store.money += 100
        add_chemistry(who, 4)
        reset_interaction(who)

        # Флаги
        set_flag("helped_{}_today".format(who.lower()))
        set_flag("helped_someone_today")
