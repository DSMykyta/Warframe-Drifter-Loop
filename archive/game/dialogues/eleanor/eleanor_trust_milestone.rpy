# game/dialogues/eleanor/eleanor_trust_milestone.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "eleanor_trust_milestone",
        "who": "Елеонор",
        "conditions": {
            "flag_false": ["eleanor_trust_milestone_done"],
            "chemistry_min": ("Елеонор", 60),
        },
        "priority": 80,
        "chance": 100,
        "label": "eleanor_trust_milestone",
    })

label eleanor_trust_milestone:
    show eleanor at char_center
    $ store.talked_today.add("Елеонор")

    el "Зачекай. Перш ніж ти щось скажеш — я маю тобі дещо сказати."
    $ advance_time(5)

    mc "Що таке?"
    $ advance_time(5)

    el "Я читала твої думки. З першого дня. Кожного разу, коли ми розмовляли — я знала, що ти думаєш насправді."
    $ advance_time(5)

    mc "..."
    $ advance_time(5)

    el "Не ображайся. Це не вибір — це як дихання. Я не можу просто «не чути»."
    $ advance_time(5)

    el "Але з тобою... Я вирішила спробувати. Зупинитись. Не слухати."
    $ advance_time(5)

    mc "Чому?"
    $ advance_time(5)

    el "Бо ти заслуговуєш на приватність. Бо довіра — це коли ти чекаєш, поки людина скаже сама. Навіть якщо можеш дізнатись раніше."
    $ advance_time(5)

    el "Це... складно. Як затуляти вуха під час концерту. Але я хочу спробувати. Для тебе."
    $ advance_time(5)

    $ add_chemistry("Елеонор", 5)

    $ store.seen_dialogues.add("eleanor_trust_milestone")
    $ set_flag("eleanor_trust_milestone_done")
    $ add_insight("eleanor_respects_privacy", "Елеонор свідомо перестала читати мої думки. Для неї це величезне зусилля — і знак довіри.")

    hide eleanor
    return
