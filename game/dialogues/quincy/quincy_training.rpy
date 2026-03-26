# game/dialogues/quincy/quincy_training.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "quincy_training",
        "who": "Квінсі",
        "conditions": {
            "flag_true": ["quincy_camera_done"],
            "flag_false": ["quincy_training_done"],
            "rank_min": 1,
            "chemistry_min": ("Квінсі", 15),
        },
        "priority": 50,
        "chance": 100,
        "label": "quincy_training",
    })

label quincy_training:
    show quince at char_center
    $ store.talked_today.add("Квінсі")

    qu "Oi. Бачив як ти стріляєш. No offence, але це було painful."
    $ advance_time(5)

    mc "Дякую за підтримку."
    $ advance_time(5)

    qu "I'm serious, mate. Ти тримаєш зброю як лопату. Хочеш — навчу?"
    $ advance_time(5)

    mc "А ти хороший стрілець?"
    $ advance_time(5)

    qu "Хороший? Mate."
    $ advance_time(5)

    qu "Бачиш ту банку на полиці? Третій ряд, п'ята зліва."
    $ advance_time(5)

    qu "..."
    $ advance_time(5)

    mc "...Ти щойно влучив у неї, навіть не дивлячись?"
    $ advance_time(5)

    menu:
        "Навчи мене. Серйозно.":
            $ advance_time(5)
            mc "Навчи мене. Серйозно."

            qu "Right then. Завтра, тир, шоста ранку. Запізнишся — я not waiting."
            $ advance_time(5)
            $ set_flag("quincy_offered_training")

        "Показуха, але вражає.":
            $ advance_time(5)
            mc "Показуха, але вражає."

            qu "Показуха? Mate, це базовий рівень. Я не промахуюсь. Ніколи. Це не хвастощі — це факт."
            $ advance_time(5)
            $ set_flag("quincy_offered_training")

    qu "Стрільба — це не про силу. Це про дихання, терпіння і момент. Як снайпер тобі кажу."
    $ advance_time(5)

    $ store.seen_dialogues.add("quincy_training")
    $ set_flag("quincy_training_done")
    $ add_insight("quincy_marksman", "Квінсі — найкращий стрілець в Гексі. Не промахується ніколи")

    hide quince
    return
