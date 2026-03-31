# game/dispatcher.rpy
# ═══════════════════════════════════════════════════
# CONDITION-BASED DIALOGUE SYSTEM — ЯДРО
# ═══════════════════════════════════════════════════

init -5 python:

    # ═══ ГОЛОВНІ БАЗИ ═══

    DIALOGUE_ENTRIES = []       # Кожен діалог в грі — запис тут
    BANTER_ENTRIES = []         # Фонові репліки (0 хв)
    HELP_REQUEST_ENTRIES = []   # Запити допомоги через пейджер
    RAW_THOUGHT_DEFS = [
        # Зв'язки — потребують 2+ факти для появи, потім 30 хв "обдумування"
        {
            "id": "thought_arthur_leadership",
            "requires": ["arthur_leader", "arthur_cooks_for_team"],
            "text": "Артур лідирує не наказами, а турботою. Готує для всіх, бере відповідальність. Це не просто командир — це людина, яка тримає групу разом.",
            "connection": "arthur_true_leader",
        },
        {
            "id": "thought_lettie_warmth",
            "requires": ["quincy_sniper", "lettie_cares"],
            "text": "Летті ховає емоції за сарказмом. Квінсі — за тролінгом. Вони обоє дбають, але не можуть це показати відкрито.",
            "connection": "masks_of_care",
        },
        {
            "id": "thought_aoi_patience",
            "requires": ["aoi_observer", "aoi_silence"],
            "text": "Аоі спостерігає, чекає, аналізує. Її терпіння — не слабкість, а зброя. Вона бачить те, що інші пропускають.",
            "connection": "aoi_strategic_patience",
        },
        {
            "id": "thought_team_dynamics",
            "requires": ["arthur_leader", "amir_tech", "quincy_sniper"],
            "text": "Артур командує, Амір технічно забезпечує, Квінсі прикриває. Троє людей — три рівні бою. Разом вони працюють як механізм.",
            "connection": "team_combat_synergy",
        },
        {
            "id": "thought_trust_circle",
            "requires": ["arthur_trust", "aoi_silence"],
            "text": "Довіра в цьому загоні будується не словами, а мовчанням. Хто витримує тишу поруч — той свій.",
            "connection": "trust_through_silence",
        },
    ]

    # ═══ ЗАГЛУШКИ — ТЕМИ ═══

    STUB_TOPICS = {
        "Артур": [
            "square_food", "keys", "danko", "sword_cleaning",
            "weather", "cooking", "drinks", "sleep", "silence", "quincy_annoying",
        ],
        "Аоі": [
            "origami", "music", "bubbletea", "bikes", "sleep",
            "weather", "quincy_noise", "mall_stores", "dreams", "stars",
        ],
        "Амір": [
            "games", "electronics", "future", "food", "sleep",
            "weather", "high_score", "mall_people", "energy", "jokes",
        ],
        "Квінсі": [
            "weapons", "silence", "trolling", "training", "sleep",
            "weather", "amir_loud", "film", "accuracy", "boredom",
        ],
        "Летті": [
            "rats", "coffee", "health", "sarcasm", "sleep",
            "weather", "patients", "silence", "research", "cynicism",
        ],
        "Елеонор": [
            "philosophy", "observations", "writing", "plants", "sleep",
            "weather", "patterns", "books", "quiet", "riddles",
        ],
    }

    # ═══ МАРШРУТИ ПЛІТОК ═══

    GOSSIP_ROUTES = {
        "Аоі": ["Летті"],
        "Летті": ["Аоі"],
        "Артур": ["Елеонор"],
        "Елеонор": ["Артур"],
        "Квінсі": ["Амір"],
        "Амір": ["Квінсі"],
    }


    # ═══════════════════════════════════════════════
    # ПЕРЕВІРКА УМОВ
    # ═══════════════════════════════════════════════

    def check_stable_conditions(conds):
        """Стабільні умови — перевіряються раз на день при build_daily_deck."""
        if "chemistry_min" in conds:
            name, val = conds["chemistry_min"]
            if store.chemistry.get(name, 0) < val:
                return False
        if "chemistry_max" in conds:
            name, val = conds["chemistry_max"]
            if store.chemistry.get(name, 0) >= val:
                return False
        if "flag_true" in conds:
            for f in conds["flag_true"]:
                if not store.flags.get(f):
                    return False
        if "flag_false" in conds:
            for f in conds["flag_false"]:
                if store.flags.get(f):
                    return False
        if "rank_min" in conds:
            if store.syndicate_rank < conds["rank_min"]:
                return False
        if "rank_max" in conds:
            if store.syndicate_rank >= conds["rank_max"]:
                return False
        if "day_min" in conds:
            if store.day < conds["day_min"]:
                return False
        if "day_max" in conds:
            if store.day >= conds["day_max"]:
                return False
        if "dating" in conds:
            if store.dating != conds["dating"]:
                return False
        if "persistent" in conds:
            if not getattr(persistent, conds["persistent"], False):
                return False
        return True

    def check_dynamic_conditions(conds):
        """Динамічні умови — перевіряються при кожному get_dialogue."""
        # Підтримка обох форматів: time_min/time_max і time_from/time_to
        _t_min = conds.get("time_min", conds.get("time_from"))
        _t_max = conds.get("time_max", conds.get("time_to"))
        if _t_min is not None:
            if store.minutes < _t_min:
                return False
        if _t_max is not None:
            if store.minutes >= _t_max:
                return False
        if "location" in conds:
            if store.current_location != conds["location"]:
                return False
        if "talked_today" in conds:
            name = conds.get("who", "")
            expected = conds["talked_today"]
            if expected and name not in store.talked_today:
                return False
            if not expected and name in store.talked_today:
                return False
        if "mission_partner" in conds:
            if store.current_mission_partner != conds["mission_partner"]:
                return False
        if "chars_at_location" in conds:
            here = get_chars_at(store.current_location)
            for c in conds["chars_at_location"]:
                if c not in here:
                    return False
        return True


    # ═══════════════════════════════════════════════
    # DAILY DECK — ОПТИМІЗАЦІЯ
    # ═══════════════════════════════════════════════

    def build_daily_deck():
        """Раз на день: фільтрує DIALOGUE_ENTRIES по стабільних умовах."""
        store.daily_deck = {}
        for entry in DIALOGUE_ENTRIES:
            if entry["id"] in store.seen_dialogues and not entry.get("repeatable"):
                continue
            if not check_stable_conditions(entry.get("conditions", {})):
                continue
            name = entry["who"]
            if name not in store.daily_deck:
                store.daily_deck[name] = []
            store.daily_deck[name].append(entry)

    def update_deck(name):
        """Точкове оновлення після критичного флагу."""
        store.daily_deck[name] = []
        for entry in DIALOGUE_ENTRIES:
            if entry["who"] != name:
                continue
            if entry["id"] in store.seen_dialogues and not entry.get("repeatable"):
                continue
            if not check_stable_conditions(entry.get("conditions", {})):
                continue
            store.daily_deck[name].append(entry)


    # ═══════════════════════════════════════════════
    # ДИСПЕТЧЕР ДІАЛОГІВ
    # ═══════════════════════════════════════════════

    def get_active_dialogue(name):
        """Обирає ОДИН eligible діалог для NPC (за пріоритетом/шансом).
        Повертає entry dict з "titles" або None.

        Диспетчер обирає один діалог — його titles розгортаються в меню.
        Бонусні опції та подарунок додаються окремо в location_loop."""
        deck = store.daily_deck.get(name, [])
        eligible = []
        for entry in deck:
            if not entry.get("titles"):
                continue
            if entry["id"] in store.seen_dialogues and not entry.get("repeatable"):
                continue
            if not check_dynamic_conditions(entry.get("conditions", {})):
                continue
            if "cooldown_tag" in entry:
                used = store.tags_used_today.get(name, set())
                if entry["cooldown_tag"] in used:
                    continue
            eligible.append(entry)

        if not eligible:
            return None

        # Найвищий пріоритет
        max_pri = max(e["priority"] for e in eligible)
        top = [e for e in eligible if e["priority"] == max_pri]

        # Chance
        passed = []
        for e in top:
            ch = e.get("chance", 100)
            if ch >= 100 or renpy.random.randint(1, 100) <= ch:
                passed.append(e)

        if not passed:
            remaining = [e for e in eligible if e["priority"] < max_pri]
            if remaining:
                next_pri = max(e["priority"] for e in remaining)
                for e in [x for x in remaining if x["priority"] == next_pri]:
                    ch = e.get("chance", 100)
                    if ch >= 100 or renpy.random.randint(1, 100) <= ch:
                        passed.append(e)

        if not passed:
            return None

        return renpy.random.choice(passed)

    def check_forced_dialogue(location):
        """Перевіряє чи є forced діалог від NPC в цій локації.
        Forced = NPC ініціює розмову сам при вході гравця.
        Повертає entry dict або None."""
        chars_here = get_chars_at(location)
        for name in chars_here:
            deck = store.daily_deck.get(name, [])
            for entry in deck:
                if not entry.get("forced"):
                    continue
                if entry["id"] in store.seen_dialogues:
                    continue
                if not check_dynamic_conditions(entry.get("conditions", {})):
                    continue
                return entry
        return None

    def get_dialogue(name):
        """Головна функція: шукає в Daily Deck, повертає label або None."""
        deck = store.daily_deck.get(name, [])
        eligible = []
        for entry in deck:
            if entry["id"] in store.seen_dialogues and not entry.get("repeatable"):
                continue
            if not check_dynamic_conditions(entry.get("conditions", {})):
                continue
            # Cooldown перевірка
            if "cooldown_tag" in entry:
                used = store.tags_used_today.get(name, set())
                if entry["cooldown_tag"] in used:
                    continue
            eligible.append(entry)

        if not eligible:
            return get_stub(name)

        # Найвищий пріоритет
        max_pri = max(e["priority"] for e in eligible)
        top = [e for e in eligible if e["priority"] == max_pri]

        # Chance — кидок кубика
        passed = []
        for e in top:
            ch = e.get("chance", 100)
            if ch >= 100 or renpy.random.randint(1, 100) <= ch:
                passed.append(e)

        if not passed:
            # Chance провалено — пробуємо нижчий пріоритет
            remaining = [e for e in eligible if e["priority"] < max_pri]
            if remaining:
                next_pri = max(e["priority"] for e in remaining)
                for e in [x for x in remaining if x["priority"] == next_pri]:
                    ch = e.get("chance", 100)
                    if ch >= 100 or renpy.random.randint(1, 100) <= ch:
                        passed.append(e)

        if not passed:
            return get_stub(name)

        return renpy.random.choice(passed)["label"]

    def get_banter(location):
        """Перевіряє BANTER_ENTRIES для локації. Повертає текст або None."""
        chars_here = get_chars_at(location)
        eligible = []
        for entry in BANTER_ENTRIES:
            if entry["id"] in store.seen_dialogues:
                continue
            # Фільтр по локації (None = будь-де)
            entry_loc = entry.get("location")
            if entry_loc is not None and entry_loc != location:
                continue
            # Підтримка "who" (одиночний) і "chars" (парний)
            if "who" in entry:
                if entry["who"] not in chars_here:
                    continue
            elif "chars" in entry:
                if not all(c in chars_here for c in entry["chars"]):
                    continue
            else:
                continue
            conds = entry.get("conditions", {})
            if not check_stable_conditions(conds):
                continue
            if not check_dynamic_conditions(conds):
                continue
            eligible.append(entry)

        if not eligible:
            return None

        max_pri = max(e.get("priority", 1) for e in eligible)
        top = [e for e in eligible if e.get("priority", 1) == max_pri]
        winner = renpy.random.choice(top)
        store.seen_dialogues.add(winner["id"])
        # Встановити flag_false флаги щоб banter не повторювався сьогодні
        for f in winner.get("conditions", {}).get("flag_false", []):
            set_flag(f)
        return winner


    # ═══════════════════════════════════════════════
    # ЗАГЛУШКИ
    # ═══════════════════════════════════════════════

    def get_player_state():
        """Повертає стан гравця для заглушок."""
        if store.minutes >= 1380:  # після 23:00
            return "tired"
        if store.days_without_mission >= 3:
            return "stressed"
        return "normal"

    def get_stub(name):
        """Модульна заглушка: тема з пулу + локація + стан."""
        pool = store.stub_pools.get(name)
        if not pool:
            store.stub_pools[name] = list(STUB_TOPICS.get(name, []))
            pool = store.stub_pools[name]
        if not pool:
            return "generic_stub"
        topic = renpy.random.choice(pool)
        pool.remove(topic)
        loc = store.current_location
        state = get_player_state()
        # Спробувати специфічний label
        label = "stub_{}_{}_{}_{}".format(name, topic, loc, state)
        if not renpy.has_label(label):
            label = "stub_{}_{}".format(name, topic)
        if not renpy.has_label(label):
            label = "generic_stub"
        return label


    # ═══════════════════════════════════════════════
    # МІСІЙНІ МІНІ-ДІАЛОГИ
    # ═══════════════════════════════════════════════

    MISSION_DIALOGUE_ENTRIES = []

    def get_mission_dialogue(partner):
        """Повертає label місійного міні-діалогу для напарника, або None."""
        eligible = []
        for entry in MISSION_DIALOGUE_ENTRIES:
            if entry.get("who") != partner:
                continue
            if entry["id"] in store.seen_dialogues:
                continue
            conds = entry.get("conditions", {})
            if not check_stable_conditions(conds):
                continue
            eligible.append(entry)
        if not eligible:
            return None
        max_pri = max(e.get("priority", 1) for e in eligible)
        top = [e for e in eligible if e.get("priority", 1) == max_pri]
        winner = renpy.random.choice(top)
        return winner["label"]


    # ═══════════════════════════════════════════════
    # ФЛАГИ ТА ІНСАЙТИ
    # ═══════════════════════════════════════════════

    def set_flag(name, value=True):
        """Ставить флаг + записує день."""
        store.flags[name] = value
        store.flags[name + "_day"] = store.day

    def add_insight(id, text):
        """Додає простий факт в Шафу Думок. Миттєвий."""
        set_flag(id)
        store.insights_log.append({
            "id": id, "text": text, "day": store.day, "type": "fact"
        })
        check_raw_thoughts()

    def check_raw_thoughts():
        """Перевіряє чи зібрані факти для нових зв'язків."""
        for rt in RAW_THOUGHT_DEFS:
            if rt["id"] in [r["id"] for r in store.raw_thoughts]:
                continue
            if store.flags.get(rt["id"]):
                continue
            if all(store.flags.get(f) for f in rt["requires"]):
                store.raw_thoughts.append(dict(rt))

    def contemplate(thought_id):
        """Осмислити сиру думку. Витрачає 30 хв. Активує флаг."""
        advance_time(30)
        set_flag(thought_id)
        store.raw_thoughts = [r for r in store.raw_thoughts if r["id"] != thought_id]
        store.insights_log.append({
            "id": thought_id, "text": "...", "day": store.day, "type": "connection"
        })

    def has_raw_thoughts():
        """Чи є необдумані зв'язки."""
        return len(store.raw_thoughts) > 0


    # ═══════════════════════════════════════════════
    # ЩОДЕННИК
    # ═══════════════════════════════════════════════

    def add_journal_entry(text, entry_type="note"):
        """Додає запис в щоденник Дріфтера."""
        store.journal_entries.append({
            "day": store.day,
            "text": text,
            "type": entry_type,
        })


    # ═══════════════════════════════════════════════
    # РОЗПАД СТОСУНКІВ (DECAY)
    # ═══════════════════════════════════════════════

    def apply_decay():
        """Зменшує хімію якщо давно не взаємодіяв. Викликається в next_day().
        Баланс v2: decay починається з дня 7, grace period 2 дні."""
        if store.day <= store.decay_paused_until:
            return
        for name in CAST:
            d = store.days_since_interaction.get(name, 0)
            if d >= 14:
                add_chemistry(name, -3)
            elif d >= 10:
                add_chemistry(name, -2)
            elif d >= 7:
                add_chemistry(name, -1)
            # Інкремент лічильника (grace period = 2 дні реалізовано через reset_interaction)
            store.days_since_interaction[name] = d + 1

    def reset_interaction(name):
        """Скидає лічильник днів без взаємодії."""
        store.days_since_interaction[name] = 0


    # ═══════════════════════════════════════════════
    # ПРОТУХАЮЧІ ІВЕНТИ
    # ═══════════════════════════════════════════════

    def check_expired_events():
        """Обробляє протухлі івенти. Викликається в next_day()."""
        for entry in DIALOGUE_ENTRIES:
            if "expires_in_days" not in entry:
                continue
            if entry["id"] in store.seen_dialogues:
                continue
            if entry["id"] in store.expired_events:
                continue
            conds = entry.get("conditions", {})
            if not check_stable_conditions(conds):
                continue
            # Визначити коли став eligible
            flag_list = conds.get("flag_true", [])
            if flag_list:
                became_day = store.flags.get(flag_list[0] + "_day", store.day)
            else:
                became_day = 1
            if store.day - became_day > entry["expires_in_days"]:
                # Протух — виконати наслідки
                on_exp = entry.get("on_expire", {})
                for flag in on_exp.get("flags_set", []):
                    set_flag(flag)
                for n, delta in on_exp.get("chemistry_change", {}).items():
                    add_chemistry(n, delta)
                store.gossip_heat += on_exp.get("gossip_heat", 0)
                store.expired_events.add(entry["id"])


    # ═══════════════════════════════════════════════
    # ПЛІТКИ
    # ═══════════════════════════════════════════════

    def add_gossip(fact, initial_knowers, spread_delay=2):
        """Створює нову плітку."""
        store.active_gossip.append({
            "fact": fact,
            "knowers": list(initial_knowers),
            "day_created": store.day,
            "spread_delay": spread_delay,
        })

    def spread_gossip():
        """Поширює плітки через GOSSIP_ROUTES. Викликається в next_day()."""
        for g in store.active_gossip:
            if store.day - g["day_created"] < g.get("spread_delay", 2):
                continue
            new_knowers = []
            for knower in g["knowers"]:
                for target in GOSSIP_ROUTES.get(knower, []):
                    if target not in g["knowers"] and target not in new_knowers:
                        new_knowers.append(target)
                        set_flag("gossip_{}_known_by_{}".format(
                            g["fact"], char_flag(target)))
                        store.gossip_heat += 2
            g["knowers"].extend(new_knowers)


    # ═══════════════════════════════════════════════
    # MISSION NEGLECT
    # ═══════════════════════════════════════════════

    def check_mission_neglect():
        """Перевіряє чи гравець ігнорує місії. Викликається в next_day().
        Баланс v2: одноразові штрафи з ресетом лічильника."""
        d = store.days_without_mission
        if d >= 6:
            for name in CAST:
                add_chemistry(name, -3)
            set_flag("mission_neglect_critical")
            store.days_without_mission = 0  # Ресет лічильника — новий цикл
        elif d == 5:
            for name in CAST:
                add_chemistry(name, -2)
            set_flag("mission_neglect_warning")

    def on_mission_complete():
        """Викликати після кожної успішної місії."""
        store.days_without_mission = 0

    # ═══ ПЕЙДЖЕР ═══

    # ═══ ПЕЙДЖЕР: РЕЖИМИ ═══
    # "status" — час/локація/гроші
    # "message" — повідомлення (гортається ◄►)
    # "request" — запит з ▲ТАК / ▼НІ

    def add_pager_message(text):
        """Додає повідомлення на пейджер."""
        store.pager_messages.append(text)
        store.pager_mode = "message"
        store.pager_msg_index = len(store.pager_messages) - 1
        store.pager_unread = True
        renpy.sound.play("<to 2.1>audio/pager_beep.mp3", channel="sound")

    def get_pager_messages():
        """Повертає всі повідомлення."""
        return store.pager_messages

    def pager_click():
        """Звук кліку кнопки."""
        renpy.sound.play("audio/pager_click.mp3", channel="sound")

    def pager_next_msg():
        """Наступне повідомлення."""
        pager_click()
        if store.pager_messages:
            store.pager_msg_index = min(store.pager_msg_index + 1, len(store.pager_messages) - 1)

    def pager_prev_msg():
        """Попереднє повідомлення."""
        pager_click()
        store.pager_msg_index = max(store.pager_msg_index - 1, 0)

    def pager_dismiss():
        """Закрити повідомлення, повернутись до статусу."""
        pager_click()
        store.pager_mode = "status"
        store.pager_unread = False

    def pager_send_request(text, on_accept_label=None, on_decline_label=None):
        """Надіслати запит з вибором ТАК/НІ."""
        store.pager_mode = "request"
        store.pager_request_text = text
        store.pager_request_accept = on_accept_label
        store.pager_request_decline = on_decline_label
        store.pager_unread = True
        renpy.sound.play("<to 2.1>audio/pager_beep.mp3", channel="sound")

    def clear_pager():
        """Очищує пейджер."""
        store.pager_messages = []
        store.pager_mode = "status"
        store.pager_msg_index = 0
        store.pager_unread = False


# ═══════════════════════════════════════════════════
# GENERIC STUB LABEL (fallback)
# ═══════════════════════════════════════════════════

label generic_stub:
    "..."
    $ advance_time(5)
    return
