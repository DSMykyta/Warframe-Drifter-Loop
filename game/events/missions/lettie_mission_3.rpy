# game/events/missions/lettie_mission_3.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "lettie_mission_3",
        "who": "Летті",
        "conditions": {
        },
        "priority": 50,
        "label": "lettie_mission_3",
    })

label lettie_mission_3:
    le "Бачиш оті випари? Токсичні. Не дихай глибоко."
    mc "А як мені тоді дихати?"
    le "Поверхнево і з вдячністю, що я тебе попередила."
    mc "Зрозумів."
    le "І тримайся подалі від тих контейнерів. Витік може бути де завгодно."
    return
