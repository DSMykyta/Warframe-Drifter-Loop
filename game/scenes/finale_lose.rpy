# game/scenes/finale_lose.rpy
# ═══════════════════════════════════════════════
# ФІНАЛ: ПОРАЗКА (ЧАСОВА ПЕТЛЯ)
# ═══════════════════════════════════════════════

label finale_defeat:
    scene black
    pause 1.0

    "День 31. Новий Рік. Реактор."
    pause 1.0

    "Ви стоїте перед реактором. Але щось не так."
    pause 1.0

    "Погляди не зустрічаються. Руки не впевнені. Слова — порожні."
    pause 1.0

    show arthur at char_center
    ar "Ми... спробуємо."
    $ advance_time(5)

    mc "Артуре..."
    $ advance_time(5)

    ar "Я знаю. Я теж це відчуваю."
    $ advance_time(5)

    hide arthur

    scene white
    pause 0.5
    scene black
    pause 1.0

    "Реактор нестабільний. Команда не синхронізована."
    pause 1.0

    "Хтось помиляється. Потім інший. Ланцюгова реакція."
    pause 1.0

    "Вибух."
    pause 2.0

    "..."
    pause 1.0

    "Темрява."
    pause 2.0

    "..."
    pause 1.0

    "Будильник. Ранок."
    pause 1.0

    "Знову."
    pause 2.0

    # Зберегти дані для петлі
    $ persistent.loop_count = getattr(persistent, 'loop_count', 0) + 1
    $ persistent.insights_log = list(store.insights_log)           # Факти залишаються повністю
    $ persistent.previous_journal = [e for e in store.journal_entries if e.get("type") in ("romance", "milestone")][:3]

    scene black

    $ _loop_num = persistent.loop_count
    "Петля #[_loop_num]."
    pause 1.0

    "Щось залишилось. Тінь спогаду. Дежавю."
    pause 1.0

    "Може, цього разу..."
    pause 2.0

    return
