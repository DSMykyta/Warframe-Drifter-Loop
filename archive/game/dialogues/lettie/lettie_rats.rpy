# game/dialogues/lettie/lettie_rats.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "lettie_rats",
        "who": "Летті",
        "conditions": {
            "flag_false": ["lettie_rats_done"],
            "rank_min": 1,
        },
        "priority": 50,
        "chance": 100,
        "label": "lettie_rats",
    })

label lettie_rats:
    show lettie at char_center
    $ store.talked_today.add("Летті")

    le "Тихіше. Канела тільки заснула."
    $ advance_time(5)

    mc "Канела?"
    $ advance_time(5)

    le "Мій щур. Ну, одна з двох. Друга — Пім'єнта. Вони сестри."
    $ advance_time(5)

    mc "Ти назвала щурів іменами спецій?"
    $ advance_time(5)

    le "Кориця і Перець. Канела — спокійна, тепла, любить спати у мене на плечі. Пім'єнта — кусає все, що рухається, і половину того, що ні."
    $ advance_time(5)

    menu:
        "Можна їх погладити?":
            $ advance_time(5)
            mc "Можна їх погладити?"
            le "Канелу — так. Пім'єнту... на свій ризик. Вона кусається не зі злості. Просто перевіряє, чи ти їстівний."
            $ advance_time(5)
            $ set_flag("lettie_pet_rats")

        "Навіщо тримати щурів у медвідсіку?":
            $ advance_time(5)
            mc "Навіщо тримати щурів у медвідсіку?"
            le "А навіщо тримати людей? Щури хоча б не скаржаться і не брешуть про симптоми."
            $ advance_time(5)
            le "І вони чесні. Якщо Канела тебе облизує — ти їй подобаєшся. Якщо Пім'єнта кусає — теж подобаєшся. Просто інакше."
            $ advance_time(5)

    le "Вони — найкраще, що в мене є тут. Не кажи їм, що я це сказала."
    $ advance_time(5)

    $ store.seen_dialogues.add("lettie_rats")
    $ set_flag("lettie_rats_done")
    $ add_insight("lettie_rats_names", "Імена щурів Летті — Канела і Пім'єнта")

    hide letty
    return
