# screen_say.rpy — HEX KIM-CHAT STYLE
# ═══════════════════════════════════════

# Елеонор — телепатичний текст: з'являється, трохи пливе
transform eleanor_telepathy:
    alpha 0.0 yoffset 10
    ease 0.5 alpha 1.0 yoffset 0
    linear 3.0 yoffset -5
    linear 3.0 yoffset 5


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

    # ── Елеонор — телепатія: текст по центру, без вікна ──
    if who == "Елеонор":
        text what id "what":
            size 28
            color "#d8b4fe"
            outlines [(2, "#1a0a2e", 0, 0), (1, "#3a1a5a", 1, 1)]
            xalign 0.5
            yalign 0.45
            text_align 0.5
            xmaximum 900
            italic True
            at eleanor_telepathy

    # ── Решта персонажів — звичайний діалог ──
    else:
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
