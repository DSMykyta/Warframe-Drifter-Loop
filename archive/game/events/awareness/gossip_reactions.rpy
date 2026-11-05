# game/events/awareness/gossip_reactions.rpy
# Персонажі реагують на плітки (gossip_heat)

init python:
    DIALOGUE_ENTRIES.append({
        "id": "arthur_gossip_warning",
        "who": "Артур",
        "conditions": {
            "flag_false": ["arthur_gossip_warned"],
        },
        "priority": 3,
        "chance": 30,
        "label": "arthur_gossip_warning",
    })

    DIALOGUE_ENTRIES.append({
        "id": "quincy_gossip_tease",
        "who": "Квінсі",
        "conditions": {
            "flag_false": ["quincy_gossip_teased"],
        },
        "priority": 2,
        "chance": 40,
        "label": "quincy_gossip_tease",
    })

label arthur_gossip_warning:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    if store.gossip_heat >= 5:
        ar "Люди говорять. Про тебе."
        $ advance_time(5)

        mc "Що саме?"
        $ advance_time(5)

        ar "Не важливо що. Важливо скільки. Коли всі обговорюють одну людину — це проблема."
        $ advance_time(5)

        ar "Будь обережніший. Менше привертай увагу."
        $ advance_time(5)

        $ set_flag("arthur_gossip_warned")
    else:
        ar "Ні, нічого. Забудь."
        $ advance_time(5)
        $ set_flag("arthur_gossip_warned")

    $ store.seen_dialogues.add("arthur_gossip_warning")

    hide arthur
    return

label quincy_gossip_tease:
    show quince at char_center
    $ store.talked_today.add("Квінсі")

    if store.gossip_heat >= 3:
        qu "Про тебе балакають."
        $ advance_time(5)

        mc "І?"
        $ advance_time(5)

        qu "І нічого. Мені подобається слухати. Продовжуй."
        $ advance_time(5)

        qu "Тільки не забувай — я теж вмію розповідати."
        $ advance_time(5)

        $ set_flag("quincy_gossip_teased")
    else:
        qu "Скучно. Ти нудний. Давай хоч якийсь скандал."
        $ advance_time(5)
        $ set_flag("quincy_gossip_teased")

    $ store.seen_dialogues.add("quincy_gossip_tease")

    hide quince
    return
