# ═══════════════════════════════════════════════════
# ДЕМО: Обіцянка — зустріч у конкретному місці/часі
# ═══════════════════════════════════════════════════
# Діалог створює обіцянку: NPC чекатиме в місці у вікно часу.
# Якщо гравець прийде — +5 хімії. Не прийде — -5 хімії.
#
# Обіцянка = тригер позиції NPC (переміщує в зазначене місце)
# + нагадування на пейджері за 30 хв.
#
# Два файли: діалог-запрошення + діалог-зустріч (окремий label).

init python:
    DIALOGUE_ENTRIES.append({
        "id": "demo_promise_invite",
        "who": "Артур",
        "conditions": {
            "flag_false": ["demo_promise_invite_done"],
            "chemistry_min": ("Артур", 30),
        },
        "priority": 60,
        "chance": 100,
        "titles": [
            ("Привіт.", "demo_promise_invite_main"),
        ],
    })


label demo_promise_invite_main:
    mc "Привіт."

    ar "Вечором буду в барі. Якщо хочеш — приходь."

    menu:
        "Буду.":
            mc "Буду. О котрій?"
            ar "Після двадцятої. До двадцять другої."

            # Створити обіцянку: Артур, бар, 20:00-22:00, завтра
            $ create_promise("Артур", "bar", 1200, 1320, store.day + 1, "demo_promise_meeting")

            $ add_chemistry("Артур", 2)
            $ set_flag("demo_promise_invite_done")
            $ add_journal_entry("Артур запросив у бар завтра ввечері.", "promise")

        "Не впевнений.":
            mc "Не впевнений що встигну."
            ar "Як знаєш."
            $ set_flag("demo_promise_invite_done")

    return


# Діалог зустрічі — тригериться коли гравець приходить в бар
# під час вікна обіцянки (20:00-22:00, наступного дня).
# NPC автоматично переміщений в бар через _check_promise_location().

label demo_promise_meeting:
    show arthur at char_center

    ar "Прийшов. Добре."

    ar "Сідай."

    menu:
        "Що п'єш?":
            mc "Що п'єш?"
            ar "Щось міцне. Як завжди."
            $ add_chemistry("Артур", 4)

        "Розкажи щось.":
            mc "Ну, розказуй."
            ar "Про що саме?"
            $ add_chemistry("Артур", 2)

    # Виконати обіцянку (+5 хімії через add_chemistry)
    $ fulfill_promise("Артур")

    $ set_flag("demo_promise_meeting_done")
    $ add_journal_entry("Посидів з Артуром в барі. Як він і обіцяв.", "conversation")

    hide arthur
    return
