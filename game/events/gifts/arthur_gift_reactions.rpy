# game/events/gifts/arthur_gift_reactions.rpy
# Реакції Артура на погані подарунки

# ═══════════════════════════════════════════════
# БРЕЛОКИ — дешевий сувенір
# ═══════════════════════════════════════════════

init python:
    DIALOGUE_ENTRIES.append({
        "id": "arthur_bad_gift_keychains",
        "who": "Артур",
        "conditions": {
            "flag_true": ["bad_gift_артур_keychains"],
            "flag_false": ["gift_arthur_keychains_done"],
            "rank_min": 1,
        },
        "priority": 75,
        "chance": 100,
        "label": "arthur_bad_gift_keychains",
    })

label arthur_bad_gift_keychains:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    ar "Зачекай. Про вчорашнє."
    $ advance_time(5)

    ar "Ті брелоки... Що це мало значити?"
    $ advance_time(5)

    mc "Я просто хотів щось подарувати."
    $ advance_time(5)

    ar "Просто. Саме в цьому проблема."
    $ advance_time(5)

    ar "Ми ризикуємо життям щодня. А ти приносиш блискучу дрібницю з кіоску."
    $ advance_time(5)

    mc "Вибач. Я не подумав."
    $ advance_time(5)

    ar "Я не ображаюсь. Але якщо хочеш зробити приємне — думай."
    $ advance_time(5)

    ar "Не купуй перше-ліпше. Добре?"
    $ advance_time(5)

    mc "Добре. Зрозумів."
    $ advance_time(5)

    ar "Проїхали."
    $ advance_time(5)

    $ set_flag("gift_arthur_keychains_done")
    $ store.seen_dialogues.add("arthur_bad_gift_keychains")
    $ add_insight("arthur_gift_pref", "Артур цінує продумані подарунки, не дешеві сувеніри.")

    hide arthur
    return


# ═══════════════════════════════════════════════
# ДОРОЖНІ ЗНАКИ — безглуздий подарунок
# ═══════════════════════════════════════════════

init python:
    DIALOGUE_ENTRIES.append({
        "id": "arthur_bad_gift_roadsigns",
        "who": "Артур",
        "conditions": {
            "flag_true": ["bad_gift_артур_roadsigns"],
            "flag_false": ["gift_arthur_roadsigns_done"],
            "rank_min": 1,
        },
        "priority": 75,
        "chance": 100,
        "label": "arthur_bad_gift_roadsigns",
    })

label arthur_bad_gift_roadsigns:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    ar "Один момент."
    $ advance_time(5)

    ar "Дорожні знаки. Ти подарував мені дорожні знаки."
    $ advance_time(5)

    mc "Ну... вони були в магазині."
    $ advance_time(5)

    ar "Багато чого є в магазині. Це не привід тягти все сюди."
    $ advance_time(5)

    ar "Я лідер оперативної групи, а не колекціонер металобрухту."
    $ advance_time(5)

    mc "Так, це було нерозумно. Вибач."
    $ advance_time(5)

    ar "Наступного разу — або нормальний подарунок, або нічого."
    $ advance_time(5)

    ar "Без образ. Просто стандарти."
    $ advance_time(5)

    $ set_flag("gift_arthur_roadsigns_done")
    $ store.seen_dialogues.add("arthur_bad_gift_roadsigns")
    $ add_insight("arthur_standards", "Артур очікує поваги навіть у дрібницях. Дорожні знаки — не подарунок.")

    hide arthur
    return
