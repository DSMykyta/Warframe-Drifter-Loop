# game/dialogues/lettie/lettie_intro.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "lettie_intro",
        "who": "Летті",
        "conditions": {
            "flag_false": ["lettie_intro_done"],
            "rank_min": 1,
        },
        "priority": 90,
        "chance": 100,
        "label": "lettie_intro",
    })

label lettie_intro:
    show lettie at char_center
    $ store.talked_today.add("Летті")

    le "Хей, я Летті. Я ловлю настрій місця."
    $ advance_time(5)

    mc "Що каже настрій про сьогодні?"
    $ advance_time(5)

    le "Що варто посміхнутися, навіть якщо попереду хаос."
    $ advance_time(5)

    $ store.seen_dialogues.add("lettie_intro")
    $ set_flag("lettie_intro_done")
    $ add_insight("lettie_medic", "Летті — медик Гексу. Відчуває настрій оточення.")

    hide letty
    return
