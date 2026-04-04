# game/quests/coffee/coffee_quest_extract.rpy
# ═══════════════════════════════════════════════════
# КВЕСТ КАВИ — ЕТАП 3-4: Спецмісія з Аоі
# ═══════════════════════════════════════════════════

# ═══ СПЕЦМІСІЯ: Витягти кавомашину ═══

init python:
    SPECIAL_MISSION_ENTRIES.append({
        "id": "coffee_extract_mission",
        "name": "Витягти кавомашину",
        "level": 2,
        "conditions": {
            "flag_true": ["coffee_extract_available"],
            "flag_false": ["coffee_machine_extracted"],
        },
        "chance": 100,
        "partner": "Аоі",
        "partner_count": 1,
        "reward": 50,
        "rep": 1,
        "label": "coffee_extract_scene",
    })


# ═══ ПЕРЕВІРКА ДЕДЛАЙНУ (в location_loop або next_day) ═══

init python:

    def check_coffee_extract_deadline():
        """Перевіряє дедлайн місії з Аоі. Викликати в next_day()."""
        if not store.flags.get("coffee_extract_available"):
            return
        if store.flags.get("coffee_machine_extracted"):
            return
        if store.flags.get("coffee_extract_reminded"):
            return
        deadline = getattr(store, '_coffee_extract_deadline', 0)
        if store.day > deadline:
            # Дедлайн пройшов — пейджер від Аоі
            pager_send_request(
                "Аоі",
                "Ми ще йдемо за кавомашиною?",
                "coffee_extract_pager_yes",
                "coffee_extract_pager_no"
            )
            set_flag("coffee_extract_reminded")


# ═══ РЕАКЦІЯ НА ПЕЙДЖЕР ═══

label coffee_extract_pager_yes:
    # Гравець прийняв — ще 1 день
    $ store._coffee_extract_deadline = store.day + 1
    $ store.flags["coffee_extract_reminded"] = False
    $ add_pager_message("Аоі", "Добре! Я готова. Побачимось на місії. (◕‿◕)")
    $ add_journal_entry("Домовились з Аоі — завтра дістаємо кавомашину.", "event")
    return

label coffee_extract_pager_no:
    # Гравець відхилив — доп опція з'являється на 7 днів
    $ set_flag("coffee_extract_delayed")
    $ store._coffee_extract_delay_until = store.day + 7
    $ add_pager_message("Аоі", "...Ок. Коли будеш готовий — скажи.")
    return


# ═══ БОНУСНА ОПЦІЯ: нагадування (якщо відхилив пейджер) ═══

init python:
    BONUS_OPTIONS.append({
        "id": "coffee_extract_remind",
        "who": "Аоі",
        "text": "Про ту кавомашину — ти ще готова?",
        "label": "coffee_extract_remind_scene",
        "conditions": {
            "flag_true": ["coffee_extract_delayed"],
            "flag_false": ["coffee_machine_extracted"],
        },
        "once": True,
    })


label coffee_extract_remind_scene:
    ao "Я завжди готова."

    ao "Місія доступна. Коли скажеш."

    $ store.flags["coffee_extract_delayed"] = False
    $ store._coffee_extract_deadline = store.day + 2
    $ add_chemistry("Аоі", 1)

    return


# ═══════════════════════════════════════════════════
# ЕТАП 4: СЦЕНА МІСІЇ З АОЇ
# ═══════════════════════════════════════════════════

label coffee_extract_scene:
    scene bg_warehouse

    "Аоі вже на місці."

    show aoi at char_center

    ao "Бачиш? Три балки."

    "Хромований край кавомашини під завалом."

    ao "Нижня — несуча. Зсуну верхні дві, нижня впаде сама."

    mc "Що робити мені?"

    ao "Стій збоку. Якщо щось поїде не туди — тягни мене назад."

    "Аоі підносить руки. Метал стогне."

    "Перша балка повільно зсувається вбік. Падає."

    ao "Одна."

    "Друга — заржавіла, вросла в стіну."

    ao "Зараз..."

    "Аоі стискає кулаки. Метал тріщить, гнеться..."

    "Балка з'їжджає вбік."

    ao "Є."

    "Нижня падає. Пил. Тиша."

    "Під брудом — хромована кавомашина. Ціла."

    # Зображення кавомашини на весь екран
    if renpy.loadable("images/hex-assets/1999ResourceUncommonB.png"):
        scene expression "images/hex-assets/1999ResourceUncommonB.png"
        pause 2.0

    scene bg_warehouse
    show aoi at char_center

    ao "...Вона ціла."

    ao "Дивно. Все навколо зруйноване, а вона — ні."

    menu:
        "Ти молодець.":
            mc "Ти молодець. Без тебе б не вийшло."

            ao "..."

            "Аоі відводить погляд. Ледь помітна посмішка."

            ao "Дякую."

            $ add_chemistry("Аоі", 4)

        "Амір буде в захваті.":
            mc "Амір буде в захваті."

            ao "Він буде НЕСТЕРПНИЙ."

            ao "Але... так. Я теж рада."

            $ add_chemistry("Аоі", 3)

    ao "Я віднесу Аміру. Він розбереться що з нею."

    ao "А ти... дякую. За те що покликав мене."

    $ set_flag("coffee_machine_extracted")
    $ set_flag("coffee_parts_mission_pending")
    $ store.flags["coffee_extract_available"] = False
    $ add_chemistry("Аоі", 2)
    $ add_journal_entry("Дістали кавомашину з-під завалів. Аоі відносить Аміру.", "event")
    $ add_insight("aoi_magnetic", "Аоі рухає метал. Без інструментів, без дотику. Точно, мовчки.")

    hide aoi
    return
