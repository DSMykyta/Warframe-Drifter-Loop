# game/dialogues/arthur/arthur_future.rpy
# Пізній діалог — Артур роздумує про життя після петлі

init python:
    DIALOGUE_ENTRIES.append({
        "id": "arthur_future",
        "who": "Артур",
        "conditions": {
            "flag_true": ["arthur_icr_trauma_done"],
            "flag_false": ["arthur_future_done"],
            "chemistry_min": ("Артур", 100),
            "rank_min": 4,
        },
        "priority": 50,
        "chance": 100,
        "label": "arthur_future",
    })

label arthur_future:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    ar "Ти коли-небудь думав, що буде, коли це все скінчиться?"
    $ advance_time(5)

    mc "Петля? Війна? Все разом?"
    $ advance_time(5)

    ar "Все разом. Якщо уявити, що одного дня ми прокидаємось і більше не треба воювати. Що тоді?"
    $ advance_time(5)

    mc "А ти що хочеш?"
    $ advance_time(5)

    ar "Ось у цьому проблема. Я не знаю."
    $ advance_time(5)

    ar "Все моє доросле життя — це служба, потім втеча, потім боротьба. Я не вмію жити без ворога."
    $ advance_time(5)

    ar "Іноді я думаю — може, відкрити кафе? Готувати для людей. Не тому, що вони йдуть на бій, а просто... тому що їм смачно."
    $ advance_time(5)

    mc "Артур Петершем, власник кафе. Мені подобається."
    $ advance_time(5)

    ar "Не смійся."
    $ advance_time(5)

    mc "Я серйозно."
    $ advance_time(5)

    menu:
        "Ти заслуговуєш на спокійне життя":
            $ advance_time(5)
            mc "Ти заслуговуєш на спокій, Артуре. Більше за більшість."

            ar "Заслуговую? Не знаю. Але хочу — це точно."
            $ advance_time(5)

            ar "Може, цього достатньо. Хотіти."
            $ advance_time(5)
            $ set_flag("arthur_wants_peace")
            $ chemistry["Артур"] += 3

        "Ми могли б відкрити його разом":
            $ advance_time(5)
            mc "Слухай, якщо ти серйозно — я з тобою. Будемо партнерами."

            ar "...Ти зараз серйозно пропонуєш мені бізнес-план посеред апокаліпсису?"
            $ advance_time(5)

            mc "А чому ні? Треба ж мати мету."
            $ advance_time(5)

            ar "Артур і Дрифтер. Кафе «Скана». Звучить жахливо. Мені подобається."
            $ advance_time(5)
            $ set_flag("arthur_cafe_plan")
            $ chemistry["Артур"] += 5

        "Спочатку давай виживемо":
            $ advance_time(5)
            mc "Гарні мрії. Але спочатку треба пережити завтрашній день."

            ar "Практичний підхід. Я це ціную."
            $ advance_time(5)

            ar "Але мрії — це не слабкість. Це паливо. Без них ти просто машина, яка воює, поки не зламається."
            $ advance_time(5)
            $ set_flag("arthur_pragmatic_future")
            $ chemistry["Артур"] += 3

    ar "Дякую за цю розмову. Серйозно. Я рідко дозволяю собі думати про «потім»."
    $ advance_time(5)

    ar "Але з тобою... здається, «потім» можливе."
    $ advance_time(5)

    $ store.seen_dialogues.add("arthur_future")
    $ set_flag("arthur_future_done")
    $ add_insight("arthur_dream", "Артур мріє про кафе після війни. Хоче готувати для людей просто тому, що їм смачно — не заради виживання.")

    hide arthur
    return
