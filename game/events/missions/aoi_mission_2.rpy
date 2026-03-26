# game/events/missions/aoi_mission_2.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "aoi_mission_2",
        "who": "Аоі",
        "conditions": {
            "flag_true": ["aoi_intro_done"],
        },
        "priority": 50,
        "label": "aoi_mission_2",
    })

label aoi_mission_2:
    ao "Патруль змінився вісім хвилин тому. Наступна зміна — за чотири."
    mc "Встигнемо?"
    ao "Якщо не зупинятимешся — так."
    mc "Тоді рухаємось."
    ao "Вже рухаюсь. Наздоганяй."
    return
