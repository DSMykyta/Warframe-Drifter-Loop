# game/events/missions/lettie_mission_5.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "lettie_mission_5",
        "who": "Летті",
        "conditions": {
            "flag_true": ["lettie_intro_done"],
        },
        "priority": 50,
        "label": "lettie_mission_5",
    })

label lettie_mission_5:
    le "Гей. Зачекай секунду."
    mc "Що таке?"
    le "Нічого. Просто... будь обережніше, добре? Ти мені потрібен живим."
    mc "Летті, ти що, хвилюєшся за мене?"
    le "Не льсти собі. Мені просто не хочеться заповнювати рапорт про втрати."
    $ set_flag("mission_lettie_showed_concern")
    return
