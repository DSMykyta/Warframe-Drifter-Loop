# game/dialogues/quincy/quincy_sarcasm.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "quincy_sarcasm",
        "who": "Квінсі",
        "conditions": {
            "flag_false": ["quincy_sarcasm_done"],
            "rank_min": 1,
        },
        "priority": 45,
        "chance": 100,
        "label": "quincy_sarcasm",
    })

label quincy_sarcasm:
    show quince at char_center
    $ store.talked_today.add("Квінсі")

    qu "Lovely day, innit. Такий самий як вчора. І позавчора. І до того."
    $ advance_time(5)

    mc "Ти завжди такий оптимістичний?"
    $ advance_time(5)

    qu "Mate, я реаліст. Ми живемо в торговому центрі, який перезавантажується, як bloody комп'ютер. Оптимізм тут — розкіш."
    $ advance_time(5)

    qu "Бачиш ту крамницю? Там раніше продавали взуття. Тепер там сплять щури. Progress."
    $ advance_time(5)

    mc "Ти ж з Британії, так? Як ти опинився тут?"
    $ advance_time(5)

    qu "Long story. Коротка версія — я прокинувся тут, і ніхто не пояснив правил. Classic."
    $ advance_time(5)

    qu "Але знаєш що? Принаймні тут не треба платити за bloody rent. Cheers to that."
    $ advance_time(5)

    $ store.seen_dialogues.add("quincy_sarcasm")
    $ set_flag("quincy_sarcasm_done")
    $ add_insight("quincy_uk", "Квінсі родом з Британії. Тому і акцент і сленг")

    hide quince
    return
