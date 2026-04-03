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

# ── ВЕРХНЄ МЕНЮ — вкладки ──
screen hud():
    zorder 50

    frame:
        xfill True
        ysize 50
        xpos 0
        ypos 0
        background "#0d0d1ae0"
        padding (20, 0, 20, 0)

        hbox:
            yalign 0.5
            spacing 6

            # Вкладки
            for _tab in [("map", "КАРТА"), ("journal", "ЩОДЕННИК"), ("insights", "ШАФА ДУМОК"), ("shop", "ІНВЕНТАР"), ("gallery", "ГАЛЕРЕЯ")]:
                button:
                    padding (16, 8, 16, 8)
                    background "#ffffff08"
                    hover_background "#a855f730"
                    action Return(_tab[0])
                    text _tab[1] size 13 color "#d8b4fe" bold True

        # Системні кнопки (справа)
        hbox:
            xalign 1.0
            yalign 0.5
            spacing 16
            textbutton "Зберегти" action ShowMenu("save") text_size 12 text_color "#ffffff30" text_hover_color "#facc15"
            textbutton "Завантажити" action ShowMenu("load") text_size 12 text_color "#ffffff30" text_hover_color "#facc15"
            textbutton "Меню" action MainMenu() text_size 12 text_color "#ffffff30" text_hover_color "#fca5a5"

# ── Звуки пейджера ──
define audio.pager_beep = "<to 2.1>audio/pager_beep.mp3"
define audio.pager_click = "audio/pager_click.mp3"

# ── ПЕЙДЖЕР ПЕРЕНЕСЕНО В screen_pager_fix.rpy ──


# ═══════════════════════════════════
# LOCATION UI — екран взаємодії з поточною локацією
# ═══════════════════════════════════

screen location_ui():
    # hud і pager_hud показуються через show screen в script.rpy
    use scanlines

    # Назва локації
    $ _loc_name = LOCATION_NAMES.get(current_location, current_location)

    vbox:
        align (0.5, 0.4)
        spacing 12

        text "[_loc_name]" size 28 color "#d8b4fe" xalign 0.5 bold True

        null height 10

        # Персонажі в локації — клікабельні імена (спрайти показуються через show_location_chars)
        $ _chars_here = get_chars_at(current_location)

        if _chars_here:
            for _ch in _chars_here:
                button:
                    style "hex_btn"
                    xalign 0.5
                    xminimum 200
                    action Return(("interact", _ch))
                    text "[_ch]" size 20 color "#d8b4fe"
        else:
            if is_night():
                text "Порожньо. Всі пішли." size 16 color "#ffffff30" xalign 0.5
            else:
                text "Тут нікого." size 16 color "#ffffff30" xalign 0.5

    # Контекстні кнопки (по центру під персонажами)
    hbox:
        align (0.5, 0.75)
        spacing 16

        # Карта (тільки після знахідки)
        if store.flags.get("has_map"):
            button:
                style "hex_btn"
                action Return("map")
                text "Карта" size 18 color "#d8b4fe"

        # Місії (тільки в гаражі)
        if current_location == "garage":
            button:
                style "hex_btn"
                action Return("missions")
                text "Місії" size 18 color "#fca5a5"

        # Автомат (тільки в кав'ярні)
        if current_location == "cafe" and store.flags.get("coffee_machine_found"):
            button:
                style "hex_btn"
                action Return("coffee")
                text "Автомат" size 18 color "#facc15"

        # Зачекати (не вночі)
        if not is_night():
            button:
                style "hex_btn"
                action Return("wait")
                text "Зачекати" size 18 color "#a5f3fc"

    # Спати (тільки в бекрумі)
    if current_location == "backroom":
        button:
            style "hex_btn_accent"
            xpos 0.96
            ypos 0.85
            xanchor 1.0
            yanchor 1.0
            action Return("sleep")
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
