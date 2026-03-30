# game/events/missions/aoi_mission_5.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "aoi_mission_5",
        "who": "Аоі",
        "conditions": {
        },
        "priority": 50,
        "label": "aoi_mission_5",
    })

label aoi_mission_5:
    ao "...Непогано."
    mc "Що саме?"
    ao "Твій рух. Тихий. Точний. Раніше ти був гучнішим."
    mc "Вчуся у кращих."
    ao "Хм. Не підлещуйся. Але... дякую."
    return
