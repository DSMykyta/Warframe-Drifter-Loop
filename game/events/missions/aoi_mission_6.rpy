# game/events/missions/aoi_mission_6.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "aoi_mission_6",
        "who": "Аоі",
        "conditions": {
            "flag_true": ["aoi_intro_done"],
        },
        "priority": 50,
        "label": "aoi_mission_6",
    })

label aoi_mission_6:
    ao "Знаєш, що спільного між тінню і нами?"
    mc "Що?"
    ao "Тінь не існує без світла. А ми — без того, проти чого боремось."
    mc "Це... несподівано глибоко для середини місії."
    ao "Найкращий час для роздумів — коли смерть поруч."
    return
