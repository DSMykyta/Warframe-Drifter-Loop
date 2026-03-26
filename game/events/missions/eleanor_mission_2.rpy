# game/events/missions/eleanor_mission_2.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "eleanor_mission_2",
        "who": "Елеонора",
        "conditions": {
            "flag_true": ["eleanor_intro_done"],
        },
        "priority": 50,
        "label": "eleanor_mission_2",
    })

label eleanor_mission_2:
    el "Цікаво. Вони не атакують одночасно — чергуються."
    mc "І що це значить?"
    el "Що це не звірі. Звірі кидаються зграєю. А ці — чекають своєї черги."
    mc "Тобто в них є дисципліна."
    el "Або хтось, хто її насаджує."
    return
