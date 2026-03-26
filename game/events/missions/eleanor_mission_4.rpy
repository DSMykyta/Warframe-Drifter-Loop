# game/events/missions/eleanor_mission_4.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "eleanor_mission_4",
        "who": "Елеонора",
        "conditions": {
            "flag_true": ["eleanor_intro_done"],
        },
        "priority": 50,
        "label": "eleanor_mission_4",
    })

label eleanor_mission_4:
    el "Знаєш, що найцінніше на полі бою?"
    mc "Зброя? Боєприпаси?"
    el "Інформація. Той, хто знає більше — стріляє менше."
    mc "Красиво сказано."
    el "Це не краса. Це статистика виживання."
    return
