# images.rpy  ───────────────────────────────────────

# якщо ще не вказував розмір екрана
define config.screen_width  = 1920
define config.screen_height = 1080

# === ФОНИ ===
image bg mall = "backgrounds/Hollvania_Central_Mall.webp"
image bg_arcade = "backgrounds/bg_arcade.png"
image bg_backroom = "backgrounds/bg_backroom.png"
image bg_bar = "backgrounds/bg_bar.png"
image bg_comp_club = "backgrounds/bg_comp_club.png"
image bg_foodcourt = "backgrounds/bg_foodcourt.png"
image bg_furniture = "backgrounds/bg_furniture.png"
image bg_info_desk = "backgrounds/bg_info_desk.png"
image bg_medbay = "backgrounds/bg_medbay.png"
image bg_music_shop = "backgrounds/bg_music_shop.png"
image bg_range = "backgrounds/bg_range.png"

# === ФОНИ (раніше були плейсхолдери) ===
image bg_info_counter = "backgrounds/bg_info_counter.png"
image bg_garage = "backgrounds/bg_garage.png"
image bg_rooftop = Solid("#0a1a2a")
image bg_mall = "backgrounds/bg-hub-mall.jpg"
image bg_mall_foodcourt = "backgrounds/bg_foodcourt.png"

# === НОВІ ЛОКАЦІЇ ===
image bg_balcony = "backgrounds/bg_balcony.png"
image bg_cafe = "backgrounds/bg_cafe.png"
image bg_cafe_balcony = "backgrounds/bg_cafe_balcony.png"
image bg_utility = "backgrounds/bg_utility.webp"
image bg_warehouse = "backgrounds/bg_warehouse.webp"

# === МАППІНГ ЛОКАЦІЙ → ФОНІВ ===
init python:
    LOCATION_BG = {
        "mall":       "bg mall",
        "arcade":     "bg_arcade",
        "backroom":   "bg_backroom",
        "bar":        "bg_bar",
        "comp_club":  "bg_comp_club",
        "foodcourt":  "bg_foodcourt",
        "furniture":  "bg_furniture",
        "info_desk":  "bg_info_desk",
        "info_counter": "bg_info_counter",
        "medbay":     "bg_medbay",
        "music_shop": "bg_music_shop",
        "range":      "bg_range",
        "garage":     "bg_garage",
        "rooftop":    "bg_rooftop",
        "balcony":    "bg_balcony",
        "cafe":       "bg_cafe",
        "cafe_balcony": "bg_cafe_balcony",
        "utility":    "bg_utility",
        "warehouse":  "bg_warehouse",
    }

    def show_location_bg(loc=None):
        if loc is None:
            loc = store.current_location
        bg_name = LOCATION_BG.get(loc, "bg mall")
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

# === СПРАЙТИ ===
# ConditionSwitch: якщо хтось говорить і це НЕ я → затемнений.
# Інакше (я говорю АБО ніхто не говорить) → нормальний.
# Позиції (at far_left, at center тощо) залишаються незмінними!

image arthur = ConditionSwitch(
    "_speaking_char is not None and _speaking_char != 'arthur'",
    Transform("character_sprites/Arthur.png", matrixcolor=TintMatrix(Color("#555555"))),
    "True",
    "character_sprites/Arthur.png",
)

image eleanor = ConditionSwitch(
    "_speaking_char is not None and _speaking_char != 'eleanor'",
    Transform("character_sprites/Eleanor.png", matrixcolor=TintMatrix(Color("#555555"))),
    "True",
    "character_sprites/Eleanor.png",
)

image lettie = ConditionSwitch(
    "_speaking_char is not None and _speaking_char != 'lettie'",
    Transform("character_sprites/Lettie.png", matrixcolor=TintMatrix(Color("#555555"))),
    "True",
    "character_sprites/Lettie.png",
)

image amir = ConditionSwitch(
    "_speaking_char is not None and _speaking_char != 'amir'",
    Transform("character_sprites/Amir.png", matrixcolor=TintMatrix(Color("#555555"))),
    "True",
    "character_sprites/Amir.png",
)

image aoi = ConditionSwitch(
    "_speaking_char is not None and _speaking_char != 'aoi'",
    Transform("character_sprites/Aoi.png", matrixcolor=TintMatrix(Color("#555555"))),
    "True",
    "character_sprites/Aoi.png",
)

image quince = ConditionSwitch(
    "_speaking_char is not None and _speaking_char != 'quince'",
    Transform("character_sprites/Quincy.png", matrixcolor=TintMatrix(Color("#555555"))),
    "True",
    "character_sprites/Quincy.png",
)

# === ТРАНСФОРМИ ===

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
