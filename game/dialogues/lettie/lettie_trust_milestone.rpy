# game/dialogues/lettie/lettie_trust_milestone.rpy
# MILESTONE: Летті визнає, що гравець "не зовсім безнадійний"

init python:
    DIALOGUE_ENTRIES.append({
        "id": "lettie_trust_milestone",
        "who": "Летті",
        "conditions": {
            "flag_false": ["lettie_trust_milestone_done"],
            "rank_min": 2,
            "chemistry_min": ("Летті", 60),
        },
        "priority": 80,
        "chance": 100,
        "label": "lettie_trust_milestone",
    })

label lettie_trust_milestone:
    show letty at char_center
    $ store.talked_today.add("Летті")

    le "Гей. Сядь."
    $ advance_time(5)

    mc "Щось трапилось?"
    $ advance_time(5)

    le "Ні. Просто... Мені треба дещо сказати, і я скажу це рівно один раз. Тож слухай."
    $ advance_time(5)

    le "Я звикла працювати одна. Мій медвідсік, мої правила, мої щури. Решта — пацієнти. Прийшли, вилікувались, пішли."
    $ advance_time(5)

    mc "А я?"
    $ advance_time(5)

    le "Ти... не зовсім безнадійний. Не кажи нікому, що я це сказала."
    $ advance_time(5)

    le "Ти приходиш не тільки коли болить. Ти приходиш поговорити. Ніхто цього не робить. Навіть Аоі обходить медвідсік, якщо не мусить."
    $ advance_time(5)

    menu:
        "Мені подобається з тобою розмовляти.":
            $ advance_time(5)
            mc "Мені подобається з тобою розмовляти."
            le "...Не перестарайся. Я вже й так сказала більше, ніж планувала."
            $ advance_time(5)

        "Ти теж не безнадійна, Летті.":
            $ advance_time(5)
            mc "Ти теж не безнадійна, Летті."
            le "Хм. Прийнятна відповідь. Не ідеальна, але прийнятна."
            $ advance_time(5)

    le "Ладно. Цей момент закінчився. Повертаємось до нормального режиму, де я сварлива і ти мовчиш."
    $ advance_time(5)

    le "...Але дякую. Що приходиш."
    $ advance_time(5)

    $ chemistry["Летті"] += 5

    $ store.seen_dialogues.add("lettie_trust_milestone")
    $ set_flag("lettie_trust_milestone_done")
    $ add_insight("lettie_trust", "Летті сказала що гравець не зовсім безнадійний — для неї це майже зізнання в дружбі")

    hide letty
    return
