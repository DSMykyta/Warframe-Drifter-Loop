# game/dialogues/arthur/arthur_daily_routine.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "arthur_daily_routine",
        "who": "Артур",
        "conditions": {
            "flag_false": ["arthur_daily_routine_done"],
            "rank_min": 1,
        },
        "priority": 45,
        "chance": 100,
        "label": "arthur_daily_routine",
    })

label arthur_daily_routine:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    mc "Ти завжди тут сидиш, біля інфо-стійки?"
    $ advance_time(5)

    ar "Щоранку перевіряю звіти. Хто що бачив, що змінилося на периметрі."
    $ advance_time(5)

    mc "І оновлюєш карту?"
    $ advance_time(5)

    ar "Так. Карта — це наше виживання. Неточна карта — мертва команда."
    $ advance_time(5)

    ar "Потім розподіляю завдання, перевіряю запаси. Рутина, але без неї — хаос."
    $ advance_time(5)

    mc "Тобі це не набридає? Кожен день одне й те саме."
    $ advance_time(5)

    ar "Набридає — це розкіш. Ми не можемо собі дозволити пропустити хоча б один день."
    $ advance_time(5)

    $ store.seen_dialogues.add("arthur_daily_routine")
    $ set_flag("arthur_daily_routine_done")
    $ add_insight("arthur_reports", "Артур щодня перевіряє звіти і оновлює карту")

    hide arthur
    return
