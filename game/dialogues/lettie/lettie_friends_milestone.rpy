# game/dialogues/lettie/lettie_friends_milestone.rpy
# MILESTONE: Летті знайомить гравця зі щурами по іменах — великий жест довіри

init python:
    DIALOGUE_ENTRIES.append({
        "id": "lettie_friends_milestone",
        "who": "Летті",
        "conditions": {
            "flag_true": ["lettie_trust_milestone_done"],
            "flag_false": ["lettie_friends_milestone_done"],
            "rank_min": 2,
            "chemistry_min": ("Летті", 120),
        },
        "priority": 85,
        "chance": 100,
        "label": "lettie_friends_milestone",
    })

label lettie_friends_milestone:
    show letty at char_center
    $ store.talked_today.add("Летті")

    le "Заходь. Тільки тихо. І закрий двері."
    $ advance_time(5)

    mc "Щось серйозне?"
    $ advance_time(5)

    le "Серйозніше, ніж ти думаєш. Я хочу тебе комусь представити. Офіційно."
    $ advance_time(5)

    le "Канело, Пім'єнто — це... мій друг. Ну, може, не друг. Людина, якій я довіряю. Що вже більше, ніж я можу сказати про більшість."
    $ advance_time(5)

    mc "Ти представляєш мене своїм щурам?"
    $ advance_time(5)

    le "Не \"своїм щурам\". Моїй родині. Канела і Пім'єнта були зі мною до Гексу. До петлі. До всього цього."
    $ advance_time(5)

    le "Я нікого до них не підпускаю. Летті-від-медвідсіку і Летті-з-щурами — це різні люди. Другу бачить тільки той, кому я дозволяю."
    $ advance_time(5)

    menu:
        "Я ціную це, Летті. Серйозно.":
            $ advance_time(5)
            mc "Я ціную це, Летті. Серйозно."
            le "...Знаю. Тому ти тут."
            $ advance_time(5)

        "Привіт, Канело. Привіт, Пім'єнто.":
            $ advance_time(5)
            mc "Привіт, Канело. Привіт, Пім'єнто."
            le "Канела щойно облизала тобі палець. Це найвища оцінка. Пім'єнта спостерігає — вона виносить вердикт пізніше."
            $ advance_time(5)

    le "Якщо ти комусь розкажеш, що я плакала, коли Канела вперше захворіла — я відмовлю тобі в медичній допомозі. Назавжди."
    $ advance_time(5)

    le "А тепер сиди тихо. Канела хоче спати в тебе на колінах. Це привілей, не право."
    $ advance_time(5)

    $ chemistry["Летті"] += 10

    $ store.seen_dialogues.add("lettie_friends_milestone")
    $ set_flag("lettie_friends_milestone_done")
    $ add_insight("lettie_family", "Летті представила гравця Канелі й Пім'єнті — для неї щури це родина і вона нікого до них не підпускає")

    hide letty
    return
