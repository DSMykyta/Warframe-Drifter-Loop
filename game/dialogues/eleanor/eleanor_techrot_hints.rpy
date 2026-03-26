# game/dialogues/eleanor/eleanor_techrot_hints.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "eleanor_techrot_hints",
        "who": "Елеонор",
        "conditions": {
            "flag_true": ["eleanor_observations_done"],
            "flag_false": ["eleanor_techrot_hints_done"],
            "rank_min": 1,
            "chemistry_min": ("Елеонор", 20),
        },
        "priority": 55,
        "chance": 100,
        "label": "eleanor_techrot_hints",
    })

label eleanor_techrot_hints:
    show eleanor at char_center
    $ store.talked_today.add("Елеонор")

    el "Ти вчора думав піти до Амір поговорити про генератор, так?"
    $ advance_time(5)

    mc "...Звідки ти знаєш? Я нікому не казав."
    $ advance_time(5)

    el "Ти... напевно згадував це. При мені. Або..."
    $ advance_time(5)

    el "Ні, зачекай. Ти справді не казав?"
    $ advance_time(5)

    mc "Точно ні. Я лише подумав про це, коли йшов повз медвідсік."
    $ advance_time(5)

    el "Мабуть... я просто здогадалась. Логічний висновок. Генератор барахлив, Амір — інженер, ти — відповідальний."
    $ advance_time(5)

    el "Нічого дивного. Просто дедукція."
    $ advance_time(5)

    mc "Якщо ти так кажеш."
    $ advance_time(5)

    $ store.seen_dialogues.add("eleanor_techrot_hints")
    $ set_flag("eleanor_techrot_hints_done")
    $ add_insight("eleanor_techrot", "Елеонор іноді знає речі які не могла чути. Якось дивно...")

    hide eleanor
    return
