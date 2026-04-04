# game/quests/coffee/coffee_debug.rpy
# ═══════════════════════════════════════════════════
# ДЕБАГ КАВОВОГО КВЕСТУ — видалити перед релізом
# ═══════════════════════════════════════════════════
#
# Shift+C → консоль → jump coffee_debug
# Або через меню розробника

init python:
    config.developer = True
    config.console = True

    def _coffee_debug_reset():
        """Скидає ВСІ флаги кавового квесту."""
        _coffee_flags = [
            "coffee_quest_started", "coffee_quest_refused",
            "coffee_find_machine_done",
            "coffee_aoi_agreed", "coffee_extract_available",
            "coffee_extract_reminded", "coffee_extract_delayed",
            "coffee_machine_extracted", "coffee_parts_mission_pending",
            "cafe_find_pager_sent", "cafe_find_scene_available",
            "cafe_location_found", "cafe_find_rude",
            "cafe_unlocked", "cafe_balcony_unlocked",
            "coffee_parts_pager_sent", "coffee_parts_mission_available",
            "coffee_parts_mission_done", "coffee_parts_got",
            "coffee_parts_failed", "coffee_parts_stealth",
            "coffee_parts_declined", "coffee_amir_found_parts",
            "coffee_apology_done",
            "coffee_machine_found",
            "coffee_group_scene_pending", "coffee_group_scene_done",
            "milk_quest_started", "milk_quest_delayed",
            "milk_mission_done", "milk_drinks_unlocked",
            "milk_cappuccino_unlocked",
            "milk_type_fresh", "milk_type_pasteurized", "milk_type_dry",
            "also_got_dry_milk",
        ]
        for f in _coffee_flags:
            store.flags[f] = False
        for sid in list(store.seen_dialogues):
            if "coffee" in sid or "cafe" in sid or "milk" in sid:
                store.seen_dialogues.discard(sid)

    def _coffee_debug_set_stage(stage):
        """Встановлює квест на потрібний етап."""
        _coffee_debug_reset()

        # Базові вимоги для всіх етапів
        store.flags["intro_done"] = True
        store.flags["met_amir"] = True
        store.flags["met_aoi"] = True
        store.flags["met_quincy"] = True
        for _n in CAST:
            store.chemistry[_n] = max(store.chemistry.get(_n, 0), 15)

        if stage >= 1:
            # Після знахідки
            store.flags["coffee_quest_started"] = True
            store.flags["coffee_find_machine_done"] = True
            store.seen_dialogues.add("coffee_find_machine")

        if stage >= 2:
            # Аоі погодилась
            store.flags["coffee_aoi_agreed"] = True
            store.flags["coffee_extract_available"] = True

        if stage >= 3:
            # Машину витягли
            store.flags["coffee_extract_available"] = False
            store.flags["coffee_machine_extracted"] = True
            store.flags["coffee_parts_mission_pending"] = True

        if stage >= 4:
            # Кав'ярню знайдено
            store.flags["cafe_unlocked"] = True
            store.flags["cafe_balcony_unlocked"] = True
            store.flags["cafe_location_found"] = True
            store.flags["cafe_find_pager_sent"] = True

        if stage >= 5:
            # Деталі пейджер відправлений
            store.flags["coffee_parts_pager_sent"] = True
            store.flags["coffee_parts_mission_available"] = True

        if stage >= 6:
            # Деталі дістали
            store.flags["coffee_parts_mission_available"] = False
            store.flags["coffee_parts_mission_done"] = True
            store.flags["coffee_parts_got"] = True

        if stage >= 7:
            # Кав'ярня працює
            store.flags["coffee_machine_found"] = True
            store.flags["coffee_group_scene_pending"] = True

        if stage >= 8:
            # Групова сцена пройдена
            store.flags["coffee_group_scene_pending"] = False
            store.flags["coffee_group_scene_done"] = True

        if stage >= 9:
            # Молоко квест
            store.flags["milk_quest_started"] = True

        if stage >= 10:
            # Все пройдено
            store.flags["milk_mission_done"] = True
            store.flags["milk_drinks_unlocked"] = True
            store.flags["milk_cappuccino_unlocked"] = True
            store.flags["milk_type_fresh"] = True


label coffee_debug:
    scene black

    "=== КАВОВИЙ КВЕСТ — ДЕБАГ ==="

    menu:
        "--- ПЕРЕЙТИ ДО ЕТАПУ ---" if False:
            pass

        "0. Скинути все":
            $ _coffee_debug_reset()
            "Квест скинутий."

        "1. Перед знахідкою (місія з Аміром/Квінсі)":
            $ _coffee_debug_set_stage(0)
            "Етап 0. Йди на місію з Аміром (chemistry >= 10)."

        "2. Знайшли → поговорити з Аоі":
            $ _coffee_debug_set_stage(1)
            "Етап 1. Бонус-опція з Аоі доступна."

        "3. Аоі погодилась → спецмісія витягнення":
            $ _coffee_debug_set_stage(2)
            "Етап 2. Місія 'Витягти кавомашину' на дошці."

        "4. Машину витягли → чекаємо ранок (кав'ярня)":
            $ _coffee_debug_set_stage(3)
            "Етап 3. next_day() відкриє кав'ярню + пейджер Аоі."

        "4.5. Кав'ярня відкрита → зайти для діалогу":
            $ _coffee_debug_set_stage(3)
            $ store.flags["cafe_unlocked"] = True
            $ store.flags["cafe_balcony_unlocked"] = True
            $ store.flags["cafe_find_scene_available"] = True
            $ store.flags["cafe_find_pager_sent"] = True
            "Етап 3+. Кав'ярня відкрита, Аоі чекає. Зайди в cafe."

        "5. Кав'ярня знайдена → пейджер Аміра про деталі":
            $ _coffee_debug_set_stage(4)
            "Етап 4. next_day() відправить пейджер Аміра."

        "6. Місія складів доступна":
            $ _coffee_debug_set_stage(5)
            "Етап 5. Місія 'Склади Скальдри' на дошці."

        "7. Деталі є → чекаємо відкриття":
            $ _coffee_debug_set_stage(6)
            "Етап 6. next_day() запустить кавомашину."

        "8. Кавомашина працює → групова сцена":
            $ _coffee_debug_set_stage(7)
            "Етап 7. Зайди в cafe для групової сцени."

        "9. Групова пройдена → квест молока":
            $ _coffee_debug_set_stage(8)
            "Етап 8. Бонус-опція або місія молока."

        "10. Все пройдено":
            $ _coffee_debug_set_stage(10)
            "Квест завершений. Всі напої доступні."

        "--- ТЕСТИ ---" if False:
            pass

        "Тест: forced cafe_find_scene":
            $ _coffee_debug_set_stage(3)
            $ store.flags["cafe_unlocked"] = True
            $ store.flags["cafe_balcony_unlocked"] = True
            $ store.flags["cafe_find_scene_available"] = True
            $ store.current_location = "cafe"
            jump cafe_find_scene

        "Тест: групова сцена":
            $ _coffee_debug_set_stage(7)
            $ store.current_location = "cafe"
            jump coffee_group_scene

        "Тест: данжн складів":
            $ _coffee_debug_set_stage(5)
            jump coffee_warehouse_dungeon

        "Тест: місія молока":
            $ _coffee_debug_set_stage(9)
            jump coffee_milk_scene

        "Тест: кавовий автомат":
            $ _coffee_debug_set_stage(10)
            $ store.money = 500
            jump coffee_machine_interact

        "Тест: подарувати каву":
            $ _coffee_debug_set_stage(10)
            $ store.money = 500
            $ buy_coffee("coffee_espresso")
            $ buy_coffee("coffee_latte")
            $ buy_coffee("coffee_black")
            $ buy_coffee("coffee_cocoa")
            "Куплено 4 кави. Поговори з NPC, опція 'Тримай. Приніс каву.'"

        "Назад до гри":
            jump location_loop

    jump coffee_debug
