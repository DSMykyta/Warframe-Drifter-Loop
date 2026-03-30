# game/dialogues/lettie/lettie_rank1_convo1.rpy
# Летті — Ранг 1, Розмова 1: Як стала медиком / Що привело до Гексу

init python:
    DIALOGUE_ENTRIES.append({
        "id": "lettie_rank1_convo1",
        "who": "Летті",
        "conditions": {
            "flag_true": ["lettie_intro_done"],
            "flag_false": ["lettie_rank1_convo1_done"],
            "rank_min": 1,
        },
        "priority": 50,
        "chance": 100,
        "label": "lettie_rank1_convo1",
    })

label lettie_rank1_convo1:
    show lettie at char_center
    $ store.talked_today.add("Летті")
    $ dialogue_begin()

    menu:
        "Летті, як ти стала медиком?":
            jump lettie_r1c1_medic

        "Летті, що привело тебе сюди?":
            jump lettie_r1c1_here

label lettie_r1c1_medic:
    mc "Летті, як ти стала медиком?"

    le "Це моя робота."

    le "А ти чому робиш... що б ти там не робив?"

    menu:
        "Я не дуже мав вибір.":
            jump lettie_r1c1_no_choice

        "Я тебе дратую?":
            jump lettie_r1c1_bothering

    return

label lettie_r1c1_here:
    mc "Летті, що привело тебе в Гелльванію?"

    le "Хм?"

    le "А тебе що привело?"

    menu:
        "Я не дуже мав вибір.":
            jump lettie_r1c1_no_choice

        "Я тебе дратую?":
            jump lettie_r1c1_bothering

    return

label lettie_r1c1_no_choice:
    mc "Я не дуже мав вибір, чесно кажучи."

    le "Тоді у нас є дещо спільне."

    le "І не став дурних питань, бабас."

    jump lettie_r1c1_what_to_talk

label lettie_r1c1_bothering:
    mc "Я тебе, мабуть, дратую?"

    le "Чому? Що тобі дало таку ідею?"

    le "Ніби я не зайнята чи щось. Латаю людей цілий день."

    menu:
        "Просто хотів по-дружньому. Вибач.":
            jump lettie_r1c1_friendly

        "Про що тоді з тобою говорити?":
            jump lettie_r1c1_what_to_talk

label lettie_r1c1_friendly:
    mc "Просто хотів по-дружньому поговорити. Вибач."

    le "Та ладно. Нормально."

    le "Просто не спала нормально."

    menu:
        "Я теж.":
            mc "Я теж."

            jump lettie_r1c1_want_something

        "Чому не спала?":
            mc "Чому не спала?"

            le "Ніколи не сплю."

            jump lettie_r1c1_want_something

label lettie_r1c1_want_something:
    le "Тобі щось треба? Чи просто час вбиваєш?"

    menu:
        "Просто хотів привітатися.":
            mc "Просто хотів привітатися."

            $ add_chemistry("Летті", 2)

            jump lettie_r1c1_end

        "Просто вбиваю час.":
            mc "Просто вбиваю час."

            jump lettie_r1c1_end

        "Хотів дізнатись, як ти.":
            jump lettie_r1c1_how_are_you

label lettie_r1c1_how_are_you:
    mc "Просто хотів дізнатись, як ти."

    le "Зайнята. Втомлена. У стресі."

    le "Як завжди."

    menu:
        "Тоді не буду заважати.":
            mc "Тоді не буду заважати."

            jump lettie_r1c1_end

        "Може, чимось допомогти?":
            mc "Може, чимось допомогти?"

            le "Переконай місцевих не лізти між Технорот і скальдру. Було б чудово."

            le "А крім того? Подумаю."

            $ add_chemistry("Летті", 4)
            $ add_insight("lettie_overwhelmed", "Летті перевантажена роботою — лікує і Гекс, і цивільних. Хронічно не висипається.")

            jump lettie_r1c1_end

label lettie_r1c1_what_to_talk:
    menu:
        "Про що тоді з тобою говорити?":
            mc "Добре, і які питання не дурні?"

        "Ладно, я правда не знаю, про що говорити.":
            mc "Ладно, я правда не знаю, про що говорити. Підкажеш?"

    le "Підказка: якщо вже перериваєш мій день — зроби це цікавим, добре?"

    menu:
        "Зробити цікавим. Зрозуміло. Піду... думати...":
            mc "Зробити цікавим. Зрозуміло. Піду... думати... про цікаві речі..."

            le "Успіхів."

            $ add_chemistry("Летті", 2)

        "Я тебе дратую — все, йду.":
            mc "Зрозуміло. Не буду заважати."

    jump lettie_r1c1_end

label lettie_r1c1_end:

    $ dialogue_end()
    $ store.seen_dialogues.add("lettie_rank1_convo1")
    $ set_flag("lettie_rank1_convo1_done")

    hide lettie
    return
