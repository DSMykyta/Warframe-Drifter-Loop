# game/dialogues/lettie/lettie_coffee_addiction.rpy
# Летті пояснює, що кава — це не залежність, а ритуал

init python:
    DIALOGUE_ENTRIES.append({
        "id": "lettie_coffee_addiction",
        "who": "Летті",
        "conditions": {
            "flag_true": ["lettie_coffee_done"],
            "flag_false": ["lettie_coffee_addiction_done"],
            "rank_min": 2,
            "chemistry_min": ("Летті", 40),
        },
        "priority": 45,
        "chance": 100,
        "label": "lettie_coffee_addiction",
    })

label lettie_coffee_addiction:
    show lettie at char_center
    $ store.talked_today.add("Летті")

    le "Третя чашка. Не коментуй."
    $ advance_time(5)

    mc "Я нічого не казав."
    $ advance_time(5)

    le "Ти дивився на чашку з виразом обличчя Квінсі. Це гірше, ніж слова."
    $ advance_time(5)

    mc "Три чашки до обіду — це ж не нормально?"
    $ advance_time(5)

    le "А що тут нормально? Ми живемо в торговому центрі, застрягли в часовій петлі, і мій медвідсік знаходиться між магазином взуття і кінотеатром."
    $ advance_time(5)

    le "Кава — це не про кофеїн. Це про ритуал. Нагріти воду. Відміряти зерна. Почекати. В цьому хаосі — єдине, що я контролюю від початку до кінця."
    $ advance_time(5)

    menu:
        "Тобі потрібно щось передбачуване.":
            $ advance_time(5)
            mc "Тобі потрібно щось передбачуване."
            le "...Так. Саме так. Кожного ранку я не знаю, хто прийде з пораненням, хто не прокинеться, що зміниться. Але кава — кава завжди та сама."
            $ advance_time(5)

        "Може, спробуєш чай?":
            $ advance_time(5)
            mc "Може, спробуєш чай?"
            le "Чай — це для людей, які ще вірять, що світ м'який. Я вже давно знаю, що він гіркий. Як моя кава."
            $ advance_time(5)

    le "Коли все розвалюється — а все завжди розвалюється — я сиджу з чашкою і дихаю парою. П'ять хвилин тиші. П'ять хвилин, де ніхто не кровоточить."
    $ advance_time(5)

    le "Це не залежність. Це — якір."
    $ advance_time(5)

    $ store.seen_dialogues.add("lettie_coffee_addiction")
    $ set_flag("lettie_coffee_addiction_done")
    $ add_insight("lettie_coffee_ritual", "Кава для Летті не залежність а ритуал — єдине передбачуване в хаосі петлі")

    hide letty
    return
