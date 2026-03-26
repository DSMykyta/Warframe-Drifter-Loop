# game/dialogues/amir/amir_gaming.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "amir_gaming",
        "who": "Амір",
        "conditions": {
            "flag_true": ["amir_intro_done"],
            "flag_false": ["amir_gaming_done"],
            "rank_min": 1,
        },
        "priority": 50,
        "chance": 100,
        "label": "amir_gaming",
    })

label amir_gaming:
    show amir at char_center
    $ store.talked_today.add("Амір")

    am "О, ти якраз вчасно! Я тільки що побив свій рекорд у Void Runner."
    $ advance_time(5)

    mc "Void Runner? Це один з автоматів?"
    $ advance_time(5)

    am "Один з?! Тут дванадцять автоматів, і я тримаю рекорди на КОЖНОМУ."
    $ advance_time(5)

    am "Серйозно, ніхто навіть близько не підійшов. Летті якось пробувала — здалася за п'ять хвилин."
    $ advance_time(5)

    menu:
        "Можеш навчити мене грати?":
            $ advance_time(5)
            mc "Можеш навчити мене грати?"

            am "О-о-о, нарешті хтось зацікавився! Давай, сідай. Тільки попереджаю — я жахливий вчитель, бо занадто швидко натискаю кнопки."
            $ advance_time(5)
            $ set_flag("amir_offered_gaming")

        "Дванадцять рекордів? Ти серйозно?":
            $ advance_time(5)
            mc "Дванадцять рекордів? Ти серйозно?"

            am "Абсолютно! Можеш перевірити таблиці. Всюди AMR на першому місці. Це моє царство."
            $ advance_time(5)

    am "Ігри — це єдине, що тут не змінюється між петлями. Рекорди залишаються. Це... заспокоює."
    $ advance_time(5)

    $ store.seen_dialogues.add("amir_gaming")
    $ set_flag("amir_gaming_done")
    $ add_insight("amir_gamer", "Амір тримає рекорди на всіх автоматах в аркаді")

    hide amir
    return
