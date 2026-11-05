# game/dialogues/arthur/arthur_skana_story.rpy
# Артур розповідає історію меча Скана — емоційний момент у барі

init python:
    DIALOGUE_ENTRIES.append({
        "id": "arthur_skana_story",
        "who": "Артур",
        "conditions": {
            "flag_true": ["arthur_bar_meeting_done"],
            "flag_false": ["arthur_skana_story_done"],
            "chemistry_min": ("Артур", 40),
            "location": "bar_skana",
            "rank_min": 2,
        },
        "priority": 55,
        "chance": 100,
        "label": "arthur_skana_story",
    })

label arthur_skana_story:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    ar "Знаєш, чому цей бар називається «Скана»?"
    $ advance_time(5)

    mc "Ні. Думав, просто назва."
    $ advance_time(5)

    ar "Скана — це тип клинка. Старий, ще довоєнний дизайн. Прямий, без вигадок."
    $ advance_time(5)

    ar "У мене є такий. Ти, можливо, бачив його у мене в кімнаті."
    $ advance_time(5)

    mc "Бачив. Він виглядає... бувалим."
    $ advance_time(5)

    ar "Бо він бувалий."
    $ advance_time(5)

    ar "Його власника звали Мартін. Ми разом служили в ICR. Він був... старший за мене на п'ять років. Навчив мене половині того, що я знаю."
    $ advance_time(5)

    ar "Мартін був ідеалістом. Вірив, що ICR існує, щоб захищати людей. Не контролювати. Не придушувати."
    $ advance_time(5)

    mc "А ти?"
    $ advance_time(5)

    ar "Я вірив йому. Цього було достатньо."
    $ advance_time(5)

    ar "Одного дня нас відправили на зачистку селища. Сказали — повстанці. Виявилось — фермери, які відмовились здати врожай."
    $ advance_time(5)

    ar "Мартін відмовився стріляти. Став між нашими і цивільними."
    $ advance_time(5)

    mc "Що сталося?"
    $ advance_time(5)

    ar "Командир дав наказ. Мартін не відійшов."
    $ advance_time(5)

    ar "Він помирав повільно. Встиг віддати мені свій клинок. Сказав — «не забудь, для чого ми тримаємо зброю»."
    $ advance_time(5)

    ar "Я не забув."
    $ advance_time(5)

    ar "Тому я тут, а не там."
    $ advance_time(5)

    menu:
        "Мартін звучить як гідна людина":
            $ advance_time(5)
            mc "Мартін звучить як людина, яка заслуговувала кращого."

            ar "Заслуговував. Як і більшість тих, кого ми втратили."
            $ advance_time(5)

            $ add_chemistry("Артур", 2)

        "Ти тримаєш цей клинок як пам'ять?":
            $ advance_time(5)
            mc "Ти тримаєш Скану як пам'ять про нього?"

            ar "Як нагадування. Пам'ять — це м'яко. Нагадування — це те, що не дає повторити помилку."
            $ advance_time(5)

            $ add_chemistry("Артур", 2)

        "Важко з цим жити?":
            $ advance_time(5)
            mc "Тобі важко з цим жити?"

            ar "Щодня. Але не жити з цим — ще важче."
            $ advance_time(5)

            $ add_chemistry("Артур", 4)

    ar "Дякую, що вислухав. Я рідко кому це розповідаю."
    $ advance_time(5)

    $ store.seen_dialogues.add("arthur_skana_story")
    $ set_flag("arthur_skana_story_done")
    $ set_flag("arthur_skana_story_told")
    $ add_insight("arthur_skana_origin", "Скана — клинок Мартіна, наставника Артура з ICR. Мартін загинув, захищаючи цивільних від власного командира.")
    $ add_insight("arthur_icr_defection", "Артур пішов з ICR через вбивство невинних. Скана — його нагадування.")

    hide arthur
    return
