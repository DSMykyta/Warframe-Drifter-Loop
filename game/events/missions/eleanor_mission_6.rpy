# game/events/missions/eleanor_mission_6.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "eleanor_mission_6",
        "who": "Елеонора",
        "conditions": {
            "flag_true": ["eleanor_intro_done"],
        },
        "priority": 50,
        "label": "eleanor_mission_6",
    })

label eleanor_mission_6:
    el "За статистикою, найнебезпечніший момент місії — останні п'ять хвилин."
    mc "Чому?"
    el "Люди розслабляються. Думають, що вже все позаду."
    mc "А насправді?"
    el "А насправді позаду тільки те, що ми вже пережили. Попереду — все інше."
    return
