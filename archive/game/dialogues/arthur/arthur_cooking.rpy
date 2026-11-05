# game/dialogues/arthur/arthur_cooking.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "arthur_cooking",
        "who": "Артур",
        "conditions": {
            "flag_true": ["arthur_about_team_done"],
            "flag_false": ["arthur_cooking_done"],
            "rank_min": 1,
            "chemistry_min": ("Артур", 15),
        },
        "priority": 50,
        "chance": 100,
        "label": "arthur_cooking",
    })

label arthur_cooking:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    mc "Артуре, я чув ти знову щось готував вранці. Пахло на весь коридор."
    $ advance_time(5)

    ar "Каша з сушеними грибами. Нічого особливого."
    $ advance_time(5)

    mc "Для тебе — нічого особливого. Для решти — свято."
    $ advance_time(5)

    ar "...Перебільшуєш."
    $ advance_time(5)

    ar "Я просто не люблю, коли люди йдуть на завдання голодними. Це впливає на концентрацію."
    $ advance_time(5)

    mc "Тобто це тактичне рішення, а не турбота?"
    $ advance_time(5)

    ar "Можеш називати як хочеш."
    $ advance_time(5)

    menu:
        "Звідки ти взагалі навчився готувати?":
            $ advance_time(5)
            mc "Звідки ти взагалі навчився готувати?"

            ar "Мати вчила. Давно. Ще до того, як все змінилося."
            $ advance_time(5)

            ar "Вона казала — хто вміє готувати, той ніколи не буде самотнім."
            $ advance_time(5)
            $ set_flag("arthur_mentioned_mother")

        "А що з кухонним обладнанням тут?":
            $ advance_time(5)
            mc "А що з кухонним обладнанням тут?"

            ar "Жахливе. Але я знайшов робочий тостер на минулому рейді. Це було... приємно."
            $ advance_time(5)

            ar "Дрібниці тримають на плаву. Тостер, гострий ніж, чиста сковорідка."
            $ advance_time(5)

    $ store.seen_dialogues.add("arthur_cooking")
    $ set_flag("arthur_cooking_done")
    $ add_insight("arthur_kitchen", "Артур любить тостери і кухонну техніку")

    hide arthur
    return
