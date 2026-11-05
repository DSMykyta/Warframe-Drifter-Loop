# game/quests/coffee/coffee_quest_open.rpy
# ═══════════════════════════════════════════════════
# КВЕСТ КАВИ — ЕТАП 6-7: Кав'ярня відкрита + Групова сцена
# ═══════════════════════════════════════════════════

# ═══ ВІДКРИТТЯ КАВ'ЯРНІ (next_day) ═══

init python:

    def check_coffee_cafe_open():
        """Відкриває кав'ярню якщо деталі є. Викликати в next_day()."""
        if store.flags.get("cafe_unlocked"):
            return
        if not store.flags.get("coffee_parts_got"):
            return
        # Деталі є — запустити кавомашину наступного дня
        if not store.flags.get("cafe_unlocked"):
            set_flag("cafe_unlocked")
            set_flag("cafe_balcony_unlocked")
        set_flag("coffee_machine_found")
        set_flag("coffee_group_scene_pending")
        add_pager_message("Амір", "КАВ'ЯРНЯ ПРАЦЮЄ!!! ПРИХОДЬ!!!")
        add_journal_entry("Кав'ярня відкрита! Амір запустив кавомашину.", "event")


# ═══ ГРУПОВА СЦЕНА — FORCED при вході в кав'ярню ═══

init python:
    DIALOGUE_ENTRIES.append({
        "id": "coffee_group_opening",
        "who": "Амір",
        "conditions": {
            "flag_true": ["coffee_group_scene_pending"],
            "flag_false": ["coffee_group_scene_done"],
            "location": "cafe",
        },
        "priority": 95,
        "chance": 100,
        "forced": True,
        "label": "coffee_group_scene",
    })


label coffee_group_scene:
    scene bg_cafe
    # Показати всіх
    show arthur at far_left
    show eleanor at center_left
    show lettie at center
    show amir at center_right
    show aoi at right_of_center
    show quince at far_right

    am "ВСЕ! ВСІМ ТИХО!"

    am "Дами і джентльмени. Квінсі."

    qu "Wow. Hilarious."

    am "Дозвольте представити..."

    "Кавомашина. Хромована, вичищена."

    am "ТА-ДАМ!"

    am "Робоча. Кавомашина. В нашому молі."

    ar "Ти серйозно зібрав нас заради кавомашини."

    am "Артуре. КАВА. Справжня. Гаряча. Не та бурда з пакетиків."

    el "Насправді, я вражена. Хто її знайшов?"

    am "Марті знайшов! На місії. А Аоі витягла з-під завалів."

    ao "..."

    am "А деталі..."

    if store.flags.get("coffee_amir_found_parts"):
        am "...я сам дістав. Не питайте як."
    elif store.flags.get("coffee_parts_stealth"):
        am "...Марті дістав. Тихо і чисто. Як ніндзя."
        $ add_chemistry("Амір", 1)
    else:
        am "...Марті дістав. Було... шумно. Але дістав."

    le "Вона хоча б чиста?"

    am "Я промив тричі! Все стерильно!"

    le "..."

    le "Покажи."

    "Летті оглядає. Витирає пальцем."

    le "...Прийнятно."

    am "ВІД ЛЕТТІ ЦЕ КОМПЛІМЕННТ!"

    # ═══ Розгалуження ═══

    menu:
        "А латте можна?":
            mc "А латте можна? Або щось з молоком?"

            am "О-о-о. Молоко. Проблема."

            am "Машина може, але в нас нема молока. Ні свіжого, ні сухого."

            am "Десь на складах може бути. Або в аптечних запасах — пастеризоване."

            ao "Я бачила сухе молоко на складі поруч з консервами."

            am "Марті? Береш квест на молоко?"

            menu:
                "Беру.":
                    mc "Беру."

                    am "КРАСАВА! Знайдеш молоко — лате, какао, капучіно, все буде!"

                    $ set_flag("milk_quest_started")
                    $ add_chemistry("Амір", 2)
                    $ add_journal_entry("Амір просить знайти молоко. Сухе, свіже, або пастеризоване.", "event")

                "Потім.":
                    mc "Потім. Хай спочатку чорна кава буде."

                    am "Теж варіант. Але якщо надумаєш — скажи."

                    $ set_flag("milk_quest_delayed")

        "Як вона працює?":
            mc "Покажи як працює."

            am "О! Дивись."

            am "Монетку кидаєш — ні, жартую. Вона безкоштовна. Ми ж тут одні."

            am "Натискаєш кнопку — зверху чорна кава. Міцна, гірка."

            am "Є ще еспресо — подвійний удар. Для справжніх людей."

            $ add_insight("coffee_machine_works", "Кавомашина працює. Чорна кава і еспресо. Безкоштовно... якщо не рахувати квест.")

        "Непогано, Аміре.":
            mc "Непогано."

            am "НЕПОГАНО?! Це ШЕДЕВР!"

            ar "Це кавомашина."

            am "Артуре. Ти не розумієш. Ти ніколи не розумієш."

            ar "Я розумію каву. Подвійний еспресо є?"

            am "...Є."

            ar "Тоді нормально."

            $ add_chemistry("Артур", 1)

    # Завершення

    am "Ну все! Кав'ярня офіційно відкрита!"

    qu "Nobody asked for a ceremony, mate."

    am "Квінсі, ти отримаєш каву ОСТАННІМ."

    qu "...Fair."

    $ set_flag("coffee_group_scene_done")
    $ store.flags["coffee_group_scene_pending"] = False

    # +2 хімії всім за груповий івент
    python:
        for _cn in CAST:
            add_chemistry(_cn, 2)

    $ add_journal_entry("Кав'ярня відкрита. Амір у своєму елементі.", "event")

    hide arthur
    hide eleanor
    hide lettie
    hide amir
    hide aoi
    hide quince

    return


# ═══ БОНУСНА ОПЦІЯ: Молоко (якщо відклав) ═══

init python:
    BONUS_OPTIONS.append({
        "id": "milk_quest_ask_amir",
        "who": "Амір",
        "text": "Про молоко для кавомашини — я готовий.",
        "label": "milk_quest_start_delayed",
        "conditions": {
            "flag_true": ["milk_quest_delayed", "coffee_group_scene_done"],
            "flag_false": ["milk_quest_started"],
        },
        "once": True,
    })


label milk_quest_start_delayed:
    am "О! Нарешті!"

    am "Місія на дошці. Сухе молоко — на складах біля консервів."

    am "Але якщо знайдеш щось краще — бери."

    $ set_flag("milk_quest_started")
    $ store.flags["milk_quest_delayed"] = False
    $ add_chemistry("Амір", 2)
    $ add_journal_entry("Квест на молоко активний.", "event")

    return


# ═══ ТРИГЕР ЛЕТТІ В КАВ'ЯРНЮ ═══

init 1 python:
    # Летті приходить в кав'ярню коли вона відкрита
    # (додати в LOCATION_TRIGGERS в triggers.rpy)
    LOCATION_TRIGGERS.append({
        "id": "lettie_cafe_morning",
        "chars": ["Летті"],
        "location": "cafe",
        "condition": lambda: store.flags.get("coffee_machine_found") and store.minutes >= 480 and store.minutes < 600 and not is_npc_injured("Летті"),
    })

    LOCATION_TRIGGERS.append({
        "id": "lettie_cafe_evening",
        "chars": ["Летті"],
        "location": "cafe",
        "condition": lambda: store.flags.get("coffee_machine_found") and store.minutes >= 1200 and store.minutes < 1380 and not is_npc_injured("Летті"),
    })
