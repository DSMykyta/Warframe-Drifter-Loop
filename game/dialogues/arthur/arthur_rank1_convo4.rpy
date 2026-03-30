# game/dialogues/arthur/arthur_rank1_convo4.rpy
# ArthurRank1Convo4 — Артур питає де Дрифтер навчився воювати. Важча тема — смерть, петлі, Дувірі.

init python:
    DIALOGUE_ENTRIES.append({
        "id": "arthur_rank1_convo4",
        "who": "Артур",
        "conditions": {
            "flag_true": ["arthur_intro_done", "arthur_rank1_convo2_done"],
            "flag_false": ["arthur_rank1_convo4_done"],
            "rank_min": 1,
        },
        "priority": 45,
        "chance": 100,
        "label": "arthur_rank1_convo4",
    })

label arthur_rank1_convo4:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    ar "Дрифтер. Маю питання, яке давно крутиться в голові."
    $ advance_time(3)

    ar "Ти вмієш битися. Це видно. Але де ти цьому навчився?"
    $ advance_time(3)

    menu:
        "Був наставник. Тешін.":
            jump arthur_r1c4_teshin

        "Методом проб і помилок.":
            jump arthur_r1c4_trial

        "Не хочу про це.":
            jump arthur_r1c4_dismiss

label arthur_r1c4_teshin:
    mc "У мене був вчитель. Тешін. Він навчив мене основ — дисципліни, техніки, витримки."
    $ advance_time(3)

    ar "Тешін. Не чув такого імені. Але за результатом — він знав свою справу."
    $ advance_time(3)

    mc "Він був суворий. Інколи жорстокий. Але все, що я вмію — завдяки йому."
    $ advance_time(3)

    ar "Суворий наставник — не найгірше, що може бути. Повір, я знаю."
    $ advance_time(3)

    $ add_chemistry("Артур", 2)
    $ add_insight("drifter_teshin", "Дрифтер навчився битися у наставника на ім'я Тешін. Суворого, але ефективного.")

    jump arthur_r1c4_deeper

label arthur_r1c4_trial:
    mc "Ніхто не вчив. Просто... пробував. Помилявся. Падав. Вставав."
    $ advance_time(3)

    ar "Самоучка? Це або вроджений талант, або дуже багато шрамів."
    $ advance_time(3)

    mc "Друге. Дуже, дуже багато шрамів."
    $ advance_time(3)

    ar "Хм. Це я поважаю. Не кожен може навчитись без системи."
    $ advance_time(3)

    $ add_chemistry("Артур", 2)

    jump arthur_r1c4_deeper

label arthur_r1c4_dismiss:
    mc "Давай не будемо про це."
    $ advance_time(3)

    ar "Зрозумів. Кожен має теми, яких не чіпає."
    $ advance_time(3)

    ar "Але знай — я питаю не з цікавості. Мені важливо розуміти, на кого я можу покластися в бою."
    $ advance_time(3)

    mc "...Справедливо. Може, іншим разом."
    $ advance_time(3)

    jump arthur_r1c4_end

label arthur_r1c4_deeper:
    ar "Але є щось, що мене бентежить. Ти б'єшся як людина, яка не боїться смерті."
    $ advance_time(3)

    ar "Це або хоробрість, або ти знаєш щось, чого не знаю я."
    $ advance_time(3)

    menu:
        "Я помирав. Багато разів.":
            $ advance_time(3)
            mc "Я не боюся смерті, тому що вже помирав. Не один раз. Не два."

            ar "...Що?"
            $ advance_time(3)

            mc "Часові петлі. Дувірі. Там смерть — це не кінець. Це перезавантаження."
            $ advance_time(3)

            mc "Прокидаєшся знову. Пам'ятаєш біль, але тіло ціле. І все починається спочатку."
            $ advance_time(3)

            ar "Це..."
            $ advance_time(3)

            ar "Я навіть не знаю, що на це сказати."
            $ advance_time(3)

            $ add_chemistry("Артур", 4)
            $ add_insight("drifter_death_loops", "Дрифтер помирав безліч разів у часових петлях Дувірі. Для нього смерть — це перезавантаження.")

            jump arthur_r1c4_reflection

        "Просто звик до ризику.":
            $ advance_time(3)
            mc "Коли досить довго живеш на межі, перестаєш відчувати страх. Або він стає фоновим шумом."

            ar "Фоновий шум... Це я розумію. Занадто добре розумію."
            $ advance_time(3)

            $ add_chemistry("Артур", 2)

            jump arthur_r1c4_reflection

label arthur_r1c4_reflection:
    ar "Слухай. Я не буду робити вигляд, що зрозумів усе, що ти сказав."
    $ advance_time(3)

    ar "Але я бачу, що за цим стоїть щось серйозне. Щось, про що не розповідають між справою."
    $ advance_time(3)

    menu:
        "Колись розкажу більше. Коли будемо готові.":
            $ advance_time(3)
            mc "Є речі, які важко пояснити. Особливо тому, хто цього не пережив."

            mc "Але колись, коли буде час і довіра — розкажу."
            $ advance_time(3)

            ar "Добре. Я зачекаю. Я вмію чекати."
            $ advance_time(3)

            $ add_chemistry("Артур", 4)
            $ set_flag("arthur_drifter_past_hinted")

        "Це не має значення. Головне — теперішнє.":
            $ advance_time(3)
            mc "Минуле — це минуле. Зараз я тут, з вами. Це єдине, що важливо."

            ar "Практичний підхід. Не найгірша філософія."
            $ advance_time(3)

            $ add_chemistry("Артур", 2)

    ar "Дрифтер."
    $ advance_time(3)

    mc "Так?"
    $ advance_time(3)

    ar "Дякую, що не збрехав. Навіть якщо не сказав усього — ти не збрехав."
    $ advance_time(3)

    jump arthur_r1c4_end

label arthur_r1c4_end:

    $ store.seen_dialogues.add("arthur_rank1_convo4")
    $ set_flag("arthur_rank1_convo4_done")

    hide arthur
    return
