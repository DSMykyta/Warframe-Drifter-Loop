# game/events/missions/eleanor_mission_3.rpy

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "eleanor_mission_3",
        "who": "Елеонора",
        "conditions": {
        },
        "priority": 50,
        "label": "eleanor_mission_3",
    })

label eleanor_mission_3:
    el "Пропоную обійти зліва. Там мертва зона для їхніх сенсорів."
    mc "Звідки ти знаєш про мертву зону?"
    el "Рахую інтервали між патрулями. Є проміжок у двадцять секунд."
    mc "Двадцять секунд — це мало."
    el "Достатньо, якщо не зупинятися."
    return
