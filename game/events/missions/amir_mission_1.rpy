# game/events/missions/amir_mission_1.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "amir_mission_1",
        "who": "Амір",
        "conditions": {
        },
        "priority": 50,
        "label": "amir_mission_1",
    })

label amir_mission_1:
    am "Оце планування рівня... Довгий коридор, укриття по боках — класичний шутер."
    mc "Це не гра, Аміре."
    am "Я знаю. Але якби це була гра, попереду точно був би міні-бос."
    mc "І що ти пропонуєш?"
    am "Перевірити за тим кутом, перш ніж бігти вперед. У іграх це завжди працює."
    return
