# game/day_logic.rpy
# ═══════════════════════════════════════════════════
# ЛОГІКА ДНЯ — next_day() та допоміжні функції
# ═══════════════════════════════════════════════════

init python:

    def next_day():
        """Завершує день і починає новий. Центральна функція."""

        # 1. Штраф за пізній сон
        penalty = max(0, store.minutes - 1440)  # хвилини після 24:00
        wake_up = min(720, 480 + penalty)        # кеп на 12:00

        # 2. Інкрементувати день
        store.day += 1
        store.minutes = wake_up
        store.hour = wake_up // 60

        # 3. Скинути щоденні лічильники
        store.talked_today = set()
        store.gifted_today = set()
        store.mission_chem_today = set()
        store.tags_used_today = {}
        store.missions_today_with = {}
        # Скинути daily chemistry cap
        for _n in CAST:
            store.chemistry_gained_today[_n] = 0

        # 4. Лічильник днів без місій
        store.days_without_mission += 1

        # 5. Перевірка порушених обіцянок
        check_broken_promises()

        # 6. Штраф за ігнорування місій
        check_mission_neglect()

        # 7. Розпад стосунків
        apply_decay()

        # 7a. Загоєння травм
        check_injuries_heal()

        # 7b. Скинути одноденні флаги
        _daily_flags = [
            "lettie_healed_today",
            "amir_saw_bruises", "aoi_saw_injury", "arthur_saw_injury", "quincy_saw_injury",
            "helped_someone_today",
            "helped_lettie_today", "helped_amir_today", "helped_arthur_today",
            "helped_aoi_today", "helped_quincy_today", "helped_eleanor_today",
        ]
        for _f in _daily_flags:
            if store.flags.get(_f):
                store.flags[_f] = False

        # 8. Генерація місій
        generate_missions()

        # 9. Перевірка rank-up
        try_rank_up()

        # 10. Обробити протухлі івенти (перед deck — ставить флаги)
        check_expired_events()

        # 11. Побудувати колоду eligible діалогів на день
        build_daily_deck()

        # 12. Поширити плітки
        spread_gossip()

        # 13. Очистити пейджер від вчорашніх повідомлень
        clear_pager()

        # 14. Переміщення в бекрум (прокинувся)
        store.current_location = "backroom"
