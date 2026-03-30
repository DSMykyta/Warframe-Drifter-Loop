# game/clothing.rpy
# ═══════════════════════════════════════════════════════════════
# СИСТЕМА ОДЯГУ — LAYERED SPRITES + РАНДОМІЗАЦІЯ
# ═══════════════════════════════════════════════════════════════
#
# !!! ЗРАЗКОВИЙ ФАЙЛ — ПОТРЕБУЄ ДООПРАЦЮВАННЯ !!!
#
# Ця система замінює одиночні ConditionSwitch спрайти в images.rpy
# на багатошарові LayeredImage з динамічним вибором одягу.
#
# ═══════════════════════════════════════════════════════════════
# КОНВЕНЦІЯ НАЗВ ФАЙЛІВ СПРАЙТІВ:
# ═══════════════════════════════════════════════════════════════
#
#   {Character}-{slot}-{item}-{zindex}-{pose}.png
#
#   Character: Arthur, Eleanor, Lettie, Amir, Aoi, Quincy
#   slot:      base, underwear, bottom, top, extra, face
#   item:      назва конкретного предмету (leather_jacket_black, jeans_blue, scarf_red)
#   zindex:    zindex10, zindex20, ... zindex90 — порядок накладання (вище = поверх)
#   pose:      arms_crossed, hand_on_hip, clenched_hands, etc.
#
# Z-INDEX СЛОТИ (від низу до верху):
#   zindex10 = base (голе тіло)
#   zindex20 = underwear (білизна)
#   zindex30 = bottom (штани, спідниця)
#   zindex40 = top_under (футболка, сорочка — під курткою)
#   zindex50 = top_over (куртка, пальто — поверх)
#   zindex60 = extra (шарф, рушник, бинти)
#   zindex70 = face (емоції)
#   zindex80 = injury_overlay (бинти від травм)
#   zindex90 = effects (спецефекти, світіння)
#
# ПРИКЛАДИ:
#
#   Arthur-base-body-zindex10-arms_crossed.png        ← голе тіло
#   Arthur-underwear-boxers-zindex20-arms_crossed.png ← білизна
#   Arthur-bottom-jeans_blue-zindex30-arms_crossed.png ← штани
#   Arthur-top-tshirt_white-zindex40-arms_crossed.png  ← футболка (під курткою)
#   Arthur-top-leather_jacket_black-zindex50-arms_crossed.png ← куртка (поверх)
#   Arthur-extra-scarf_red-zindex60-arms_crossed.png   ← шарф
#   Arthur-face-calm-zindex70.png                      ← обличчя (без пози!)
#   Arthur-injury-bandages-zindex80-arms_crossed.png   ← бинти від травм
#
# !!! ВАЖЛИВО: КОЖЕН .png = ОДИН ПРЕДМЕТ ОДЯГУ. КУРТКА = ТІЛЬКИ КУРТКА.
# !!! Z-INDEX ВИЗНАЧАЄ ПОРЯДОК НАКЛАДАННЯ АВТОМАТИЧНО.
# !!! FACE НЕ МАЄ ПОЗИ — ЕМОЦІЇ УНІВЕРСАЛЬНІ ДЛЯ ВСІХ ПОЗ.
#
# ═══════════════════════════════════════════════════════════════
# ЯК ЦЕ ПРАЦЮЄ
# ═══════════════════════════════════════════════════════════════
#
# 1. При старті дня (next_day) або при вході в локацію —
#    система вибирає outfit для кожного NPC
#
# 2. Outfit = набір шарів: {top, bottom, extra}
#    Кожен шар = назва файлу garment без розширення
#
# 3. LayeredImage збирає: base + bottom + top + extra + face
#
# 4. Що одягнути залежить від:
#    - Час доби (ранок/день/вечір/ніч)
#    - Локація NPC (бекрум = casual, місія = protoframe)
#    - Погода/настрій (якщо є відповідні прапори)
#    - Рандом з пулу допустимих комбінацій
#
# ═══════════════════════════════════════════════════════════════


# ═══════════════════════════════════════════════════════════════
# ГАРДЕРОБ КОЖНОГО ПЕРСОНАЖА
# ═══════════════════════════════════════════════════════════════
#
# !!! ДОПОВНИТИ КОЛИ БУДУТЬ ВСІ СПРАЙТИ !!!
# !!! ЗАРАЗ ТІЛЬКИ ARTHUR ЯК ЗРАЗОК !!!

init -5 python:

    # ═══ СТРУКТУРА АУТФІТУ ═══
    # Кожен outfit — словник шарів які накладаються зверху на base
    # Порядок рендеру (знизу вгору): base → bottom → top → extra → face
    # Якщо шар = None — не показується

    WARDROBE = {

        # ══════════════════════════════════════════
        # АРТУР — ЗРАЗОК (РЕШТУ ПЕРСОНАЖІВ ДОДАТИ)
        # ══════════════════════════════════════════

        "Артур": {
            # Пози які є (кожна поза = окремий набір спрайтів)
            "poses": ["arms_crossed"],
            # !!! ДОДАТИ: "hand_on_hip", "clenched_hands" КОЛИ БУДУТЬ СПРАЙТИ

            # Гардероб: назва → шари {top, bottom, extra}
            # top    = те що на торсі (футболка, сорочка, куртка)
            # bottom = те що на ногах (штани, спортивки)
            # extra  = додаткове (шарф, рушник, бинти)

            "outfits": {
                # Повсякденний (default) — шкірянка + джинси
                "casual": {
                    "top": "jacket_leather",
                    "bottom": "jeans_blue",
                    "extra": None,
                },
                # Домашній — футболка + спортивки + рушник
                "home": {
                    "top": "tshirt_white",
                    "bottom": "sweats_black",
                    "extra": "towel",
                },
                # Куртка на плечах — без футболки під нею, куртка накинута
                "jacket_draped": {
                    "top": "jacket_leather_draped",
                    "bottom": "jeans_blue",
                    "extra": None,
                },
                # Без сорочки — після тренування або в бекрумі вночі
                "shirtless": {
                    "top": None,
                    "bottom": "jeans_blue",
                    "extra": None,
                },
                # Прото-фрейм (Excalibur) — на місіях
                "protoframe": {
                    "top": "protoframe",
                    "bottom": "protoframe",
                    "extra": None,
                },

                # !!! ДОДАТИ НОВІ АУТФІТИ КОЛИ БУДУТЬ СПРАЙТИ:
                # "flannel": {"top": "shirt_flannel", "bottom": "jeans_blue", "extra": None},
                # "scarf":   {"top": "jacket_leather", "bottom": "jeans_blue", "extra": "scarf"},
                # "formal":  {"top": "shirt_button", "bottom": "pants_dark", "extra": None},
            },

            # Пули аутфітів за контекстом (рандом вибирає з пулу)
            "pools": {
                "morning":  ["home", "shirtless"],          # щойно прокинувся
                "day":      ["casual", "jacket_draped"],    # нормальний день
                "evening":  ["casual", "home"],             # вечір, розслаблений
                "night":    ["home", "shirtless"],          # пізно, в бекрумі
                "mission":  ["protoframe"],                 # завжди protoframe
                "bar":      ["casual", "jacket_draped"],    # вихід у бар
            },
        },

        # ══════════════════════════════════════════
        # !!! ЕЛЕОНОР — ДОДАТИ КОЛИ БУДУТЬ СПРАЙТИ
        # ══════════════════════════════════════════
        # "Елеонор": {
        #     "poses": ["arms_crossed", "hand_on_hip"],
        #     "outfits": {
        #         "casual":     {"top": "blouse_dark", "bottom": "skirt_long", "extra": None},
        #         "home":       {"top": "sweater_oversized", "bottom": "leggings", "extra": None},
        #         "lab":        {"top": "labcoat", "bottom": "pants_dark", "extra": None},
        #         "protoframe": {"top": "protoframe", "bottom": "protoframe", "extra": None},
        #     },
        #     "pools": {
        #         "morning": ["home"], "day": ["casual", "lab"], "evening": ["casual"],
        #         "night": ["home"], "mission": ["protoframe"], "bar": ["casual"],
        #     },
        # },

        # ══════════════════════════════════════════
        # !!! ЛЕТТІ — ДОДАТИ КОЛИ БУДУТЬ СПРАЙТИ
        # ══════════════════════════════════════════
        # "Летті": { ... },

        # ══════════════════════════════════════════
        # !!! АМІР — ДОДАТИ КОЛИ БУДУТЬ СПРАЙТИ
        # ══════════════════════════════════════════
        # "Амір": { ... },

        # ══════════════════════════════════════════
        # !!! АОІ — ДОДАТИ КОЛИ БУДУТЬ СПРАЙТИ
        # ══════════════════════════════════════════
        # "Аоі": { ... },

        # ══════════════════════════════════════════
        # !!! КВІНСІ — ДОДАТИ КОЛИ БУДУТЬ СПРАЙТИ
        # ══════════════════════════════════════════
        # "Квінсі": { ... },
    }


    # ═══════════════════════════════════════════════════════════
    # ПОТОЧНИЙ ОДЯГ КОЖНОГО NPC (змінюється щодня/при подіях)
    # ═══════════════════════════════════════════════════════════

    # !!! НЕ ВИДАЛЯТИ — ЦЕ RUNTIME СТАН !!!

    def get_time_context():
        """Визначає контекст часу доби для вибору одягу."""
        h = store.minutes // 60
        if h < 9:
            return "morning"
        elif h < 18:
            return "day"
        elif h < 22:
            return "evening"
        else:
            return "night"

    def get_outfit_context(name):
        """Визначає контекст для вибору одягу NPC.
        Пріоритет: місія > локація > час доби."""
        # На місії — завжди protoframe
        if store.current_mission_partner == name:
            return "mission"
        # В барі
        loc = get_char_location(name) if name in CAST else None
        if loc == "bar":
            return "bar"
        # Час доби
        return get_time_context()

    def pick_outfit(name):
        """Вибирає рандомний аутфіт для NPC з відповідного пулу.
        Повертає назву outfit або "casual" як fallback."""
        wardrobe = WARDROBE.get(name)
        if not wardrobe:
            return "casual"
        context = get_outfit_context(name)
        pool = wardrobe.get("pools", {}).get(context, ["casual"])
        return renpy.random.choice(pool)

    def pick_pose(name):
        """Вибирає рандомну позу для NPC.
        Повертає назву пози або "arms_crossed" як fallback."""
        wardrobe = WARDROBE.get(name)
        if not wardrobe:
            return "arms_crossed"
        poses = wardrobe.get("poses", ["arms_crossed"])
        return renpy.random.choice(poses)

    def get_outfit_layers(name):
        """Повертає dict шарів для поточного аутфіту NPC.
        {"top": "jacket_leather", "bottom": "jeans_blue", "extra": None}"""
        wardrobe = WARDROBE.get(name)
        if not wardrobe:
            return {"top": None, "bottom": None, "extra": None}
        outfit_name = store.current_outfits.get(name, "casual")
        return wardrobe.get("outfits", {}).get(outfit_name, {"top": None, "bottom": None, "extra": None})

    def refresh_all_outfits():
        """Перевибирає одяг для всіх NPC. Викликати в next_day() та при зміні контексту."""
        for name in CAST:
            store.current_outfits[name] = pick_outfit(name)
            store.current_poses[name] = pick_pose(name)

    def set_outfit(name, outfit_name):
        """Примусово встановлює конкретний аутфіт (для скриптових сцен)."""
        store.current_outfits[name] = outfit_name

    def set_pose(name, pose_name):
        """Примусово встановлює позу."""
        store.current_poses[name] = pose_name


    # ═══════════════════════════════════════════════════════════
    # ПОБУДОВА ШЛЯХУ ДО ФАЙЛУ СПРАЙТА
    # ═══════════════════════════════════════════════════════════
    #
    # !!! КЛЮЧОВА ФУНКЦІЯ — ЗБИРАЄ ШЛЯХ З ШАРІВ !!!
    #
    # Конвенція файлів:
    #   character_sprites/{CharFolder}/{crop}-{pose}-{garment}.png
    #
    # Приклад:
    #   character_sprites/Arthur/knee-arms_crossed-jacket_leather.png
    #   character_sprites/Arthur/face-calm.png

    CHAR_SPRITE_ID = {
        "Артур":   "Arthur",
        "Елеонор": "Eleanor",
        "Летті":   "Lettie",
        "Амір":    "Amir",
        "Аоі":     "Aoi",
        "Квінсі":  "Quincy",
    }

    # Z-index для кожного слоту
    SLOT_ZINDEX = {
        "base":       "zindex10",
        "underwear":  "zindex20",
        "bottom":     "zindex30",
        "top_under":  "zindex40",
        "top_over":   "zindex50",
        "extra":      "zindex60",
        "face":       "zindex70",
        "injury":     "zindex80",
        "effects":    "zindex90",
    }

    def sprite_path(name, slot, item, pose):
        """Повертає шлях до файлу спрайта за новою конвенцією.
        sprite_path("Артур", "top_over", "leather_jacket_black", "arms_crossed")
        → "character_sprites/Arthur/Arthur-top-leather_jacket_black-zindex50-arms_crossed.png"
        """
        char_id = CHAR_SPRITE_ID.get(name, name)
        zindex = SLOT_ZINDEX.get(slot, "zindex50")
        # slot в назві файлу скорочується: top_under/top_over → top
        file_slot = slot.replace("_under", "").replace("_over", "")
        return "character_sprites/{}/{}-{}-{}-{}-{}.png".format(
            char_id, char_id, file_slot, item, zindex, pose)

    def face_path(name, emotion):
        """Повертає шлях до файлу емоції (без пози!).
        face_path("Артур", "calm")
        → "character_sprites/Arthur/Arthur-face-calm-zindex70.png"
        """
        char_id = CHAR_SPRITE_ID.get(name, name)
        return "character_sprites/{}/{}-face-{}-zindex70.png".format(
            char_id, char_id, emotion)


# ═══════════════════════════════════════════════════════════════
# RUNTIME ЗМІННІ
# ═══════════════════════════════════════════════════════════════

default current_outfits = {
    "Артур":   "casual",
    "Елеонор": "casual",
    "Летті":   "casual",
    "Амір":    "casual",
    "Аоі":     "casual",
    "Квінсі":  "casual",
}

default current_poses = {
    "Артур":   "arms_crossed",
    "Елеонор": "arms_crossed",
    "Летті":   "arms_crossed",
    "Амір":    "arms_crossed",
    "Аоі":     "arms_crossed",
    "Квінсі":  "arms_crossed",
}


# ═══════════════════════════════════════════════════════════════
# LAYERED IMAGE — ЗРАЗОК ДЛЯ АРТУРА
# ═══════════════════════════════════════════════════════════════
#
# !!! ЦЕ ЗРАЗОК. КОЛИ БУДУТЬ НАРІЗАНІ СПРАЙТИ ДЛЯ КОЖНОГО
# !!! ПЕРСОНАЖА — СТВОРИТИ АНАЛОГІЧНИЙ БЛОК ДЛЯ КОЖНОГО.
# !!!
# !!! ПОКИ СПРАЙТИ НЕ ГОТОВІ — images.rpy ВИКОРИСТОВУЄ
# !!! СТАРИЙ ConditionSwitch. КОЛИ ГОТОВІ — ЗАМІНИТИ НА ЦЕЙ.
# !!!
# !!! КРОК 1: Нарізати спрайти по конвенції (один файл = один шар)
# !!! КРОК 2: Заповнити WARDROBE для кожного персонажа
# !!! КРОК 3: Розкоментувати layeredimage нижче
# !!! КРОК 4: Видалити старі image arthur = ConditionSwitch(...) з images.rpy
#
# ═══════════════════════════════════════════════════════════════
# АРТУР — ГЛОБАЛЬНИЙ LAYERED IMAGE
# ═══════════════════════════════════════════════════════════════
#
# Поки тільки обличчя (емоції). Тіло/одяг — додати коли будуть спрайти.
#
# Використання в діалогах:
#     show arthur calm at char_center
#     show arthur angry
#     show arthur smile

layeredimage arthur:

    # ── Обличчя (емоція) ── zorder 70
    group face:
        zorder 70
        attribute calm default:
            "character_sprites/Arthur/face-calm.png"
        attribute smile:
            "character_sprites/Arthur/face-smile.png"
        attribute laugh:
            "character_sprites/Arthur/face-laugh.png"
        attribute angry:
            "character_sprites/Arthur/face-angry.png"
        attribute angry_teeth:
            "character_sprites/Arthur/face-angry_teeth.png"
        attribute aggressive:
            "character_sprites/Arthur/face-aggressive.png"
        attribute surprised:
            "character_sprites/Arthur/face-surprised.png"
        attribute very_surprised:
            "character_sprites/Arthur/face-very_surprised.png"
        attribute tired:
            "character_sprites/Arthur/face-tired.png"

    # ── Тіло/одяг — ДОДАТИ КОЛИ БУДУТЬ ПОШАРОВІ СПРАЙТИ ──
    # always:
    #     zorder 10
    #     sprite_path("Артур", "base", "body", current_poses["Артур"])
    # group bottom:
    #     zorder 30
    #     ...
    # group top:
    #     zorder 50
    #     ...


# ═══════════════════════════════════════════════════════════════
# ІНТЕГРАЦІЯ З NEXT_DAY()
# ═══════════════════════════════════════════════════════════════
#
# !!! ДОДАТИ В day_logic.rpy В ФУНКЦІЮ next_day() !!!
# !!! ПІСЛЯ build_daily_deck() !!!
#
#     # 14. Рандомізувати одяг NPC на день
#     refresh_all_outfits()
#
# Це перевибере одяг для всіх NPC на основі часу доби.
# Протягом дня одяг НЕ ЗМІНЮЄТЬСЯ автоматично
# (тільки якщо скрипт викличе set_outfit() явно).


# ═══════════════════════════════════════════════════════════════
# СКРИПТОВА ЗМІНА ОДЯГУ В ДІАЛОГАХ
# ═══════════════════════════════════════════════════════════════
#
# Приклади використання в .rpy діалогах:
#
#     # Артур знімає куртку під час відвертої розмови
#     $ set_outfit("Артур", "home")
#     show arthur tired
#     ar "Знаєш, іноді я втомлюється від цих обладунків."
#
#     # Місійна сцена — всі в protoframe
#     $ set_outfit("Артур", "protoframe")
#     $ set_outfit("Аоі", "protoframe")
#     show arthur aggressive
#     ar "Рухаємось."
#
#     # Ранок у бекрумі — Артур без сорочки з рушником
#     $ set_outfit("Артур", "home")
#     show arthur calm
#
#     # Скинути на рандом (наприклад після місії)
#     $ store.current_outfits["Артур"] = pick_outfit("Артур")


# ═══════════════════════════════════════════════════════════════
# !!! TODO: СИСТЕМА ПОДАРОВАНОГО ОДЯГУ !!!
# ═══════════════════════════════════════════════════════════════
#
# Ідея: гравець може ПОДАРУВАТИ одяг NPC, і той почне його носити.
# Це додає предмети в pools і збільшує шанс що NPC одягне подарунок.
#
# Приклад:
#   $ gift_clothing("Артур", "scarf_red", {"top": "jacket_leather", "extra": "scarf_red"})
#   → Артур тепер може з'явитись у шарфі (додається в pool "day" і "evening")
#   → +chemistry бонус коли гравець бачить NPC в подарованому одязі
#
# !!! ІМПЛЕМЕНТУВАТИ КОЛИ БУДЕ СИСТЕМА ПОДАРУНКІВ ОДЯГУ !!!


# ═══════════════════════════════════════════════════════════════
# !!! TODO: ТРАВМИ ВПЛИВАЮТЬ НА СПРАЙТ !!!
# ═══════════════════════════════════════════════════════════════
#
# Якщо NPC має injury_stacks >= 1:
#   → Додати шар "bandages" поверх одягу
#   → Файл: knee-{pose}-bandages.png
#
# Якщо injury_stacks >= 2:
#   → Додати шар "bandages_heavy.png"
#   → Замінити позу на "leaning" (якщо є)
#
# !!! ІМПЛЕМЕНТУВАТИ КОЛИ БУДУТЬ СПРАЙТИ БИНТІВ !!!
