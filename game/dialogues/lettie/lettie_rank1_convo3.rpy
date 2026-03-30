# game/dialogues/lettie/lettie_rank1_convo3.rpy
# Летті — Ранг 1, Розмова 3: Аніта з'їла бинти / Потрібна марля

init python:
    DIALOGUE_ENTRIES.append({
        "id": "lettie_rank1_convo3",
        "who": "Летті",
        "conditions": {
            "flag_false": ["lettie_rank1_convo3_done"],
            "chemistry_min": ("Летті", 10),
        },
        "priority": 45,
        "chance": 100,
        "titles": [
            ("Привіт. Потрібна допомога?", "lettie_r1c3_anita"),
            ("Летті, як справи?", "lettie_r1c3_anita"),
            ("Чим допомогти?", "lettie_r1c3_grab_some"),
        ],
    })

label lettie_r1c3_anita:
    show lettie at char_center
    mc "Аніта — це хто?"

    le "Мій новий щуреня. Ще вчиться поводитись."

    $ add_insight("lettie_rat_anita", "У Летті є новий щур на ім'я Аніта. Гризе медичні припаси.")

    mc "А чому ти тримаєш щурів?"

    le "А ти скажи."

    mc "Що?"

    le "Хочу знати, чому ти думаєш, що я люблю щурів. Давай."

    menu:
        "Бо вони розумні, ласкаві і грайливі?":
            mc "Бо вони розумні, ласкаві і грайливі?"

            le "Луна врятуй... Ні."

            jump lettie_r1c3_rats_story

        "Бо їх часто не помічають і не розуміють?":
            mc "Бо їх часто не помічають і не розуміють?"

            le "..."

            jump lettie_r1c3_rats_story

        "Летті, я тебе взагалі не розумію. Але щури реально милі.":
            mc "Летті? Я тебе взагалі не розумію. Але щури реально милі."

            le "ХА!"

            le "Скромність від нашого рятівника. Подобається."

            $ add_chemistry("Летті", 4)

            jump lettie_r1c3_rats_story

label lettie_r1c3_rats_story:
    le "Не росла з грошима. Район не поганий був, але й не розкішний."

    le "Щурів легко тримати. Мама не заперечувала."

    le "Так, ти дістанеш ту марлю?"

    menu:
        "Звичайно, щось придумаю.":
            mc "Звичайно, щось придумаю."

            le "Дякую. Буду боржна. Трохи."

            $ add_chemistry("Летті", 4)
            $ set_flag("lettie_gauze_quest")

        "Твій щур — ти й шукай.":
            mc "Це ж твій щур з'їв. Сама й діставай."

            le "Авжеж, з усім моїм вільним часом. Між штопанням Гексу і цивільних."

            le "Дякую за нічого, бабас."

    jump lettie_r1c3_end

label lettie_r1c3_grab_some:
    show lettie at char_center

    mc "Якщо побачу марлю — візьму."

    le "Дякую. Буду боржна. Трохи."

    $ add_chemistry("Летті", 2)
    $ set_flag("lettie_gauze_quest")

    jump lettie_r1c3_end

label lettie_r1c3_end:

    $ dialogue_end()
    $ store.seen_dialogues.add("lettie_rank1_convo3")
    $ set_flag("lettie_rank1_convo3_done")

    hide lettie
    return
