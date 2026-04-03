# game/screens/screen_map.rpy
# ═══════════════════════════════════════════════════
# ІНТЕРАКТИВНА КАРТА МОЛУ — 2 ПОВЕРХИ ПОРУЧ
# ═══════════════════════════════════════════════════
# Поверх 1 зліва (0-940), Поверх 2 справа (980-1920)

init python:

    # ═══ ПОВЕРХ 1 (зліва) ═══
    MAP_BUTTON_POS_F1 = {
        "mall":          (480, 420),
        "foodcourt":     (544, 200),
        "info_desk":     (645, 200),
        "arcade":        (407, 220),
        "music_shop":    (292, 220),
        "range":         (370, 450),
        "bar":           (416, 680),
        "wc":            (498, 730),
        "furniture":     (627, 450),
        "security_desk": (718, 380),
        "security_room": (810, 330),
        "garage":        (783, 560),
        "cinema":        (168, 180),
        "gym":           (155, 400),
        "billiard":      (168, 580),
        "barbershop":    (223, 740),
        "photo_studio":  (315, 800),
        "laundry":       (627, 700),
        "parking":       (737, 760),
    }

    # ═══ ПОВЕРХ 2 (справа) ═══
    MAP_BUTTON_POS_F2 = {
        "medbay":        (1128, 250),
        "recovery_room": (1128, 370),
        "room_1":        (1238, 160),
        "room_2":        (1353, 120),
        "utility":       (1468, 120),
        "shop_1":        (1578, 160),
        "shop_2":        (1669, 260),
        "shop_3":        (1724, 400),
        "clothing_shop": (1743, 560),
        "backroom":      (1779, 700),
        "comp_club":     (1642, 800),
        "cafe":          (1504, 860),
        "cafe_balcony":  (1504, 760),
        "bookshop":      (1390, 860),
        "warehouse":     (1275, 800),
        "rooftop":       (1147, 680),
        "balcony":       (1440, 500),
    }

    # Об'єднаний словник
    MAP_BUTTON_POS = dict(MAP_BUTTON_POS_F1)
    MAP_BUTTON_POS.update(MAP_BUTTON_POS_F2)

    # На якому поверсі кожна локація
    LOCATION_FLOOR = {}
    for _loc in MAP_BUTTON_POS_F1:
        LOCATION_FLOOR[_loc] = 1
    for _loc in MAP_BUTTON_POS_F2:
        LOCATION_FLOOR[_loc] = 2


screen mall_map():
    modal True

    # Фон
    add Solid("#0a0a14")

    # Сітка
    for _gx in range(0, 1920, 40):
        add Solid("#1a1a3f", xsize=1, ysize=1080) xpos _gx
    for _gy in range(0, 1080, 40):
        add Solid("#1a1a3f", xsize=1920, ysize=1) ypos _gy

    # Роздільник між поверхами
    add Solid("#a855f740", xsize=2, ysize=1000) xpos 960 ypos 40

    # Заголовки поверхів
    text "ПОВЕРХ 1 — АТРІУМ" size 14 color "#a855f780" xpos 470 ypos 50 xanchor 0.5 bold True
    text "ПОВЕРХ 2 — БАЛКОН" size 14 color "#a855f780" xpos 1440 ypos 50 xanchor 0.5 bold True

    # Рамка
    add Solid("#a855f730", xsize=1880, ysize=2) xpos 20 ypos 30
    add Solid("#a855f730", xsize=1880, ysize=2) xpos 20 ypos 1050
    add Solid("#a855f730", xsize=2, ysize=1020) xpos 20 ypos 30
    add Solid("#a855f730", xsize=2, ysize=1020) xpos 1898 ypos 30

    # Годинник
    $ _time_str = get_time_display()
    frame:
        background "#00000088"
        xpos 50 ypos 60 padding (10, 4, 10, 4)
        text "[_time_str]" size 22 color "#22d3ee" bold True

    # ═══ Кнопки локацій — обидва поверхи одразу ═══
    for _loc_id, _pos in MAP_BUTTON_POS_F1.items():
        use map_btn(_loc_id, _pos[0], _pos[1])

    for _loc_id, _pos in MAP_BUTTON_POS_F2.items():
        use map_btn(_loc_id, _pos[0], _pos[1])

    # Закрити
    button:
        xpos 1860 ypos 50 xanchor 1.0
        action Return()
        frame:
            background "#00000088"
            padding (8, 4, 8, 4)
            text "X" size 22 color "#fca5a5" bold True


# ═══ Іконки локацій ═══
init python:
    LOCATION_ICONS = {
        "mall":           "gui/icons/mall_white.png",
        "info_desk":      "gui/icons/info_desk_white.png",
        "security_desk":  "gui/icons/security_desk_white.png",
        "security_room":  "gui/icons/security_room_white.png",
        "arcade":         "gui/icons/arcade_white.png",
        "music_shop":     "gui/icons/music_shop_white.png",
        "furniture":      "gui/icons/furniture_white.png",
        "range":          "gui/icons/range_white.png",
        "bar":            "gui/icons/bar_white.png",
        "foodcourt":      "gui/icons/foodcourt_white.png",
        "garage":         "gui/icons/garage_white.png",
        "cinema":         "gui/icons/cinema_white.png",
        "gym":            "gui/icons/gym_white.png",
        "billiard":       "gui/icons/billiard_white.png",
        "barbershop":     "gui/icons/barbershop_white.png",
        "photo_studio":   "gui/icons/photo_studio_white.png",
        "laundry":        "gui/icons/laundry_white.png",
        "parking":        "gui/icons/parking_white.png",
        "wc":             "gui/icons/wc_white.png",
        "medbay":         "gui/icons/medbay_white.png",
        "recovery_room":  "gui/icons/room_white.png",
        "room_1":         "gui/icons/room_white.png",
        "room_2":         "gui/icons/room_white.png",
        "utility":        "gui/icons/utility_white.png",
        "shop_1":         "gui/icons/shop_white.png",
        "shop_2":         "gui/icons/shop_white.png",
        "shop_3":         "gui/icons/shop_white.png",
        "clothing_shop":  "gui/icons/clothing_shop_white.png",
        "backroom":       "gui/icons/backroom_white.png",
        "comp_club":      "gui/icons/comp_club_white.png",
        "cafe":           "gui/icons/cafe_white.png",
        "cafe_balcony":   "gui/icons/cafe_white.png",
        "bookshop":       "gui/icons/bookshop_white.png",
        "balcony":        "gui/icons/balcony_white.png",
        "warehouse":      "gui/icons/warehouse_white.png",
        "rooftop":        "gui/icons/rooftop_white.png",
    }

# ═══ Кнопка однієї локації ═══
screen map_btn(loc_id, bx, by):
    $ _loc_label = LOCATION_NAMES.get(loc_id, loc_id)
    $ _cost = travel_cost(current_location, loc_id)
    $ _chars = get_chars_at(loc_id)
    $ _is_current = (current_location == loc_id)
    $ _chars_text = ", ".join(_chars) if _chars else ""
    $ _locked = is_locked(loc_id)
    $ _hidden = is_hidden(loc_id)
    $ _icon = LOCATION_ICONS.get(loc_id)

    if not _hidden:
        button:
            xpos bx ypos by xanchor 0.5 yanchor 0.5
            if _is_current:
                background "#a855f760"
            elif _locked:
                background "#09090faa"
            else:
                background "#09090fcc"
                hover_background "#a855f750"
            padding (8, 5, 8, 5)

            if _is_current or _locked:
                action NullAction()
            else:
                action [Function(travel_to, loc_id), Return()]

            vbox:
                spacing 1
                hbox:
                    spacing 4
                    yalign 0.5
                    if _locked:
                        if renpy.loadable("gui/icons/lock_white.png"):
                            add "gui/icons/lock_white.png" zoom 0.6 yalign 0.5
                    elif _icon and renpy.loadable(_icon):
                        add _icon zoom 0.6 yalign 0.5
                    text "[_loc_label]" size 11 color ("#666666" if _locked else "#d8b4fe") bold True
                    if _is_current:
                        text "ТУТ" size 9 color "#facc15" bold True
                    elif not _locked and _cost > 0:
                        text "[_cost]хв" size 9 color "#22d3ee"
                if _chars_text and not _locked:
                    text "[_chars_text]" size 9 color "#ffffffa0"
