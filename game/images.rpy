# images.rpy  ───────────────────────────────────────

# якщо ще не вказував розмір екрана
define config.screen_width  = 1920
define config.screen_height = 1080

# ═══ ФОНИ ЛОКАЦІЙ ═══
# Стандарт: 1920x1080, PNG, bg_{location_id}.png
# --- Поверх 1 (атріум) ---
image bg_mall            = "backgrounds/bg-hub-mall.png"
image bg_foodcourt       = "backgrounds/bg_foodcourt.jpg"
image bg_info_desk       = "backgrounds/bg_info_desk.png"
image bg_arcade          = "backgrounds/bg_arcade.png"
image bg_music_shop      = "backgrounds/bg_music_shop.png"
image bg_range           = "backgrounds/bg_range.png"
image bg_bar             = "backgrounds/bg_bar.png"
image bg_wc              = "backgrounds/bg_wc.png"
image bg_furniture       = "backgrounds/bg_furniture.png"
image bg_security_desk   = "backgrounds/bg_security_desk.png"
image bg_security_room   = "backgrounds/bg_security_room.png"
image bg_garage          = "backgrounds/bg_garage.png"
image bg_cinema          = "backgrounds/bg_cinema.png"
image bg_gym             = "backgrounds/bg_gym.png"
image bg_billiard        = "backgrounds/bg_billiard.png"
image bg_barbershop      = "backgrounds/bg_barbershop.png"
image bg_photo_studio    = "backgrounds/bg_photo_studio.png"
image bg_laundry         = "backgrounds/bg_laundry.png"
image bg_parking         = "backgrounds/bg_parking.png"
# --- Поверх 2 (балкон по колу) ---
image bg_medbay          = "backgrounds/bg_medbay.png"
image bg_recovery_room   = "backgrounds/bg_recovery_room.png"
image bg_pharmacy          = "backgrounds/bg_pharmacy.png"
image bg_room_2          = "backgrounds/bg_room_2.png"
image bg_utility         = "backgrounds/bg_utility.webp"
image bg_video_rental          = "backgrounds/bg_video_rental.png"
image bg_electronics          = "backgrounds/bg_electronics.png"
image bg_jewelry          = "backgrounds/bg_jewelry.png"
image bg_clothing_shop   = "backgrounds/bg_clothing_shop.png"
image bg_backroom        = "backgrounds/bg_backroom.png"
image bg_comp_club       = "backgrounds/bg_comp_club.png"
image bg_cafe            = "backgrounds/bg_cafe.png"
image bg_cafe_balcony    = "backgrounds/bg_cafe_balcony.png"
image bg_balcony         = "backgrounds/bg_balcony.png"
image bg_bookshop        = "backgrounds/bg_bookshop.png"
image bg_warehouse       = "backgrounds/bg_warehouse.webp"
image bg_rooftop         = "backgrounds/bg_rooftop.png"

# ═══ МАППІНГ ЛОКАЦІЙ → ФОНІВ ═══
init python:
    LOCATION_BG = {
        # Поверх 1
        "mall":           "bg_mall",
        "foodcourt":      "bg_foodcourt",
        "info_desk":      "bg_info_desk",
        "arcade":         "bg_arcade",
        "music_shop":     "bg_music_shop",
        "range":          "bg_range",
        "bar":            "bg_bar",
        "wc":             "bg_wc",
        "furniture":      "bg_furniture",
        "security_desk":  "bg_security_desk",
        "security_room":  "bg_security_room",
        "garage":         "bg_garage",
        "cinema":         "bg_cinema",
        "gym":            "bg_gym",
        "billiard":       "bg_billiard",
        "barbershop":     "bg_barbershop",
        "photo_studio":   "bg_photo_studio",
        "laundry":        "bg_laundry",
        "parking":        "bg_parking",
        # Поверх 2
        "medbay":         "bg_medbay",
        "recovery_room":  "bg_recovery_room",
        "pharmacy":         "bg_pharmacy",
        "room_2":         "bg_room_2",
        "utility":        "bg_utility",
        "video_rental":         "bg_video_rental",
        "electronics":         "bg_electronics",
        "jewelry":         "bg_jewelry",
        "clothing_shop":  "bg_clothing_shop",
        "backroom":       "bg_backroom",
        "comp_club":      "bg_comp_club",
        "cafe":           "bg_cafe",
        "cafe_balcony":   "bg_cafe_balcony",
        "balcony":        "bg_balcony",
        "bookshop":       "bg_bookshop",
        "warehouse":      "bg_warehouse",
        "rooftop":        "bg_rooftop",
    }

    # Флаг → локація → новий фон
    BG_OVERRIDES = {
        # "wc_cleaned": {"wc": "bg_wc_clean"},
        # "coffee_machine_found": {"cafe": "bg_cafe_coffee"},
    }

    def show_location_bg(loc=None):
        if loc is None:
            loc = store.current_location
        bg_name = LOCATION_BG.get(loc, "bg_mall")
        # Перевірити оверрайди (останній активний виграє)
        for flag, overrides in BG_OVERRIDES.items():
            if loc in overrides and store.flags.get(flag):
                bg_name = overrides[loc]
        renpy.scene()
        renpy.show(bg_name)

    # === МАППІНГ: кирилиця → image tag ===
    CHAR_IMAGE_TAG = {
        "Артур":   "arthur",
        "Елеонор": "eleanor",
        "Летті":   "lettie",
        "Амір":    "amir",
        "Аоі":     "aoi",
        "Квінсі":  "quince",
    }

    # Позиції для N персонажів в локації
    CHAR_POSITIONS = {
        1: [0.5],
        2: [0.3, 0.7],
        3: [0.2, 0.5, 0.8],
        4: [0.15, 0.38, 0.62, 0.85],
        5: [0.1, 0.3, 0.5, 0.7, 0.9],
        6: [0.05, 0.25, 0.45, 0.55, 0.75, 0.95],
    }

    def show_location_chars():
        """Показує спрайти NPC в поточній локації."""
        chars = get_chars_at(store.current_location)
        n = len(chars)
        if n == 0:
            return
        positions = CHAR_POSITIONS.get(n, CHAR_POSITIONS[6][:n])
        for i, name in enumerate(chars):
            tag = CHAR_IMAGE_TAG.get(name, "arthur")
            xpos = positions[i]
            renpy.show(tag, at_list=[Transform(zoom=char_zoom, xalign=xpos, yalign=1.0)])

    def hide_all_chars():
        """Ховає всі спрайти NPC."""
        for tag in CHAR_IMAGE_TAG.values():
            renpy.hide(tag)

# === ПІДСВІЧУВАННЯ: змінна хто говорить ===
default _speaking_char = None

init -10 python:
    _CHAR_TAGS = {"arthur", "eleanor", "lettie", "amir", "aoi", "quince"}

    def speaker_callback(speaker_tag):
        """Фабрика: callback тільки виставляє хто говорить. Все."""
        def _cb(event, interact=True, **kwargs):
            if not interact:
                return
            if event == "begin":
                store._speaking_char = speaker_tag
            elif event == "end":
                store._speaking_char = None
        return _cb

# ═══ СПРАЙТИ ═══
# ConditionSwitch: якщо хтось говорить і це НЕ я → затемнений.
# Інакше (я говорю АБО ніхто не говорить) → нормальний.

image arthur = ConditionSwitch(
    "_speaking_char is not None and _speaking_char != 'arthur'",
    Transform("character_sprites/Character-Arthur-Hex/knee-test.png", matrixcolor=TintMatrix(Color("#555555"))),
    "True",
    "character_sprites/Character-Arthur-Hex/knee-test.png",
)

image eleanor = ConditionSwitch(
    "_speaking_char is not None and _speaking_char != 'eleanor'",
    Transform("character_sprites/Character-Eleanor-Hex/knee-test.png", matrixcolor=TintMatrix(Color("#555555"))),
    "True",
    "character_sprites/Character-Eleanor-Hex/knee-test.png",
)

image lettie = ConditionSwitch(
    "_speaking_char is not None and _speaking_char != 'lettie'",
    Transform("character_sprites/Character-Lettie-Hex/knee-test.png", matrixcolor=TintMatrix(Color("#555555"))),
    "True",
    "character_sprites/Character-Lettie-Hex/knee-test.png",
)

image amir = ConditionSwitch(
    "_speaking_char is not None and _speaking_char != 'amir'",
    Transform("character_sprites/Character-Amir-Hex/knee-test.png", matrixcolor=TintMatrix(Color("#555555"))),
    "True",
    "character_sprites/Character-Amir-Hex/knee-test.png",
)

image aoi = ConditionSwitch(
    "_speaking_char is not None and _speaking_char != 'aoi'",
    Transform("character_sprites/Character-Aoi-Hex/knee-test.png", matrixcolor=TintMatrix(Color("#555555"))),
    "True",
    "character_sprites/Character-Aoi-Hex/knee-test.png",
)

image quince = ConditionSwitch(
    "_speaking_char is not None and _speaking_char != 'quince'",
    Transform("character_sprites/Character-Quincy-Hex/knee-test.png", matrixcolor=TintMatrix(Color("#555555"))),
    "True",
    "character_sprites/Character-Quincy-Hex/knee-test.png",
)

# ═══ ТРАНСФОРМИ ═══

# Соло/дует — персонаж на ~74% висоти екрана
define char_zoom = 1080.0 / 1456.0        # 0.742

# Група (6 персонажів) — менші, щоб вмістилися
define group_zoom = 1080.0 / 2100.0       # 0.514

transform char_center:
    zoom char_zoom
    xalign 0.5
    yalign 1.0

# Позиції для 2 персонажів
transform left:
    zoom char_zoom
    xalign 0.25
    yalign 1.0

transform right:
    zoom char_zoom
    xalign 0.75
    yalign 1.0

# Позиції для 6 персонажів (інтро, групові сцени) — менший zoom
transform far_left:
    zoom group_zoom
    xalign 0.05
    yalign 1.0

transform center_left:
    zoom group_zoom
    xalign 0.25
    yalign 1.0

transform center:
    zoom group_zoom
    xalign 0.5
    yalign 1.0

transform center_right:
    zoom group_zoom
    xalign 0.7
    yalign 1.0

transform right_of_center:
    zoom group_zoom
    xalign 0.85
    yalign 1.0

transform far_right:
    zoom group_zoom
    xalign 0.95
    yalign 1.0
