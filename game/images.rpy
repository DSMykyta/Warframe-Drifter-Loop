# images.rpy  ───────────────────────────────────────

# якщо ще не вказував розмір екрана
define config.screen_width  = 1920
define config.screen_height = 1080

# === ФОНИ ===
image bg mall = "backgrounds/Hollvania_Central_Mall.webp"
image bg_arcade = "backgrounds/bg_arcade.png"
image bg_backroom = "backgrounds/bg_backroom.png"
image bg_bar = "backgrounds/bg_bar.jpg"
image bg_comp_club = "backgrounds/bg_comp_club.png"
image bg_foodcourt = "backgrounds/bg_foodcourt.png"
image bg_furniture = "backgrounds/bg_furniture.png"
image bg_info_desk = "backgrounds/bg_info_desk.png"
image bg_medbay = "backgrounds/bg_medbay.png"
image bg_music_shop = "backgrounds/bg_music_shop.png"
image bg_range = "backgrounds/bg_range.png"

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
