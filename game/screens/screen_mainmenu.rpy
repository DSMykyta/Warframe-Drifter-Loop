## Екран головного меню ##########################################################

screen main_menu():

    tag menu

    add gui.main_menu_background

    ## Центрований блок заголовку
    vbox:
        xalign 0.5
        yalign 0.35
        spacing 10

        text "W A R F R A M E":
            xalign 0.5
            size 28
            color "#8888aa"
            font "fonts/CourierNew-Regular.ttf"
            kerning 2.0

        text "1999":
            xalign 0.5
            size 120
            font "fonts/CourierNew-Bold.ttf"
            color "#d946ef"

        text "T H E   H E X":
            xalign 0.5
            size 28
            color "#8888aa"
            font "fonts/CourierNew-Regular.ttf"
            kerning 2.0

        null height 15

        text "Твольванія. Останній день 1999. Реактор.\nШестеро протофреймів. Один рік. Один шанс.":
            xalign 0.5
            text_align 0.5
            size 18
            color "#555570"
            font "fonts/CourierNew-Regular.ttf"

    ## Центровані кнопки
    vbox:
        xalign 0.5
        yalign 0.72
        spacing 10

        textbutton _("► ПОЧАТИ НОВУ"):
            xalign 0.5
            action Start()
            style "mm_start_button"

    ## Нижні кнопки меню
    hbox:
        xalign 0.5
        yalign 0.85
        spacing 40

        textbutton _("Завантажити"):
            action ShowMenu("load")
            style "mm_nav_button"

        textbutton _("Налаштування"):
            action ShowMenu("preferences")
            style "mm_nav_button"

        textbutton _("Про гру"):
            action ShowMenu("about")
            style "mm_nav_button"

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            textbutton _("Вийти"):
                action Quit(confirm=False)
                style "mm_nav_button"


## Стилі

style mm_start_button:
    xminimum 500
    ypadding 18
    xpadding 40
    background Frame("gui/button/mm_start_idle.png", 14, 14)
    hover_background Frame("gui/button/mm_start_hover.png", 14, 14)

style mm_start_button_text:
    xalign 0.5
    font "fonts/CourierNew-Bold.ttf"
    size 30
    color "#d8b4fe"
    hover_color "#facc15"

style mm_nav_button:
    background None
    hover_background None

style mm_nav_button_text:
    font "fonts/CourierNew-Regular.ttf"
    size 20
    color "#555570"
    hover_color "#d946ef"
