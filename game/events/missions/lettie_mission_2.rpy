# game/events/missions/lettie_mission_2.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "lettie_mission_2",
        "who": "Летті",
        "conditions": {
            "flag_true": ["lettie_intro_done"],
        },
        "priority": 50,
        "label": "lettie_mission_2",
    })

label lettie_mission_2:
    le "О, чудово. Ще один коридор, повний речей, які хочуть нас вбити."
    mc "Ти завжди така оптимістична?"
    le "Це не песимізм. Це статистика."
    mc "І яка статистика?"
    le "Краще тобі не знати. Просто йди за мною і не чіпай нічого блискучого."
    return
