# game/dialogues/lettie/lettie_rank1_convo3.rpy
# Летті — Ранг 1, Розмова 3: Аніта з'їла бинти / Потрібна марля

init python:
    DIALOGUE_ENTRIES.append({
        "id": "lettie_rank1_convo3",
        "who": "Летті",
        "conditions": {
            "flag_true": ["lettie_intro_done", "lettie_rank1_convo2_done"],
            "flag_false": ["lettie_rank1_convo3_done"],
            "rank_min": 1,
        },
        "priority": 45,
        "chance": 100,
        "label": "lettie_rank1_convo3",
    })

label lettie_rank1_convo3:
    show lettie at char_center
    $ store.talked_today.add("Летті")
    $ dialogue_begin()

    le "Бабас. Слухай сюди."

    menu:
        "Це таке привітання?":
            mc "Це таке привітання?"

            le "Так, привіт, добрий ранок — чи що там зараз."

        "Слухаю.":
            mc "Слухаю."

    le "Мені потрібна марля. Запаси закінчуються."

    le "Аніта дісталася до коробки і прогризла частину."

    menu:
        "Хто така Аніта?":
            jump lettie_r1c3_anita

        "Я поняття не маю, хто це, Летті.":
            jump lettie_r1c3_anita

        "Якщо побачу марлю — візьму.":
            jump lettie_r1c3_grab_some

label lettie_r1c3_anita:
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
