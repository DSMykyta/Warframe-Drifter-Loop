# game/screen_map.rpy
# ═══════════════════════════════════════════════════
# ІНТЕРАКТИВНА КАРТА МОЛУ
# ═══════════════════════════════════════════════════
# Фон: backgrounds/map_mall.png (1920x1080, малюєш сам)
# Кнопки кімнат розміщені на абсолютних координатах поверх фону.
# Щоб змінити позицію кнопки — міняй числа в MAP_BUTTON_POS.

init python:
    # Координати кнопок: loc_id → (x, y)
    # Підганяй під свій малюнок
    MAP_BUTTON_POS = {
        "rooftop":    (890, 80),
        "backroom":   (115, 225),
        "music_shop": (465, 215),
        "arcade":     (285, 345),
        "mall":       (860, 470),
        "foodcourt":  (990, 300),
        "info_desk":  (1300, 215),
        "security_desk":  (1555, 130),
        "security_room":  (1700, 80),
        "range":      (185, 530),
        "medbay":     (355, 645),
        "bar":        (700, 790),
        "furniture":  (1085, 625),
        "comp_club":  (1330, 505),
        "garage":     (1570, 610),
        "balcony":    (660, 200),
        "cafe":       (500, 470),
        "cafe_balcony": (500, 340),
        "utility":    (1400, 790),
        "warehouse":  (1600, 790),
    }

screen mall_map():
    modal True

    # Фон — твій малюнок (заміни на свій файл)
    # Поки fallback на темний фон
    if renpy.loadable("backgrounds/map_mall.png"):
        add "backgrounds/map_mall.png"
    else:
        # Тимчасовий темний фон
        add Solid("#0a0a14")
        # Сітка
        for _gx in range(0, 1920, 40):
            add Solid("#1a1a3f", xsize=1, ysize=1080) xpos _gx
        for _gy in range(0, 1080, 40):
            add Solid("#1a1a3f", xsize=1920, ysize=1) ypos _gy
        # Рамка
        add Solid("#a855f730", xsize=1880, ysize=2) xpos 20 ypos 20
        add Solid("#a855f730", xsize=1880, ysize=2) xpos 20 ypos 1058
        add Solid("#a855f730", xsize=2, ysize=1040) xpos 20 ypos 20
        add Solid("#a855f730", xsize=2, ysize=1040) xpos 1898 ypos 20
        text "HOLLVANIA CENTRAL MALL — FLOOR PLAN" size 12 color "#a855f760" xpos 960 ypos 35 xanchor 0.5

    # Годинник
    $ _time_str = get_time_display()
    frame:
        background "#00000088"
        xpos 50 ypos 50 padding (10, 4, 10, 4)
        text "[_time_str]" size 22 color "#22d3ee" bold True

    # Кнопки локацій
    for _loc_id, _pos in MAP_BUTTON_POS.items():
        use map_btn(_loc_id, _pos[0], _pos[1])

    # Закрити
    button:
        xpos 1860 ypos 50 xanchor 1.0
        action Return()
        frame:
            background "#00000088"
            padding (8, 4, 8, 4)
            text "X" size 22 color "#fca5a5" bold True


# ═══ Кнопка однієї локації ═══
screen map_btn(loc_id, bx, by):
    $ _loc_label = LOCATION_NAMES.get(loc_id, loc_id)
    $ _cost = travel_cost(current_location, loc_id)
    $ _chars = get_chars_at(loc_id)
    $ _is_current = (current_location == loc_id)
    $ _chars_text = ", ".join(_chars) if _chars else ""

    button:
        xpos bx ypos by
        if _is_current:
            background "#a855f760"
        else:
            background "#09090fcc"
            hover_background "#a855f750"
        padding (10, 6, 10, 6)
        xminimum 150

        if _is_current:
            action NullAction()
        else:
            action [Function(travel_to, loc_id), Return()]

        vbox:
            spacing 2
            hbox:
                spacing 6
                text "[_loc_label]" size 13 color "#d8b4fe" bold True
                if _is_current:
                    text "ТУТ" size 10 color "#facc15" bold True
                elif _cost > 0:
                    text "[_cost]хв" size 10 color "#22d3ee"
            if _chars_text:
                text "[_chars_text]" size 11 color "#ffffffa0"
