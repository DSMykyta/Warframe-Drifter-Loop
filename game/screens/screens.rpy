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

# ── ПЕЙДЖЕР — правий нижній кут (тільки після отримання від Аміра) ──
screen pager_hud():
    zorder 50

    if store.flags.get("has_pager"):
        fixed:
            xpos 1900
            ypos 1060
            xanchor 1.0
            yanchor 1.0
            xsize 400
            ysize 220

            # 1. Фон LCD
            add Solid("#477220", xsize=285, ysize=86) xpos 54 ypos 43

            # 2. LCD вміст (текст)
            fixed:
                xpos 54
                ypos 43
                xsize 285
                ysize 86

                $ _hud_time = get_time_display()
                $ _hud_loc = LOCATION_NAMES.get(current_location, current_location)

                if pager_mode == "request":
                    # ═══ ЗАПИТ ═══
                    text "[pager_request_who]" xpos 6 ypos 4 size 18 color "#131f1f" bold True font "fonts/JetBrainsMono-Bold.ttf"
                    fixed:
                        xpos 6 ypos 22
                        xsize 240 ysize 58
                        text "[pager_request_text]" size 16 color "#131f1f" bold True font "fonts/JetBrainsMono-Bold.ttf"

                elif pager_mode == "message" and pager_messages:
                    # ═══ ПОВІДОМЛЕННЯ ═══
                    $ _pi = min(pager_msg_index, len(pager_messages) - 1)
                    $ _pmsg_entry = pager_messages[_pi]
                    $ _pmsg_who = _pmsg_entry["who"]
                    $ _pmsg_text = _pmsg_entry["text"]
                    $ _pnum = _pi + 1
                    $ _ptotal = len(pager_messages)
                    text "[_pmsg_who]" xpos 6 ypos 4 size 18 color "#131f1f" bold True font "fonts/JetBrainsMono-Bold.ttf"
                    fixed:
                        xpos 6 ypos 22
                        xsize 240 ysize 58
                        text "[_pmsg_text]" size 16 color "#131f1f" bold True font "fonts/JetBrainsMono-Bold.ttf"
                    text "[_pnum]/[_ptotal]" xpos 251 ypos 63 size 18 color "#131f1f" bold True font "fonts/JetBrainsMono-Bold.ttf"

                else:
                    # ═══ СТАТУС ═══
                    text "[_hud_loc]" xpos 6 ypos 8 size 20 color "#131f1f" font "fonts/JetBrainsMono-Regular.ttf"
                    text "[_hud_time]" xpos 6 ypos 38 size 36 color "#131f1f" bold True font "fonts/JetBrainsMono-Bold.ttf"
                    text "[hex_rep]" xpos 240 ypos 50 size 20 color "#131f1f" bold True font "fonts/JetBrainsMono-Bold.ttf"
                    if renpy.loadable("gui/icons/the-hex_pager.png"):
                        add "gui/icons/the-hex_pager.png" xpos 255 ypos 45 zoom 0.4

            # 3. Overlay-effect поверх тексту (обрізаний до LCD)
            add Crop((0, 0, 285, 86), "gui/overlay-effect.png") xpos 54 ypos 43

            # 4. Каркас пейджера (масштабований)
            add "gui/pager.png" zoom 0.4 align (0.0, 0.0)

            # ═══ 3 ФІЗИЧНІ КНОПКИ ═══

            # Кнопка 1 — ліва (зелена): prev / ТАК
            imagebutton:
                xpos 60 ypos 139 xsize 80 ysize 28
                idle Solid("#ffffff00", xsize=80, ysize=28)
                hover Solid("#ffffff18", xsize=80, ysize=28)
                focus_mask True
                if pager_mode == "message":
                    action [SetVariable("pager_msg_index", max(pager_msg_index - 1, 0)), Function(pager_click)]
                elif pager_mode == "request":
                    action Return(("pager_accept", pager_request_accept))
                else:
                    action NullAction()

            # Кнопка 2 — центральна: dismiss / toggle
            imagebutton:
                xpos 153 ypos 139 xsize 80 ysize 28
                idle Solid("#ffffff00", xsize=80, ysize=28)
                hover Solid("#ffffff18", xsize=80, ysize=28)
                focus_mask True
                if pager_mode == "request":
                    action NullAction()
                elif pager_mode == "message":
                    action [SetVariable("pager_mode", "status"), Function(pager_click)]
                elif pager_messages:
                    action [SetVariable("pager_mode", "message"), Function(pager_click)]
                else:
                    action NullAction()

            # Кнопка 3 — права (червона): next / НІ
            imagebutton:
                xpos 246 ypos 139 xsize 80 ysize 28
                idle Solid("#ffffff00", xsize=80, ysize=28)
                hover Solid("#ffffff18", xsize=80, ysize=28)
                focus_mask True
                if pager_mode == "message" and pager_messages:
                    action [SetVariable("pager_msg_index", min(pager_msg_index + 1, len(pager_messages) - 1)), Function(pager_click)]
                elif pager_mode == "request":
                    action Return(("pager_decline", pager_request_decline))
                else:
                    action NullAction()


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
