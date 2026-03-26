# game/dialogues/aoi/aoi_friends_milestone.rpy
# MILESTONE: Аоі дарує журавлика номер 999

init python:
    DIALOGUE_ENTRIES.append({
        "id": "aoi_friends_milestone",
        "who": "Аоі",
        "conditions": {
            "flag_false": ["aoi_friends_milestone_done"],
            "chemistry_min": ("Аоі", 120),
        },
        "priority": 85,
        "chance": 100,
        "label": "aoi_friends_milestone",
    })

label aoi_friends_milestone:
    show aoi at char_center
    $ store.talked_today.add("Аоі")

    "Аоі чекає на тебе. В її руках — паперовий журавлик. Але цей інший. Акуратніший. Кожен згин — ідеальний."
    $ advance_time(5)

    ao "Стій. Не рухайся."
    $ advance_time(5)

    mc "Що це?"
    $ advance_time(5)

    ao "Журавлик. Номер дев'ятсот дев'яносто дев'ять."
    $ advance_time(5)

    "Вона простягає його тобі. Її руки ледь помітно тремтять."
    $ advance_time(5)

    ao "Знаєш, скільки часу я складала ці журавлики? Місяці. Цикли. Я втратила рахунок петель."
    $ advance_time(5)

    ao "Дев'ятсот дев'яносто дев'ять. Одного не вистачає."
    $ advance_time(5)

    mc "Чому ти віддаєш його мені?"
    $ advance_time(5)

    ao "Тому що останній — тисячний — ти маєш скласти сам."
    $ advance_time(5)

    ao "Сенбазуру працює тільки коли хтось вкладає в нього щось справжнє. Я вклала дев'ятсот дев'яносто дев'ять хвилин тиші. Але остання хвилина — твоя."
    $ advance_time(5)

    menu:
        "Я складу його. Обіцяю.":
            $ advance_time(5)
            mc "Я складу його. Обіцяю."

            ao "Я знаю. Саме тому — тобі."
            $ advance_time(5)

        "А яке бажання загадаєш?":
            $ advance_time(5)
            mc "А яке бажання загадаєш?"

            ao "Я більше не хочу забувати. Вперше... я хочу запам'ятати."
            $ advance_time(5)

    "Аоі посміхається. Вперше — без навушників, без бар'єрів."
    $ advance_time(5)

    ao "Ти — тисячний журавлик, якого я не очікувала."
    $ advance_time(5)

    $ chemistry["Аоі"] += 10

    $ store.seen_dialogues.add("aoi_friends_milestone")
    $ set_flag("aoi_friends_milestone_done")
    $ add_insight("aoi_crane_999", "Аоі віддала мені 999-го журавлика. Тисячного я маю скласти сам. Вона більше не хоче забувати")

    hide aoi
    return
