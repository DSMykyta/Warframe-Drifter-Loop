## Екрани збереження/завантаження

screen save():
    tag menu
    add "gui/main_menu.png"
    text "ЗБЕРЕГТИ" xpos 80 ypos 30 size 36 color "#d8b4fe" font "fonts/CourierNew-Bold.ttf"

    vbox:
        xpos 60 ypos 90 xsize 1800
        spacing 4

        for i in range(1, 21):
            textbutton "{} — {}".format(i, FileTime(i, format="%d.%m.%Y %H:%M", empty="порожній слот")):
                xfill True
                action FileSave(i, confirm=not FileLoadable(i))
                text_size 20
                text_color "#d946ef"
                text_hover_color "#facc15"
                text_font "fonts/CourierNew-Regular.ttf"

    textbutton "◄ НАЗАД" xpos 60 ypos 1000 action Return() text_size 20 text_color "#8888aa" text_hover_color "#d946ef" text_font "fonts/CourierNew-Bold.ttf"


screen load():
    tag menu
    add "gui/main_menu.png"
    text "ЗАВАНТАЖИТИ" xpos 80 ypos 30 size 36 color "#d8b4fe" font "fonts/CourierNew-Bold.ttf"

    vbox:
        xpos 60 ypos 90 xsize 1800
        spacing 4

        for i in range(1, 21):
            textbutton "{} — {}".format(i, FileTime(i, format="%d.%m.%Y %H:%M", empty="порожній слот")):
                xfill True
                if FileLoadable(i):
                    action FileLoad(i, confirm=False)
                else:
                    action NullAction()
                text_size 20
                text_color "#d946ef"
                text_hover_color "#facc15"
                text_font "fonts/CourierNew-Regular.ttf"

    textbutton "◄ НАЗАД" xpos 60 ypos 1000 action Return() text_size 20 text_color "#8888aa" text_hover_color "#d946ef" text_font "fonts/CourierNew-Bold.ttf"
