# game/dialogues/arthur/arthur_about_team.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "arthur_about_team",
        "who": "Артур",
        "conditions": {
            "flag_true": ["arthur_intro_done"],
            "flag_false": ["arthur_about_team_done"],
            "rank_min": 1,
        },
        "priority": 50,
        "chance": 100,
        "label": "arthur_about_team",
    })

label arthur_about_team:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    mc "Артуре, можеш розповісти про команду? Як ви тримаєтесь разом?"
    $ advance_time(5)

    ar "Гекс — це шестеро людей, які вирішили довіряти одне одному. Це головне."
    $ advance_time(5)

    ar "Я не обирав бути лідером. Просто хтось мав приймати рішення, коли всі вагалися."
    $ advance_time(5)

    mc "І це завжди був ти?"
    $ advance_time(5)

    ar "Не завжди. Але достатньо часто, щоб це стало звичкою."
    $ advance_time(5)

    menu:
        "А що для тебе найважче в цій ролі?":
            $ advance_time(5)
            mc "А що для тебе найважче в цій ролі?"

            ar "Знати, що кожне моє рішення може когось вбити. І все одно приймати його."
            $ advance_time(5)
            $ set_flag("arthur_admitted_weight")

        "Ти ще й готуєш для всіх, чув.":
            $ advance_time(5)
            mc "Ти ще й готуєш для всіх, чув."

            ar "...Хто розповів? Летті, мабуть."
            $ advance_time(5)

            ar "Так, готую. Коли є час і продукти. Це... заспокоює."
            $ advance_time(5)

    ar "Команда — це не лише бійці. Це люди, яких ти хочеш бачити живими завтра."
    $ advance_time(5)

    $ store.seen_dialogues.add("arthur_about_team")
    $ set_flag("arthur_about_team_done")
    $ add_insight("arthur_cooks", "Артур готує для команди коли є час")

    hide arthur
    return
