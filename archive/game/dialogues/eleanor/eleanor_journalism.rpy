# game/dialogues/eleanor/eleanor_journalism.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "eleanor_journalism",
        "who": "Елеонор",
        "conditions": {
            "flag_false": ["eleanor_journalism_done"],
            "rank_min": 1,
        },
        "priority": 50,
        "chance": 100,
        "label": "eleanor_journalism",
    })

label eleanor_journalism:
    show eleanor at char_center
    $ store.talked_today.add("Елеонор")

    el "Знаєш, я раніше писала. Статті, розслідування... Справжню журналістику."
    $ advance_time(5)

    mc "Ти була журналісткою?"
    $ advance_time(5)

    el "Була. До того як світ вирішив, що правда — розкіш, яку ніхто не може собі дозволити."
    $ advance_time(5)

    el "Іноді я ловлю себе на тому, що формулюю заголовки. Для подій, які ніхто ніколи не прочитає."
    $ advance_time(5)

    menu:
        "Може, варто знову почати писати?":
            $ advance_time(5)
            mc "Може, варто знову почати писати?"
            el "Для кого? Тут немає читачів. Тільки люди, які намагаються дожити до завтра."
            $ advance_time(5)
            el "...Хоча, може ти маєш рацію. Хтось має записувати, що тут відбувається."
            $ advance_time(5)
            $ set_flag("eleanor_encouraged_writing")

        "Напевно, це було небезпечно.":
            $ advance_time(5)
            mc "Напевно, це було небезпечно."
            el "Небезпечно — це м'яко сказано. Я копала там, де не хотіли, щоб копали."
            $ advance_time(5)
            el "Але знаєш що? Я сумую за цим. За відчуттям, що слова щось значать."
            $ advance_time(5)

    el "Вибач. Рідко згадую ті часи вголос."
    $ advance_time(5)

    $ store.seen_dialogues.add("eleanor_journalism")
    $ set_flag("eleanor_journalism_done")
    $ add_insight("eleanor_journalist", "Елеонор була журналісткою до того як все змінилось")

    hide eleanor
    return
