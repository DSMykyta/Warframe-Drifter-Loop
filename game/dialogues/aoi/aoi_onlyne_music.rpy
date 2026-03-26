# game/dialogues/aoi/aoi_onlyne_music.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "aoi_onlyne_music",
        "who": "Аоі",
        "conditions": {
            "flag_true": ["aoi_intro_done"],
            "flag_false": ["aoi_onlyne_music_done"],
            "rank_min": 1,
        },
        "priority": 45,
        "chance": 100,
        "label": "aoi_onlyne_music",
    })

label aoi_onlyne_music:
    show aoi at char_center
    $ store.talked_today.add("Аоі")

    ao "♪ ...connected to the void, we are on-lyne... ♪"
    $ advance_time(5)

    mc "Що це за пісня?"
    $ advance_time(5)

    ao "On-Lyne! Найкращий гурт у всесвіті. Ти серйозно не чув?!"
    $ advance_time(5)

    ao "Вони грали синт-поп з елементами орокінської акустики. Я знаю кожну пісню напам'ять. Кожну!"
    $ advance_time(5)

    mc "Де ти їх слухаєш? Тут же нема інтернету."
    $ advance_time(5)

    ao "Знайшла стару касету в музичному магазині. Тепер це мій найцінніший скарб. Квінсі каже, що я одержима. А я кажу — він просто не розуміє мистецтва."
    $ advance_time(5)

    ao "Музика — це єдине, що робить петлю стерпною. Без неї тут тільки тиша і скрип молу."
    $ advance_time(5)

    $ store.seen_dialogues.add("aoi_onlyne_music")
    $ set_flag("aoi_onlyne_music_done")
    $ add_insight("aoi_onlyne", "Аоі фанатіє від On-Lyne. Знає всі їхні пісні напам'ять")

    hide aoi
    return
