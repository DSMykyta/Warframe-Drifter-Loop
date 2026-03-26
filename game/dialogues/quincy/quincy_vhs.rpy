# game/dialogues/quincy/quincy_vhs.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "quincy_vhs",
        "who": "Квінсі",
        "conditions": {
            "flag_true": ["quincy_intro_done"],
            "flag_false": ["quincy_vhs_done"],
            "rank_min": 1,
        },
        "priority": 45,
        "chance": 100,
        "label": "quincy_vhs",
    })

label quincy_vhs:
    show quince at char_center
    $ store.talked_today.add("Квінсі")

    qu "...Ти нічого не бачив. Clear?"
    $ advance_time(5)

    mc "Ти дивився 'Circle of Comrades'?"
    $ advance_time(5)

    qu "No. Absolutely not. Я просто... перевіряв чи працює відеомагнітофон."
    $ advance_time(5)

    mc "На екрані досі пауза на сцені з визнанням у дружбі."
    $ advance_time(5)

    qu "...Fk off. Це... це іронічний перегляд. Я дивлюсь це іронічно. Серіал — rubbish."
    $ advance_time(5)

    mc "Тоді чому касета так затерта? Ти її явно дивився не раз."
    $ advance_time(5)

    qu "...Right. Може, я переглядав це кілька разів. Може, п'ятнадцять. Але якщо ти комусь розкажеш — especially Аоі — I swear, mate."
    $ advance_time(5)

    $ store.seen_dialogues.add("quincy_vhs")
    $ set_flag("quincy_vhs_done")
    $ add_insight("quincy_vhs", "Квінсі дивиться 'Circle of Comrades' на VHS. Не признається але це його улюблений серіал")

    hide quince
    return
