# game/dialogues/amir/amir_electronics.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "amir_electronics",
        "who": "Амір",
        "conditions": {
            "flag_true": ["amir_intro_done"],
            "flag_false": ["amir_electronics_done"],
            "rank_min": 1,
        },
        "priority": 45,
        "chance": 100,
        "label": "amir_electronics",
    })

label amir_electronics:
    show amir at char_center
    $ store.talked_today.add("Амір")

    am "Хвилинку... Ще трішки... Є!"
    $ advance_time(5)

    mc "Що ти робиш?"
    $ advance_time(5)

    am "Полагодив передавач. Елеонор казала, що він мертвий. А я кажу — мертвої електроніки не буває."
    $ advance_time(5)

    am "Кожна плата — це пазл. Треба зрозуміти, що куди йде, де обрив, де згорів конденсатор. І потім — клац — все працює."
    $ advance_time(5)

    mc "Де ти цього навчився?"
    $ advance_time(5)

    am "Ніде, якщо чесно. Просто розбирав усе, що потрапляло до рук, ще коли був маленький. Мама казала — зламаєш. А я лагодив."
    $ advance_time(5)

    am "Тепер це єдина причина, чому половина обладнання Гексу ще працює. Так що... дякую, мамо."
    $ advance_time(5)

    $ store.seen_dialogues.add("amir_electronics")
    $ set_flag("amir_electronics_done")
    $ add_insight("amir_tech_skills", "Амір може полагодити будь-яку електроніку. Каже що це як пазл")

    hide amir
    return
