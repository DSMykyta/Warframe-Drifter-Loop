# game/events/missions/arthur_mission_1.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "arthur_mission_1",
        "who": "Артур",
        "conditions": {
            "flag_true": ["arthur_intro_done"],
        },
        "priority": 50,
        "label": "arthur_mission_1",
    })

label arthur_mission_1:
    ar "Тримай дистанцію. Не підставляй спину."
    mc "Зрозуміло."
    ar "І не геройствуй. Герої рідко повертаються."
    return
