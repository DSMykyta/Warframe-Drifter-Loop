# game/dialogues/amir/amir_high_score.rpy
# Амір пояснює одержимість рекордами — в петлі рахунок це доказ існування

init python:
    DIALOGUE_ENTRIES.append({
        "id": "amir_high_score",
        "who": "Амір",
        "conditions": {
            "flag_true": ["amir_gaming_done"],
            "flag_false": ["amir_high_score_done"],
            "rank_min": 1,
            "chemistry_min": ("Амір", 25),
        },
        "priority": 50,
        "chance": 100,
        "label": "amir_high_score",
    })

label amir_high_score:
    show amir at char_center
    $ store.talked_today.add("Амір")

    am "Бачиш цей екран? AMR — 9,847,200. Мій кращий результат у Void Runner."
    $ advance_time(5)

    mc "Вражає. Але навіщо тобі рекорди, якщо ніхто не змагається?"
    $ advance_time(5)

    am "О, ти не розумієш. Це не про змагання."
    $ advance_time(5)

    am "В петлі все скидається. Їжа, яку ти з'їв — знову на полиці. Речі, які ти полагодив — знову зламані. Але рахунок на автоматі? Він залишається."
    $ advance_time(5)

    mc "Серйозно? Рекорди зберігаються між петлями?"
    $ advance_time(5)

    am "Так. Не питай мене чому — я не знаю. Може, автомати поза часом. Може, це баг у матриці. Але AMR стоїть на першому місці кожного ранку."
    $ advance_time(5)

    menu:
        "Це як доказ, що ти існуєш.":
            $ advance_time(5)
            mc "Це як доказ, що ти існуєш."
            am "...Так. Саме так. Коли все повторюється, і ти не впевнений, чи був учорашній день справжнім — дивишся на екран, а там твої ініціали."
            $ advance_time(5)

        "А якщо хтось поб'є твій рекорд?":
            $ advance_time(5)
            mc "А якщо хтось поб'є твій рекорд?"
            am "Тоді я поб'ю його знову. Але чесно? Було б приємно. Значить, хтось ще тут. Хтось ще грає. Хтось ще існує."
            $ advance_time(5)

    am "Люди кажуть — \"це просто ігри\". Ні. Це — єдиний слід, який я залишаю. Три літери на екрані. AMR. Я тут. Я був."
    $ advance_time(5)

    am "Трохи сумно, якщо подумати. Тож краще не думати. Краще грати."
    $ advance_time(5)

    $ store.seen_dialogues.add("amir_high_score")
    $ set_flag("amir_high_score_done")
    $ add_insight("amir_scores_exist", "Рекорди Аміра зберігаються між петлями — для нього це доказ існування")

    hide amir
    return
