## Екрани збереження/завантаження ################################################

screen save():
    tag menu
    use file_slots(_("ЗБЕРЕГТИ"))

screen load():
    tag menu
    use file_slots(_("ЗАВАНТАЖИТИ"))

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Сторінка {}"), auto=_("Авто збереження"), quick=_("Швидке збереження"))

    ## Темний фон як на головному меню
    add "gui/main_menu.png"

    ## Заголовок
    vbox:
        xalign 0.5
        ypos 40

        text title:
            xalign 0.5
            size 28
            color "#8888aa"
            font "fonts/CourierNew-Regular.ttf"
            kerning 2.0

    ## Сітка слотів збереження
    fixed:
        xpos 80
        xsize 1760
        ypos 130
        ysize 820

        ## Навігація по сторінках
        hbox:
            xalign 0.5
            yalign 0.0
            spacing 30

            textbutton _("<") action FilePagePrevious():
                style "sl_page_btn"

            if config.has_autosave:
                textbutton _("{#auto_page}А") action FilePage("auto"):
                    style "sl_page_btn"

            if config.has_quicksave:
                textbutton _("{#quick_page}Ш") action FilePage("quick"):
                    style "sl_page_btn"

            for i in range(1, 10):
                textbutton "[i]" action FilePage(i):
                    style "sl_page_btn"

            textbutton _(">") action FilePageNext():
                style "sl_page_btn"

        ## Слоти
        grid gui.file_slot_cols gui.file_slot_rows:
            xalign 0.5
            yalign 1.0
            spacing 20

            for i in range(gui.file_slot_cols * gui.file_slot_rows):
                $ slot = i + 1

                button:
                    action FileAction(slot)
                    style "sl_slot_button"

                    has vbox
                    spacing 8

                    ## Мініатюра
                    add FileScreenshot(slot):
                        xalign 0.5
                        size (config.thumbnail_width, config.thumbnail_height)

                    ## Інформація
                    hbox:
                        xalign 0.5
                        spacing 15

                        text FileTime(slot, format=_("{#file_time}%d.%m.%Y %H:%M"), empty=_("Порожній слот")):
                            style "sl_slot_text"

                    key "save_delete" action FileDelete(slot)


    ## Кнопка повернення
    textbutton _("◄"):
        xpos 40
        ypos 980
        action Return()
        style "sl_back_btn"


## Стилі

style sl_page_btn:
    xminimum 50
    ypadding 8
    xpadding 12
    background Solid("#a855f720")
    hover_background Solid("#a855f740")
    selected_background Solid("#a855f766")

style sl_page_btn_text:
    xalign 0.5
    font "fonts/CourierNew-Bold.ttf"
    size 24
    color "#8888aa"
    hover_color "#d946ef"
    selected_color "#facc15"

style sl_slot_button:
    xsize 414
    ysize 309
    xpadding 10
    ypadding 10
    background Solid("#0d0d1a99")
    hover_background Solid("#a855f733")
    selected_background Solid("#a855f744")

style sl_slot_text:
    font "fonts/CourierNew-Regular.ttf"
    size 18
    color "#8888aa"
    hover_color "#d8b4fe"

style sl_back_btn:
    xsize 60
    ysize 60
    background Frame("gui/button/sl_back_idle.png", 14, 14)
    hover_background Frame("gui/button/sl_back_hover.png", 14, 14)

style sl_back_btn_text:
    xalign 0.5
    yalign 0.5
    font "fonts/CourierNew-Bold.ttf"
    size 30
    color "#d8b4fe"
    hover_color "#facc15"
