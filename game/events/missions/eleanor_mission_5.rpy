# game/events/missions/eleanor_mission_5.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "eleanor_mission_5",
        "who": "Елеонора",
        "conditions": {
        },
        "priority": 50,
        "label": "eleanor_mission_5",
    })

label eleanor_mission_5:
    el "Стій. Бачиш ту панель на стіні?"
    mc "Звичайний термінал. Що з ним?"
    el "Він увімкнений. А живлення в цьому секторі вирубали годину тому."
    mc "Автономне джерело?"
    el "Або хтось підключив його навмисно. Нам варто це запам'ятати."
    $ set_flag("mission_eleanor_noticed_detail")
    return
