# game/events/missions/aoi_mission_4.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "aoi_mission_4",
        "who": "Аоі",
        "conditions": {
            "flag_true": ["aoi_intro_done"],
        },
        "priority": 50,
        "label": "aoi_mission_4",
    })

label aoi_mission_4:
    ao "Зачекай. Бачиш оту вентиляційну решітку?"
    mc "Ту, за контейнерами?"
    ao "Так. Вона веде в обхід. Повз усю охорону."
    mc "Гарний око."
    ao "Просто звичка — дивитись туди, куди інші не дивляться."
    $ set_flag("mission_aoi_found_passage")
    return
