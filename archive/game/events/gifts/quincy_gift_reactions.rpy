# game/events/gifts/quincy_gift_reactions.rpy
# Реакція Квінсі на поганий подарунок (медична аптечка — натяк на слабкість)

init python:
    DIALOGUE_ENTRIES.append({
        "id": "quincy_bad_gift_medical_kit",
        "who": "Квінсі",
        "conditions": {
            "flag_true": ["bad_gift_quincy_medical_kit"],
            "flag_false": ["gift_quincy_medical_kit_done"],
            "rank_min": 1,
        },
        "priority": 75,
        "chance": 100,
        "label": "quincy_bad_gift_medical_kit",
    })

label quincy_bad_gift_medical_kit:
    show quince at char_center
    $ store.talked_today.add("Квінсі")

    qu "Так. Про твій подарунок."
    $ advance_time(5)

    qu "Аптечка. Ти серйозно приніс мені аптечку."
    $ advance_time(5)

    mc "Я подумав, що може стати в пригоді..."
    $ advance_time(5)

    qu "Стати в пригоді. Мені."
    $ advance_time(5)

    qu "Ти думаєш, я не можу подбати про себе?"
    $ advance_time(5)

    mc "Ні, я не це мав на увазі."
    $ advance_time(5)

    qu "Я пережив речі, про які ти навіть не здогадуєшся."
    $ advance_time(5)

    qu "І кожного разу — сам. Без чиєїсь дурної аптечки."
    $ advance_time(5)

    qu "Не треба мене рятувати. Я не проект."
    $ advance_time(5)

    mc "Зрозумів. Не хотів образити."
    $ advance_time(5)

    qu "..."
    $ advance_time(5)

    qu "Ладно. Проїхали. Тільки не повторюй."
    $ advance_time(5)

    $ set_flag("gift_quincy_medical_kit_done")
    $ store.seen_dialogues.add("quincy_bad_gift_medical_kit")
    $ add_insight("quincy_pride", "Квінсі сприймає аптечку як натяк на слабкість. Він пишається своєю витривалістю.")

    hide quince
    return
