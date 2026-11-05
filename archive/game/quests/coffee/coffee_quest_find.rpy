# game/quests/coffee/coffee_quest_find.rpy
# ═══════════════════════════════════════════════════
# КВЕСТ КАВИ — ЕТАП 1-2: Знахідка + Аоі
# ═══════════════════════════════════════════════════

# ═══ ЕТАП 1: Місійний діалог — знайшли кавомашину ═══

init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "coffee_find_machine",
        "who": "Амір",
        "conditions": {
            "flag_false": ["coffee_find_machine_done", "coffee_quest_started", "coffee_quest_refused"],
            "chemistry_min": ("Амір", 10),
        },
        "priority": 60,
        "chance": 100,
        "label": "coffee_find_machine",
    })

    MISSION_DIALOGUE_ENTRIES.append({
        "id": "coffee_find_machine_q",
        "who": "Квінсі",
        "conditions": {
            "flag_false": ["coffee_find_machine_done", "coffee_quest_started", "coffee_quest_refused"],
            "chemistry_min": ("Квінсі", 10),
        },
        "priority": 60,
        "chance": 100,
        "label": "coffee_find_machine_quincy",
    })


# ═══ СЦЕНА: З АМІРОМ ═══

label coffee_find_machine:
    scene bg_warehouse
    show amir at char_center

    am "Стій-стій-стій."

    am "Бач оте? Під балкою."

    "Під завалом — щось хромоване."

    am "Це ж... ні."

    am "Це КАВОМАШИНА, Марті!"

    mc "Де?"

    am "ТАМ! Бачиш хромований край?"

    "Амір штовхає балку. Не рухається."

    am "Затиснута. Тонна металу зверху."

    menu:
        "Це багато мороки. Потім.":
            mc "Аміре, ми на місії. Потім."

            am "...Ну добре. Але я запам'ятаю де це."

            $ set_flag("coffee_quest_refused")
            $ store.seen_dialogues.add("coffee_find_machine")
            $ set_flag("coffee_find_machine_done")
            return

        "О. Ідея є.":
            mc "Зачекай. Якщо підняти балку..."

            am "Одному? Та вона вагу трьох людей."

            mc "Не одному. Треба когось хто може метал зсунути."

            am "О! Аоі! Вона ж Маг — металом рухає як нічого!"

            mc "Саме."

            am "Марті, ти ГЕНІЙ. Повернемось і розкажемо їй."

            $ set_flag("coffee_quest_started")
            $ add_chemistry("Амір", 4)
            $ add_insight("coffee_machine_spotted", "Під завалами на одній з місій знайшли кавомашину.")
            $ add_journal_entry("Знайшли кавомашину під завалами. Амір в захваті. Треба поговорити з Аоі.", "event")
            $ store.seen_dialogues.add("coffee_find_machine")
            $ set_flag("coffee_find_machine_done")

    return


# ═══ СЦЕНА: З КВІНСІ ═══

label coffee_find_machine_quincy:
    scene bg_warehouse
    show quince at char_center

    "Квінсі зупиняється."

    qu "...hm."

    mc "Що?"

    qu "Під балкою. Chrome штука."

    "Під завалом — хромований край."

    mc "Кавомашина?"

    qu "Looks like it."

    "Квінсі штовхає балку ногою. Ніяк."

    qu "Важка. Треба когось, mate."

    menu:
        "Це багато мороки. Потім.":
            mc "Ладно, потім розберемось."

            qu "Whatever, cuz."

            $ set_flag("coffee_quest_refused")
            $ store.seen_dialogues.add("coffee_find_machine_q")
            $ set_flag("coffee_find_machine_done")
            return

        "О. Ідея є.":
            mc "Квінсі, якщо привести когось хто може метал зсунути..."

            qu "Аоі. Вона пів молу розібрала коли ми тут селились."

            mc "Саме так."

            qu "Скажи їй. I don't do conversations."

            $ set_flag("coffee_quest_started")
            $ add_chemistry("Квінсі", 2)
            $ add_insight("coffee_machine_spotted", "Під завалами на одній з місій знайшли кавомашину.")
            $ add_journal_entry("Знайшли кавомашину під завалами. Квінсі запримітив. Треба поговорити з Аоі.", "event")
            $ store.seen_dialogues.add("coffee_find_machine_q")
            $ set_flag("coffee_find_machine_done")

    return


# ═══════════════════════════════════════════════════
# ЕТАП 2: Бонусна опція в діалозі з Аоі
# ═══════════════════════════════════════════════════

init python:
    BONUS_OPTIONS.append({
        "id": "coffee_tell_aoi",
        "who": "Аоі",
        "text": "Слухай, ми дещо знайшли на місії...",
        "label": "coffee_tell_aoi_scene",
        "conditions": {
            "flag_true": ["coffee_quest_started"],
            "flag_false": ["coffee_aoi_agreed"],
        },
        "once": True,
    })


label coffee_tell_aoi_scene:
    ao "Що знайшли?"

    mc "Кавомашину. Під завалами, на одній з ділянок."

    ao "...Кавомашину?"

    mc "Хромовану. Здається робочу. Але вона під купою металу."

    ao "Металеві балки?"

    mc "Так. Тонна мінімум."

    "Аоі мовчить."

    ao "Я можу зсунути балки. Але мені потрібен хтось поруч — підстрахувати."

    ao "Підемо разом?"

    menu:
        "Домовились.":
            mc "Домовились. Коли?"

            ao "Завтра? Або коли будеш вільний."

            $ add_chemistry("Аоі", 3)

        "Це не небезпечно?":
            mc "Це не небезпечно? Завал все-таки."

            ao "Я обережна. Завжди."

            ao "Але вдвох — безпечніше."

            $ add_chemistry("Аоі", 2)

    ao "Добре. Я підготуюсь."

    $ set_flag("coffee_aoi_agreed")
    $ set_flag("coffee_extract_available")
    $ store._coffee_extract_deadline = store.day + 2
    $ add_journal_entry("Аоі погодилась допомогти дістати кавомашину. Спецмісія доступна.", "event")

    return
