# game/events/missions/quincy_mission_3.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "quincy_mission_3",
        "who": "Квінсі",
        "conditions": {
            "flag_true": ["quincy_intro_done"],
        },
        "priority": 50,
        "label": "quincy_mission_3",
    })

label quincy_mission_3:
    qu "Гей, Дріфтере. Ти коли-небудь чув про концепцію 'влучити у ціль'?"
    mc "Я влучив!"
    qu "У стіну за два метри від нього — так, влучив. Бездоганно."
    mc "Він все одно впав."
    qu "Від сміху, мабуть."
    return
