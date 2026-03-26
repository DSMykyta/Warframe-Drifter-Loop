# game/dialogues/aoi/aoi_icr_past.rpy
# Аоі натякає на своє минуле в ICR

init python:
    DIALOGUE_ENTRIES.append({
        "id": "aoi_icr_past",
        "who": "Аоі",
        "conditions": {
            "flag_true": ["aoi_intro_done", "aoi_origami_done"],
            "flag_false": ["aoi_icr_past_done"],
            "rank_min": 2,
            "chemistry_min": ("Аоі", 40),
        },
        "priority": 50,
        "chance": 100,
        "label": "aoi_icr_past",
    })

label aoi_icr_past:
    show aoi at char_center
    $ store.talked_today.add("Аоі")

    "Аоі сидить на підлозі. Навколо неї — десятки паперових журавликів. Її рухи механічні, але точні."
    $ advance_time(5)

    ao "О. Привіт. Вибач, я... рахую."
    $ advance_time(5)

    mc "Скільки вже?"
    $ advance_time(5)

    ao "Дев'ятсот вісімдесят сім. Кожен журавлик — це хвилина, яку я не думаю про те, що було раніше."
    $ advance_time(5)

    mc "Що було раніше?"
    $ advance_time(5)

    ao "..."
    $ advance_time(5)

    ao "Тисяча журавликів — і бажання здійсниться. Сенбазуру. Ти вже знаєш."
    $ advance_time(5)

    mc "Ти казала, що бажання завжди одне й те саме."
    $ advance_time(5)

    ao "Так. Забути. Завжди — забути."
    $ advance_time(5)

    "Її пальці зупиняються на мить. Потім продовжують складати."
    $ advance_time(5)

    ao "Є речі, які не варто знати про людей. Те, що вони справді думають. Те, що вони планують, коли посміхаються."
    $ advance_time(5)

    ao "Я колись працювала з людьми, які спеціалізувалися на знанні таких речей. І... я навчилася занадто добре."
    $ advance_time(5)

    mc "Хто ці люди?"
    $ advance_time(5)

    ao "Може, колись розкажу. Коли журавликів стане достатньо."
    $ advance_time(5)

    ao "А поки що... просто посидь тут. Мовчки. Це допомагає більше, ніж ти думаєш."
    $ advance_time(5)

    $ store.seen_dialogues.add("aoi_icr_past")
    $ set_flag("aoi_icr_past_done")
    $ add_insight("aoi_past", "Аоі натякає на минуле — працювала з людьми які знали чужі секрети. Складає журавликів щоб забути")

    hide aoi
    return
