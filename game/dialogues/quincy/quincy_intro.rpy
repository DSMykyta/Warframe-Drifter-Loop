# game/dialogues/quincy/quincy_intro.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "quincy_intro",
        "who": "Квінсі",
        "conditions": {
            "flag_false": ["quincy_intro_done"],
            "rank_min": 1,
        },
        "priority": 90,
        "chance": 100,
        "label": "quincy_intro",
    })

label quincy_intro:
    show quince at char_center
    $ store.talked_today.add("Квінсі")

    qu "Квінсі. Привіт. Ходімо одразу до суті."
    $ advance_time(5)

    mc "Суть у тому, щоб вижити й виграти час."
    $ advance_time(5)

    qu "Час виграє той, хто ризикує обережно. Запам'ятай."
    $ advance_time(5)

    $ store.seen_dialogues.add("quincy_intro")
    $ set_flag("quincy_intro_done")
    $ add_insight("quincy_sniper", "Квінсі — снайпер. Прямий, цінує суть.")

    hide quince
    return
