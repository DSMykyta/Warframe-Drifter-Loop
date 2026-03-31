## Екрани збереження/завантаження

screen save():
    tag menu
    add "gui/main_menu.png"
    text "ЗБЕРЕЖЕННЯ" xpos 120 ypos 62 size 120 color "#d8b4fe" font "fonts/CourierNew-Bold.ttf"

    viewport:
        xpos 120 ypos 200 xsize 1000 ysize 750
        mousewheel True
        scrollbars "vertical"

        vbox:
            spacing 12

            # Автосейв
            if FileLoadable("auto-1"):
                button:
                    background "gui/save/save_slot_auto.png"
                    hover_background "gui/save/save_slot_auto.png"
                    xsize 1000 ysize 100
                    action NullAction()
                    text FileTime("auto-1", format="%d.%m.%Y", empty="") xpos 24 ypos 24 size 24 color "#1a1a2e" font "fonts/CourierNew-Regular.ttf"
                    text FileTime("auto-1", format="%H:%M", empty="") xpos 24 ypos 58 size 24 color "#1a1a2e" font "fonts/CourierNew-Regular.ttf"
                    text FileSaveName("auto-1", empty="") xpos 210 ypos 24 size 24 color "#1a1a2e" font "fonts/CourierNew-Bold.ttf"
                    text "АВТО" xpos 900 ypos 38 size 18 color "#1a1a2e" bold True font "fonts/CourierNew-Bold.ttf"

            # Ручні слоти
            for i in range(1, 21):
                $ _slot_bg = "gui/save/save_slot_hover.png" if FileLoadable(i) else "gui/save/save_slot.png"
                $ _slot_name_color = "#d8b4fe" if FileLoadable(i) else "#d946ef"
                $ _slot_name_text = FileSaveName(i, empty="") if FileLoadable(i) else "порожній слот"
                $ _slot_name_font = "fonts/CourierNew-Bold.ttf" if FileLoadable(i) else "fonts/CourierNew-Regular.ttf"
                button:
                    background _slot_bg
                    hover_background "gui/save/save_slot_hover.png"
                    xsize 1000 ysize 100
                    action FileSave(i, confirm=FileLoadable(i))
                    text FileTime(i, format="%d.%m.%Y", empty="—") xpos 24 ypos 24 size 24 color "#8888aa" font "fonts/CourierNew-Regular.ttf"
                    text FileTime(i, format="%H:%M", empty="") xpos 24 ypos 58 size 24 color "#8888aa" font "fonts/CourierNew-Regular.ttf"
                    text _slot_name_text xpos 210 ypos 24 size 24 color _slot_name_color font _slot_name_font

    add "gui/save/save_side_block.png" xpos 1280 ypos 200
    vbox:
        xpos 1300 ypos 220 spacing 10
        text "ІНФОРМАЦІЯ" size 24 color "#d8b4fe" font "fonts/CourierNew-Bold.ttf"
        null height 10
        text "Ранг: —" size 18 color "#8888aa" font "fonts/CourierNew-Regular.ttf"
        text "Крони: —" size 18 color "#8888aa" font "fonts/CourierNew-Regular.ttf"
        text "HEX: —" size 18 color "#8888aa" font "fonts/CourierNew-Regular.ttf"

    textbutton "◄ НАЗАД" xpos 120 ypos 980 action Return() text_size 20 text_color "#8888aa" text_hover_color "#d946ef" text_font "fonts/CourierNew-Bold.ttf"


screen load():
    tag menu
    add "gui/main_menu.png"
    text "ЗАВАНТАЖИТИ" xpos 120 ypos 62 size 120 color "#d8b4fe" font "fonts/CourierNew-Bold.ttf"

    viewport:
        xpos 120 ypos 200 xsize 1000 ysize 750
        mousewheel True
        scrollbars "vertical"

        vbox:
            spacing 12

            # Автосейв
            if FileLoadable("auto-1"):
                button:
                    background "gui/save/save_slot_auto.png"
                    hover_background "gui/save/save_slot_auto.png"
                    xsize 1000 ysize 100
                    action FileLoad("auto-1", confirm=False)
                    text FileTime("auto-1", format="%d.%m.%Y", empty="") xpos 24 ypos 24 size 24 color "#1a1a2e" font "fonts/CourierNew-Regular.ttf"
                    text FileTime("auto-1", format="%H:%M", empty="") xpos 24 ypos 58 size 24 color "#1a1a2e" font "fonts/CourierNew-Regular.ttf"
                    text FileSaveName("auto-1", empty="") xpos 210 ypos 24 size 24 color "#1a1a2e" font "fonts/CourierNew-Bold.ttf"
                    text "АВТО" xpos 900 ypos 38 size 18 color "#1a1a2e" bold True font "fonts/CourierNew-Bold.ttf"

            # Ручні слоти
            for i in range(1, 21):
                $ _slot_bg = "gui/save/save_slot_hover.png" if FileLoadable(i) else "gui/save/save_slot.png"
                $ _slot_name_color = "#d8b4fe" if FileLoadable(i) else "#d946ef"
                $ _slot_name_text = FileSaveName(i, empty="") if FileLoadable(i) else "порожній слот"
                $ _slot_name_font = "fonts/CourierNew-Bold.ttf" if FileLoadable(i) else "fonts/CourierNew-Regular.ttf"
                $ _slot_action = FileLoad(i, confirm=False) if FileLoadable(i) else NullAction()
                button:
                    background _slot_bg
                    hover_background "gui/save/save_slot_hover.png"
                    xsize 1000 ysize 100
                    action _slot_action
                    text FileTime(i, format="%d.%m.%Y", empty="—") xpos 24 ypos 24 size 24 color "#8888aa" font "fonts/CourierNew-Regular.ttf"
                    text FileTime(i, format="%H:%M", empty="") xpos 24 ypos 58 size 24 color "#8888aa" font "fonts/CourierNew-Regular.ttf"
                    text _slot_name_text xpos 210 ypos 24 size 24 color _slot_name_color font _slot_name_font

    add "gui/save/save_side_block.png" xpos 1280 ypos 200
    vbox:
        xpos 1300 ypos 220 spacing 10
        text "ІНФОРМАЦІЯ" size 24 color "#d8b4fe" font "fonts/CourierNew-Bold.ttf"
        null height 10
        text "Ранг: —" size 18 color "#8888aa" font "fonts/CourierNew-Regular.ttf"
        text "Крони: —" size 18 color "#8888aa" font "fonts/CourierNew-Regular.ttf"
        text "HEX: —" size 18 color "#8888aa" font "fonts/CourierNew-Regular.ttf"
        null height 30
        textbutton "ВИДАЛИТИ" action NullAction() text_size 18 text_color "#fb0062" text_hover_color "#ff3388" text_font "fonts/CourierNew-Bold.ttf"

    textbutton "◄ НАЗАД" xpos 120 ypos 980 action Return() text_size 20 text_color "#8888aa" text_hover_color "#d946ef" text_font "fonts/CourierNew-Bold.ttf"
