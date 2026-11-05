# game/events/gifts/eleanor_gift_reactions.rpy
# Реакції Елеонор на погані подарунки (гучні/шумні речі)

# ═══════════════════════════════════════════════
# АКУСТИЧНА СИСТЕМА
# ═══════════════════════════════════════════════

init python:
    DIALOGUE_ENTRIES.append({
        "id": "eleanor_bad_gift_speaker_system",
        "who": "Елеонор",
        "conditions": {
            "flag_true": ["bad_gift_eleanor_speaker_system"],
            "flag_false": ["gift_eleanor_speaker_system_done"],
            "rank_min": 1,
        },
        "priority": 75,
        "chance": 100,
        "label": "eleanor_bad_gift_speaker_system",
    })

label eleanor_bad_gift_speaker_system:
    show eleanor at char_center
    $ store.talked_today.add("Елеонор")

    el "Маю дещо сказати. Про вчорашнє."
    $ advance_time(5)

    el "Акустична система. Ти приніс мені акустичну систему."
    $ advance_time(5)

    mc "Я думав, музика допомагає розслабитись..."
    $ advance_time(5)

    el "Музика — можливо. Але не на такій гучності."
    $ advance_time(5)

    el "Ти знаєш, що в мене постійний шум у голові?"
    $ advance_time(5)

    el "Техрот робить так, що кожен зайвий звук — як цвях."
    $ advance_time(5)

    el "І ти приносиш пристрій, створений щоб шуміти."
    $ advance_time(5)

    mc "Я не знав. Вибач."
    $ advance_time(5)

    el "Тепер знаєш. Тиша — це не порожнеча. Це те, що мене тримає."
    $ advance_time(5)

    $ set_flag("gift_eleanor_speaker_system_done")
    $ store.seen_dialogues.add("eleanor_bad_gift_speaker_system")
    $ add_insight("eleanor_sensory", "Елеонор чутлива до звуків через Техрот. Гучні подарунки заподіюють їй біль.")

    hide eleanor
    return


# ═══════════════════════════════════════════════
# КОЛОНКА
# ═══════════════════════════════════════════════

init python:
    DIALOGUE_ENTRIES.append({
        "id": "eleanor_bad_gift_speaker",
        "who": "Елеонор",
        "conditions": {
            "flag_true": ["bad_gift_eleanor_speaker"],
            "flag_false": ["gift_eleanor_speaker_done"],
            "rank_min": 1,
        },
        "priority": 75,
        "chance": 100,
        "label": "eleanor_bad_gift_speaker",
    })

label eleanor_bad_gift_speaker:
    show eleanor at char_center
    $ store.talked_today.add("Елеонор")

    el "Той динамік."
    $ advance_time(5)

    el "Я його не ввімкнула. І не ввімкну."
    $ advance_time(5)

    mc "Чому?"
    $ advance_time(5)

    el "Тому що мій мозок вже й так працює як зламане радіо."
    $ advance_time(5)

    el "Мені не потрібно більше шуму. Мені потрібно менше."
    $ advance_time(5)

    mc "Я зрозумів. Більше не буду."
    $ advance_time(5)

    el "Добре. Дякую, що слухаєш."
    $ advance_time(5)

    $ set_flag("gift_eleanor_speaker_done")
    $ store.seen_dialogues.add("eleanor_bad_gift_speaker")
    $ add_insight("eleanor_quiet", "Елеонор потребує тиші. Її мозок і так перевантажений через Техрот.")

    hide eleanor
    return


# ═══════════════════════════════════════════════
# ХОКЕЙНИЙ СТІЛ
# ═══════════════════════════════════════════════

init python:
    DIALOGUE_ENTRIES.append({
        "id": "eleanor_bad_gift_hockey_table",
        "who": "Елеонор",
        "conditions": {
            "flag_true": ["bad_gift_eleanor_hockey_table"],
            "flag_false": ["gift_eleanor_hockey_table_done"],
            "rank_min": 1,
        },
        "priority": 75,
        "chance": 100,
        "label": "eleanor_bad_gift_hockey_table",
    })

label eleanor_bad_gift_hockey_table:
    show eleanor at char_center
    $ store.talked_today.add("Елеонор")

    el "Хокейний стіл."
    $ advance_time(5)

    el "Ти подарував мені хокейний стіл."
    $ advance_time(5)

    mc "Думав, буде весело..."
    $ advance_time(5)

    el "Весело. Шайба б'ється об борти. Постійний стукіт."
    $ advance_time(5)

    el "Ти взагалі мене знаєш? Хоч трохи?"
    $ advance_time(5)

    mc "Мабуть, недостатньо. Вибач."
    $ advance_time(5)

    el "Я ціную тишу. Книги. Рослини. Речі, що не грюкають."
    $ advance_time(5)

    el "Запам'ятай це. Будь ласка."
    $ advance_time(5)

    $ set_flag("gift_eleanor_hockey_table_done")
    $ store.seen_dialogues.add("eleanor_bad_gift_hockey_table")
    $ add_insight("eleanor_preferences", "Елеонор любить тихі речі — книги, рослини. Ніякого шуму.")

    hide eleanor
    return
