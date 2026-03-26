# game/events/awareness/spending_time_aoi.rpy
# Інші помічають що гравець проводить багато часу з Аоі

init python:
    DIALOGUE_ENTRIES.append({
        "id": "eleanor_notices_aoi_time",
        "who": "Елеонор",
        "conditions": {
            "flag_true": ["eleanor_intro_done", "aoi_intro_done"],
            "flag_false": ["eleanor_noticed_aoi_time"],
            "chemistry_min": ("Аоі", 50),
        },
        "priority": 2,
        "chance": 30,
        "label": "eleanor_notices_aoi_time",
    })

    DIALOGUE_ENTRIES.append({
        "id": "amir_notices_aoi_time",
        "who": "Амір",
        "conditions": {
            "flag_true": ["amir_intro_done", "aoi_intro_done"],
            "flag_false": ["amir_noticed_aoi_time"],
            "chemistry_min": ("Аоі", 60),
        },
        "priority": 2,
        "chance": 25,
        "label": "amir_notices_aoi_time",
    })

label eleanor_notices_aoi_time:
    show eleanor at char_center
    $ store.talked_today.add("Елеонор")

    el "Ти часто буваєш біля Аоі."
    $ advance_time(5)

    mc "А ти часто це помічаєш."
    $ advance_time(5)

    el "Я все помічаю. Це моя робота."
    $ advance_time(5)

    el "Аоі... непроста. Вона бачить більше ніж каже. Будь уважний."
    $ advance_time(5)

    $ set_flag("eleanor_noticed_aoi_time")
    $ store.seen_dialogues.add("eleanor_notices_aoi_time")

    hide eleanor
    return

label amir_notices_aoi_time:
    show amir at char_center
    $ store.talked_today.add("Амір")

    am "Слухай, ти й Аоі... Вам добре разом?"
    $ advance_time(5)

    mc "Ми просто друзі."
    $ advance_time(5)

    am "Угу. Як скажеш. Я просто... вона рідко кого до себе підпускає."
    $ advance_time(5)

    am "Якщо ти один з небагатьох — цінуй це."
    $ advance_time(5)

    $ set_flag("amir_noticed_aoi_time")
    $ store.seen_dialogues.add("amir_notices_aoi_time")

    hide amir
    return
