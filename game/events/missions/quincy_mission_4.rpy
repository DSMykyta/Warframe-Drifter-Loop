# game/events/missions/quincy_mission_4.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "quincy_mission_4",
        "who": "Квінсі",
        "conditions": {
        },
        "priority": 50,
        "label": "quincy_mission_4",
    })

label quincy_mission_4:
    qu "Паршиве місце для бою. Забагато кутів, замало висоти."
    mc "Для снайпера — так. Для решти нормально."
    qu "Для решти — могила. Без прикриття зверху ви як на долоні."
    mc "Тоді знайди собі точку."
    qu "Вже знайшов. Просто попереджаю, щоб не лізли під мій сектор."
    return
