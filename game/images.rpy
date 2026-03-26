# images.rpy  ───────────────────────────────────────

# якщо ще не вказував розмір екрана
define config.screen_width  = 1920
define config.screen_height = 1080

# === ФОНИ ===
image bg mall = "backgrounds/Hollvania_Central_Mall.webp"
image bg_mall_foodcourt = "backgrounds/Hollvania_Central_Mall.webp"  # TODO: окремий фон футкорту
image bg_backroom = "backgrounds/Hollvania_Central_Mall.webp"        # TODO: окремий фон бекруму

# === СПРАЙТИ (базові пози) ===
image arthur  = "character_sprites/Arthur.png"
image eleanor = "character_sprites/Eleanor.png"
image letty   = "character_sprites/Lettie.png"
image amir    = "character_sprites/Amir.png"
image aoi     = "character_sprites/Aoi.png"
image quince  = "character_sprites/Quincy.png"

# === ТРАНСФОРМИ ===
define char_zoom = 1080.0 / 1456.0        # 0.742

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

# Позиції для 6 персонажів (інтро, групові сцени)
transform far_left:
    zoom char_zoom
    xalign 0.05
    yalign 1.0

transform center_left:
    zoom char_zoom
    xalign 0.3
    yalign 1.0

transform center:
    zoom char_zoom
    xalign 0.5
    yalign 1.0

transform center_right:
    zoom char_zoom
    xalign 0.7
    yalign 1.0

transform far_right:
    zoom char_zoom
    xalign 0.95
    yalign 1.0
