# game/events/missions/arthur_mission_6.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "arthur_mission_6",
        "who": "Артур",
        "conditions": {
            "flag_true": ["arthur_intro_done"],
        },
        "priority": 50,
        "label": "arthur_mission_6",
    })

label arthur_mission_6:
    ar "Тихо тут. Занадто тихо."
    mc "Може, ми їх уже зачистили?"
    ar "Ні. Подивись на стіни — сліди від вибухів старі. Тут давно ніхто не живе."
    mc "Тоді хто включив освітлення?"
    ar "Саме це мене і турбує."
    $ add_insight("arthur_area_observation", "Артур помітив: хтось підтримує системи в покинутих секторах")
    return
