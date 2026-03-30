# game/dialogues/arthur/arthur_rank1_convo3.rpy
# ArthurRank1Convo3 — Дрифтер просить позичити Атомоцикл. Артур дуже захисний.

init python:
    DIALOGUE_ENTRIES.append({
        "id": "arthur_rank1_convo3",
        "who": "Артур",
        "conditions": {
            "flag_true": ["arthur_intro_done", "arthur_rank1_convo1_done"],
            "flag_false": ["arthur_rank1_convo3_done"],
            "rank_min": 1,
        },
        "priority": 45,
        "chance": 100,
        "label": "arthur_rank1_convo3",
    })

label arthur_rank1_convo3:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    mc "Артуре, можна питання?"
    $ advance_time(3)

    ar "Залежить від питання."
    $ advance_time(3)

    mc "Твій Атомоцикл. Можна позичити на вечір?"
    $ advance_time(3)

    ar "Ні."
    $ advance_time(3)

    mc "Ти навіть не подумав."
    $ advance_time(3)

    ar "Я подумав ще до того, як ти закінчив речення. Відповідь — ні."
    $ advance_time(3)

    menu:
        "А якщо я дуже обережно?":
            $ advance_time(3)
            mc "Обіцяю повернути без жодної подряпини. Навіть заправлю."

            ar "Ти не розумієш. Це не питання довіри до тебе. Це мій Атомоцикл."
            $ advance_time(3)

            ar "Я зібрав його власноруч. Кожну деталь підганяв місяцями."
            $ advance_time(3)

            $ add_chemistry("Артур", 2)

            menu:
                "Я розумію. Вибач.":
                    $ advance_time(3)
                    mc "Зрозуміло. Це як зброя — особиста річ. Не треба було питати."

                    ar "...Ні. Нормально, що спитав. Просто знай — це єдине, чим я не ділюся."
                    $ advance_time(3)

                    ar "Але якщо колись буде потреба кудись дістатись... Я можу підвезти."
                    $ advance_time(3)

                    $ add_chemistry("Артур", 4)
                    $ set_flag("arthur_ride_offer")
                    $ add_insight("arthur_atomicycle", "Артур зібрав Атомоцикл сам. Для нього це більше ніж транспорт.")

                "Тоді навчи мене збирати свій":
                    $ advance_time(3)
                    mc "Ну, тоді може навчиш мене, як зібрати власний?"

                    ar "Це... не найгірша ідея. Але для цього потрібні запчастини, яких тут немає."
                    $ advance_time(3)

                    $ add_chemistry("Артур", 2)

        "Я візьму силою, якщо доведеться":
            $ advance_time(3)
            mc "А що як я просто візьму без дозволу?"

            ar "Тоді я знайду тебе. І це буде неприємна розмова."
            $ advance_time(3)

            ar "Повір мені. Ти не хочеш цієї розмови."
            $ advance_time(3)

            $ add_chemistry("Артур", -2)

            menu:
                "Жартую, жартую":
                    $ advance_time(3)
                    mc "Розслабся, це був жарт. Хоча твоє обличчя зараз — безцінне."

                    ar "...Дуже смішно."
                    $ advance_time(3)

                    ar "Наступного разу жартуй про щось інше. Не про мій транспорт."
                    $ advance_time(3)

                "Надіслати смайлик :)":
                    $ advance_time(3)
                    mc "Я потім надішлю тобі повідомлення. З усміхненим обличчям. Ось таким — :)"

                    ar "Що це означає? Двокрапка і дужка?"
                    $ advance_time(3)

                    mc "Це... емотикон. Усмішка."
                    $ advance_time(3)

                    ar "Навіщо малювати обличчя з розділових знаків, коли можна просто посміхнутись?"
                    $ advance_time(3)

                    mc "Це для повідомлень. Коли тебе не бачать."
                    $ advance_time(3)

                    ar "Якщо я хочу щось сказати — скажу в обличчя. Як нормальна людина."
                    $ advance_time(3)

                    $ add_chemistry("Артур", 2)
                    $ add_insight("arthur_emoticons", "Артур не розуміє емотикони. І не збирається вчитись.")

        "Ладно, забудь":
            $ advance_time(3)
            mc "Гаразд, зрозумів. Забудь що питав."

            ar "Вже забув."
            $ advance_time(3)

    $ store.seen_dialogues.add("arthur_rank1_convo3")
    $ set_flag("arthur_rank1_convo3_done")

    hide arthur
    return
