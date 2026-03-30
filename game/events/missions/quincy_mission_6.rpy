# game/events/missions/quincy_mission_6.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "quincy_mission_6",
        "who": "Квінсі",
        "conditions": {
        },
        "priority": 50,
        "label": "quincy_mission_6",
    })

label quincy_mission_6:
    qu "О, ще одна хвиля. Яка несподіванка. Хто б міг подумати."
    mc "Тобі не набридає скаржитись?"
    qu "Мені набридає, що вони такі повільні. Хоч би бігли швидше."
    mc "Ти хочеш, щоб вороги бігли на нас швидше?"
    qu "Хочу, щоб було хоч трохи цікаво. Це ж навіть не розминка."
    return
