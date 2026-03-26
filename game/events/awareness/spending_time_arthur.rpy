# game/events/awareness/spending_time_arthur.rpy
# Інші персонажі помічають що гравець проводить багато часу з Артуром

init python:
    DIALOGUE_ENTRIES.append({
        "id": "lettie_notices_arthur_time",
        "who": "Летті",
        "conditions": {
            "flag_true": ["lettie_intro_done", "arthur_intro_done"],
            "flag_false": ["lettie_noticed_arthur_time"],
            "chemistry_min": ("Артур", 50),
        },
        "priority": 2,
        "chance": 30,
        "label": "lettie_notices_arthur_time",
    })

    DIALOGUE_ENTRIES.append({
        "id": "quincy_notices_arthur_time",
        "who": "Квінсі",
        "conditions": {
            "flag_true": ["quincy_intro_done", "arthur_intro_done"],
            "flag_false": ["quincy_noticed_arthur_time"],
            "chemistry_min": ("Артур", 60),
        },
        "priority": 2,
        "chance": 25,
        "label": "quincy_notices_arthur_time",
    })

label lettie_notices_arthur_time:
    show lettie at char_center
    $ store.talked_today.add("Летті")

    le "Ти багато часу проводиш з Артуром."
    $ advance_time(5)

    mc "Просто спілкуємось."
    $ advance_time(5)

    le "Ага. 'Просто спілкуємось.' Він так не розмовляв ні з ким уже давно."
    $ advance_time(5)

    le "Не зламай його. Він виглядає міцним, але це фасад."
    $ advance_time(5)

    $ set_flag("lettie_noticed_arthur_time")
    $ store.seen_dialogues.add("lettie_notices_arthur_time")

    hide lettie
    return

label quincy_notices_arthur_time:
    show quince at char_center
    $ store.talked_today.add("Квінсі")

    qu "Артур і ти. Нерозлийвода."
    $ advance_time(5)

    mc "Ревнуєш?"
    $ advance_time(5)

    qu "Пф. Ні. Просто рідко бачу щоб він комусь довіряв так швидко."
    $ advance_time(5)

    qu "Не підведи його. Серйозно."
    $ advance_time(5)

    $ set_flag("quincy_noticed_arthur_time")
    $ store.seen_dialogues.add("quincy_notices_arthur_time")

    hide quince
    return
