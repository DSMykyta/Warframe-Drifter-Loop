# game/screen_journal.rpy
# ═══════════════════════════════════════════════════
# ЩОДЕННИК ДРІФТЕРА
# ═══════════════════════════════════════════════════

screen journal():
    modal True

    use hud

    add Solid("#09090fee")

    vbox:
        align (0.5, 0.08)
        text "ЩОДЕННИК" size 28 color "#a855f7" xalign 0.5 bold True
        text "Записи Дріфтера" size 14 color "#ffffff40" xalign 0.5

    if journal_entries:
        viewport:
            align (0.5, 0.5)
            xmaximum 800
            ymaximum 700
            scrollbars "vertical"
            mousewheel True
            draggable True

            vbox:
                spacing 16

                # Від найновіших до найстаріших
                for _entry in reversed(journal_entries):
                    frame:
                        background "#a855f710"
                        padding (20, 14, 20, 14)
                        xfill True

                        vbox:
                            spacing 6
                            hbox:
                                spacing 12
                                text "День [_entry[day]]" size 14 color "#facc15" bold True
                                $ _entry_type = _entry.get("type", "note")
                                if _entry_type == "conversation":
                                    text "розмова" size 12 color "#d8b4fe"
                                elif _entry_type == "mission":
                                    text "місія" size 12 color "#fca5a5"
                                elif _entry_type == "promise":
                                    text "обіцянка" size 12 color "#a5f3fc"
                                elif _entry_type == "insight":
                                    text "інсайт" size 12 color "#f0abfc"

                            text "[_entry[text]]" size 16 color "#ffffffcc"
    else:
        text "Поки порожньо." size 18 color "#ffffff30" align (0.5, 0.5)

    # Закрити
    button:
        xpos 0.96
        ypos 0.06
        xanchor 1.0
        action Return()
        text "Закрити" size 16 color "#fca5a5"
