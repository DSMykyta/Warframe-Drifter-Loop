# game/events/missions/amir_mission_6.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "amir_mission_6",
        "who": "Амір",
        "conditions": {
            "flag_true": ["amir_intro_done"],
        },
        "priority": 50,
        "label": "amir_mission_6",
    })

label amir_mission_6:
    am "Гей, а знаєш, як називається наша тактика?"
    mc "Яка тактика?"
    am "Заходимо без плану, імпровізуємо, якось виживаємо. В іграх це називається 'спідран'."
    mc "А в реальності?"
    am "В реальності це називається 'щасливчики'. Але мені подобається перша назва більше."
    return
