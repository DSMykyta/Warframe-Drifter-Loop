# game/events/missions/aoi_mission_3.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "aoi_mission_3",
        "who": "Аоі",
        "conditions": {
            "flag_true": ["aoi_intro_done"],
        },
        "priority": 50,
        "label": "aoi_mission_3",
    })

label aoi_mission_3:
    ao "Шестеро зліва. Двоє — з важким озброєнням. Решта — стандартні."
    mc "Пропозиції?"
    ao "Важких зняти першими. Тихо. Решта розгубиться без підтримки."
    mc "Приймаю."
    return
