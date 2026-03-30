# game/events/missions/lettie_mission_4.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "lettie_mission_4",
        "who": "Летті",
        "conditions": {
        },
        "priority": 50,
        "label": "lettie_mission_4",
    })

label lettie_mission_4:
    le "Вологість тут запредельна. Мої інструменти іржавіють просто від повітря."
    mc "Може, відкладемо?"
    le "Ні. Ми вже тут. Я просто буду скаржитись і одночасно рятувати тобі життя."
    mc "Звучить як план."
    le "Звучить як моя щоденна рутина."
    return
