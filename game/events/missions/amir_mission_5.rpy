# game/events/missions/amir_mission_5.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "amir_mission_5",
        "who": "Амір",
        "conditions": {
            "flag_true": ["amir_intro_done"],
        },
        "priority": 50,
        "label": "amir_mission_5",
    })

label amir_mission_5:
    am "..."
    mc "Аміре? Ти чого замовк?"
    am "Просто думаю. У грі, коли програєш — перезавантажуєшся. А тут..."
    mc "Тут ми не програємо."
    am "Так. Ти правий. Просто... давай будемо уважніші. Без жартів."
    return
