# game/events/missions/amir_mission_3.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "amir_mission_3",
        "who": "Амір",
        "conditions": {
            "flag_true": ["amir_intro_done"],
        },
        "priority": 50,
        "label": "amir_mission_3",
    })

label amir_mission_3:
    am "О! Ти бачиш це? Контролери сервоприводів! Ще робочі!"
    mc "Ти серйозно зараз збираєш деталі?"
    am "Ти навіть не уявляєш, що я можу з цього зібрати. Дай мені хвилину."
    mc "Тільки швидко."
    am "Є! Це нам дуже знадобиться. Повір мені."
    $ set_flag("mission_amir_found_components")
    return
