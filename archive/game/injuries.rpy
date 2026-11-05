# game/injuries.rpy
# ═══════════════════════════════════════════════════
# СИСТЕМА ТРАВМ v2
# ═══════════════════════════════════════════════════
#
# Стак 0 — здоровий
# Стак 1 — легка травма. Може на місію. +5% шанс.
# Стак 2 — серйозна. Може на місію (гра попереджає). +10% шанс.
# Стак 3 — критичний. Тільки через місію (3-й стак під час бою).
#   NPC: переміщується в recovery_room, відсутній 2 дні.
#   Дріфтер: непритомний, emergency_skip 2 дні.
#   Обидва: Гекс рятує, emergency_skip 3 дні.
#
# Летті на місії = 0% шанс + знімає ВСІ стаки з усіх учасників.

init -5 python:

    # ═══ БАЗОВИЙ ШАНС ТРАВМИ ═══

    INJURY_CHANCE = {
        1: 3,
        2: 5,
        3: 8,
        4: 12,
        5: 18,
        6: 25,
    }

    # ═══ ЧИТАННЯ СТАКІВ ═══

    def get_injury_stacks(name):
        return store.injury_stacks.get(name, 0)

    def is_npc_injured(name):
        return get_injury_stacks(name) > 0

    def is_player_injured():
        return get_injury_stacks("player") > 0

    def get_injury_text(target):
        stacks = get_injury_stacks(target)
        if stacks == 0:
            return None
        if stacks == 1:
            return "Легка травма"
        if stacks == 2:
            return "Серйозна травма"
        return "Критична травма"

    # ═══ ДОДАВАННЯ / ЗНЯТТЯ СТАКІВ ═══

    def add_injury_stack(name):
        current = store.injury_stacks.get(name, 0)
        new_val = min(3, current + 1)
        store.injury_stacks[name] = new_val

        if name not in store.injury_day_gained:
            store.injury_day_gained[name] = []
        store.injury_day_gained[name].append(store.day)

        if name != "player":
            char_key = char_flag(name)
            set_flag(char_key + "_injured")
            if new_val >= 2:
                set_flag(char_key + "_injured_severe")
            if new_val >= 3:
                # NPC в палату на 2 дні
                store.npc_recovery_until[name] = store.day + 2
                set_flag(char_key + "_in_recovery")
        else:
            set_flag("player_injured")
            if new_val >= 2:
                set_flag("player_injured_severe")

        return new_val

    def remove_injury_stack(name):
        current = store.injury_stacks.get(name, 0)
        if current <= 0:
            return
        new_val = current - 1
        store.injury_stacks[name] = new_val

        if name in store.injury_day_gained and store.injury_day_gained[name]:
            store.injury_day_gained[name].pop(0)

        if name != "player":
            char_key = char_flag(name)
            if new_val == 0:
                store.flags[char_key + "_injured"] = False
            if new_val < 2:
                store.flags[char_key + "_injured_severe"] = False
        else:
            if new_val == 0:
                store.flags["player_injured"] = False
            if new_val < 2:
                store.flags["player_injured_severe"] = False

    def remove_all_stacks(name):
        """Знімає ВСІ стаки. Використовується Летті на місії."""
        while get_injury_stacks(name) > 0:
            remove_injury_stack(name)

    # ═══ ПАЛАТА (recovery_room) ═══

    def is_npc_in_recovery(name):
        """NPC в палаті (3 стаки, без свідомості)."""
        until = store.npc_recovery_until.get(name, 0)
        return store.day < until

    def is_npc_absent(name):
        """NPC відсутній = в палаті."""
        return is_npc_in_recovery(name)

    # ═══ КИДОК НА ТРАВМУ ═══

    def roll_mission_injury(mission_level, partner_name, partner2_name=None):
        """Кидає на травму для кожного учасника окремо.
        Летті = 0% + лікує всіх.
        Повертає dict або None."""

        participants = ["player"]
        if partner_name:
            participants.append(partner_name)
        if partner2_name:
            participants.append(partner2_name)

        # Летті на місії — повна імунність + лікування
        lettie_present = "Летті" in participants
        if lettie_present:
            # Зняти ВСІ стаки з усіх учасників
            for p in participants:
                if get_injury_stacks(p) > 0:
                    remove_all_stacks(p)
            return None

        base_chance = INJURY_CHANCE.get(mission_level, 10)

        result = {}
        any_hit = False

        for p in participants:
            # Індивідуальний шанс
            stacks = get_injury_stacks(p)
            stack_bonus = stacks * 5

            repeat_bonus = 0
            if p != "player" and p in store.missions_today_with:
                repeats = store.missions_today_with.get(p, 0)
                repeat_bonus = max(0, (repeats - 1)) * 5

            chance = base_chance + stack_bonus + repeat_bonus

            if renpy.random.randint(1, 100) <= chance:
                result[p] = True
                any_hit = True
            else:
                result[p] = False

        if not any_hit:
            return None
        return result

    # ═══ ЗАСТОСУВАННЯ ТРАВМ ═══

    def apply_mission_injuries(result, partner_name, partner2_name=None):
        """Застосовує травми. Повертає (messages, outcome).
        outcome: "normal" / "partner_evac" / "player_evac" / "both_evac"
        """
        messages = []
        player_down = False
        any_partner_down = False

        # Гравець
        if result.get("player"):
            stacks = add_injury_stack("player")
            if stacks >= 3:
                player_down = True
                messages.append("Ти впав. Темрява.")
            else:
                messages.append("Ти отримав травму. (Стаків: {}/3)".format(stacks))
                add_journal_entry("Травма на місії. Стаків: {}/3.".format(stacks), "event")

        # Напарники
        for p_name in [partner_name, partner2_name]:
            if p_name is None:
                continue
            if not result.get(p_name):
                continue
            stacks = add_injury_stack(p_name)
            if stacks >= 3:
                any_partner_down = True
                messages.append("{} без свідомості. Критичний стан.".format(p_name))
                add_journal_entry(
                    "{} критично поранений на місії.".format(p_name), "event"
                )
            else:
                messages.append("{} отримав травму. (Стаків: {}/3)".format(p_name, stacks))

        # Визначити outcome
        if player_down and any_partner_down:
            outcome = "both_evac"
        elif player_down:
            outcome = "player_evac"
        elif any_partner_down:
            outcome = "partner_evac"
        else:
            outcome = "normal"

        return messages, outcome

    # ═══ EMERGENCY SKIP ═══

    def emergency_skip(days):
        """Дріфтер непритомний. Скіп N днів.
        Обіцянки не штрафуються. NPC які мали обіцянки — прийдуть потім."""
        set_flag("emergency_skip_active")

        # Зберегти хто мав обіцянки — вони прийдуть після
        store._emergency_visitors = set()
        for p in store.promises:
            if p["day"] >= store.day and p["day"] < store.day + days:
                store._emergency_visitors.add(p["who"])

        # Скіп днів
        for _ in range(days):
            next_day()

        store.flags["emergency_skip_active"] = False
        store.current_location = "medbay"

        # Зняти 1 стак гравця (Летті лікувала поки був непритомний)
        if get_injury_stacks("player") > 0:
            remove_injury_stack("player")

        add_journal_entry(
            "Прокинувся в медвідділі. Пропустив {} дн.".format(days), "event"
        )

    def get_emergency_visitors():
        """Повертає set імен NPC які прийшли поки Дріфтер був непритомний."""
        return getattr(store, '_emergency_visitors', set())

    def clear_emergency_visitors():
        store._emergency_visitors = set()

    # ═══ ПЕЙДЖЕР: ПОВІДОМЛЕННЯ ПРО ТРАВМИ ═══

    def send_injury_pager_messages(result, partner_name, partner2_name=None):
        """Надсилає повідомлення від Летті на пейджер після травм."""
        for p_name in [partner_name, partner2_name]:
            if p_name is None or p_name == "Летті":
                continue
            if not result.get(p_name):
                continue
            stacks = get_injury_stacks(p_name)
            if stacks >= 3:
                add_pager_message("Летті", "{} без свідомості. Палата закрита.".format(p_name))
            elif stacks == 2:
                add_pager_message("Летті", "{} серйозно поранений. Веди до мене.".format(p_name))
            elif stacks == 1:
                add_pager_message("Летті", "{} зачепило. Нічого серйозного.".format(p_name))

        # Якщо гравця поранено
        if result.get("player") and get_injury_stacks("player") < 3:
            add_pager_message("Летті", "Ти поранений. Зайди до мене.")

    # ═══ ЗАГОЄННЯ (next_day) ═══

    def check_injuries_heal():
        """Знімає стаки що 'дозріли' — отримані 2+ дні тому.
        Стак день X → є день X+1 → зникає день X+2."""
        for name in list(store.injury_stacks.keys()):
            if store.injury_stacks[name] <= 0:
                continue
            days = store.injury_day_gained.get(name, [])
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

        # Перевірити recovery — повернути NPC зі стаком 1
        expired = []
        for name, until_day in store.npc_recovery_until.items():
            if store.day >= until_day:
                expired.append(name)
                char_key = char_flag(name)
                store.flags.pop(char_key + "_in_recovery", None)
        for name in expired:
            del store.npc_recovery_until[name]
            # NPC повертається зі стаком 1 (вже зняті загоєнням)
            # Якщо загоєння ще не зняло — залишається скільки є


# ═══════════════════════════════════════════════════
# ЗМІННІ
# ═══════════════════════════════════════════════════

default injury_stacks = {}
default injury_day_gained = {}
default npc_recovery_until = {}        # {"Амір": 14} — день до якого NPC в палаті
default _emergency_visitors = set()    # NPC які мали обіцянки під час emergency skip


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

    # Летті НАПОЛЯГАЄ якщо гравець на 2 стаках
    DIALOGUE_ENTRIES.append({
        "id": "lettie_forced_heal",
        "who": "Летті",
        "conditions": {
            "flag_true": ["player_injured_severe"],
            "flag_false": ["lettie_healed_today"],
        },
        "priority": 95,
        "chance": 100,
        "forced": True,
        "label": "lettie_forced_heal",
        "repeatable": True,
    })


# ═══════════════════════════════════════════════════
# LABELS
# ═══════════════════════════════════════════════════

label lettie_heal_player:
    show lettie at char_center
    $ store.talked_today.add("Летті")

    $ _inj_text = get_injury_text("player")

    le "Стій. Не рухайся."

    le "[_inj_text]? На місії?"

    menu:
        "Так, не пощастило.":
            le "Пощастило що я тут. Сідай."

        "Нічого страшного.":
            le "Я вирішу що страшно а що ні. Сідай."

    le "Готово. Не геройствуй."

    $ remove_injury_stack("player")
    $ set_flag("lettie_healed_today")
    $ add_chemistry("Летті", 2)
    $ add_journal_entry("Летті залатала травму.", "event")

    hide lettie
    return


label lettie_forced_heal:
    show lettie at char_center
    $ store.talked_today.add("Летті")

    le "Сядь."

    mc "Я нор—"

    le "Сядь. Зараз."

    "Летті не питає. Вона бере тебе за плече і садить на стілець."

    le "Два стаки. Ти ледь стоїш. Ніяких місій поки я не скажу."

    $ remove_injury_stack("player")
    $ set_flag("lettie_healed_today")
    $ add_chemistry("Летті", 3)
    $ add_journal_entry("Летті примусово залатала. Серйозна мова.", "event")

    hide lettie
    return


# ═══════════════════════════════════════════════════
# LABEL: ПРОКИДАННЯ ПІСЛЯ EMERGENCY SKIP
# ═══════════════════════════════════════════════════

label emergency_wake_up:
    scene black
    pause 1.0
    "..."
    pause 1.0
    "...тиша."
    pause 1.5

    scene bg_medbay
    pause 0.5

    "Прокидаєшся в медвідділі. Голова болить. Тіло — ще більше."

    $ _skip_visitors = get_emergency_visitors()

    if "Летті" in _skip_visitors or True:
        show lettie at char_center
        le "Живий."
        le "Не рухайся. Ти тут вже два дні."

        menu:
            "Що сталося?":
                le "Тебе принесли. Без свідомості."
            "Скільки я пропустив?":
                le "Достатньо. Лежи."

        hide lettie

    # Відвідувачі — NPC які мали обіцянки
    if _skip_visitors:
        python:
            for _vname in _skip_visitors:
                if _vname == "Летті":
                    continue
                add_chemistry(_vname, 2)
                add_journal_entry("{} приходив поки я був непритомний.".format(_vname), "event")

    $ clear_emergency_visitors()
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
