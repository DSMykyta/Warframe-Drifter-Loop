# game/screen_thought_cabinet.rpy
# ═══════════════════════════════════════════════════
# ШАФА ДУМОК — 3 колонки
# ═══════════════════════════════════════════════════

init python:
    def get_char_facts(ckey):
        return [i for i in store.insights_log if i["type"] == "fact" and ckey in i["id"]]

    def get_general_facts():
        _char_keys = {"arthur", "eleanor", "lettie", "amir", "aoi", "quincy"}
        return [i for i in store.insights_log if i["type"] == "fact" and not any(k in i["id"] for k in _char_keys)]

default _cabinet_selected = None

screen thought_cabinet():
    modal True
    add Solid("#09090bf0")

    # Заголовок
    vbox:
        align (0.5, 0.02)
        text "ШАФА ДУМОК" size 28 color "#a855f7" xalign 0.5 bold True
        text "Факти та зв'язки" size 12 color "#ffffff40" xalign 0.5

    # ═══ 3 КОЛОНКИ ═══
    hbox:
        align (0.5, 0.55)
        spacing 2

        # ──── КОЛОНКА 1: Список персонажів ────
        frame:
            background "#ffffff08"
            padding (12, 16, 12, 16)
            xminimum 260
            xmaximum 260
            yminimum 700

            vbox:
                spacing 4

                text "ПЕРСОНАЖІ" size 14 color "#ffffff50" bold True
                null height 8

                # Загальне
                button:
                    xfill True
                    padding (12, 10, 12, 10)
                    if _cabinet_selected == "general":
                        background "#a855f730"
                    else:
                        background "#ffffff06"
                    hover_background "#a855f720"
                    action SetVariable("_cabinet_selected", "general")

                    hbox:
                        spacing 10
                        text ">" size 14 color "#a855f7"
                        text "Загальне" size 16 color "#d8b4fe"

                null height 4

                for _cn in CAST:
                    $ _ck = CHAR_FLAG_ID[_cn]
                    $ _chem = store.chemistry.get(_cn, 0)

                    button:
                        xfill True
                        padding (12, 10, 12, 10)
                        if _cabinet_selected == _ck:
                            background "#a855f730"
                        else:
                            background "#ffffff06"
                        hover_background "#a855f720"
                        action SetVariable("_cabinet_selected", _ck)

                        hbox:
                            spacing 10
                            text ">" size 14 color "#a855f7"
                            vbox:
                                text "[_cn]" size 16 color "#d8b4fe"
                                text "Хімія: [_chem]" size 11 color "#ffffff30"

        # ──── КОЛОНКА 2: Факти обраного персонажа ────
        frame:
            background "#ffffff05"
            padding (16, 16, 16, 16)
            xminimum 440
            xmaximum 440
            yminimum 700

            vbox:
                spacing 8

                text "ВІДОМІ ФАКТИ" size 14 color "#ffffff50" bold True
                null height 4

                if _cabinet_selected is not None:
                    if _cabinet_selected == "general":
                        $ _facts = get_general_facts()
                    else:
                        $ _facts = get_char_facts(_cabinet_selected)

                    if _facts:
                        for _f in _facts:
                            $ _ft = _f.get("text", "")
                            frame:
                                background "#a855f70a"
                                padding (12, 8, 12, 8)
                                xfill True
                                hbox:
                                    spacing 8
                                    text ">" size 14 color "#a855f7"
                                    text "[_ft]" size 14 color "#ffffffaa"
                    else:
                        text "Немає фактів." size 14 color "#ffffff20"
                else:
                    text "Обери персонажа зліва." size 14 color "#ffffff20"

        # ──── КОЛОНКА 3: Емоції / стан ────
        frame:
            background "#ffffff05"
            padding (16, 16, 16, 16)
            xminimum 380
            xmaximum 380
            yminimum 700

            vbox:
                spacing 8

                text "СТАН" size 14 color "#ffffff50" bold True
                null height 4

                if _cabinet_selected is not None and _cabinet_selected != "general":
                    # Поки текстовий placeholder
                    text "Дані про емоційний стан" size 14 color "#ffffff20"
                    text "поки не зібрані." size 14 color "#ffffff20"
                else:
                    text "" size 14

    # Закрити
    button:
        xpos 0.96
        ypos 0.03
        xanchor 1.0
        action Return()
        text "Закрити" size 16 color "#fca5a5"
