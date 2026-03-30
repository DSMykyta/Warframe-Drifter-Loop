# game/events/group/rooftop_stargazing.rpy
# Групова сцена: спостереження за зірками на даху

init python:
    DIALOGUE_ENTRIES.append({
        "id": "rooftop_stargazing",
        "who": "Аоі",
        "conditions": {
            "flag_false": ["group_rooftop_stargazing_done"],
            "location": "rooftop",
            "chars_at_location": ["Аоі", "Елеонор"],
            "rank_min": 1,
            "time_from": 1260,  # після 21:00
        },
        "priority": 70,
        "chance": 50,
        "label": "rooftop_stargazing",
    })

label rooftop_stargazing:
    $ store.talked_today.add("Аоі")
    $ store.talked_today.add("Елеонор")

    show aoi at left
    show eleanor at right

    ao "Тихо тут. Добре."
    $ advance_time(5)

    el "Погоджуюсь. Рідко буває так спокійно."
    $ advance_time(5)

    mc "Що ви тут робите?"
    $ advance_time(5)

    ao "Дивлюсь на зірки. Намагаюсь знайти Орігон."
    $ advance_time(5)

    el "Я записую. Якого кольору небо о різних годинах. Це... заспокоює."
    $ advance_time(5)

    menu:
        "Сісти поруч і дивитись":
            $ advance_time(5)
            mc "Можна з вами?"

            ao "Місця вистачить."
            $ advance_time(5)

            el "Тільки тихо."
            $ advance_time(5)

            "Ви сидите втрьох на даху. Вітер несе запах іржі та далекого дощу."
            $ advance_time(10)

            ao "Ось. Та зірка. Бачиш?"
            $ advance_time(5)

            mc "Яскрава."
            $ advance_time(5)

            el "Вона завжди там. Навіть коли все інше змінюється."
            $ advance_time(5)

            ao "Тому і дивлюсь."
            $ advance_time(5)

            $ add_chemistry("Аоі", 2)
            $ add_chemistry("Елеонор", 2)

        "Запитати про сузір'я":
            $ advance_time(5)
            mc "Орігон — це яке сузір'я?"

            ao "Не знаю чи воно існує тут. Але шукаю все одно."
            $ advance_time(5)

            el "Може, ти його вигадала?"
            $ advance_time(5)

            ao "Може. Це не заважає шукати."
            $ advance_time(5)

            el "...Гарна думка. Запишу."
            $ advance_time(5)

            $ add_chemistry("Аоі", 2)
            $ add_chemistry("Елеонор", 2)

    $ store.seen_dialogues.add("rooftop_stargazing")
    $ set_flag("group_rooftop_stargazing_done")
    $ add_insight("aoi_stars", "Аоі шукає сузір'я Орігон на даху вночі. Не впевнена, чи воно існує.")

    hide aoi
    hide eleanor
    return
