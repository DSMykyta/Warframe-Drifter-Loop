# ═══════════════════════════════════════════════════
# ДЕМО: Звичайний діалог з titles
# ═══════════════════════════════════════════════════
# Гравець клікає на NPC → диспетчер обирає цей діалог →
# titles розгортаються в меню → гравець обирає гілку.
#
# show/hide/dialogue_begin/dialogue_end/seen_dialogues/set_flag —
# ВСЕ робить location_loop автоматично. НЕ писати в діалозі!
#
# Гілки закінчуються return — все інше автоматичне.

init python:
    DIALOGUE_ENTRIES.append({
        "id": "demo_regular_dialogue",
        "who": "Артур",
        "conditions": {
            "flag_false": ["demo_regular_dialogue_done"],
            "chemistry_min": ("Артур", 10),     # з'являється при хімії 10+
            # НЕ використовуй flag_true для ланцюжків — тільки chemistry_min
            # НЕ використовуй _intro_done — гарантоване системою
        },
        "priority": 50,                         # 50 = стандартний, 90 = інтро
        "chance": 100,                          # 100% = завжди, 75% = з шансом
        # titles = список кортежів. Кожен = один пункт в меню.
        # Формат: ("текст в меню", "label_гілки")
        # Або: ("текст", "label", "required_flag") — видно тільки якщо flag True
        "titles": [
            ("Привіт, як справи?", "demo_rd_casual"),
            ("Слухай, є питання.", "demo_rd_serious"),
            ("Хай, бро.", "demo_rd_bro", "demo_bro_flag"),  # бонусна гілка
        ],
    })


# Кожна гілка — окремий label. Починається з mc "..." (озвучення вибору).
# Потім NPC відповідає. Далі — menu всередині якщо потрібно.

label demo_rd_casual:
    mc "Привіт, як справи?"

    ar "Нормально. Ти щось хотів?"

    menu:
        "Та просто перепитати.":
            ar "Хм. Ну добре."
            $ add_chemistry("Артур", 2)     # +2 за добрий вибір

        "Хотів поговорити серйозно.":
            ar "Серйозно — це як?"
            $ add_chemistry("Артур", 4)     # +4 за відмінний (рідко!)

    # Після menu — діалог продовжується
    ar "Ще щось?"

    menu:
        "Ні, все.":
            ar "Добре."
        "Де гараж?":
            ar "Через комп'ютерний клуб."
            $ add_insight("demo_garage_location", "Гараж через комп'ютерний клуб.")

    # return — ВСЕ! location_loop зробить seen_dialogues + set_flag + hide
    return


label demo_rd_serious:
    mc "Слухай, є одне питання."

    ar "Кажи."

    mc "Як давно ти тут?"

    ar "Достатньо."

    $ add_chemistry("Артур", 2)
    $ set_flag("demo_asked_arthur_time")    # кастомний прапор для майбутніх діалогів

    return


label demo_rd_bro:
    # Ця гілка видна тільки якщо demo_bro_flag = True
    # (3-й елемент кортежу в titles)
    mc "Хай, бро."

    ar "Як ти мене назвав?"

    $ add_chemistry("Артур", -2)    # мінус за грубість
    $ set_flag("demo_bro_incident")

    return
