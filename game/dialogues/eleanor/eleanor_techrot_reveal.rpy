# game/dialogues/eleanor/eleanor_techrot_reveal.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "eleanor_techrot_reveal",
        "who": "Елеонор",
        "conditions": {
            "flag_true": ["eleanor_techrot_hints_done", "eleanor_journalism_past_done"],
            "flag_false": ["eleanor_techrot_reveal_done"],
            "chemistry_min": ("Елеонор", 70),
            "rank_min": 3,
        },
        "priority": 55,
        "chance": 100,
        "cooldown_tag": "heavy_lore",
        "label": "eleanor_techrot_reveal",
    })

label eleanor_techrot_reveal:
    show eleanor at char_center
    $ store.talked_today.add("Елеонор")

    el "Сядь. Мені треба тобі щось показати."
    $ advance_time(5)

    el "Пам'ятаєш, я розповідала про ІКР? Про міста, що вмирали після їхньої «допомоги»?"
    $ advance_time(5)

    mc "Технологічний занепад. Ти казала — як іржа."
    $ advance_time(5)

    el "Я знайшла назву. Те, що робить це з технологією — називається Техрот."
    $ advance_time(5)

    el "Не вірус. Не зброя. Щось... інше. Воно поводиться як хвороба, але вражає не людей — а все, до чого люди торкаються."
    $ advance_time(5)

    mc "Як це можливо?"
    $ advance_time(5)

    el "Я провела місяці, зіставляючи дані. Карти поширення, хронологію, звіти аварійних служб. І побачила патерн."
    $ advance_time(5)

    el "Техрот не поширюється випадково. Він іде маршрутами. Як вода по руслах. Від вузла до вузла."
    $ advance_time(5)

    el "І вузли — це завжди місця, де ІКР встановлювала свої «ретранслятори допомоги»."
    $ advance_time(5)

    mc "Ти хочеш сказати, що ІКР навмисно—"
    $ advance_time(5)

    el "Я не знаю. Може, вони не розуміли, що робили. Може, розуміли і їм було байдуже. А може..."
    $ advance_time(5)

    el "Може, Техрот — це не побічний ефект. А мета."
    $ advance_time(5)

    el "Я знаю, як це звучить. Параноя журналістки, яка бачить змови скрізь. Але патерни не брешуть."
    $ advance_time(5)

    mc "Що ще ти знаєш?"
    $ advance_time(5)

    el "Техрот прискорюється. Раніше місту потрібен був рік, щоб впасти. Зараз — тижні. Щось змінилось. І мене це лякає більше за все інше."
    $ advance_time(5)

    $ store.seen_dialogues.add("eleanor_techrot_reveal")
    $ set_flag("eleanor_techrot_reveal_done")
    $ add_insight("techrot_pattern", "Техрот поширюється маршрутами ІКР-ретрансляторів. Елеонор вважає — це може бути не випадковість, а мета. І він прискорюється.")

    hide eleanor
    return
