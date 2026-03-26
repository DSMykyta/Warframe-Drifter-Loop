# game/dialogues/amir/amir_intro.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "amir_intro",
        "who": "Амір",
        "conditions": {
            "flag_false": ["amir_intro_done"],
            "rank_min": 1,
        },
        "priority": 90,
        "chance": 100,
        "label": "amir_intro",
    })

label amir_intro:
    show amir at char_center
    $ store.talked_today.add("Амір")

    am "Амір. Питаєш — відповідаю, не питаєш — споглядаю."
    $ advance_time(5)

    mc "Тоді скажи, на що звернути увагу зараз?"
    $ advance_time(5)

    am "На дрібниці. Через них ламаються великі плани."
    $ advance_time(5)

    $ store.seen_dialogues.add("amir_intro")
    $ set_flag("amir_intro_done")
    $ add_insight("amir_tech", "Амір — технік. Уважний до деталей.")

    hide amir
    return
