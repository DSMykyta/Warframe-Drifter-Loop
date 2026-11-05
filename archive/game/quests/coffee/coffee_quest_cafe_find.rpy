# game/quests/coffee/coffee_quest_cafe_find.rpy
# ═══════════════════════════════════════════════════
# КВЕСТ КАВИ — ЕТАП 4.5: Аоі знайшла місце для кав'ярні
# ═══════════════════════════════════════════════════
#
# Ранок після витягнення машини:
#   - cafe + cafe_balcony відкриваються автоматично
#   - Аоі шле пейджер
#   - Прийшов → forced діалог з розгалуженнями (+/- хімія)

init python:

    def check_coffee_cafe_find():
        """Відкриває кав'ярню і шле пейджер. Викликати в next_day()."""
        if not store.flags.get("coffee_machine_extracted"):
            return
        if store.flags.get("cafe_find_pager_sent"):
            return

        # Відкрити локації
        set_flag("cafe_unlocked")
        set_flag("cafe_balcony_unlocked")
        set_flag("cafe_find_scene_available")

        # Пейджер (просто повідомлення, не запит)
        add_pager_message("Аоі", "Всім!! Знайшла місце для кавомашини на другому поверсі біля балкону і вже прибрала (≧◡≦) Заходьте зацінити!!")
        set_flag("cafe_find_pager_sent")


# ═══ ТРИГЕР: Аоі чекає в кав'ярні поки гравець не прийде ═══

init 1 python:
    LOCATION_TRIGGERS.append({
        "id": "aoi_cafe_waiting",
        "chars": ["Аоі"],
        "location": "cafe",
        "condition": lambda: store.flags.get("cafe_find_scene_available") and not store.flags.get("cafe_location_found"),
    })


# ═══ FORCED ДІАЛОГ: при вході в кав'ярню ═══

init python:
    DIALOGUE_ENTRIES.append({
        "id": "coffee_cafe_find_scene",
        "who": "Аоі",
        "conditions": {
            "flag_true": ["cafe_find_scene_available"],
            "flag_false": ["cafe_location_found"],
            "location": "cafe",
        },
        "priority": 95,
        "chance": 100,
        "forced": True,
        "label": "cafe_find_scene",
    })


label cafe_find_scene:
    scene bg_cafe

    show aoi at char_center

    ao "Ось. Дивись."

    "Стійка, крісла під чохлами, вітрина."

    ao "Тут була кав'ярня. До всього цього."

    ao "Я прибрала. Ну... зсунула сміття."

    menu:
        "Затишно. Навіть з пилом.":
            mc "Затишно. Навіть з пилом."

            ao "Правда?"

            ao "Ходила повз сто разів. А потім подумала — навіщо це пустує?"

            $ add_chemistry("Аоі", 3)

        "Ти сама все прибрала?":
            mc "Ти сама все це?"

            ao "Ну... метал зсунула. Решту руками."

            ao "Не хотіла чекати."

            mc "Вражає."

            ao "..."

            $ add_chemistry("Аоі", 4)

        "Тут досі брудно.":
            mc "Тут досі брудно."

            "Аоі замовкає."

            ao "...Я знаю."

            ao "Я прибирала пів ночі."

            mc "Ну, може варто було більше постаратись."

            ao "..."

            "Аоі дивиться в підлогу."

            ao "Вибач. Я думала тобі сподобається."

            $ add_chemistry("Аоі", -3)

    ao "Як тільки Амір запустить машину — тут буде кав'ярня."

    if not store.flags.get("cafe_find_rude"):
        ao "Справжня."

    menu:
        "Балкон теж відкритий?":
            mc "А балкон?"

            ao "Так. Розчистила вихід."

            ao "Вид на атріум. Тихо."

            $ add_chemistry("Аоі", 2)

        "Дякую, Аоі.":
            mc "Дякую. Серйозно."

            ao "Не дякуй. Просто хотілось щоб тут було щось живе."

            $ add_chemistry("Аоі", 2)

        "Місце паршиве.":
            mc "Чесно? Місце паршиве."

            "Тиша."

            ao "...Паршиве."

            mc "Маленьке, брудне, тісно."

            ao "Я... Добре. Зрозуміла."

            "Аоі відвертається."

            ao "Може й маєш рацію."

            $ add_chemistry("Аоі", -4)
            $ set_flag("cafe_find_rude")

    if store.flags.get("cafe_find_rude"):
        "Аоі йде мовчки. Не озирається."
    else:
        ao "Добре. Я ще трохи тут поприбираю."

    $ set_flag("cafe_location_found")
    $ store.flags["cafe_find_scene_available"] = False
    $ add_journal_entry("Аоі знайшла і прибрала місце для кав'ярні. Другий поверх, біля балкону.", "event")
    $ add_insight("aoi_cafe_initiative", "Аоі сама знайшла і прибрала місце для кав'ярні. Без прохань.")

    hide aoi
    return
