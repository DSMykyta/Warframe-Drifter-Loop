# game/dialogues/lettie/lettie_cynicism.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "lettie_cynicism",
        "who": "Летті",
        "conditions": {
            "flag_true": ["lettie_intro_done"],
            "flag_false": ["lettie_cynicism_done"],
            "rank_min": 1,
        },
        "priority": 45,
        "chance": 100,
        "label": "lettie_cynicism",
    })

label lettie_cynicism:
    show letty at char_center
    $ store.talked_today.add("Летті")

    le "Знаєш, що найсмішніше в цьому торговому центрі? Він досі виглядає так, ніби чекає на покупців."
    $ advance_time(5)

    mc "Ну, ми ж тут живемо."
    $ advance_time(5)

    le "Саме. Живемо в місці, яке було створене, щоб люди витрачали гроші на речі, які їм не потрібні. А тепер ми тут ховаємось від речей, які нас вбивають."
    $ advance_time(5)

    le "Ірронія така густа, що її можна різати ножем."
    $ advance_time(5)

    mc "Ти завжди бачиш все так... похмуро?"
    $ advance_time(5)

    le "Не похмуро. Чесно. Різниця в тому, що після чесності я все одно встаю і роблю свою роботу."
    $ advance_time(5)

    le "Хтось має бути реалістом, поки інші мріють про \"повернення до нормального життя\". Нормального вже не буде. Є тільки — нове."
    $ advance_time(5)

    $ store.seen_dialogues.add("lettie_cynicism")
    $ set_flag("lettie_cynicism_done")
    $ add_insight("lettie_sarcasm", "Летті жартує гостро. Але за сарказмом ховається турбота")

    hide letty
    return
