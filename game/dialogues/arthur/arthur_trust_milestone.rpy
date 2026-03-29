# game/dialogues/arthur/arthur_trust_milestone.rpy
# MILESTONE: Артур визнає довіру до гравця

init python:
    DIALOGUE_ENTRIES.append({
        "id": "arthur_trust_milestone",
        "who": "Артур",
        "conditions": {
            "flag_true": ["arthur_intro_done"],
            "flag_false": ["arthur_trust_milestone_done"],
            "chemistry_min": ("Артур", 60),
        },
        "priority": 80,
        "chance": 100,
        "label": "arthur_trust_milestone",
    })

label arthur_trust_milestone:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    ar "Зачекай. Є щось, що я хочу сказати."
    $ advance_time(5)

    ar "Я не кажу цього часто. Взагалі майже ніколи."
    $ advance_time(5)

    mc "Слухаю."
    $ advance_time(5)

    ar "Я тобі довіряю."
    $ advance_time(5)

    ar "Це не просто слова. Для мене довіра — це рішення. Свідоме. І я його прийняв."
    $ advance_time(5)

    ar "Ти довів, що на тебе можна покластися. Не словами — діями."
    $ advance_time(5)

    mc "Дякую, Артуре. Це багато для мене значить."
    $ advance_time(5)

    ar "Не дякуй. Просто... не змушуй мене шкодувати."
    $ advance_time(5)

    $ add_chemistry("Артур", 5)
    $ store.decay_paused_until = store.day + 2
    $ store.seen_dialogues.add("arthur_trust_milestone")
    $ set_flag("arthur_trust_milestone_done")
    $ add_insight("arthur_trusts_player", "Артур офіційно довіряє Дрифтеру. Для нього це свідоме, вагоме рішення.")

    hide arthur
    return
