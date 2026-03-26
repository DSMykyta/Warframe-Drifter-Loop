# game/dialogues/eleanor/eleanor_twin_perspective.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "eleanor_twin_perspective",
        "who": "Елеонор",
        "conditions": {
            "flag_true": ["eleanor_intro_done", "arthur_eleanor_secret_done"],
            "flag_false": ["eleanor_twin_perspective_done"],
            "chemistry_min": ("Елеонор", 40),
            "rank_min": 2,
        },
        "priority": 50,
        "chance": 100,
        "label": "eleanor_twin_perspective",
    })

label eleanor_twin_perspective:
    show eleanor at char_center
    $ store.talked_today.add("Елеонор")

    el "Артур розповідав тобі про нас. Про близнюків."
    $ advance_time(5)

    mc "Так. Він сказав, що ви... особливі."
    $ advance_time(5)

    el "Він сказав це делікатно, правда? Він завжди делікатний. А правда — жорстокіша."
    $ advance_time(5)

    el "Я чую думки. Його, твої, всіх навколо. А він — ні. Нічого. Тиша."
    $ advance_time(5)

    mc "Він знає, що ти чуєш його думки?"
    $ advance_time(5)

    el "Здогадується. Але не уявляє масштаб. Він думає — я іноді ловлю уривки. Як радіо з перешкодами."
    $ advance_time(5)

    el "Насправді — я чую все. Кожну його тривогу, кожен сумнів, кожну ніч, коли він не спить і думає, чи достатньо він добрий лідер."
    $ advance_time(5)

    el "І я не можу йому сказати. Бо тоді він почне фільтрувати думки при мені. А це... зламає його."
    $ advance_time(5)

    mc "Тобі не самотньо від цього? Знати все — і мовчати?"
    $ advance_time(5)

    el "Самотньо? Ні. Це гірше за самотність. Це — бути поруч і знати, що він ніколи не зможе бути поруч так само."
    $ advance_time(5)

    el "Асиметрія. Я знаю його повністю. Він мене — лише наполовину. І це моя провина."
    $ advance_time(5)

    $ store.seen_dialogues.add("eleanor_twin_perspective")
    $ set_flag("eleanor_twin_perspective_done")
    $ add_insight("eleanor_twin_guilt", "Елеонор відчуває провину за те, що чує думки Артура, а він не чує її. Асиметрія, яка її роз'їдає.")

    hide eleanor
    return
