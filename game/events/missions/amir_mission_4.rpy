# game/events/missions/amir_mission_4.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "amir_mission_4",
        "who": "Амір",
        "conditions": {
            "flag_true": ["amir_intro_done"],
        },
        "priority": 50,
        "label": "amir_mission_4",
    })

label amir_mission_4:
    am "Окей, класика. Їх більше, вони сильніші. Знаєш, що робити?"
    mc "Тікати?"
    am "Ні! Агрити по одному. Не тягни всю групу — відтягни одного, знищ, повтори."
    mc "Ти це з рейду взяв?"
    am "З рейду, де ми три години вайпалися. Повір, я навчився."
    return
