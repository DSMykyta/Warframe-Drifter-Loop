# game/events/missions/quincy_mission_5.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "quincy_mission_5",
        "who": "Квінсі",
        "conditions": {
            "flag_true": ["quincy_intro_done"],
        },
        "priority": 50,
        "label": "quincy_mission_5",
    })

label quincy_mission_5:
    qu "...Слухай."
    mc "Що?"
    qu "Ти прикрив мій фланг, коли я перезаряджав. Більшість не помічають."
    mc "Команда є команда."
    qu "Так. Є. Дякую."
    $ set_flag("mission_quincy_acknowledged_teamwork")
    return
