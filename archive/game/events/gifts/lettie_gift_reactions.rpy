# game/events/gifts/lettie_gift_reactions.rpy
# Особлива реакція Летті на кавоварку (улюблений подарунок, +20)

init python:
    DIALOGUE_ENTRIES.append({
        "id": "lettie_coffee_machine_react",
        "who": "Летті",
        "conditions": {
            "flag_true": ["gifted_lettie_coffee_machine"],
            "flag_false": ["gift_lettie_coffee_machine_done"],
            "rank_min": 1,
        },
        "priority": 75,
        "chance": 100,
        "label": "lettie_coffee_machine_react",
    })

label lettie_coffee_machine_react:
    show lettie at char_center
    $ store.talked_today.add("Летті")

    le "Зачекай. Сядь."
    $ advance_time(5)

    le "Та кавоварка, що ти приніс."
    $ advance_time(5)

    mc "Сподобалась?"
    $ advance_time(5)

    le "Сподобалась — це м'яко сказано."
    $ advance_time(5)

    le "Я зранку зварила каву. Справжню. Не ту бурду з пакетиків."
    $ advance_time(5)

    le "Перша нормальна кава за... я навіть не пам'ятаю скільки."
    $ advance_time(5)

    mc "Радий, що влучив."
    $ advance_time(5)

    le "Влучив — це не те слово. Ти потрапив точно в ціль."
    $ advance_time(5)

    le "Знаєш, тут мало хто звертає увагу на такі речі."
    $ advance_time(5)

    le "Всі зайняті місіями, зброєю, планами..."
    $ advance_time(5)

    le "А ти помітив, що мені потрібна кава."
    $ advance_time(5)

    mc "Ну, ти п'єш її постійно. Не важко здогадатись."
    $ advance_time(5)

    le "Саме. Ти звернув увагу. Це... приємно."
    $ advance_time(5)

    le "Дякую. Серйозно."
    $ advance_time(5)

    $ set_flag("gift_lettie_coffee_machine_done")
    $ store.seen_dialogues.add("lettie_coffee_machine_react")
    $ add_insight("lettie_coffee_love", "Кавоварка — ідеальний подарунок для Летті. Вона цінує увагу до деталей.")

    hide lettie
    return
