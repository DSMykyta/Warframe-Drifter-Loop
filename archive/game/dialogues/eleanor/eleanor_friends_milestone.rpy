# game/dialogues/eleanor/eleanor_friends_milestone.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "eleanor_friends_milestone",
        "who": "Елеонор",
        "conditions": {
            "flag_false": ["eleanor_friends_milestone_done"],
            "chemistry_min": ("Елеонор", 120),
        },
        "priority": 85,
        "chance": 100,
        "label": "eleanor_friends_milestone",
    })

label eleanor_friends_milestone:
    show eleanor at char_center
    $ store.talked_today.add("Елеонор")

    el "У мене дещо є. Тримай."
    $ advance_time(5)

    mc "Що це? Зошит?"
    $ advance_time(5)

    el "Мій щоденник. Не журналістський — особистий. Я веду його з дитинства."
    $ advance_time(5)

    mc "Елеонор, я не можу це взяти. Це ж—"
    $ advance_time(5)

    el "Можеш. Я хочу, щоб ти прочитав."
    $ advance_time(5)

    el "Там усе. Перший раз, коли я почула чужу думку — мені було вісім. Я подумала, що сходжу з розуму."
    $ advance_time(5)

    el "Роки, коли я намагалась бути нормальною. Журналістика. ІКР. Втеча. Гекс."
    $ advance_time(5)

    el "І ти. Останні сторінки — про тебе."
    $ advance_time(5)

    mc "Я не знаю, що сказати."
    $ advance_time(5)

    el "Не кажи нічого. Просто прочитай. І потім — якщо захочеш — поговоримо."
    $ advance_time(5)

    el "Ти перша людина, якій я це даю. Навіть Артур не бачив усього."
    $ advance_time(5)

    $ add_chemistry("Елеонор", 8)

    $ store.seen_dialogues.add("eleanor_friends_milestone")
    $ set_flag("eleanor_friends_milestone_done")
    $ add_insight("eleanor_journal_shared", "Елеонор дала мені свій особистий щоденник. Там все — від першої почутої думки до сьогодення. Навіть Артур не читав.")

    hide eleanor
    return
