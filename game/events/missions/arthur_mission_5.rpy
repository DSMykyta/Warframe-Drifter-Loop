# game/events/missions/arthur_mission_5.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "arthur_mission_5",
        "who": "Артур",
        "conditions": {
            "flag_true": ["arthur_intro_done"],
        },
        "priority": 50,
        "label": "arthur_mission_5",
    })

label arthur_mission_5:
    ar "...Непогано."
    mc "Що?"
    ar "Той фланговий маневр. Чисто, швидко, без зайвих рухів."
    mc "Ти мене хвалиш?"
    ar "Констатую факт. Не звикай."
    $ set_flag("mission_arthur_praised")
    return
