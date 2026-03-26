# game/dialogues/amir/amir_nightmares_hint.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "amir_nightmares_hint",
        "who": "Амір",
        "conditions": {
            "flag_true": ["amir_gaming_done"],
            "flag_false": ["amir_nightmares_hint_done"],
            "rank_min": 1,
            "chemistry_min": ("Амір", 15),
        },
        "priority": 50,
        "chance": 100,
        "label": "amir_nightmares_hint",
    })

label amir_nightmares_hint:
    show amir at char_center
    $ store.talked_today.add("Амір")

    am "...А? Що? Вибач, задумався."
    $ advance_time(5)

    mc "Ти виглядаєш втомленим. Все гаразд?"
    $ advance_time(5)

    am "Так, нормально. Просто... не дуже спав сьогодні. Знову ці..."
    $ advance_time(5)

    am "...Нічого. Забудь."
    $ advance_time(5)

    menu:
        "Кошмари?":
            $ advance_time(5)
            mc "Кошмари?"

            am "...Слухай, я не хочу про це. Справді. Просто іноді сняться речі, які... не повинні снитися."
            $ advance_time(5)

            am "Це не важливо. Я граю до ранку і тоді не снить нічого. Система працює."
            $ advance_time(5)
            $ set_flag("amir_nightmares_pressed")

        "Добре, не буду питати.":
            $ advance_time(5)
            mc "Добре, не буду питати."

            am "Дякую. Серйозно. Просто... дякую."
            $ advance_time(5)

    am "Краще розкажи мені щось веселе. Або пограємо. Будь-що, тільки не тиша."
    $ advance_time(5)

    $ store.seen_dialogues.add("amir_nightmares_hint")
    $ set_flag("amir_nightmares_hint_done")
    $ add_insight("amir_nightmares", "Амір погано спить. Має кошмари але не хоче говорити про що")

    hide amir
    return
