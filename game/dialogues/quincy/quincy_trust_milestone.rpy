# game/dialogues/quincy/quincy_trust_milestone.rpy
# MILESTONE: Квінсі перестає тролити гравця

init python:
    DIALOGUE_ENTRIES.append({
        "id": "quincy_trust_milestone",
        "who": "Квінсі",
        "conditions": {
            "flag_false": ["quincy_trust_milestone_done"],
            "chemistry_min": ("Квінсі", 60),
        },
        "priority": 80,
        "chance": 100,
        "label": "quincy_trust_milestone",
    })

label quincy_trust_milestone:
    show quince at char_center
    $ store.talked_today.add("Квінсі")

    qu "Ey. Маю тобі щось сказати."
    $ advance_time(5)

    mc "Черговий жарт?"
    $ advance_time(5)

    qu "No. Саме в цьому і справа."
    $ advance_time(5)

    "Квінсі стоїть рівно. Без звичної посмішки. Без кута рота, піднятого в сарказмі."
    $ advance_time(5)

    qu "Я тролю всіх. Ти знаєш. Аміра, Летті, навіть Артура коли він не дивиться."
    $ advance_time(5)

    mc "Помітив, так."
    $ advance_time(5)

    qu "Це тест. Завжди був тестом. Я дивлюсь, як люди реагують. Хто сердиться, хто ігнорує, хто грає разом."
    $ advance_time(5)

    qu "Але тебе я більше не хочу тестувати."
    $ advance_time(5)

    mc "Чому?"
    $ advance_time(5)

    qu "Тому що ти — перша людина, з якою мені не треба гратися. Не треба бути смішним, щоб тебе помітили."
    $ advance_time(5)

    qu "Ти просто... бачиш мене. Without the show. І це, mate... це нова territory для мене."
    $ advance_time(5)

    qu "Тож — no more trolling. З тобою. З рештою... well, Амір сам напрошується."
    $ advance_time(5)

    $ chemistry["Квінсі"] += 5

    $ store.seen_dialogues.add("quincy_trust_milestone")
    $ set_flag("quincy_trust_milestone_done")
    $ add_insight("quincy_trust", "Квінсі перестав тролити мене. Каже я перший з ким не треба бути смішним щоб бути поміченим")

    hide quince
    return
