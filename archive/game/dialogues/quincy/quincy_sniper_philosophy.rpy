# game/dialogues/quincy/quincy_sniper_philosophy.rpy
# Снайперська філософія Квінсі

init python:
    DIALOGUE_ENTRIES.append({
        "id": "quincy_sniper_philosophy",
        "who": "Квінсі",
        "conditions": {
            "flag_true": ["quincy_training_done"],
            "flag_false": ["quincy_sniper_philosophy_done"],
            "rank_min": 2,
            "chemistry_min": ("Квінсі", 45),
        },
        "priority": 50,
        "chance": 100,
        "label": "quincy_sniper_philosophy",
    })

label quincy_sniper_philosophy:
    show quince at char_center
    $ store.talked_today.add("Квінсі")

    "Квінсі чистить гвинтівку. Рухи повільні, ритуальні."
    $ advance_time(5)

    qu "Знаєш, що найважче для снайпера?"
    $ advance_time(5)

    mc "Влучити?"
    $ advance_time(5)

    qu "No. Чекати. Влучити — це фінал. Але до фіналу є години. Іноді — дні."
    $ advance_time(5)

    qu "Ти лежиш. Не рухаєшся. Дихаєш через раз. І дивишся в приціл. One shot, one truth. Приціл не бреше."
    $ advance_time(5)

    mc "One truth?"
    $ advance_time(5)

    qu "Через приціл бачиш людину такою, яка вона є. Без масок. Без bullshit. Вона не знає, що ти дивишся — і тому вона справжня."
    $ advance_time(5)

    qu "Я бачив, як генерали плачуть, коли думають що вони одні. Як солдати танцюють під дощем. Як люди... живуть."
    $ advance_time(5)

    mc "Це зробило тебе терплячим?"
    $ advance_time(5)

    qu "Терплячим — так. Але і самотнім. Снайпер завжди на відстані. Це правило. Ти не можеш бути close — фізично чи emotionally."
    $ advance_time(5)

    qu "Знаєш яке друге правило? Після пострілу — іди. Не оглядайся. Не прив'язуйся."
    $ advance_time(5)

    mc "Але ти ж тут. З нами."
    $ advance_time(5)

    qu "Yeah. Maybe I'm breaking the rules. First time for everything."
    $ advance_time(5)

    $ store.seen_dialogues.add("quincy_sniper_philosophy")
    $ set_flag("quincy_sniper_philosophy_done")
    $ add_insight("quincy_distance", "Снайпер завжди тримає дистанцію — фізичну і емоційну. Квінсі вперше порушує це правило")

    hide quince
    return
