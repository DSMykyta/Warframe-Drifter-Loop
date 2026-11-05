# ═══════════════════════════════════════════════════
# ДЕМО: Banter — фонова репліка при вході в локацію
# ═══════════════════════════════════════════════════
# Одна коротка фраза від NPC при вході в локацію.
# Без menu, без вибору, без хімії. Просто атмосфера.
# Одноразова — після показу зникає назавжди.
#
# Два типи:
# 1. Текстовий (просто text, без label) — одна фраза
# 2. Парний (chars: [2 NPC]) — діалог між двома NPC

init python:
    # ═══ Тип 1: Одиночний текстовий banter ═══
    BANTER_ENTRIES.append({
        "id": "demo_banter_solo",
        "who": "Квінсі",               # хто говорить
        "conditions": {
            "flag_false": ["demo_banter_solo_seen"],
        },
        "location": "range",            # тільки в тирі (None = будь-де)
        "text": "nice shot m8. oh wait that was me",  # текст без label
    })

    # ═══ Тип 2: Парний banter (два NPC) ═══
    BANTER_ENTRIES.append({
        "id": "demo_banter_pair",
        "chars": ["Амір", "Аоі"],       # обидва мають бути в локації
        "conditions": {
            "flag_false": ["demo_banter_pair_seen"],
        },
        "location": "arcade",           # тільки в аркадах
        "label": "demo_banter_pair",    # є label — значить є діалог
    })


label demo_banter_pair:
    show amir at left
    show aoi at right

    am "Я ПОБИВ РЕКОРД!"
    ao "Це мій рекорд, Аміре."
    am "...деталі."

    $ set_flag("demo_banter_pair_seen")
    $ store.seen_dialogues.add("demo_banter_pair")

    hide amir
    hide aoi
    return
