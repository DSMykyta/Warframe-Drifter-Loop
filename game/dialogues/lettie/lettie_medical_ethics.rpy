# game/dialogues/lettie/lettie_medical_ethics.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "lettie_medical_ethics",
        "who": "Летті",
        "conditions": {
            "flag_true": ["lettie_rats_done"],
            "flag_false": ["lettie_medical_ethics_done"],
            "rank_min": 1,
            "chemistry_min": ("Летті", 15),
        },
        "priority": 50,
        "chance": 100,
        "label": "lettie_medical_ethics",
    })

label lettie_medical_ethics:
    show letty at char_center
    $ store.talked_today.add("Летті")

    le "Знаєш, скільки разів на тиждень хтось приходить із травмою, якої можна було уникнути?"
    $ advance_time(5)

    mc "Часто?"
    $ advance_time(5)

    le "Кожен. Другий. День. \"Летті, я впав з драбини.\" Навіщо ти ліз на драбину? \"Летті, я поріз руку.\" Тому що тримав ніж не тим кінцем."
    $ advance_time(5)

    mc "Але ти ж все одно лікуєш."
    $ advance_time(5)

    le "Звісно лікую. Я ж медик. Але не кажи мені, що я маю співчувати, коли хтось вдруге за місяць обпікається на тому самому генераторі."
    $ advance_time(5)

    le "Гіппократ казав — \"не нашкодь\". Він нічого не казав про те, що я мушу посміхатись при цьому."
    $ advance_time(5)

    menu:
        "Може, їм просто потрібна підтримка, а не лекція.":
            $ advance_time(5)
            mc "Може, їм просто потрібна підтримка, а не лекція."
            le "...Можливо. Але лекція ефективніша. Підтримка лікує настрій. Лекція запобігає наступному перелому."
            $ advance_time(5)
            le "Хоча... іноді я бачу, як вони тремтять. І тоді — так, я просто мовчу і лікую."
            $ advance_time(5)
            $ set_flag("lettie_softened")

        "Ти цинічна, але справедлива.":
            $ advance_time(5)
            mc "Ти цинічна, але справедлива."
            le "Цинічна — це коли тобі байдуже. Мені не байдуже. Мені просто набридло дивитись, як люди самі собі шкодять."
            $ advance_time(5)
            le "Я лікую всіх. Без винятків. Навіть тих, хто цього не заслуговує. Це і є етика."
            $ advance_time(5)

    le "Ладно, досить філософії. В мене ще три пацієнти з \"загадковими\" синцями."
    $ advance_time(5)

    $ store.seen_dialogues.add("lettie_medical_ethics")
    $ set_flag("lettie_medical_ethics_done")
    $ add_insight("lettie_cynical_medic", "Летті лікує всіх але вважає що люди самі винні в половині своїх ран")

    hide letty
    return
