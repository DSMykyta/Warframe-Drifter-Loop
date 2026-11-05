# game/dialogues/aoi/aoi_bubbletea.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "aoi_bubbletea",
        "who": "Аоі",
        "conditions": {
            "flag_true": ["aoi_origami_done"],
            "flag_false": ["aoi_bubbletea_done"],
            "rank_min": 1,
            "chemistry_min": ("Аоі", 15),
        },
        "priority": 50,
        "chance": 100,
        "label": "aoi_bubbletea",
    })

label aoi_bubbletea:
    show aoi at char_center
    $ store.talked_today.add("Аоі")

    ao "Тримай. Спробуй."
    $ advance_time(5)

    mc "Що це?"
    $ advance_time(5)

    ao "Бабл ті! Ну, моя версія. Справжнього тапіока тут нема, тож я використовую желатинові цукерки з кондитерської на другому поверсі."
    $ advance_time(5)

    mc "...Це несподівано смачно."
    $ advance_time(5)

    ao "Правда?! Я місяць підбирала пропорції! Чай знайшла в старому складі, а молоко — Летті дістала звідкись."
    $ advance_time(5)

    ao "Найскладніше — знайти сироп. Шукаю по всьому молу. Іноді після петлі з'являються нові запаси в рандомних місцях."
    $ advance_time(5)

    menu:
        "Можеш навчити мене готувати?":
            $ advance_time(5)
            mc "Можеш навчити мене готувати?"

            ao "Звісно! Тільки попереджаю — якщо ти зіпсуєш мій запас чаю, я тебе не прощу. Ну... прощу. Але буду сумувати за чаєм."
            $ advance_time(5)
            $ set_flag("aoi_shared_recipe")

        "Ти серйозно шукаєш інгредієнти по всьому молу?":
            $ advance_time(5)
            mc "Ти серйозно шукаєш інгредієнти по всьому молу?"

            ao "А ти думав! Це ціла операція. Я навіть маршрути склала. Логістика бабл ті — мій побічний проєкт."
            $ advance_time(5)

    ao "Знаєш, коли все навкруги повторюється, маленькі речі стають великими. Чашка чаю — це ціла подія."
    $ advance_time(5)

    ao "Тому я і роблю це. Не тільки для себе — для всіх. Кожен заслуговує на щось приємне."
    $ advance_time(5)

    $ store.seen_dialogues.add("aoi_bubbletea")
    $ set_flag("aoi_bubbletea_done")
    $ add_insight("aoi_bubbletea", "Аоі робить бабл ті сама. Шукає інгредієнти по всьому молу")

    hide aoi
    return
