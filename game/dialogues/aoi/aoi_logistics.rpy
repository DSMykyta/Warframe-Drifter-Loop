# game/dialogues/aoi/aoi_logistics.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "aoi_logistics",
        "who": "Аоі",
        "conditions": {
            "flag_true": ["aoi_intro_done"],
            "flag_false": ["aoi_logistics_done"],
            "rank_min": 1,
        },
        "priority": 45,
        "chance": 100,
        "label": "aoi_logistics",
    })

label aoi_logistics:
    show aoi at char_center
    $ store.talked_today.add("Аоі")

    ao "Зачекай, я рахую... так, продуктів вистачить на чотири цикли. Якщо Амір не з'їсть все за два."
    $ advance_time(5)

    mc "Ти ведеш облік запасів?"
    $ advance_time(5)

    ao "Облік запасів, маршрути постачання, графіки чергувань, карту безпечних зон. Хтось же має це робити."
    $ advance_time(5)

    ao "Артур — лідер, він приймає рішення. Але хто дає йому дані для цих рішень? Ось."
    $ advance_time(5)

    mc "Ти — мозок операції?"
    $ advance_time(5)

    ao "Не люблю так казати. Але... так. Без логістики ми б уже тричі залишилися без води і двічі — без набоїв."
    $ advance_time(5)

    ao "Стратегія — це не про великі битви. Це про те, щоб у тебе було що їсти, коли битва закінчиться."
    $ advance_time(5)

    $ store.seen_dialogues.add("aoi_logistics")
    $ set_flag("aoi_logistics_done")
    $ add_insight("aoi_strategist", "Аоі планує логістику для всього Гексу. Без неї б нічого не працювало")

    hide aoi
    return
