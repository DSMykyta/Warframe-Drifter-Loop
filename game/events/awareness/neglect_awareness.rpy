# game/events/awareness/neglect_awareness.rpy
# Персонажі реагують на ігнорування — коли гравець давно не спілкувався

init python:
    DIALOGUE_ENTRIES.append({
        "id": "arthur_notices_neglect",
        "who": "Артур",
        "conditions": {
            "flag_true": ["arthur_intro_done"],
            "flag_false": ["arthur_neglect_warned"],
            "chemistry_min": ("Артур", 20),
        },
        "priority": 3,
        "chance": 40,
        "label": "arthur_notices_neglect",
    })

    DIALOGUE_ENTRIES.append({
        "id": "lettie_notices_no_missions",
        "who": "Летті",
        "conditions": {
            "flag_true": ["lettie_intro_done"],
            "flag_false": ["lettie_mission_warned"],
        },
        "priority": 3,
        "chance": 30,
        "label": "lettie_notices_no_missions",
    })

label arthur_notices_neglect:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    if store.days_since_interaction.get("Артур", 0) >= 5:
        ar "Давно не бачились. Все добре?"
        $ advance_time(5)

        mc "Просто був зайнятий."
        $ advance_time(5)

        ar "Зайнятий. Зрозуміло."
        $ advance_time(5)

        ar "Просто знай — двері завжди відкриті. Якщо хочеш поговорити."
        $ advance_time(5)

        $ set_flag("arthur_neglect_warned")
    else:
        ar "Привіт. Щось хотів?"
        $ advance_time(5)

        $ set_flag("arthur_neglect_warned")

    $ store.seen_dialogues.add("arthur_notices_neglect")

    hide arthur
    return

label lettie_notices_no_missions:
    show lettie at char_center
    $ store.talked_today.add("Летті")

    if store.days_without_mission >= 3:
        le "Ти давно не брав місій."
        $ advance_time(5)

        mc "Було багато інших справ."
        $ advance_time(5)

        le "Справи справами, але команда залежить від кожного. І від тебе теж."
        $ advance_time(5)

        le "Не змушуй мене ставити діагноз 'дезертирство'."
        $ advance_time(5)

        $ set_flag("lettie_mission_warned")
    else:
        le "Нічого. Забудь."
        $ advance_time(5)

        $ set_flag("lettie_mission_warned")

    $ store.seen_dialogues.add("lettie_notices_no_missions")

    hide lettie
    return
