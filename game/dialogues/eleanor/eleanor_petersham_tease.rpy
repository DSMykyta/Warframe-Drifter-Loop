# game/dialogues/eleanor/eleanor_petersham_tease.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "eleanor_petersham_tease",
        "who": "Елеонор",
        "conditions": {
            "flag_true": ["arthur_middlename_petersham"],
            "flag_false": ["eleanor_petersham_seen"],
        },
        "priority": 25,
        "chance": 40,
        "label": "eleanor_petersham_tease",
    })

label eleanor_petersham_tease:
    show eleanor at char_center
    $ store.talked_today.add("Елеонор")

    el "Петершем. Серйозно?"
    $ advance_time(5)

    mc "...Що? Звідки ти—"
    $ advance_time(5)

    el "Ти це подумав так голосно, що я почула з сусідньої кімнати. Через дві стіни."
    $ advance_time(5)

    mc "Зачекай. Ти чуєш думки з інших кімнат?"
    $ advance_time(5)

    el "Іноді. Коли хтось думає щось... яскраве. А «Артур Петершем» — це було дуже яскраво."
    $ advance_time(5)

    el "Не кажи йому, що я знаю. Він двадцять років ховає це по-друге ім'я."
    $ advance_time(5)

    el "...Хоча від мене сховати складно."
    $ advance_time(5)

    $ store.seen_dialogues.add("eleanor_petersham_tease")
    $ set_flag("eleanor_petersham_seen")
    $ add_insight("eleanor_hears_thoughts", "Елеонор чує думки з інших кімнат. Не лише поруч.")

    hide eleanor
    return
