# game/dialogues/aoi/aoi_intro.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "aoi_intro",
        "who": "Аоі",
        "conditions": {
            "flag_false": ["aoi_intro_done"],
            "rank_min": 1,
        },
        "priority": 90,
        "chance": 100,
        "label": "aoi_intro",
    })

label aoi_intro:
    show aoi at char_center
    $ store.talked_today.add("Аоі")

    ao "私は葵 (Аоі). Прагну зрозуміти, перш ніж діяти."
    $ advance_time(5)

    mc "Що саме хочеш зрозуміти сьогодні?"
    $ advance_time(5)

    ao "Як ти реагуєш на несподіване — це відкриє характер."
    $ advance_time(5)

    $ store.seen_dialogues.add("aoi_intro")
    $ set_flag("aoi_intro_done")
    $ add_insight("aoi_observer", "Аоі — спостережлива. Аналізує людей перш ніж діяти.")

    hide aoi
    return
