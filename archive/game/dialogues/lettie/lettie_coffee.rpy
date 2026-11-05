# game/dialogues/lettie/lettie_coffee.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "lettie_coffee",
        "who": "Летті",
        "conditions": {
            "flag_false": ["lettie_coffee_done"],
            "rank_min": 1,
        },
        "priority": 45,
        "chance": 100,
        "label": "lettie_coffee",
    })

label lettie_coffee:
    show lettie at char_center
    $ store.talked_today.add("Летті")

    le "Не зараз. Я ще не випила каву."
    $ advance_time(5)

    mc "Вже майже полудень."
    $ advance_time(5)

    le "І? Кава — це не про час. Це про стан. Без неї я — загроза для оточуючих."
    $ advance_time(5)

    le "Одного разу Квінсі заговорив зі мною до кави. Я сказала йому таке, що він три дні зі мною не розмовляв."
    $ advance_time(5)

    mc "Що саме ти сказала?"
    $ advance_time(5)

    le "Правду. Але без кави я не фільтрую. Все йде як є — без цукру і без молока, як і моя кава."
    $ advance_time(5)

    le "Тож якщо хочеш нормальну розмову — дай мені п'ять хвилин і одну чашку."
    $ advance_time(5)

    $ store.seen_dialogues.add("lettie_coffee")
    $ set_flag("lettie_coffee_done")
    $ add_insight("lettie_coffee", "Летті п'є каву кожного ранку. Без неї не функціонує")

    hide letty
    return
