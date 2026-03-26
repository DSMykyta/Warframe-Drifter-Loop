# game/events/missions/amir_mission_2.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "amir_mission_2",
        "who": "Амір",
        "conditions": {
            "flag_true": ["amir_intro_done"],
        },
        "priority": 50,
        "label": "amir_mission_2",
    })

label amir_mission_2:
    am "Зачекай. Бачиш ту панель? Вона ще під напругою."
    mc "І що?"
    am "Якщо перенаправити живлення, можна вирубити їм освітлення в сусідньому відсіку."
    mc "Дій."
    am "Готово. Тепер вони сліпі, а ми — ні. Люблю технологічну перевагу."
    return
