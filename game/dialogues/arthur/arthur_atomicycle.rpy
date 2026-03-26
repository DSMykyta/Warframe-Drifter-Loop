# game/dialogues/arthur/arthur_atomicycle.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "arthur_atomicycle",
        "who": "Артур",
        "conditions": {
            "flag_true": ["arthur_intro_done"],
            "flag_false": ["arthur_atomicycle_done"],
            "rank_min": 1,
        },
        "priority": 45,
        "chance": 100,
        "label": "arthur_atomicycle",
    })

label arthur_atomicycle:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    mc "Артуре, я бачив твій атомоцикл біля бази. Сам зібрав?"
    $ advance_time(5)

    ar "Ні. Знайшов на звалищі техніки біля Порт-Веро. Полагодив, замінив реактор."
    $ advance_time(5)

    mc "І часто їздиш?"
    $ advance_time(5)

    ar "Коли потрібно прочистити голову. Виїжджаю за периметр, роблю коло по пустці."
    $ advance_time(5)

    ar "На швидкості не думаєш ні про що. Тільки дорога і вітер. Це як медитація."
    $ advance_time(5)

    mc "В Голлванії взагалі є нормальні дороги?"
    $ advance_time(5)

    ar "Ні. Тому і подобається."
    $ advance_time(5)

    $ store.seen_dialogues.add("arthur_atomicycle")
    $ set_flag("arthur_atomicycle_done")
    $ add_insight("arthur_atomicycle", "Артур їздить на атомоциклі. Каже — це як медитація")

    hide arthur
    return
