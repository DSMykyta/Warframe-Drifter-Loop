# screens.rpy
# ═══════════════════════════════════


## Екран навігації #################################################################

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Почати") action Start()

        else:

            textbutton _("Історія") action ShowMenu("history")

            textbutton _("Зберегти") action ShowMenu("save")

        textbutton _("Завантажити") action ShowMenu("load")

        textbutton _("Налаштування") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("Закінчити повтор") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Головне меню") action MainMenu()

        textbutton _("Про гру") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            textbutton _("Допомога") action ShowMenu("help")

            textbutton _("Вийти") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation")

style navigation_button_text:
    properties gui.button_text_properties("navigation")


# ═══════════════════════════════════
# Кастомні ігрові екрани
# ═══════════════════════════════════

# ── Scanlines overlay (постійно на екрані) ──
screen scanlines():
    zorder 100
    add "#00000000"  # прозора основа
    for i in range(0, 1080, 4):
        add Solid("#00000014", xsize=1920, ysize=2) ypos i

# ── HUD — верхня панель ──
screen hud():
    zorder 50

    frame:
        xfill True
        ysize 60
        xpos 0
        ypos 0
        background "#00000099"
        padding (20, 10, 20, 10)

        hbox:
            yalign 0.5
            spacing 40

            # День
            hbox:
                spacing 8
                text "ДЕНЬ" size 16 color "#ffffff40"
                text "[day]" size 22 color "#facc15" bold True

            # Гроші
            hbox:
                spacing 8
                text "КРОНИ" size 16 color "#ffffff40"
                text "[money]" size 22 color "#facc15" bold True

            # Час (хвилини)
            hbox:
                spacing 8
                text "ЧАС" size 16 color "#ffffff40"
                $ _hud_time = get_time_display()
                text "[_hud_time]" size 22 color "#22d3ee" bold True

            # Локація
            hbox:
                spacing 8
                text "ЛОКАЦІЯ" size 16 color "#ffffff40"
                $ _hud_loc = LOCATION_NAMES.get(current_location, current_location)
                text "[_hud_loc]" size 18 color "#a5f3fc"

        # Права частина HUD
        hbox:
            xalign 1.0
            yalign 0.5
            spacing 20

            # Репутація Гекс
            hbox:
                spacing 8
                text "HEX" size 16 color "#ffffff40"
                text "[hex_rep]" size 22 color "#a855f7" bold True

            # Системні кнопки
            textbutton "Зберегти" action ShowMenu("save") text_size 14 text_color "#ffffff40" text_hover_color "#facc15"
            textbutton "Завантажити" action ShowMenu("load") text_size 14 text_color "#ffffff40" text_hover_color "#facc15"
            textbutton "Меню" action MainMenu() text_size 14 text_color "#ffffff40" text_hover_color "#fca5a5"


# ═══════════════════════════════════
# LOCATION UI — екран взаємодії з поточною локацією
# ═══════════════════════════════════

screen location_ui():

    use hud
    use scanlines
    use pager

    # Назва локації
    $ _loc_name = LOCATION_NAMES.get(current_location, current_location)

    vbox:
        align (0.5, 0.4)
        spacing 12

        text "[_loc_name]" size 28 color "#d8b4fe" xalign 0.5 bold True

        null height 10

        # Персонажі в локації
        $ _chars_here = get_chars_at(current_location)

        if _chars_here:
            text "Присутні:" size 14 color "#ffffff40" xalign 0.5

            for _ch in _chars_here:
                button:
                    style "hex_btn"
                    xalign 0.5
                    xminimum 280
                    action Return(("talk", _ch))
                    hbox:
                        spacing 8
                        xalign 0.5
                        text "Поговорити з [_ch]" size 18 color "#d8b4fe"
        else:
            if is_night():
                text "Порожньо. Всі пішли." size 16 color "#ffffff30" xalign 0.5
            else:
                text "Тут нікого." size 16 color "#ffffff30" xalign 0.5

    # Нижня панель кнопок
    hbox:
        align (0.5, 0.92)
        spacing 16

        # Карта
        button:
            style "hex_btn"
            action Return("map")
            hbox:
                spacing 8
                text "Карта" size 18 color "#d8b4fe"

        # Місії (тільки в гаражі)
        if current_location == "garage":
            button:
                style "hex_btn"
                action Return("missions")
                hbox:
                    spacing 8
                    text "Місії" size 18 color "#fca5a5"

        # Магазин
        button:
            style "hex_btn"
            action Return("shop")
            hbox:
                spacing 8
                text "Магазин" size 18 color "#d4a5f7"

        # Щоденник
        button:
            style "hex_btn"
            action Return("journal")
            hbox:
                spacing 8
                text "Щоденник" size 18 color "#a5f3fc"

        # Шафа думок — перегляд фактів завжди, обдумування тільки в бекрумі
        button:
            style "hex_btn"
            action Return("insights")
            hbox:
                spacing 8
                text "Шафа думок" size 18 color "#d8b4fe"
                if has_raw_thoughts() and current_location == "backroom":
                    text "!" size 18 color "#facc15" bold True

        # Зачекати (не вночі)
        if not is_night():
            button:
                style "hex_btn"
                action Return("wait")
                hbox:
                    spacing 8
                    text "Зачекати" size 18 color "#a5f3fc"

    # Спати (тільки в бекрумі)
    if current_location == "backroom":
        button:
            style "hex_btn_accent"
            xpos 0.96
            ypos 0.94
            xanchor 1.0
            yanchor 1.0
            action Return("sleep")
            hbox:
                spacing 8
                text "Спати" size 20 color "#facc15"


# ═══ СТИЛІ КНОПОК ═══

style hex_btn:
    background "#a855f720"
    hover_background "#a855f740"
    padding (20, 14, 20, 14)
    minimum (140, 50)

style hex_btn_disabled is hex_btn:
    background "#ffffff08"

style hex_btn_accent:
    background "#facc1520"
    hover_background "#facc1540"
    padding (24, 14, 24, 14)

style hex_btn_text:
    color "#d8b4fe"
    size 20

style hex_btn_disabled_text:
    color "#ffffff25"
    size 20
