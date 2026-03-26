# game/events/missions/eleanor_mission_1.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "eleanor_mission_1",
        "who": "Елеонора",
        "conditions": {
            "flag_true": ["eleanor_intro_done"],
        },
        "priority": 50,
        "label": "eleanor_mission_1",
    })

label eleanor_mission_1:
    el "Зачекай. Дай запам'ятаю розташування."
    mc "Ми посеред бою."
    el "Саме тому. Потім не буде часу фіксувати деталі."
    mc "Ти завжди така?"
    el "Завжди. Деталі рятують життя частіше за кулі."
    return
