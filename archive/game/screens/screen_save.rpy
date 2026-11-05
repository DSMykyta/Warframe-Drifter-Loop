# game/screens/screen_save.rpy
# ═══════════════════════════════════════════════════
# ЗБЕРЕЖЕННЯ / ЗАВАНТАЖЕННЯ — ПЕРЕПИСАНО З НУЛЯ
# ═══════════════════════════════════════════════════
# Нуль зовнішніх PNG. Все — Solid() і text.
# Замість viewport — vpgrid з фіксованим розміром.

init python:

    def _slot_meta(slot):
        """Метадані збереження."""
        try:
            j = renpy.slot_json(slot)
            return j if j else {}
        except:
            return {}

    def _fmt_minutes(m):
        if m is None:
            return "--:--"
        return "{:02d}:{:02d}".format(int(m) // 60, int(m) % 60)


# ═══════════════════════════════════════════════════
# SAVE
# ═══════════════════════════════════════════════════

screen save():
    tag menu

    # Фон
    add Solid("#09090f")

    # Заголовок
    hbox:
        xpos 80 ypos 40
        spacing 20
        text "ЗБЕРЕЖЕННЯ" size 48 color "#d8b4fe" bold True

    # Кнопка назад
    textbutton "◄ НАЗАД":
        xpos 80 ypos 980
        action Return()
        text_size 20
        text_color "#ffffff40"
        text_hover_color "#d8b4fe"

    # ── Слоти ──
    vpgrid:
        xpos 80 ypos 120
        xsize 1100 ysize 840
        cols 1
        spacing 8
        mousewheel True
        scrollbars "vertical"

        # Автослот
        use _slot_btn("auto-1", NullAction(), is_auto=True, is_save=True)

        # 20 ручних слотів
        for i in range(1, 21):
            use _slot_btn(i, FileSave(i, confirm=FileLoadable(i)), is_auto=False, is_save=True)

    # ── Інфо-панель справа ──
    use _save_info()


# ═══════════════════════════════════════════════════
# LOAD
# ═══════════════════════════════════════════════════

screen load():
    tag menu

    add Solid("#09090f")

    hbox:
        xpos 80 ypos 40
        spacing 20
        text "ЗАВАНТАЖИТИ" size 48 color "#a5f3fc" bold True

    textbutton "◄ НАЗАД":
        xpos 80 ypos 980
        action Return()
        text_size 20
        text_color "#ffffff40"
        text_hover_color "#a5f3fc"

    vpgrid:
        xpos 80 ypos 120
        xsize 1100 ysize 840
        cols 1
        spacing 8
        mousewheel True
        scrollbars "vertical"

        # Автослот (завжди видно)
        if FileLoadable("auto-1"):
            use _slot_btn("auto-1", FileLoad("auto-1", confirm=False), is_auto=True, is_save=False)
        else:
            use _slot_btn("auto-1", NullAction(), is_auto=True, is_save=False)

        # 20 ручних слотів
        for i in range(1, 21):
            if FileLoadable(i):
                use _slot_btn(i, FileLoad(i, confirm=False), is_auto=False, is_save=False)
            else:
                use _slot_btn(i, NullAction(), is_auto=False, is_save=False)


# ═══════════════════════════════════════════════════
# ШАБЛОН СЛОТА
# ═══════════════════════════════════════════════════

screen _slot_btn(slot, slot_action, is_auto=False, is_save=True):
    $ _loaded = FileLoadable(slot)
    $ _meta = _slot_meta(slot) if _loaded else {}

    button:
        xsize 1080
        ysize 82
        action slot_action
        padding (16, 10, 16, 10)

        if is_auto:
            background Solid("#facc1510")
            hover_background Solid("#facc15")
        elif _loaded:
            background Solid("#a855f710")
            hover_background Solid("#a855f7")
        else:
            background Solid("#ffffff06")
            hover_background Solid("#ffffff30")

        hbox:
            spacing 16
            yalign 0.5

            # Номер
            frame:
                xsize 50 ysize 50
                yalign 0.5
                background Solid("#ffffff08")
                padding (0, 0, 0, 0)
                if is_auto:
                    text "A" size 22 color "#facc15" bold True xalign 0.5 yalign 0.5
                else:
                    $ _sn = str(slot)
                    text "[_sn]" size 20 color "#d8b4fe" bold True xalign 0.5 yalign 0.5

            # Контент
            if _loaded:
                vbox:
                    spacing 2
                    yalign 0.5

                    # Назва збереження
                    $ _sname = FileSaveName(slot, empty="—")
                    text "[_sname]" size 17 color "#d8b4fe" bold True

                    hbox:
                        spacing 20

                        # Реальна дата
                        $ _rtime = FileTime(slot, format="%d.%m.%Y %H:%M", empty="")
                        text "[_rtime]" size 13 color "#ffffff30"

                        # Ігровий день
                        if _meta and "_game_day" in _meta:
                            $ _gday = _meta["_game_day"]
                            $ _gt = _fmt_minutes(_meta.get("_game_time"))
                            text "День [_gday] / [_gt]" size 13 color "#a5f3fc"

                        # Локація
                        if _meta and "_game_location" in _meta:
                            $ _gloc = LOCATION_NAMES.get(_meta["_game_location"], "")
                            text "[_gloc]" size 13 color "#ffffff20"

            else:
                text "порожній слот" size 15 color "#ffffff18" yalign 0.5

            # Мітка АВТО
            if is_auto and _loaded:
                text "АВТО" size 13 color "#facc1560" bold True yalign 0.5


# ═══════════════════════════════════════════════════
# ІНФО-ПАНЕЛЬ
# ═══════════════════════════════════════════════════

screen _save_info():
    frame:
        xpos 1220 ypos 120
        xsize 640 ysize 500
        background Solid("#0d0d1acc")
        padding (28, 24, 28, 24)

        vbox:
            spacing 10

            text "ІНФОРМАЦІЯ" size 20 color "#d8b4fe" bold True

            add Solid("#ffffff10", xsize=580, ysize=1)

            null height 4

            # Поточний стан гри (якщо в грі)
            if not main_menu:
                $ _cur_day = store.day
                $ _cur_time = get_time_display()
                $ _cur_loc = LOCATION_NAMES.get(store.current_location, store.current_location)
                $ _cur_rep = store.hex_rep
                $ _cur_rank = store.syndicate_rank
                $ _cur_money = store.money

                hbox:
                    spacing 10
                    text "День:" size 16 color "#ffffff40"
                    text "[_cur_day] грудня" size 16 color "#a5f3fc" bold True

                hbox:
                    spacing 10
                    text "Час:" size 16 color "#ffffff40"
                    text "[_cur_time]" size 16 color "#facc15" bold True

                hbox:
                    spacing 10
                    text "Локація:" size 16 color "#ffffff40"
                    text "[_cur_loc]" size 16 color "#d8b4fe"

                hbox:
                    spacing 10
                    text "Ранг:" size 16 color "#ffffff40"
                    text "[_cur_rank]" size 16 color "#fca5a5" bold True

                hbox:
                    spacing 10
                    text "Крони:" size 16 color "#ffffff40"
                    text "[_cur_money]" size 16 color "#facc15"

                hbox:
                    spacing 10
                    text "HEX:" size 16 color "#ffffff40"
                    text "[_cur_rep]" size 16 color "#fca5a5"

                null height 8
                add Solid("#ffffff10", xsize=580, ysize=1)
                null height 4

                text "ХІМІЯ" size 14 color "#ffffff30" bold True

                for _cn, _cv in store.chemistry.items():
                    hbox:
                        spacing 10
                        text "[_cn]" size 14 color "#ffffff30" min_width 100
                        text "[_cv]" size 14 color "#d8b4fe" bold True

            else:
                text "Запустіть гру щоб бачити стан." size 15 color "#ffffff20"


# ═══════════════════════════════════════════════════
# СТИЛІ СКРОЛБАРУ (щоб vpgrid не зламався)
# ═══════════════════════════════════════════════════

style vscrollbar:
    xsize 8
    base_bar Solid("#ffffff08")
    thumb Solid("#a855f740")
    hover_thumb Solid("#a855f770")
    unscrollable "hide"
