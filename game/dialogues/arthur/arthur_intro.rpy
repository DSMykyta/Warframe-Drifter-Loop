# game/dialogues/arthur/arthur_intro.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "arthur_intro",
        "who": "Артур",
        "conditions": {
            "flag_false": ["arthur_intro_done"],
            "rank_min": 1,
        },
        "priority": 90,
        "chance": 100,
        "label": "arthur_intro",
    })

label arthur_intro:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    ar "Я — Артур, лідер цієї групи."
    $ advance_time(5)

    mc "Як бачиш перший день роботи?"
    $ advance_time(5)

    ar "Спокійно вивчаємо обстановку й не робимо дурниць."
    $ advance_time(5)

    $ store.seen_dialogues.add("arthur_intro")
    $ set_flag("arthur_intro_done")
    $ add_insight("arthur_leader", "Артур — лідер Гексу. Спокійний, обережний.")

    hide arthur
    return
