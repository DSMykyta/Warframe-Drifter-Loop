# game/injuries.rpy
# ═══════════════════════════════════════════════════
# СИСТЕМА ТРАВМ — стаки, місійні поранення
# ═══════════════════════════════════════════════════
#
# Стак отриманий в день X → присутній день X+1 → зникає день X+2 (якщо нового не було).
# 2 стаки = NPC не потрапляє в пул місій.
# 3-й стак на місії = місія переривається (евакуація).
# 3 стаки поза місією = NPC відсутній до кінця наступного дня.
# Летті як напарник = 0% шанс травми для всіх.

init -5 python:

    # ═══ БАЗОВИЙ ШАНС ТРАВМИ ЗА РІВНЕМ МІСІЇ ═══

    INJURY_CHANCE = {
        1: 5,
        2: 10,
        3: 15,
        4: 25,
        5: 35,
        6: 45,
    }

    def get_injury_stacks(name):
        """Кількість стаків травм. name = ім'я NPC або 'player'."""
        return store.injury_stacks.get(name, 0)

    def add_injury_stack(name):
        """Додає стак травми. Повертає нову кількість стаків."""
        current = store.injury_stacks.get(name, 0)
        new_val = min(3, current + 1)
        store.injury_stacks[name] = new_val
        # Запам'ятати день отримання (для загоєння)
        if name not in store.injury_day_gained:
            store.injury_day_gained[name] = []
        store.injury_day_gained[name].append(store.day)

        # Флаги
        if name != "player":
            char_key = name.lower()
            set_flag(char_key + "_injured")
            if new_val >= 2:
                set_flag(char_key + "_injured_severe")
            if new_val >= 3:
                store.npc_absent_until[name] = store.day + 2
                set_flag(char_key + "_absent")
        else:
            set_flag("player_injured")

        return new_val

    def remove_injury_stack(name):
        """Знімає 1 стак травми."""
        current = store.injury_stacks.get(name, 0)
        if current <= 0:
            return
        new_val = current - 1
        store.injury_stacks[name] = new_val

        # Прибрати найстаріший день з історії
        if name in store.injury_day_gained and store.injury_day_gained[name]:
            store.injury_day_gained[name].pop(0)

        if name != "player":
            char_key = name.lower()
            if new_val == 0:
                store.flags[char_key + "_injured"] = False
            if new_val < 2:
                store.flags[char_key + "_injured_severe"] = False
        else:
            if new_val == 0:
                store.flags["player_injured"] = False

    def is_npc_absent(name):
        """Чи NPC відсутній через 3 стаки травм."""
        until = store.npc_absent_until.get(name, 0)
        return store.day < until

    def is_npc_mission_eligible(name):
        """Чи NPC може йти на місію (менше 2 стаків)."""
        return get_injury_stacks(name) < 2

    def roll_mission_injury(mission_level, partner_name):
        """Кидає на травму після місії.
        Летті як напарник = 0% шанс.
        +10% за кожну повторну місію з напарником сьогодні.
        +10% за кожен існуючий стак напарника."""

        # Летті = повна імунність
        if partner_name == "Летті":
            return None

        base_chance = INJURY_CHANCE.get(mission_level, 10)

        # +10% за повторну місію з цим напарником сьогодні
        repeats = store.missions_today_with.get(partner_name, 0)
        repeat_bonus = max(0, (repeats - 1)) * 10

        # +10% за кожен існуючий стак напарника
        partner_stacks = get_injury_stacks(partner_name)
        stack_bonus = partner_stacks * 10

        chance = base_chance + repeat_bonus + stack_bonus

        result = {"player": False, "partner": False}

        # Шанс травми гравця
        if renpy.random.randint(1, 100) <= chance:
            result["player"] = True

        # Шанс травми напарника
        if renpy.random.randint(1, 100) <= chance:
            result["partner"] = True

        if not result["player"] and not result["partner"]:
            return None
        return result

    def apply_mission_injuries(result, partner_name):
        """Застосовує травми. Повертає (messages, abort).
        abort=True якщо напарник отримав 3-й стак — місія переривається."""
        messages = []
        abort = False

        if result["player"]:
            stacks = add_injury_stack("player")
            messages.append("Ти отримав травму. (Стаків: {}/3)".format(stacks))
            add_journal_entry("Травма на місії. Стаків: {}/3.".format(stacks), "event")

        if result["partner"]:
            stacks = add_injury_stack(partner_name)
            if stacks >= 3:
                # 3-й стак = евакуація, місія перервана
                abort = True
                messages.append("{} критично поранений! Евакуація.".format(partner_name))
                messages.append("Місію перервано. Нагород немає.")
                add_journal_entry(
                    "Місію перервано — {} потребував евакуації. Я допоміг.".format(partner_name),
                    "event"
                )
            else:
                messages.append("{} отримав травму. (Стаків: {}/3)".format(partner_name, stacks))

        return messages, abort

    def check_injuries_heal():
        """Знімає стаки що "дозріли" — отримані 2+ дні тому без оновлення.
        Стак отриманий день X → є день X+1 → зникає день X+2.
        Викликати в next_day()."""
        for name in list(store.injury_stacks.keys()):
            if store.injury_stacks[name] <= 0:
                continue
            days = store.injury_day_gained.get(name, [])
            # Знімати стаки отримані 2+ дні тому
            healed = 0
            remaining = []
            for d in days:
                if store.day - d >= 2:
                    healed += 1
                else:
                    remaining.append(d)
            store.injury_day_gained[name] = remaining
            for _ in range(healed):
                remove_injury_stack(name)

        # Перевірити absent — зняти флаг якщо день настав
        expired = []
        for name, until_day in store.npc_absent_until.items():
            if store.day >= until_day:
                expired.append(name)
                char_key = name.lower()
                if store.flags.get(char_key + "_absent"):
                    store.flags[char_key + "_absent"] = False
        for name in expired:
            del store.npc_absent_until[name]

    def is_player_injured():
        """Чи гравець має хоча б 1 стак."""
        return get_injury_stacks("player") > 0

    def is_npc_injured(name):
        """Чи NPC має хоча б 1 стак."""
        return get_injury_stacks(name) > 0

    def get_injury_text(target):
        """Повертає текст стану травм для UI."""
        stacks = get_injury_stacks(target)
        if stacks == 0:
            return None
        if stacks == 1:
            return "Легка травма"
        if stacks == 2:
            return "Серйозна травма"
        return "Критична травма"


# ═══════════════════════════════════════════════════
# ЗМІННІ
# ═══════════════════════════════════════════════════

default injury_stacks = {}           # {"player": 0-3, "Амір": 0-3, ...}
default injury_day_gained = {}       # {"player": [12, 13], "Амір": [12], ...} — дні отримання кожного стаку
default npc_absent_until = {}        # {"Амір": 14, ...} — день до якого NPC відсутній
# missions_today_with — визначено в vars.rpy


# ═══════════════════════════════════════════════════
# ДІАЛОГИ ТРАВМ
# ═══════════════════════════════════════════════════

# Летті реагує на травму гравця (знімає 1 стак)
init python:
    DIALOGUE_ENTRIES.append({
        "id": "lettie_heal_player",
        "who": "Летті",
        "conditions": {
            "flag_true": ["player_injured"],
            "flag_false": ["lettie_healed_today"],
        },
        "priority": 80,
        "chance": 100,
        "label": "lettie_heal_player",
        "repeatable": True,
    })


# ═══════════════════════════════════════════════════
# LABEL: ЛЕТТІ ЛІКУЄ ГРАВЦЯ (знімає 1 стак)
# ═══════════════════════════════════════════════════

label lettie_heal_player:
    show lettie at char_center
    $ store.talked_today.add("Летті")

    $ _inj_text = get_injury_text("player")
    $ _stacks = get_injury_stacks("player")

    le "Стій. Не рухайся."
    $ advance_time(5)

    le "[_inj_text]? На місії?"
    $ advance_time(5)

    menu:
        "Так, не пощастило.":
            $ advance_time(5)
            le "Пощастило що я тут. Сідай."
            $ advance_time(5)

        "Нічого страшного.":
            $ advance_time(5)
            le "Я вирішу що страшно а що ні. Сідай."
            $ advance_time(5)

    le "Готово. Не геройствуй."
    $ advance_time(5)

    $ remove_injury_stack("player")
    $ set_flag("lettie_healed_today")
    $ add_chemistry("Летті", 2)  # Баланс v2: було +3
    $ add_journal_entry("Летті залатала травму. Як завжди — мовчки і ефективно.", "event")

    hide lettie
    return


# ═══════════════════════════════════════════════════
# BANTER: РЕАКЦІЇ НА ТРАВМИ
# ═══════════════════════════════════════════════════

init python:
    BANTER_ENTRIES.append({
        "id": "amir_sees_bruises",
        "who": "Амір",
        "conditions": {
            "flag_true": ["player_injured"],
            "flag_false": ["amir_saw_bruises"],
        },
        "location": None,
        "text": "Чуваааак, ти в порядку?! Виглядаєш як після бійки з дикою кавуру.",
    })

    BANTER_ENTRIES.append({
        "id": "aoi_worried_injury",
        "who": "Аоі",
        "conditions": {
            "flag_true": ["player_injured"],
            "flag_false": ["aoi_saw_injury"],
        },
        "location": None,
        "text": "...Ти поранений. Був у Летті?",
    })

    BANTER_ENTRIES.append({
        "id": "arthur_injury_comment",
        "who": "Артур",
        "conditions": {
            "flag_true": ["player_injured"],
            "flag_false": ["arthur_saw_injury"],
        },
        "location": None,
        "text": "Живий — значить нормально. Але наступного разу — обережніше.",
    })

    BANTER_ENTRIES.append({
        "id": "quincy_injury_troll",
        "who": "Квінсі",
        "conditions": {
            "flag_true": ["player_injured"],
            "flag_false": ["quincy_saw_injury"],
        },
        "location": None,
        "text": "nice battle scars m8. very dramatic. 7 out of 10",
    })
