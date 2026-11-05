# game/dialogues/arthur/arthur_rank1_deep_reg.rpy
# Реєстрація ArthurRank1Convo1 в condition-based системі.
# Сам діалог залишається в ArthurRank1Convo1.rpy (без змін label/jump структури).

init python:
    DIALOGUE_ENTRIES.append({
        "id": "arthur_rank1_deep",
        "who": "Артур",
        "conditions": {
            "flag_false": ["arthur_rank1_deep_done"],
            "rank_min": 1,
        },
        "priority": 50,
        "chance": 100,
        "label": "ArthurRank1Convo1",
    })
