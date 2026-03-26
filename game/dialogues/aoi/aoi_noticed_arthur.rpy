# game/dialogues/aoi/aoi_noticed_arthur.rpy
# Аоі помічає що Артур відкрився гравцю

init python:
    DIALOGUE_ENTRIES.append({
        "id": "aoi_noticed_arthur",
        "who": "Аоі",
        "conditions": {
            "flag_true": ["arthur_skana_story_told"],
            "flag_false": ["aoi_noticed_arthur_opening_done"],
            "chemistry_min": ("Аоі", 30),
        },
        "priority": 25,
        "chance": 60,
        "label": "aoi_noticed_arthur",
    })

label aoi_noticed_arthur:
    show aoi at char_center
    $ store.talked_today.add("Аоі")

    ao "Ей."
    $ advance_time(5)

    mc "Так?"
    $ advance_time(5)

    ao "Артур. Він говорив з тобою. По-справжньому говорив."
    $ advance_time(5)

    mc "Ти помітила?"
    $ advance_time(5)

    ao "Я завжди помічаю. Він не розмовляв так з нікім вже роками. Буквально — роками."
    $ advance_time(5)

    ao "Що б ти не зробив — продовжуй."
    $ advance_time(5)

    "Аоі надягає навушники і відвертається. Розмова закінчена."
    $ advance_time(5)

    $ store.seen_dialogues.add("aoi_noticed_arthur")
    $ set_flag("aoi_noticed_arthur_opening_done")
    $ add_insight("aoi_observes_arthur", "Аоі помітила що Артур відкрився. Каже він так не робив роками")

    hide aoi
    return
