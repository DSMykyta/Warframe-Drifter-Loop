# game/dialogues/aoi/aoi_origami.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "aoi_origami",
        "who": "Аоі",
        "conditions": {
            "flag_true": ["aoi_intro_done"],
            "flag_false": ["aoi_origami_done"],
            "rank_min": 1,
        },
        "priority": 50,
        "chance": 100,
        "label": "aoi_origami",
    })

label aoi_origami:
    show aoi at char_center
    $ store.talked_today.add("Аоі")

    ao "Одну секунду... ще один згин... ось."
    $ advance_time(5)

    mc "Це журавлик?"
    $ advance_time(5)

    ao "千羽鶴 (Сенбазуру). Тисяча паперових журавликів — і бажання здійсниться. Так каже легенда."
    $ advance_time(5)

    mc "І скільки ти вже склала?"
    $ advance_time(5)

    ao "Тисяча сто вісімдесят три. Але бажання не здійснилося, тож я продовжую."
    $ advance_time(5)

    menu:
        "А яке бажання?":
            $ advance_time(5)
            mc "А яке бажання?"

            ao "Якщо розповісти — воно точно не здійсниться. Але... воно стосується всіх нас."
            $ advance_time(5)
            $ set_flag("aoi_wish_hinted")

        "Можеш навчити мене складати?":
            $ advance_time(5)
            mc "Можеш навчити мене складати?"

            ao "Звісно! Тобі потрібен квадратний аркуш і трішки терпіння. Ходімо, покажу."
            $ advance_time(5)
            $ set_flag("aoi_taught_origami")

    ao "Кожен журавлик — це хвилина спокою. В петлі це дорого коштує."
    $ advance_time(5)

    $ store.seen_dialogues.add("aoi_origami")
    $ set_flag("aoi_origami_done")
    $ add_insight("aoi_origami", "Аоі склала більше тисячі паперових журавликів. Каже — на щастя")

    hide aoi
    return
