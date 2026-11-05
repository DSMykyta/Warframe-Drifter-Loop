# game/dialogues/quincy/quincy_loneliness.rpy
# Квінсі визнає самотність

init python:
    DIALOGUE_ENTRIES.append({
        "id": "quincy_loneliness",
        "who": "Квінсі",
        "conditions": {
            "flag_true": ["quincy_sniper_philosophy_done"],
            "flag_false": ["quincy_loneliness_done"],
            "rank_min": 3,
            "chemistry_min": ("Квінсі", 65),
        },
        "priority": 50,
        "cooldown_tag": "heavy_lore",
        "chance": 100,
        "label": "quincy_loneliness",
    })

label quincy_loneliness:
    show quince at char_center
    $ store.talked_today.add("Квінсі")

    "Пізній вечір. Квінсі сидить біля телевізора. Екран показує статику."
    $ advance_time(5)

    mc "Нічого не дивишся?"
    $ advance_time(5)

    qu "Дивлюсь. Статику. Іноді це чесніше за будь-який фільм."
    $ advance_time(5)

    mc "Квінсі..."
    $ advance_time(5)

    qu "Right. Ти хочеш справжню розмову. Okay."
    $ advance_time(5)

    "Квінсі вимикає телевізор. Сідає навпроти."
    $ advance_time(5)

    qu "Знаєш, чому я тролю Аміра? Чому підколюю всіх? Чому не можу just shut up?"
    $ advance_time(5)

    mc "Тому що тобі весело?"
    $ advance_time(5)

    qu "Ні. Тому що якщо я annoying — люди реагують. Сваряться, сміються, відповідають."
    $ advance_time(5)

    qu "А якщо я мовчу — мене немає. Снайпер, remember? Невидимий. Непомітний. Людина-привид."
    $ advance_time(5)

    qu "В школі мене не цькували. Не били. Не ображали. Мене просто... не помічали. Як порожнє місце."
    $ advance_time(5)

    qu "Тролінг — це мій спосіб сказати: 'Ой, привіт, я тут, зверніть, блін, увагу.' Pathetic, right?"
    $ advance_time(5)

    mc "Не pathetic. Людське."
    $ advance_time(5)

    qu "..."
    $ advance_time(5)

    qu "Ти перший, хто так відповів. Зазвичай кажуть 'grow up' або 'stop being a prick.'"
    $ advance_time(5)

    qu "Cheers, mate. Seriously."
    $ advance_time(5)

    $ store.seen_dialogues.add("quincy_loneliness")
    $ set_flag("quincy_loneliness_done")
    $ add_insight("quincy_lonely", "Тролінг Квінсі — захисний механізм. Якщо дратуєш людей — вони хоч якось реагують. Краще ніж бути невидимим")

    hide quince
    return
