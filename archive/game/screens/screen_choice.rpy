# screen_choice.rpy — Екран вибору в стилі HEX
# ═══════════════════════════════════════

screen choice(items):

    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.6
        spacing 8

        for i in items:
            textbutton i.caption action i.action

# ═══ СТИЛІ ═══

style choice_vbox:
    xminimum 400
    xmaximum 700

style choice_button:
    background "#09090fdd"
    hover_background "#1a1a3fdd"
    padding (24, 12, 24, 12)
    xfill True

style choice_button_text:
    color "#d4cfc6"
    hover_color "#ffffff"
    size 22
    xalign 0.5
    text_align 0.5
