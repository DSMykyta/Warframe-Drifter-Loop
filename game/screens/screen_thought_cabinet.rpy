# game/screen_insights.rpy
# ═══════════════════════════════════════════════════
# ШАФА ДУМОК (Thought Cabinet)
# ═══════════════════════════════════════════════════

screen thought_cabinet():
    modal True

    use hud

    add Solid("#09090fee")

    vbox:
        align (0.5, 0.08)
        text "ШАФА ДУМОК" size 28 color "#a855f7" xalign 0.5 bold True
        text "Факти та зв'язки" size 14 color "#ffffff40" xalign 0.5

    viewport:
        align (0.5, 0.5)
        xmaximum 900
        ymaximum 700
        scrollbars "vertical"
        mousewheel True
        draggable True

        vbox:
            spacing 20

            # ═══ СИРІ ДУМКИ (потребують осмислення) ═══
            if raw_thoughts:
                text "НЕОБДУМАНІ ЗВ'ЯЗКИ" size 16 color "#facc15" bold True

                for _rt in raw_thoughts:
                    frame:
                        background "#facc1515"
                        padding (20, 14, 20, 14)
                        xfill True

                        hbox:
                            spacing 16

                            vbox:
                                xmaximum 600
                                text "[_rt[text]]" size 16 color "#facc15cc"
                                text "Потребує 30 хв осмислення" size 12 color "#ffffff40"

                            button:
                                style "hex_btn_accent"
                                yalign 0.5
                                action [Function(contemplate, _rt["id"]), Return()]
                                text "Обдумати" size 14 color "#facc15"

                null height 10

            # ═══ ФАКТИ (згруповані по персонажах) ═══
            if insights_log:
                text "ВІДОМІ ФАКТИ" size 16 color "#d8b4fe" bold True

                # Згрупувати по персонажах (за першим словом id)
                for _char_name in ["Артур", "Елеонор", "Летті", "Амір", "Аоі", "Квінсі"]:
                    # Знайти факти пов'язані з цим персонажем
                    $ _char_key = _char_name.lower()
                    $ _char_facts = [i for i in insights_log if i["type"] == "fact" and _char_key in i["id"].lower()]

                    if _char_facts:
                        frame:
                            background "#a855f708"
                            padding (16, 10, 16, 10)
                            xfill True

                            vbox:
                                spacing 6
                                text "[_char_name]" size 16 color "#d8b4fe" bold True

                                for _fact in _char_facts:
                                    hbox:
                                        spacing 8
                                        text ">" size 14 color "#a855f7"
                                        text "[_fact[text]]" size 14 color "#ffffffaa"

                # Зв'язки (осмислені)
                $ _connections = [i for i in insights_log if i["type"] == "connection"]
                if _connections:
                    null height 10
                    text "ОСМИСЛЕНІ ЗВ'ЯЗКИ" size 16 color "#22d3ee" bold True

                    for _conn in _connections:
                        frame:
                            background "#22d3ee10"
                            padding (16, 10, 16, 10)
                            xfill True
                            hbox:
                                spacing 8
                                text "~" size 14 color "#22d3ee"
                                text "[_conn[text]]" size 14 color "#a5f3fccc"

            elif not raw_thoughts:
                text "Поки порожньо. Спілкуйся з людьми." size 16 color "#ffffff30"

    # Закрити
    button:
        xpos 0.96
        ypos 0.06
        xanchor 1.0
        action Return()
        text "Закрити" size 16 color "#fca5a5"
