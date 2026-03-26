# game/dialogues/amir/amir_trust_milestone.rpy
# MILESTONE: Амір дає гравцю свій запасний контролер — найвищий знак довіри

init python:
    DIALOGUE_ENTRIES.append({
        "id": "amir_trust_milestone",
        "who": "Амір",
        "conditions": {
            "flag_false": ["amir_trust_milestone_done"],
            "rank_min": 1,
            "chemistry_min": ("Амір", 60),
        },
        "priority": 80,
        "chance": 100,
        "label": "amir_trust_milestone",
    })

label amir_trust_milestone:
    show amir at char_center
    $ store.talked_today.add("Амір")

    am "Тримай. Обережно."
    $ advance_time(5)

    mc "Що це?"
    $ advance_time(5)

    am "Мій запасний контролер. Модифікований. Перепаяні тригери, нові стіки, кастомна плата. Двісті годин роботи."
    $ advance_time(5)

    mc "Ти даєш мені свій контролер?"
    $ advance_time(5)

    am "Не \"свій контролер\". Свій запасний контролер. Різниця величезна. Основний я нікому не дам, навіть під загрозою смерті."
    $ advance_time(5)

    am "Але запасний — це... ну, це як ключ від квартири. Я довіряю тобі мій другий найцінніший предмет."
    $ advance_time(5)

    menu:
        "Я буду берегти його.":
            $ advance_time(5)
            mc "Я буду берегти його."
            am "Ти краще бережи. Якщо я побачу на ньому подряпину — наша дружба закінчиться. Я серйозно. Ну, майже серйозно."
            $ advance_time(5)

        "Це найкращий подарунок, який мені дарували.":
            $ advance_time(5)
            mc "Це найкращий подарунок, який мені дарували."
            am "Стоп, у мене щось в оці. Ні, серйозно. Пил. Тут пильно. Не дивись на мене так."
            $ advance_time(5)

    am "Якщо я довіряю тобі це — я довіряю тобі все. Запам'ятай."
    $ advance_time(5)

    am "А тепер давай зіграємо. Удвох. Як нормальні люди."
    $ advance_time(5)

    $ chemistry["Амір"] += 5

    $ store.seen_dialogues.add("amir_trust_milestone")
    $ set_flag("amir_trust_milestone_done")
    $ add_insight("amir_controller_trust", "Амір дав гравцю свій запасний контролер — для нього це найвищий знак довіри")

    hide amir
    return
