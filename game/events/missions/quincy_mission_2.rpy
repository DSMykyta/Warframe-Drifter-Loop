# game/events/missions/quincy_mission_2.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "quincy_mission_2",
        "who": "Квінсі",
        "conditions": {
            "flag_true": ["quincy_intro_done"],
        },
        "priority": 50,
        "label": "quincy_mission_2",
    })

label quincy_mission_2:
    qu "Бачу... дванадцять. Ні, тринадцять — один за колоною ховається."
    mc "Тринадцять — це багато."
    qu "Для кого? Я вже трьох вичеркнув, поки ти рахував."
    mc "Серйозно?"
    qu "Десять залишилось. Не дякуй."
    return
