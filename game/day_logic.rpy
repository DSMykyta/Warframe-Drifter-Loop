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

        # 7b. Скинути одноденні флаги травм
        if store.flags.get("lettie_healed_today"):
            store.flags["lettie_healed_today"] = False
        for _banter_flag in ["amir_saw_bruises", "aoi_saw_injury", "arthur_saw_injury", "quincy_saw_injury"]:
            if store.flags.get(_banter_flag):
                store.flags[_banter_flag] = False

        # 8. Генерація місій
        generate_missions()

        # 9. Побудувати колоду eligible діалогів на день
        build_daily_deck()

        # 10. Обробити протухлі івенти
        check_expired_events()

        # 11. Поширити плітки
        spread_gossip()

        # 12. Переміщення в бекрум (прокинувся)
        store.current_location = "backroom"
