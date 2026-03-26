# game/screen_map.rpy
# ═══════════════════════════════════════════════════
# ІНТЕРАКТИВНА КАРТА МОЛУ
# ═══════════════════════════════════════════════════
# Текстова версія (без focus_mask поки немає арт-ассетів)
# Буде замінена на imagebutton + focus_mask коли з'являться зображення

screen mall_map():
    modal True

    use hud

    # Фон
    add Solid("#09090fee")

    vbox:
        align (0.5, 0.08)
        text "КАРТА МОЛУ" size 24 color "#a855f7" xalign 0.5 bold True
        $ _time_str = get_time_display()
        text "[_time_str]" size 18 color "#22d3ee" xalign 0.5

    # Сітка локацій
    vpgrid:
        align (0.5, 0.5)
        cols 4
        spacing 12
        xmaximum 1400

        for _loc_id in ["backroom", "mall", "info_desk", "info_room", "arcade", "music_shop", "furniture", "range", "medbay", "bar", "foodcourt", "comp_club", "garage", "rooftop"]:
            $ _loc_label = LOCATION_NAMES.get(_loc_id, _loc_id)
            $ _cost = travel_cost(current_location, _loc_id)
            $ _chars = get_chars_at(_loc_id)
            $ _is_current = (current_location == _loc_id)

            button:
                xminimum 300
                yminimum 120
                if _is_current:
                    background "#a855f740"
                else:
                    background "#a855f715"
                    hover_background "#a855f730"
                padding (16, 12, 16, 12)

                if _is_current:
                    action NullAction()
                else:
                    action [Function(travel_to, _loc_id), Return()]

                vbox:
                    spacing 4

                    hbox:
                        spacing 8
                        text "[_loc_label]" size 16 color "#d8b4fe" bold True
                        if _is_current:
                            text "(тут)" size 12 color "#facc15"
                        elif _cost > 0:
                            text "[_cost] хв" size 12 color "#22d3ee"

                    # Персонажі в локації
                    if _chars:
                        $ _chars_text = ", ".join(_chars)
                        text "[_chars_text]" size 13 color "#ffffff60"
                    else:
                        if is_night():
                            text "порожньо" size 13 color "#ffffff20"
                        else:
                            text "нікого" size 13 color "#ffffff20"

    # Кнопка закриття
    button:
        xpos 0.96
        ypos 0.06
        xanchor 1.0
        action Return()
        text "Закрити" size 16 color "#fca5a5"
