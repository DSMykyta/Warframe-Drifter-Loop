# game/events/missions/lettie_mission_1.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "lettie_mission_1",
        "who": "Летті",
        "conditions": {
            "flag_true": ["lettie_intro_done"],
        },
        "priority": 50,
        "label": "lettie_mission_1",
    })

label lettie_mission_1:
    le "Якщо тебе поранять — кажи одразу. Не грай у героя."
    mc "А якщо не серйозно?"
    le "Я вирішу, серйозно чи ні. Це моя робота."
    return
