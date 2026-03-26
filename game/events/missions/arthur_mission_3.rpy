# game/events/missions/arthur_mission_3.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "arthur_mission_3",
        "who": "Артур",
        "conditions": {
            "flag_true": ["arthur_intro_done"],
        },
        "priority": 50,
        "label": "arthur_mission_3",
    })

label arthur_mission_3:
    ar "Меч — це продовження руки. Не зброя, а частина тіла."
    mc "Звучить як філософія."
    ar "Це практика. Коли перестаєш думати про клинок — він починає працювати сам."
    mc "Скільки часу потрібно, щоб дійти до такого?"
    ar "Роки. І багато шрамів."
    return
