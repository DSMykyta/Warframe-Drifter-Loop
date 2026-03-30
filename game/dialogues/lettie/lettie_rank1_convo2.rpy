# game/dialogues/lettie/lettie_rank1_convo2.rpy
# Летті — Ранг 1, Розмова 2: Хтось вдома сумує? / Чому щури?

init python:
    DIALOGUE_ENTRIES.append({
        "id": "lettie_rank1_convo2",
        "who": "Летті",
        "conditions": {
            "flag_true": ["lettie_intro_done", "lettie_rank1_convo1_done"],
            "flag_false": ["lettie_rank1_convo2_done"],
            "rank_min": 1,
        },
        "priority": 45,
        "chance": 100,
        "label": "lettie_rank1_convo2",
    })

label lettie_rank1_convo2:
    show lettie at char_center
    $ store.talked_today.add("Летті")
    $ dialogue_begin()

    menu:
        "Хтось вдома за тобою сумує?":
            jump lettie_r1c2_family

        "Чому ти тримаєш щурів як домашніх тварин?":
            jump lettie_r1c2_rats

label lettie_r1c2_family:
    mc "Летті... хтось вдома за тобою сумує?"

    le "Яка різниця. Не можу покинути цю нору."

    le "Навіщо думати про них."

    menu:
        "Ну... добре...":
            mc "Ну... добре..."

            jump lettie_r1c2_end

        "Ми ж спілкуємось через інтернет. І телефон існує, знаєш?":
            jump lettie_r1c2_phone

        "Іноді болючі спогади — це єдине, що тримає на плаву.":
            jump lettie_r1c2_pain

label lettie_r1c2_phone:
    mc "Ми ж спілкуємось через інтернет. І телефон існує, знаєш?"

    le "..."

    le "Є речі, які не скажеш через екран, бабас."

    $ add_chemistry("Летті", 2)

    jump lettie_r1c2_end

label lettie_r1c2_pain:
    mc "Іноді болючі спогади — це єдине, що тримає на плаву."

    le "Справді? А що ти знаєш про біль?"

    menu:
        "Я не мушу тобі нічого доводити.":
            mc "Я не мушу тобі нічого доводити."

            le "Справедливо."

            $ add_chemistry("Летті", 2)

            jump lettie_r1c2_end

        "Ти знаєш, як це — коли тобі відрубують голову? Я знаю. Помирав тисячу разів. І це боляче.":
            jump lettie_r1c2_deaths

label lettie_r1c2_deaths:
    mc "Ти знаєш, як це — коли тобі відрубують голову? Я знаю."

    mc "Помирав тисячу разів. І це боляче."

    le "Торкнутий Смертю... Ще один привид, як і ми всі."

    le "Переживаєш свої смерті знову і знову і знову."

    le "Так... є родина вдома. Нехай краще думають, що я вже мертва."

    menu:
        "Тут все ще є життя, заради якого варто жити.":
            mc "Тут все ще є життя, заради якого варто жити."

            le "Авжеж, авжеж. З іграми Аміра, випивкою Артура, музикою Аоі та малюнками Квінсі."

            le "Порожні хобі. Порожні душі. Вбивають час у вічності."

            le "Мені треба працювати. Йди."

            jump lettie_r1c2_end

        "Ти береш на себе чужий біль за власним вибором чи з обов'язку?":
            mc "Ти береш на себе чужий біль за власним вибором чи з обов'язку?"

            le "І те, і інше, мабуть. Обрала давно. Тепер пізно повертати."

            le "Мені треба працювати."

            $ add_chemistry("Летті", 4)
            $ add_insight("lettie_burden_choice", "Летті обрала нести чужий біль давно — і вважає, що вже пізно щось змінювати.")

            jump lettie_r1c2_end

label lettie_r1c2_rats:
    mc "Летті, а чому саме щурі? Як домашні тварини?"

    le "А ти скажи."

    mc "Що?"

    le "Хочу знати, чому ти думаєш, що я люблю щурів. Давай."

    menu:
        "Бо вони розумні, ласкаві і грайливі?":
            mc "Бо вони розумні, ласкаві і грайливі?"

            le "Луна врятуй... Ні."

            jump lettie_r1c2_rats_childhood

        "Бо їх часто не помічають і не розуміють?":
            mc "Бо їх часто не помічають і не розуміють?"

            le "Хм. Теплішe."

            jump lettie_r1c2_rats_childhood

        "Летті, я не розумію в тобі нічогісінько. Але щури реально милі.":
            jump lettie_r1c2_rats_honesty

label lettie_r1c2_rats_honesty:
    mc "Летті? Я не розумію в тобі нічогісінько. Але щури реально милі."

    le "ХАХАХА!"

    le "Скромність від нашого рятівника. Мені подобається."

    $ add_chemistry("Летті", 4)

    jump lettie_r1c2_rats_childhood

label lettie_r1c2_rats_childhood:
    le "Не росла з грошима. Кидало з бази на базу."

    le "Щурів було легко тримати. Мама не заперечувала."

    $ add_insight("lettie_childhood_rats", "Летті виросла небагато — кидало з бази на базу. Щурів тримала з дитинства, бо були доступні.")

    le "Мені треба повертатися до роботи. Побачимось, бабас."

    $ add_chemistry("Летті", 2)

    jump lettie_r1c2_end

label lettie_r1c2_end:

    $ dialogue_end()
    $ store.seen_dialogues.add("lettie_rank1_convo2")
    $ set_flag("lettie_rank1_convo2_done")

    hide lettie
    return
