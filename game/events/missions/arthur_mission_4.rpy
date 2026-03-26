# game/events/missions/arthur_mission_4.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "arthur_mission_4",
        "who": "Артур",
        "conditions": {
            "flag_true": ["arthur_intro_done"],
        },
        "priority": 50,
        "label": "arthur_mission_4",
    })

label arthur_mission_4:
    ar "Як ти? Поранень немає?"
    mc "Все нормально. Пара подряпин."
    ar "Покажи. ...Добре, нічого серйозного."
    mc "Дякую, що перевірив."
    ar "На місії напарник — це твоє життя. Я своє не кидаю."
    return
