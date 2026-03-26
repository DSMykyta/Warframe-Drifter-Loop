# game/events/gifts/amir_gift_reactions.rpy
# Реакції Аміра на погані подарунки (канцелярія — нудне "навчальне")

# ═══════════════════════════════════════════════
# ПАПКА-БІНДЕР
# ═══════════════════════════════════════════════

init python:
    DIALOGUE_ENTRIES.append({
        "id": "amir_bad_gift_binder",
        "who": "Амір",
        "conditions": {
            "flag_true": ["bad_gift_амір_binder"],
            "flag_false": ["gift_amir_binder_done"],
            "rank_min": 1,
        },
        "priority": 75,
        "chance": 100,
        "label": "amir_bad_gift_binder",
    })

label amir_bad_gift_binder:
    show amir at char_center
    $ store.talked_today.add("Амір")

    am "Е-е, слухай."
    $ advance_time(5)

    am "Та папка, що ти приніс."
    $ advance_time(5)

    mc "Так?"
    $ advance_time(5)

    am "Я її поставив на полицю. Між іншими речами, які я ніколи не відкрию."
    $ advance_time(5)

    mc "Тобі не сподобалось?"
    $ advance_time(5)

    am "Як тобі сказати... Папка — це як подарувати домашнє завдання."
    $ advance_time(5)

    am "Ніби ти кажеш: 'Амір, сядь і будь серйозним'."
    $ advance_time(5)

    am "А я не хочу бути серйозним. Серйозності тут і так вистачає."
    $ advance_time(5)

    mc "Зрозумів. Наступного разу щось цікавіше."
    $ advance_time(5)

    am "О так. Щось з кнопками. Або екраном. Або і тим, і тим."
    $ advance_time(5)

    $ set_flag("gift_amir_binder_done")
    $ store.seen_dialogues.add("amir_bad_gift_binder")
    $ add_insight("amir_boredom", "Амір нудьгує від канцелярії. Він хоче техніку, ігри — щось з кнопками.")

    hide amir
    return


# ═══════════════════════════════════════════════
# БЛОКНОТ
# ═══════════════════════════════════════════════

init python:
    DIALOGUE_ENTRIES.append({
        "id": "amir_bad_gift_notepad",
        "who": "Амір",
        "conditions": {
            "flag_true": ["bad_gift_амір_notepad"],
            "flag_false": ["gift_amir_notepad_done"],
            "rank_min": 1,
        },
        "priority": 75,
        "chance": 100,
        "label": "amir_bad_gift_notepad",
    })

label amir_bad_gift_notepad:
    show amir at char_center
    $ store.talked_today.add("Амір")

    am "Гей. Про блокнот."
    $ advance_time(5)

    mc "Так, що з ним?"
    $ advance_time(5)

    am "Я намалював у ньому кота. На першій сторінці."
    $ advance_time(5)

    am "На другій — ще одного кота. На третій — вибухаючого кота."
    $ advance_time(5)

    mc "...І?"
    $ advance_time(5)

    am "І все. Більше ідей немає. Він мені не потрібен."
    $ advance_time(5)

    am "Я не з тих, хто записує думки. Я з тих, хто грає в ігри о третій ночі."
    $ advance_time(5)

    mc "Ладно, зрозумів натяк."
    $ advance_time(5)

    am "Це не натяк. Це прямий текст. Техніка, друже. Тех-ні-ка."
    $ advance_time(5)

    $ set_flag("gift_amir_notepad_done")
    $ store.seen_dialogues.add("amir_bad_gift_notepad")
    $ add_insight("amir_tech_lover", "Амір відверто каже: йому потрібна техніка, а не канцелярія.")

    hide amir
    return
