# game/dialogues/eleanor/eleanor_intro.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "eleanor_intro",
        "who": "Елеонор",
        "conditions": {
            "flag_false": ["eleanor_intro_done"],
            "rank_min": 1,
        },
        "priority": 90,
        "chance": 100,
        "label": "eleanor_intro",
    })

label eleanor_intro:
    show eleanor at char_center
    $ store.talked_today.add("Елеонор")

    el "Елеонор до твоїх послуг. Усе має бути системно."
    $ advance_time(5)

    mc "Системно — це зі звітами і форматами?"
    $ advance_time(5)

    el "Із чітким планом на кожну хвилину, поки інші панікують."
    $ advance_time(5)

    $ store.seen_dialogues.add("eleanor_intro")
    $ set_flag("eleanor_intro_done")
    $ add_insight("eleanor_systematic", "Елеонор — системна, планує все наперед.")

    hide eleanor
    return
