# game/dialogues/eleanor/eleanor_control.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "eleanor_control",
        "who": "Елеонор",
        "conditions": {
            "flag_true": ["eleanor_journalism_done"],
            "flag_false": ["eleanor_control_done"],
            "rank_min": 1,
            "chemistry_min": ("Елеонор", 15),
        },
        "priority": 50,
        "chance": 100,
        "label": "eleanor_control",
    })

label eleanor_control:
    show eleanor at char_center
    $ store.talked_today.add("Елеонор")

    el "Я переписала розклад чергувань. Втретє за тиждень."
    $ advance_time(5)

    mc "Щось було не так з попереднім?"
    $ advance_time(5)

    el "Ні. Просто... він міг бути кращим. Ефективнішим. Я знайшла три хвилини, які можна оптимізувати."
    $ advance_time(5)

    mc "Три хвилини?"
    $ advance_time(5)

    el "Не смійся. Три хвилини — це різниця між порядком і хаосом."
    $ advance_time(5)

    el "Якщо я не контролюю деталі — все починає розсипатися. У голові стає... голосно."
    $ advance_time(5)

    mc "Голосно?"
    $ advance_time(5)

    el "Думки. Тривога. Що може піти не так. Список росте, поки я не візьму все під контроль."
    $ advance_time(5)

    menu:
        "Це нормально — хвилюватись. Але ти не мусиш нести все сама.":
            $ advance_time(5)
            mc "Це нормально — хвилюватись. Але ти не мусиш нести все сама."
            el "...Я знаю. Теоретично. На практиці — якщо не я, то хто?"
            $ advance_time(5)
            $ set_flag("eleanor_comforted")

        "Може, тобі варто відпустити контроль хоча б на день?":
            $ advance_time(5)
            mc "Може, тобі варто відпустити контроль хоча б на день?"
            el "Ти кажеш це так, ніби я можу просто вимкнути це. Повір, я пробувала."
            $ advance_time(5)
            el "Останній раз, коли я \"відпустила\" — я не спала три ночі, бо не могла перестати думати про все, що може зламатись."
            $ advance_time(5)

    el "Дякую, що слухаєш. Артур каже, мені треба більше говорити про це."
    $ advance_time(5)

    $ store.seen_dialogues.add("eleanor_control")
    $ set_flag("eleanor_control_done")
    $ add_insight("eleanor_control", "Елеонор тримає все під контролем бо інакше тривога бере верх")

    hide eleanor
    return
