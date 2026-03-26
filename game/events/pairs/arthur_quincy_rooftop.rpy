# game/events/pairs/arthur_quincy_rooftop.rpy
# Парний діалог: Артур та Квінсі на даху

init python:
    BANTER_ENTRIES.append({
        "id": "arthur_quincy_rooftop",
        "location": "rooftop",
        "chars": ["Артур", "Квінсі"],
        "conditions": {
            "flag_true": ["arthur_intro_done", "quincy_intro_done"],
            "flag_false": ["pair_arthur_quincy_rooftop_seen"],
        },
        "label": "arthur_quincy_rooftop",
    })

label arthur_quincy_rooftop:
    show arthur at left
    show quince at right

    ar "Квінсі. Доповідай по периметру."
    $ advance_time(5)

    qu "Чисто. Як завжди. Ти щоразу питаєш."
    $ advance_time(5)

    ar "І буду питати. Це протокол."
    $ advance_time(5)

    qu "Протокол для загону з шести людей у покинутому молі?"
    $ advance_time(5)

    ar "Особливо для загону з шести людей у покинутому молі."
    $ advance_time(5)

    qu "...Справедливо."
    $ advance_time(5)

    $ set_flag("pair_arthur_quincy_rooftop_seen")
    $ store.seen_dialogues.add("arthur_quincy_rooftop")

    hide arthur
    hide quince
    return
