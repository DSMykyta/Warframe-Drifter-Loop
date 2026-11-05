# game/dialogues/arthur/arthur_intro.rpy
# ═══════════════════════════════════════════════════
# АРТУР — ІНТРО: Місії, правила, погрози
# ═══════════════════════════════════════════════════
# Основна перша розмова. Пояснює місії.
# "Хай, бро" — ОКРЕМИЙ ФАЙЛ (arthur_intro_bro.rpy)
# Після "бро" — Артур грубий, зрізає питання.
# Меню уточнень звужується: спитав — зникає. Повторив — "ти тупий?"

init python:
    DIALOGUE_ENTRIES.append({
        "id": "arthur_intro",
        "who": "Артур",
        "conditions": {
            "flag_false": ["arthur_intro_done"],
        },
        "priority": 90,
        "chance": 100,
        # "Хай, бро" — бонусна опція в arthur_intro_bro.rpy (через BONUS_OPTIONS)
        "titles": [
            ("Привіт.", "arthur_intro_normal"),
        ],
    })


label arthur_intro_normal:

    mc "Привіт."

    ar "Привіт, Марті."

    ar "Ти вчасно. Мені треба тобі дещо пояснити."

    jump arthur_intro_missions


label arthur_intro_missions:

    $ _bro = store.flags.get("arthur_bro_incident")

    ar "Місії. Це головне, чим ми тут займаємось."

    ar "Щодня генеруються завдання. Різного рівня складності."

    ar "Рівень один — розвідка. Рівень шість — ти або вони."

    ar "Нагорода залежить від рівня. Гроші, репутація."

    if _bro:
        ar "Місії в гаражі. Напарник — один з нас. Не халтур."
        ar "Все. Питання?"
    else:
        ar "Для місій потрібно йти в гараж. Там дошка завдань."
        ar "Кожна місія має напарника — когось з Гексу. Працюєте разом."
        ar "Репутація — це довіра Гексу до тебе. Чим більше — тим більше можливостей."
        ar "Питання?"

    # ═══ РОЗУМНЕ МЕНЮ: звужується після кожної відповіді ═══
    # 3 питання + "нема". Спитав — зникає. Повторив (якщо все зникло) — "ти тупий?"

    $ _asked_skip = False
    $ _asked_partner = False
    $ _asked_slacking = False

    jump arthur_intro_questions


label arthur_intro_questions:

    $ _bro = store.flags.get("arthur_bro_incident")
    $ _remaining = 0
    if not _asked_skip:
        $ _remaining += 1
    if not _asked_partner:
        $ _remaining += 1
    if not _asked_slacking:
        $ _remaining += 1

    if _remaining == 0:
        # Все спитав
        jump arthur_intro_end

    menu:
        "А якщо пропустити місію?" if not _asked_skip:
            $ _asked_skip = True

            if _bro:
                ar "Не пропускай."
            else:
                mc "А якщо я вирішу пропустити?"
                ar "Один-два дні — нічого. Три — починають питання."
                ar "П'ять — всі починають сумніватись чи ти взагалі тут потрібен."
                ar "Я не загрожую. Я попереджаю."
                $ add_chemistry("Артур", 2)

            jump arthur_intro_questions

        "Хто буде напарником?" if not _asked_partner:
            $ _asked_partner = True

            if _bro:
                ar "Хтось з нас. Далі."
            else:
                mc "Напарник — це завжди хтось конкретний?"
                ar "Кожна місія призначає напарника. Одного з Гексу."
                ar "Працюєте разом. Захищаєте одне одного."
                ar "Підставиш напарника — підставиш мого бійця. А це — особисте."
                $ add_chemistry("Артур", 2)
                $ add_insight("arthur_protects_team", "Артур захищає свою команду. Підставити напарника — особиста образа.")

            jump arthur_intro_questions

        "А якщо халтурити?" if not _asked_slacking:
            $ _asked_slacking = True

            if _bro:
                ar "Спробуй. Побачиш що буде."
            else:
                mc "А якщо... ну... не дуже старатись?"
                ar "Тоді ти підставляєш напарника. А напарник — це хтось із моїх людей."
                ar "І я це сприйму особисто."
                mc "Зрозумів."
                $ add_chemistry("Артур", 4)

            jump arthur_intro_questions

        "Нема питань." if True:
            jump arthur_intro_end


label arthur_intro_end:

    if store.flags.get("arthur_bro_incident"):
        ar "Іди. Гараж через комп'ютерний клуб."
    else:
        ar "Добре. Гараж — через комп'ютерний клуб. Побачиш вивіску."

        menu:
            "Не підведу.":
                mc "Не підведу."
                ar "Побачимо."
                $ add_chemistry("Артур", 2)

            "Зрозумів.":
                mc "Зрозумів."
                ar "Добре."

    $ store.seen_dialogues.add("arthur_intro")
    $ set_flag("arthur_intro_done")
    $ set_flag("garage_unlocked")
    $ add_journal_entry("Артур пояснив систему місій. Гараж, напарники, репутація. Халтура — не варіант.", "event")
    $ add_insight("arthur_leader", "Артур — лідер Гексу. Місії в гаражі. Не терпить халтури.")
    $ add_insight("missions_garage", "Місії — в гаражі. Щодня нові завдання.")

    ar "Гараж тепер відкритий. Підеш коли будеш готовий — там дошка з місіями."

    return
