## screen_preferences.rpy — Стилізація під main_menu
## ═══════════════════════════════════════════════════

screen preferences():

    tag menu

    add "gui/main_menu.png"

    ## Заголовок
    text "НАЛАШТУВАННЯ":
        xalign 0.5
        ypos 40
        size 28
        color "#8888aa"
        font "fonts/CourierNew-Regular.ttf"
        kerning 2.0

    ## Основний контент
    vbox:
        xalign 0.5
        ypos 130
        spacing 30

        ## Режим екрану
        vbox:
            spacing 8
            text "Режим екрану" style "pref_label"
            hbox:
                spacing 20
                textbutton _("Віконний") action Preference("display", "window") style "pref_btn"
                textbutton _("Повноекранний") action Preference("display", "fullscreen") style "pref_btn"

        ## Швидкість тексту
        vbox:
            spacing 8
            text "Швидкість тексту" style "pref_label"
            bar value Preference("text speed"):
                xsize 600
                left_bar Solid("#a855f7")
                right_bar Solid("#1a1a2e")
                thumb Solid("#d8b4fe", xsize=12, ysize=12)
                thumb_offset 6
                ysize 4

        ## Авто-перемотка
        vbox:
            spacing 8
            text "Авто-перемотка" style "pref_label"
            bar value Preference("auto-forward time"):
                xsize 600
                left_bar Solid("#a855f7")
                right_bar Solid("#1a1a2e")
                thumb Solid("#d8b4fe", xsize=12, ysize=12)
                thumb_offset 6
                ysize 4

        if config.has_music:
            vbox:
                spacing 8
                text "Гучність музики" style "pref_label"
                bar value Preference("music volume"):
                    xsize 600
                    left_bar Solid("#a855f7")
                    right_bar Solid("#1a1a2e")
                    thumb Solid("#d8b4fe", xsize=12, ysize=12)
                    thumb_offset 6
                    ysize 4

        if config.has_sound:
            vbox:
                spacing 8
                text "Гучність звуків" style "pref_label"
                bar value Preference("sound volume"):
                    xsize 600
                    left_bar Solid("#a855f7")
                    right_bar Solid("#1a1a2e")
                    thumb Solid("#d8b4fe", xsize=12, ysize=12)
                    thumb_offset 6
                    ysize 4

        if config.has_voice:
            vbox:
                spacing 8
                text "Гучність голосу" style "pref_label"
                bar value Preference("voice volume"):
                    xsize 600
                    left_bar Solid("#a855f7")
                    right_bar Solid("#1a1a2e")
                    thumb Solid("#d8b4fe", xsize=12, ysize=12)
                    thumb_offset 6
                    ysize 4

        ## Пропуск
        vbox:
            spacing 8
            text "Пропуск" style "pref_label"
            hbox:
                spacing 20
                textbutton _("Тільки прочитане") action Preference("skip", "seen") style "pref_btn"
                textbutton _("Все") action Preference("skip", "all") style "pref_btn"

        vbox:
            spacing 8
            text "Після вибору" style "pref_label"
            hbox:
                spacing 20
                textbutton _("Зупинити пропуск") action Preference("after choices", "stop") style "pref_btn"
                textbutton _("Продовжити") action Preference("after choices", "skip") style "pref_btn"

    ## Кнопка повернення
    textbutton _("◄"):
        xpos 40
        ypos 980
        action Return()
        style "sl_back_btn"


## Стилі

style pref_label:
    font "fonts/CourierNew-Bold.ttf"
    size 24
    color "#8888aa"

style pref_btn:
    xpadding 20
    ypadding 10
    background Solid("#a855f720")
    hover_background Solid("#a855f740")
    selected_background Solid("#a855f766")

style pref_btn_text:
    font "fonts/CourierNew-Regular.ttf"
    size 22
    color "#8888aa"
    hover_color "#d946ef"
    selected_color "#facc15"
