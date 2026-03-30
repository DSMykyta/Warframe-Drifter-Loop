# game/events/missions/aoi_mission_1.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "aoi_mission_1",
        "who": "Аоі",
        "conditions": {
        },
        "priority": 50,
        "label": "aoi_mission_1",
    })

label aoi_mission_1:
    ao "Три виходи. Два заблоковані. Один — під питанням."
    mc "Який рекомендуєш?"
    ao "Той, що під питанням. Несподіванка — наша перевага."
    return
