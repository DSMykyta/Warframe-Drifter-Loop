# game/dialogues/lettie/lettie_medbay_checkup.rpy
# Летті призначає огляд — створює обіцянку

init python:
    DIALOGUE_ENTRIES.append({
        "id": "lettie_medbay_checkup",
        "who": "Летті",
        "conditions": {
            "flag_true": ["lettie_intro_done"],
            "flag_false": ["lettie_medbay_checkup_done"],
            "rank_min": 1,
            "chemistry_min": ("Летті", 20),
        },
        "priority": 60,
        "chance": 70,
        "label": "lettie_medbay_checkup",
    })

label lettie_medbay_checkup:
    show lettie at char_center
    $ store.talked_today.add("Летті")

    le "Стій. Коли востаннє ти проходив медогляд?"
    $ advance_time(5)

    mc "Е... не пам'ятаю?"
    $ advance_time(5)

    le "Саме так. Завтра, десята ранку, медпункт. Без запізнень."
    $ advance_time(5)

    menu:
        "Добре, прийду":
            $ advance_time(5)
            mc "Лікарю видніше."

            le "Нарешті хтось адекватний."
            $ advance_time(5)

            $ create_promise("Летті", "medbay", 600, 720, store.day + 1, "lettie_checkup_meeting")
            $ chemistry["Летті"] += 2

        "Я здоровий, не треба":
            $ advance_time(5)
            mc "Я почуваюсь нормально, правда."

            le "Так кажуть усі. За п'ять хвилин до того, як падають."
            $ advance_time(5)

            le "Але змушувати не буду. Твоє тіло — твоя відповідальність."
            $ advance_time(5)

    $ store.seen_dialogues.add("lettie_medbay_checkup")
    $ set_flag("lettie_medbay_checkup_done")

    hide lettie
    return

label lettie_checkup_meeting:
    show lettie at char_center
    $ store.talked_today.add("Летті")

    le "Сідай. Не рухайся."
    $ advance_time(5)

    "Летті мовчки перевіряє пульс, тиск, рефлекси."
    $ advance_time(10)

    le "Живий. Вітаю."
    $ advance_time(5)

    mc "Це все?"
    $ advance_time(5)

    le "Ні. У тебе підвищений кортизол. Стрес. Очевидно, але потрібно слідкувати."
    $ advance_time(5)

    le "Більше спати. Менше геройствувати."
    $ advance_time(5)

    mc "Дякую, Летті. Серйозно."
    $ advance_time(5)

    le "...Не дякуй. Це моя робота."
    $ advance_time(5)

    $ chemistry["Летті"] += 4
    $ set_flag("lettie_checkup_meeting_done")
    $ add_insight("lettie_cares", "Летті ховає турботу за професіоналізмом. Але вона дбає.")
    $ fulfill_promise(store.promises[-1] if store.promises else None)

    hide lettie
    return
