# ═══════════════════════════════════════════════════
# ДЕМО: Місійний івент — діалог під час місії
# ═══════════════════════════════════════════════════
# Тригериться під час виконання місії якщо напарник збігається.
# Реєструється в MISSION_DIALOGUE_ENTRIES (НЕ в DIALOGUE_ENTRIES).
# БЕЗ dialogue_begin/end — час рахується місією.
# БЕЗ show/hide — спрайти не потрібні (чорний екран місії).

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "demo_mission_event",
        "who": "Артур",                 # спрацює коли Артур напарник
        "conditions": {
            "flag_false": ["demo_mission_event_done"],
            "chemistry_min": ("Артур", 30),
            "rank_min": 3,              # тільки з рангу 3
        },
        "priority": 50,
        "chance": 75,                   # 75% шанс при кожній місії з Артуром
        "label": "demo_mission_event",
    })


label demo_mission_event:
    # Під час місії — без show, без dialogue_begin
    ar "Стій."

    ar "Щось не так."

    menu:
        "Теж відчуваю.":
            mc "Теж відчуваю. Тихо зліва."
            ar "Хороший слух."
            $ add_chemistry("Артур", 2)

        "Де?":
            mc "Де?"
            ar "Скрізь. Тримай оборону."

    ar "Рухаємось."

    $ store.seen_dialogues.add("demo_mission_event")
    $ set_flag("demo_mission_event_done")
    return
