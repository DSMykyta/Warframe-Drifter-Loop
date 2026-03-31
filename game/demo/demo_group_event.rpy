# ═══════════════════════════════════════════════════
# ДЕМО: Групова сцена — 2+ NPC одночасно
# ═══════════════════════════════════════════════════
# Тригериться коли потрібні NPC разом в одній локації.
# Реєструється в DIALOGUE_ENTRIES з chars_at_location умовою.
# Має priority 70+ (вище за звичайні діалоги).
#
# show/hide спрайтів — ВРУЧНУ в label (бо кілька NPC).
# dialogue_begin/end — робить location_loop.

init python:
    DIALOGUE_ENTRIES.append({
        "id": "demo_group_event",
        "who": "Артур",                     # хто "ініціює" (для daily_deck)
        "conditions": {
            "flag_false": ["demo_group_event_done"],
            "chemistry_min": ("Артур", 20),
            "chars_at_location": ["Артур", "Летті"],  # обидва мають бути тут
            "time_from": 1140,              # після 19:00
        },
        "priority": 70,                     # вище за звичайні
        "chance": 50,                       # 50% шанс
        "forced": True,                     # починається автоматично
        "label": "demo_group_event",
    })


label demo_group_event:
    show arthur at left
    show lettie at right

    ar "Летті."
    le "Що."
    ar "Ти ще не їла сьогодні."
    le "Я не голодна."
    ar "Це не було питання."

    menu:
        "Артур правий. Їж.":
            mc "Артур правий. Їж, Летті."
            le "...Добре. Але тільки тому що ви обоє дістали."
            $ add_chemistry("Артур", 2)
            $ add_chemistry("Летті", 2)

        "[Не втручатись.]":
            ar "Летті."
            le "ДОБРЕ."
            $ add_chemistry("Артур", 2)

    $ store.seen_dialogues.add("demo_group_event")
    $ set_flag("demo_group_event_done")
    $ add_journal_entry("Артур змусив Летті поїсти. Вона опиралась.", "event")

    hide arthur
    hide lettie
    return
