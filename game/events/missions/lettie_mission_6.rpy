# game/events/missions/lettie_mission_6.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "lettie_mission_6",
        "who": "Летті",
        "conditions": {
            "flag_true": ["lettie_intro_done"],
        },
        "priority": 50,
        "label": "lettie_mission_6",
    })

label lettie_mission_6:
    le "Знаєш, яка різниця між нами і тими Грінір?"
    mc "Ми розумніші?"
    le "Ні. Ми просто ще не вмерли. Поки що."
    mc "Дуже надихаюче, Летті."
    le "Я медик, а не мотиваційний спікер. Тримай голову нижче."
    return
