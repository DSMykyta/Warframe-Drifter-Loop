# game/dialogues/aoi/aoi_bubbletea_promise.rpy
# Аоі запрошує на бабл-ті — створює обіцянку

init python:
    DIALOGUE_ENTRIES.append({
        "id": "aoi_bubbletea_promise",
        "who": "Аоі",
        "conditions": {
            "flag_false": ["aoi_bubbletea_promise_done"],
            "rank_min": 1,
            "chemistry_min": ("Аоі", 25),
        },
        "priority": 60,
        "chance": 70,
        "label": "aoi_bubbletea_promise",
    })

label aoi_bubbletea_promise:
    show aoi at char_center
    $ store.talked_today.add("Аоі")

    ao "Я знайшла працюючий апарат з бабл-ті. В фуд-корті."
    $ advance_time(5)

    mc "Серйозно? Він ще працює?"
    $ advance_time(5)

    ao "Частково. Два смаки з п'яти. Таро і матча."
    $ advance_time(5)

    ao "Завтра о п'ятнадцятій хочу спробувати. Підеш?"
    $ advance_time(5)

    menu:
        "Звісно, піду":
            $ advance_time(5)
            mc "Таро чи матча?"

            ao "Обидва. Треба ж порівняти."
            $ advance_time(5)

            $ create_promise("Аоі", "food_court", 900, 1020, store.day + 1, "aoi_bubbletea_meeting")
            $ add_chemistry("Аоі", 2)

        "Може, не завтра":
            $ advance_time(5)
            mc "Не впевнений щодо завтра..."

            ao "Зрозуміло."
            $ advance_time(5)

    $ store.seen_dialogues.add("aoi_bubbletea_promise")
    $ set_flag("aoi_bubbletea_promise_done")

    hide aoi
    return

label aoi_bubbletea_meeting:
    show aoi at char_center
    $ store.talked_today.add("Аоі")

    ao "Прийшов. Тримай."
    $ advance_time(5)

    "Аоі простягає стакан з бабл-ті зі смаком таро."
    $ advance_time(5)

    mc "Дякую. А ти?"
    $ advance_time(5)

    ao "Матча. Як завжди."
    $ advance_time(5)

    "Ви стоїте біля апарату і п'єте в тиші."
    $ advance_time(5)

    ao "Тиша з кимось — рідкість. Зазвичай люди намагаються заповнити кожну секунду словами."
    $ advance_time(5)

    mc "А ти ні?"
    $ advance_time(5)

    ao "Я цінує тих, хто не боїться мовчати поруч."
    $ advance_time(5)

    $ add_chemistry("Аоі", 4)
    $ set_flag("aoi_bubbletea_meeting_done")
    $ add_insight("aoi_silence", "Аоі цінує спільну тишу. Для неї це знак довіри.")
    $ fulfill_promise(store.promises[-1] if store.promises else None)

    hide aoi
    return
