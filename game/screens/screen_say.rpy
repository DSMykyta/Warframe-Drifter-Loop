# screen_say.rpy — HEX KIM-CHAT STYLE
# ═══════════════════════════════════════

screen say(who, what):

    style_prefix "say"

    # Визначаємо стиль namebox за іменем персонажа
    $ nb_style = "namebox_mc" if who == "Дрифтер" else "namebox_npc"

    # Визначаємо колір бордера за персонажем
    python:
        _hex_colors = {
            "Артур": "#4a7cff", "Елеонор": "#a855f7", "Летті": "#22d3ee",
            "Амір": "#facc15", "Аоі": "#d946ef", "Квінсі": "#ef4444",
            "Дрифтер": "#a855f7",
        }
        _border_color = _hex_colors.get(who, "#a855f7")

    # ── Весь блок діалогу внизу ──
    vbox:
        yalign 0.88
        xalign 0.5
        spacing 0

        # ── KIM мітка (як в hex-vn.jsx) ──
        hbox:
            xalign 0.5
            spacing 12

            # Ім'я
            if who:
                window:
                    style nb_style
                    text who id "who" size 22 bold True

            # KIM індикатор
            text "KIM" size 12 color "#ffffff30" yalign 0.5

        # ── Текст діалогу ──
        window:
            style "say_window"
            text what id "what" size 24 color "#d4cfc6"
