# game/dialogues/lettie/lettie_rat_names.rpy
# Летті розповідає, чому назвала щурів саме так і чому тримає їх

init python:
    DIALOGUE_ENTRIES.append({
        "id": "lettie_rat_names",
        "who": "Летті",
        "conditions": {
            "flag_true": ["lettie_rats_done"],
            "flag_false": ["lettie_rat_names_done"],
            "rank_min": 2,
            "chemistry_min": ("Летті", 30),
        },
        "priority": 50,
        "chance": 100,
        "label": "lettie_rat_names",
    })

label lettie_rat_names:
    show lettie at char_center
    $ store.talked_today.add("Летті")

    le "Канела сьогодні навчилась новому трюку. Встає на задні лапки, коли я клацаю пальцями."
    $ advance_time(5)

    mc "Ти серйозно тренуєш щурів?"
    $ advance_time(5)

    le "А що мені, людей тренувати? Люди не слухаються. Щури — мотивовані. Їм потрібен лише шматочок сиру і трохи терпіння."
    $ advance_time(5)

    mc "Чому саме Канела і Пім'єнта? Кориця і Перець?"
    $ advance_time(5)

    le "Моя бабуся тримала спеції в старих банках на кухні. Кориця і перець стояли поруч, завжди разом. Як вони."
    $ advance_time(5)

    le "Бабуся казала — кориця зігріває, а перець не дає заснути. Мені потрібні обидві речі."
    $ advance_time(5)

    menu:
        "Тобі не самотньо без людей?":
            $ advance_time(5)
            mc "Тобі не самотньо без людей?"
            le "З людьми — самотніше. Люди дивляться на тебе і бачать те, що хочуть. Щури дивляться і бачать — їжу. Чесніше."
            $ advance_time(5)

        "Бабуся навчила тебе готувати?":
            $ advance_time(5)
            mc "Бабуся навчила тебе готувати?"
            le "Бабуся навчила мене, що турбота не потребує слів. Просто стій поруч і тримай банку з корицею відкритою."
            $ advance_time(5)

    le "Канела і Пім'єнта не судять. Не питають, чому я не сплю. Не кажуть, що я занадто різка. Вони просто... тут."
    $ advance_time(5)

    le "Іноді цього достатньо."
    $ advance_time(5)

    $ store.seen_dialogues.add("lettie_rat_names")
    $ set_flag("lettie_rat_names_done")
    $ add_insight("lettie_rat_origin", "Летті назвала щурів на честь спецій з бабусиної кухні — Канела і Пім'єнта не судять і це для неї важливо")

    hide letty
    return
