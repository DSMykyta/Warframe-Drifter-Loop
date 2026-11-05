# game/dialogues/arthur/arthur_drinks_invite.rpy
# Артур запрошує на напої в бар — створює обіцянку

init python:
    DIALOGUE_ENTRIES.append({
        "id": "arthur_drinks_invite",
        "who": "Артур",
        "conditions": {
            "flag_true": ["arthur_cooking_done"],
            "flag_false": ["arthur_drinks_invite_done"],
            "rank_min": 1,
            "chemistry_min": ("Артур", 30),
        },
        "priority": 65,
        "chance": 80,
        "label": "arthur_drinks_invite",
    })

label arthur_drinks_invite:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    ar "Слухай. Є розмова, яку краще вести не на сухо."
    $ advance_time(5)

    mc "Ти запрошуєш мене в бар?"
    $ advance_time(5)

    ar "Якщо хочеш так це називати. Завтра, о двадцятій, Скана Бар."
    $ advance_time(5)

    menu:
        "Прийду обов'язково":
            $ advance_time(5)
            mc "Домовились. Буду."

            ar "Добре. Не спізнюйся."
            $ advance_time(5)

            $ create_promise("Артур", "bar_skana", 1200, 1320, store.day + 1, "arthur_bar_meeting")
            $ add_chemistry("Артур", 2)

        "Не впевнений, що зможу":
            $ advance_time(5)
            mc "Не знаю, чи зможу завтра..."

            ar "Зрозуміло. Може, іншим разом."
            $ advance_time(5)

            $ add_chemistry("Артур", -1)

    $ store.seen_dialogues.add("arthur_drinks_invite")
    $ set_flag("arthur_drinks_invite_done")

    hide arthur
    return

label arthur_bar_meeting:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    ar "Прийшов. Добре."
    $ advance_time(5)

    ar "Я хотів поговорити про команду. Про те, як ми працюємо разом."
    $ advance_time(5)

    mc "Щось не так?"
    $ advance_time(5)

    ar "Ні. Навпаки. Я починаю... довіряти. І це незвично для мене."
    $ advance_time(5)

    ar "Зазвичай довіра — це розкіш, яку лідер не може собі дозволити."
    $ advance_time(5)

    mc "А зараз?"
    $ advance_time(5)

    ar "Зараз я думаю, що без довіри ми не протримаємось довго."
    $ advance_time(5)

    $ add_chemistry("Артур", 4)
    $ set_flag("arthur_bar_meeting_done")
    $ add_insight("arthur_trust", "Артур рідко довіряє. Але починає. Це для нього велике.")
    $ fulfill_promise(store.promises[-1] if store.promises else None)

    hide arthur
    return
