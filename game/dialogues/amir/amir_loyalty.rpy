# game/dialogues/amir/amir_loyalty.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "amir_loyalty",
        "who": "Амір",
        "conditions": {
            "flag_true": ["amir_intro_done"],
            "flag_false": ["amir_loyalty_done"],
            "rank_min": 1,
        },
        "priority": 45,
        "chance": 100,
        "label": "amir_loyalty",
    })

label amir_loyalty:
    show amir at char_center
    $ store.talked_today.add("Амір")

    mc "Амір, чому ти залишаєшся з Гексом? Тобі ж ніхто не наказує."
    $ advance_time(5)

    am "А куди мені йти? Серйозно. Я навіть не пам'ятаю, чи була у мене сім'я до всього цього."
    $ advance_time(5)

    am "Артур підібрав мене, коли я ховався в підсобці торгового центру і намагався полагодити зламаний ліхтарик. Мені було тринадцять."
    $ advance_time(5)

    am "Він сказав: 'Нам потрібен хтось з твоїми руками.' І все. Я залишився."
    $ advance_time(5)

    mc "І ніколи не шкодував?"
    $ advance_time(5)

    am "Ні. Гекс — єдина сім'я, яку я знаю. Летті, Аоі, Квінсі, Артур, Елеонор... Я за кожного з них в петлю полізу. Буквально."
    $ advance_time(5)

    am "Хах, в петлю. Оцінив каламбур? Ми ж і так у петлі."
    $ advance_time(5)

    $ store.seen_dialogues.add("amir_loyalty")
    $ set_flag("amir_loyalty_done")
    $ add_insight("amir_loyal", "Амір каже що Гекс — єдина сім'я яку він знає")

    hide amir
    return
