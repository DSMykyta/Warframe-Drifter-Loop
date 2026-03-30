# game/dialogues/quincy/quincy_rank1_convo2.rpy
# Квінсі — Ранг 1, Розмова 2: Конфлікт з Артуром

init python:
    DIALOGUE_ENTRIES.append({
        "id": "quincy_rank1_convo2",
        "who": "Квінсі",
        "conditions": {
            "flag_false": ["quincy_rank1_convo2_done"],
            "chemistry_min": ("Квінсі", 5),
        },
        "priority": 45,
        "chance": 100,
        "label": "quincy_rank1_convo2",
    })

label quincy_rank1_convo2:
    show quince at char_center
    $ store.talked_today.add("Квінсі")
    $ dialogue_begin()

    qu "Знову тут. Йо."

    menu:
        "Ігнорувати.":
            mc "..."
            qu "Ну ладно, забий."
            jump quincy_r1c2_end_short

        "Можу спитати... що у тебе за проблема з Артуром?":
            mc "Слухай, Квінсі... можу запитати — яка у тебе проблема з Артуром?"
            jump quincy_r1c2_main

    label quincy_r1c2_main:
    qu "Lmao. Ну ти й тунель, взяв і спитав в лоба."
    qu "Хочеш знати яка в мене каша з Його Величністю? Скажу. Три речі."
    qu "Перша. Геройбой сприймає себе ЗАНАДТО серйозно."
    qu "Думає, що він досі в армії. Треба зупинитись і зрозуміти — тут немає правил."
    qu "І хіба йому так важко ПОСМІЯТИСЯ раз на тиждень?! Sols tits! А кажуть що то В МЕНЕ проблеми."

    menu:
        "Бути головним — це великий стрес.":
            qu "Ти думаєш я цього не бачу?! Я не дурень, chief. Не роби висновків просто глянувши на мене."
            qu "Я кажу що геройбою треба витягнути ту палку з дупи."
            qu "Від неї НІКОМУ користі. І мене вона конкретно дратує."
            jump quincy_r1c2_second

        "Він дійсно любить похмуритись...":
            qu "Я ЗНАЮ. Тільки тому що світ котиться в прірву, не означає що не можна іноді випустити пару."
            $ add_chemistry("Квінсі", 2)
            jump quincy_r1c2_second

        "А що друге?":
            jump quincy_r1c2_second

    label quincy_r1c2_second:
    qu "Друге. Геройбой поважає мої lux скіли, розумієш? Тому і тримає мене поряд."
    qu "Інакше б не терпів мій булшіт."
    qu "Але він мене НЕ СЛУХАЄ. Думає, що я тільки для одного придатний — стрілянини та вбивства."
    qu "Думає я просто якийсь юнак, готовий зірватися при першій проблемі. Не, cuz. Не про це."

    menu:
        "Не знаю. А ти б зірвався?":
            qu "..."
            qu "Fair point. Але ні. Не зірвався б."
            jump quincy_r1c2_techrot

        "А чому ти залишився, коли тут стало зовсім погано?":
            jump quincy_r1c2_techrot

    label quincy_r1c2_techrot:
    qu "Коли почалася техногниль? Шііт. Ти одразу в глибоку частину басейну."
    qu "Не-не. Треба спочатку ближче познайомитись, перш ніж я почну розповідати всі секрети."
    qu "Треба мати вагому причину, щоб шепотіти на вухо. ;)"

    menu:
        "Трохи рано починати фліртувати зі мною, ні?":
            qu "Ти реально тунель, знаєш? lol. Ти серйозно не вмієш розслабитись?"

            menu:
                "Моє життя не було саме розслабленим.":
                    qu "А ти думаєш моє було, m8?! lmao. Ти ще нічого про мене не знаєш."
                    $ add_chemistry("Квінсі", 2)
                    jump quincy_r1c2_third

        "Ти... фліртуєш зі мною?":
            qu "Ти реально тунель, знаєш? lol. Може так. Може ні. А ти як хочеш?"

            menu:
                "Я точно не проти.":
                    qu "Я знав, що ти оцінив товар коли тільки з'явився. І не буду брехати..."
                    qu "Мені теж подобається вид."
                    qu "Але давай повільно, да? Тут є чим зайнятись крім одне одного, LMAO."
                    $ add_chemistry("Квінсі", 4)
                    $ set_flag("quincy_flirt_positive")
                    jump quincy_r1c2_third

                "Я... ще не визначився.":
                    qu "Fair enough. Скажеш коли визначишся."
                    qu "Але не буду брехати — мені подобається вид. Ти peng, cuz."
                    qu "Але я притримаю коней. Скажеш коли будеш ready."
                    $ add_chemistry("Квінсі", 2)
                    jump quincy_r1c2_third

                "Краще не треба, без образ.":
                    qu "No big, cuz. No big."
                    jump quincy_r1c2_third

        "Ой, ми тепер фліртуємо? lol.":
            qu "Це просто взаємна оцінка lux товару, от і все, lol."
            qu "Якщо напрягає — скажи, і я зупинюсь. Я знаю що маю peng товар, але розумію що це не для всіх."

            menu:
                "Я точно не проти.":
                    qu "О, а мені подобається ця відповідь."
                    qu "Але давай повільно, ок? Тут є чим зайнятися, lmao."
                    $ add_chemistry("Квінсі", 4)
                    $ set_flag("quincy_flirt_positive")
                    jump quincy_r1c2_third

                "Я ще думаю.":
                    qu "Ок, без поспіху. Дай знати."
                    $ add_chemistry("Квінсі", 2)
                    jump quincy_r1c2_third

                "Не треба, чесно.":
                    qu "No big, cuz."
                    jump quincy_r1c2_third

    label quincy_r1c2_third:
    qu "Ладно, третє. Але це вже наступного разу."
    qu "Геройбой мене пейджить як скажений на патруль."

    mc "Біжи. Не буду затримувати."

    qu "l8r, cuz."

    label quincy_r1c2_end:

    $ dialogue_end()
    $ store.seen_dialogues.add("quincy_rank1_convo2")
    $ set_flag("quincy_rank1_convo2_done")
    $ add_insight("quincy_arthur_beef", "Квінсі має три претензії до Артура: занадто серйозний, не слухає, і третю він ще не розказав.")

    hide quince
    return

    label quincy_r1c2_end_short:

    $ dialogue_end()
    $ store.seen_dialogues.add("quincy_rank1_convo2")
    $ set_flag("quincy_rank1_convo2_done")

    hide quince
    return
