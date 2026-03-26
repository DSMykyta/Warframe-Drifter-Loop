# game/events/missions/quincy_mission_1.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "quincy_mission_1",
        "who": "Квінсі",
        "conditions": {
            "flag_true": ["quincy_intro_done"],
        },
        "priority": 50,
        "label": "quincy_mission_1",
    })

label quincy_mission_1:
    qu "Один постріл — один труп. Класика."
    mc "Можеш не коментувати кожне вбивство?"
    qu "Можу. Але тоді мені буде нудно, а нудний снайпер — поганий снайпер."
    mc "...Коментуй."
    return
