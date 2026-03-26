# game/dialogues/arthur/arthur_friends_milestone.rpy
# MILESTONE: Артур називає гравця справжнім другом

init python:
    DIALOGUE_ENTRIES.append({
        "id": "arthur_friends_milestone",
        "who": "Артур",
        "conditions": {
            "flag_true": ["arthur_trust_milestone_done"],
            "flag_false": ["arthur_friends_milestone_done"],
            "chemistry_min": ("Артур", 120),
        },
        "priority": 85,
        "chance": 100,
        "label": "arthur_friends_milestone",
    })

label arthur_friends_milestone:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    ar "Є хвилина?"
    $ advance_time(5)

    mc "Для тебе — завжди."
    $ advance_time(5)

    ar "Знаєш, я довго думав, як це назвати. Те, що між нами."
    $ advance_time(5)

    ar "Я звик до слів «союзник», «бойовий товариш», «член загону». Це зручні слова. Професійні. Безпечні."
    $ advance_time(5)

    ar "Але ти — не це."
    $ advance_time(5)

    mc "А що тоді?"
    $ advance_time(5)

    ar "Друг."
    $ advance_time(5)

    ar "Справжній друг. Не той, хто просто поруч, бо так склалися обставини. А той, кого я обрав."
    $ advance_time(5)

    ar "Мартін був таким. Після нього... я думав, що більше не зможу. Що це занадто боляче — пускати когось так близько."
    $ advance_time(5)

    ar "Але ти якось пройшов повз усі мої стіни. Навіть не помітив, мабуть."
    $ advance_time(5)

    mc "Або ти сам відчинив двері."
    $ advance_time(5)

    ar "...Можливо. І це лякає. Але вже не так, як раніше."
    $ advance_time(5)

    ar "Дякую. За все."
    $ advance_time(5)

    $ chemistry["Артур"] += 10
    $ store.decay_paused_until = store.day + 2
    $ store.seen_dialogues.add("arthur_friends_milestone")
    $ set_flag("arthur_friends_milestone_done")
    $ add_insight("arthur_true_friend", "Артур назвав Дрифтера справжнім другом — першим після Мартіна. Для нього це величезний крок.")

    hide arthur
    return
