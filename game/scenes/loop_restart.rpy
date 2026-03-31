# game/newgame_plus.rpy
# New Game+ — persistent знання з минулого проходження

init -5 python:

    def is_ng_plus():
        """Перевіряє чи це NG+."""
        return getattr(persistent, 'completed', False)

    def is_loop_restart():
        """Перевіряє чи це перезапуск петлі (поразка)."""
        return getattr(persistent, 'loop_count', 0) > 0

    def was_romanced(name):
        """Перевіряє чи був романс з цим персонажем у минулому проходженні."""
        key = "romanced_" + char_flag(name)
        return getattr(persistent, key, False)

    def get_loop_count():
        """Кількість перезапусків петлі."""
        return getattr(persistent, 'loop_count', 0)

    def get_previous_insights():
        """Повертає інсайти з минулого проходження (петля)."""
        return getattr(persistent, 'previous_insights', [])

    def get_previous_journal():
        """Повертає записи з минулого проходження (петля)."""
        return getattr(persistent, 'previous_journal', [])


# ═══════════════════════════════════════════════
# NG+ ДІАЛОГИ — нові гілки для вже знайомих сцен
# ═══════════════════════════════════════════════

# Дежавю при першій зустрічі з Артуром (петля або NG+)
init python:
    DIALOGUE_ENTRIES.append({
        "id": "arthur_intro_dejavu",
        "who": "Артур",
        "conditions": {
            "flag_false": ["arthur_intro_done", "arthur_intro_dejavu_done"],
            "persistent": "loop_count",  # loop_count > 0
            "rank_min": 1,
        },
        "priority": 95,
        "chance": 100,
        "label": "arthur_intro_dejavu",
    })

label arthur_intro_dejavu:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    ar "Я — Артур, лідер цієї групи."
    $ advance_time(5)

    menu:
        "Ми вже зустрічались." if is_loop_restart() or is_ng_plus():
            $ advance_time(5)
            ar "...Що? Ні. Ми точно не зустрічались."
            $ advance_time(5)

            ar "Хоча... щось у тебе є. Дежавю?"
            $ advance_time(5)

            mc "Щось таке."
            $ advance_time(5)

            ar "Дивне відчуття. Ладно, не важливо. Як бачиш перший день роботи?"
            $ advance_time(5)

            $ set_flag("arthur_dejavu_noticed")
            $ add_insight("dejavu_arthur", "Артур не пам'ятає. Але відчув щось.")

        "Привіт, Артуре." if is_ng_plus():
            $ advance_time(5)
            ar "...Звідки ти знаєш моє ім'я? Я ще не представився."
            $ advance_time(5)

            mc "Інтуїція."
            $ advance_time(5)

            ar "Незвичайна інтуїція. Слідкуватиму за тобою."
            $ advance_time(5)

            $ set_flag("arthur_name_known_ng")

        "Як бачиш перший день роботи?":
            $ advance_time(5)
            ar "Спокійно вивчаємо обстановку й не робимо дурниць."
            $ advance_time(5)

    $ store.seen_dialogues.add("arthur_intro_dejavu")
    $ set_flag("arthur_intro_dejavu_done")
    $ set_flag("arthur_intro_done")
    $ add_insight("arthur_leader", "Артур — лідер Гексу. Спокійний, обережний.")

    hide arthur
    return


# Елеонор відчуває щось у петлі (вона — єдина)
init python:
    DIALOGUE_ENTRIES.append({
        "id": "eleanor_dejavu_sense",
        "who": "Елеонор",
        "conditions": {
            "flag_true": ["eleanor_intro_done"],
            "flag_false": ["eleanor_dejavu_sense_done"],
            "persistent": "loop_count",
        },
        "priority": 85,
        "chance": 100,
        "label": "eleanor_dejavu_sense",
    })

label eleanor_dejavu_sense:
    show eleanor at char_center
    $ store.talked_today.add("Елеонор")

    el "Стій."
    $ advance_time(5)

    el "В тебе... шум. В голові. Не як у інших."
    $ advance_time(5)

    el "Ніби ехо. Минулого, яке ще не сталось."
    $ advance_time(5)

    mc "Ти відчуваєш це?"
    $ advance_time(5)

    el "Я завжди відчуваю. Але з тобою — інакше. Це не одне минуле. Це... кілька."
    $ advance_time(5)

    if get_loop_count() > 1:
        el "Скільки разів ти вже тут був?"
        $ advance_time(5)

        mc "...Не пам'ятаю точно."
        $ advance_time(5)

        el "Я теж. Але відчуваю. І це лякає."
        $ advance_time(5)

    $ store.seen_dialogues.add("eleanor_dejavu_sense")
    $ set_flag("eleanor_dejavu_sense_done")
    $ add_insight("eleanor_senses_loop", "Елеонор відчуває часову петлю. Єдина з Гексу.")
    $ add_journal_entry("Елеонор щось знає про петлю. Вона відчуває ехо минулих проходжень.", "lore")

    hide eleanor
    return


# NG+ гілки — коли гравець знає те що знає романсований персонаж
init python:
    for _char, _topic, _flag_need, _who_reacts, _reaction_label in [
        ("Артур", "ICR", "romanced_arthur", "Квінсі", "ng_quincy_arthur_icr"),
        ("Елеонор", "Техрот", "romanced_eleanor", "Летті", "ng_lettie_eleanor_techrot"),
        ("Летті", "першого пацієнта", "romanced_lettie", "Амір", "ng_amir_lettie_patient"),
        ("Аоі", "ICR досьє", "romanced_aoi", "Артур", "ng_arthur_aoi_past"),
        ("Амір", "кошмари", "romanced_amir", "Аоі", "ng_aoi_amir_nightmares"),
        ("Квінсі", "кіно", "romanced_quincy", "Елеонор", "ng_eleanor_quincy_film"),
    ]:
        DIALOGUE_ENTRIES.append({
            "id": _reaction_label,
            "who": _who_reacts,
            "conditions": {
                "flag_false": [_reaction_label + "_done"],
                "persistent": _flag_need,
                "chemistry_min": (_who_reacts, 20),
            },
            "priority": 40,
            "chance": 60,
            "label": _reaction_label,
        })


# NG+ label templates
label ng_quincy_arthur_icr:
    show quince at char_center
    $ store.talked_today.add("Квінсі")

    qu "Артур і ICR. Ти щось знаєш про це?"
    $ advance_time(5)

    menu:
        "Артур казав мені інше." if was_romanced("Артур"):
            $ advance_time(5)
            qu "...Він ТОБІ розповів? Мені за три роки — ні слова."
            $ advance_time(5)
            qu "Ну добре. Тоді розкажи мені."
            $ advance_time(5)
            $ add_chemistry("Квінсі", 2)
            $ set_flag("ng_shared_arthur_info")

        "Нічого не знаю.":
            $ advance_time(5)
            qu "Ага. Як скажеш."
            $ advance_time(5)

    $ set_flag("ng_quincy_arthur_icr_done")
    $ store.seen_dialogues.add("ng_quincy_arthur_icr")

    hide quince
    return

label ng_lettie_eleanor_techrot:
    show lettie at char_center
    $ store.talked_today.add("Летті")

    le "Елеонор і її 'голоси'. Ти щось розумієш в цьому?"
    $ advance_time(5)

    menu:
        "Елеонор пояснювала мені про Техрот." if was_romanced("Елеонор"):
            $ advance_time(5)
            le "...Вона ТОБІ пояснювала? Мені каже 'це складно'."
            $ advance_time(5)
            le "Ну, медичний погляд мені все одно потрібен. Розкажи."
            $ advance_time(5)
            $ add_chemistry("Летті", 2)

        "Не зовсім.":
            $ advance_time(5)
            le "Нормально. Ніхто не розуміє."
            $ advance_time(5)

    $ set_flag("ng_lettie_eleanor_techrot_done")
    $ store.seen_dialogues.add("ng_lettie_eleanor_techrot")

    hide lettie
    return

label ng_amir_lettie_patient:
    show amir at char_center
    $ store.talked_today.add("Амір")

    am "Летті. Вона ніколи не говорить про свою роботу. Ну, серйозно."
    $ advance_time(5)

    menu:
        "Вона розповідала мені про першого пацієнта." if was_romanced("Летті"):
            $ advance_time(5)
            am "...Першого? Вау. Вона довіряє тобі більше ніж мені."
            $ advance_time(5)
            $ add_chemistry("Амір", 2)

        "Вона закрита людина.":
            $ advance_time(5)
            am "Ага. Стіна з кави та сарказму."
            $ advance_time(5)

    $ set_flag("ng_amir_lettie_patient_done")
    $ store.seen_dialogues.add("ng_amir_lettie_patient")

    hide amir
    return

label ng_arthur_aoi_past:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    ar "Аоі. Вона... ніколи не говорить про ICR."
    $ advance_time(5)

    menu:
        "Аоі розповідала мені свою історію." if was_romanced("Аоі"):
            $ advance_time(5)
            ar "...Серйозно? Вона мовчить про це вже два роки."
            $ advance_time(5)
            ar "Значить, ти для неї — особливий."
            $ advance_time(5)
            $ add_chemistry("Артур", 2)

        "Я теж мало знаю.":
            $ advance_time(5)
            ar "Кожен несе свій вантаж."
            $ advance_time(5)

    $ set_flag("ng_arthur_aoi_past_done")
    $ store.seen_dialogues.add("ng_arthur_aoi_past")

    hide arthur
    return

label ng_aoi_amir_nightmares:
    show aoi at char_center
    $ store.talked_today.add("Аоі")

    ao "Амір. Він кричить уві сні. Ти знав?"
    $ advance_time(5)

    menu:
        "Він розповідав мені про кошмари." if was_romanced("Амір"):
            $ advance_time(5)
            ao "...Він довіряє тобі. Це рідкість."
            $ advance_time(5)
            ao "Бережи його. Він не такий міцний, як здається."
            $ advance_time(5)
            $ add_chemistry("Аоі", 2)

        "Ні. Не знав.":
            $ advance_time(5)
            ao "Тепер знаєш."
            $ advance_time(5)

    $ set_flag("ng_aoi_amir_nightmares_done")
    $ store.seen_dialogues.add("ng_aoi_amir_nightmares")

    hide aoi
    return

label ng_eleanor_quincy_film:
    show eleanor at char_center
    $ store.talked_today.add("Елеонор")

    el "Квінсі. За його тролінгом — щось цікаве. Ти помітив?"
    $ advance_time(5)

    menu:
        "Він був кінорежисером до війни." if was_romanced("Квінсі"):
            $ advance_time(5)
            el "...Ти знаєш про це? Він мені ніколи не розповідав."
            $ advance_time(5)
            el "Камери стали прицілами. Яка метафора."
            $ advance_time(5)
            $ add_chemistry("Елеонор", 2)

        "Щось помітив, але не впевнений.":
            $ advance_time(5)
            el "Продовжуй спостерігати. Як і я."
            $ advance_time(5)

    $ set_flag("ng_eleanor_quincy_film_done")
    $ store.seen_dialogues.add("ng_eleanor_quincy_film")

    hide eleanor
    return
