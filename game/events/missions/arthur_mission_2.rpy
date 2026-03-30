# game/events/missions/arthur_mission_2.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "arthur_mission_2",
        "who": "Артур",
        "conditions": {
        },
        "priority": 50,
        "label": "arthur_mission_2",
    })

label arthur_mission_2:
    ar "Бачиш, як вони перегруповуються? Завжди трійками."
    mc "Я думав, це випадковість."
    ar "Ніколи не випадковість. Вони координуються — хтось ними керує."
    mc "Тоді треба шукати командира."
    ar "Саме так. Зніми голову — тіло впаде."
    return
