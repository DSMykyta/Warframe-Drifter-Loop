# game/dialogues/eleanor/eleanor_control_issues.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "eleanor_control_issues",
        "who": "Елеонор",
        "conditions": {
            "flag_true": ["eleanor_control_done"],
            "flag_false": ["eleanor_control_issues_done"],
            "chemistry_min": ("Елеонор", 60),
            "rank_min": 3,
        },
        "priority": 50,
        "chance": 100,
        "label": "eleanor_control_issues",
    })

label eleanor_control_issues:
    show eleanor at char_center
    $ store.talked_today.add("Елеонор")

    el "Ти коли-небудь замислювався, чому я така? З розкладами. З контролем."
    $ advance_time(5)

    mc "Ти казала — тривога. Списки того, що може піти не так."
    $ advance_time(5)

    el "Це верхній шар. Справжня причина... глибше."
    $ advance_time(5)

    el "Уяви: ти заходиш в кімнату — і чуєш кожну думку кожної людини. Одночасно. Без паузи. Без кнопки «вимкнути»."
    $ advance_time(5)

    el "Страх, роздратування, біль, голод, сум, злість — все це не твоє, але звучить як твоє."
    $ advance_time(5)

    el "Контроль — це мій спосіб не потонути. Якщо зовні все впорядковано — всередині трохи тихіше."
    $ advance_time(5)

    mc "Тобто розклади, списки — це як стіна між тобою і чужими думками?"
    $ advance_time(5)

    el "Саме так. Тонка, крихка стіна. Але краще, ніж нічого."
    $ advance_time(5)

    menu:
        "Я можу допомогти тримати цю стіну.":
            $ advance_time(5)
            mc "Я можу допомогти тримати цю стіну."
            el "...Ти серйозно?"
            $ advance_time(5)
            el "Ніхто раніше не пропонував. Усі просто казали «відпусти» або «навчись жити з цим». Ніби я не намагаюсь щодня."
            $ advance_time(5)
            $ add_chemistry("Елеонор", 2)
            $ set_flag("eleanor_wall_supported")

        "Може, проблема не в контролі, а в тому, що ти несеш це сама?":
            $ advance_time(5)
            mc "Може, проблема не в контролі, а в тому, що ти несеш це сама?"
            el "Ти кажеш це так, ніби є альтернатива. Хто ще візьме на себе чужий шум?"
            $ advance_time(5)
            el "Хоча... сам факт, що хтось запитує — вже полегшення. Дивно, правда?"
            $ advance_time(5)

        "Гучні місця, мабуть, для тебе — пекло.":
            $ advance_time(5)
            mc "Гучні місця, мабуть, для тебе — пекло."
            el "Не «мабуть». Точно. Базар, натовп, навіть коли команда збирається разом — це як стояти під водоспадом думок."
            $ advance_time(5)
            el "Тому я часто йду першою. Не тому що нетерплячка — просто не витримую довше."
            $ advance_time(5)
            $ set_flag("eleanor_sensory_revealed")

    el "Дякую. Що слухаєш. Що не кажеш «просто перестань»."
    $ advance_time(5)

    $ store.seen_dialogues.add("eleanor_control_issues")
    $ set_flag("eleanor_control_issues_done")
    $ add_insight("eleanor_control_defense", "Контроль для Елеонор — захисний механізм від хаосу чужих думок. Без нього вона тоне у ментальному шумі.")

    hide eleanor
    return
