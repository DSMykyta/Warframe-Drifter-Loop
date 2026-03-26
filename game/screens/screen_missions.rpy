# screen_missions.rpy — HEX CYBERPUNK STYLE
# ═══════════════════════════════════════════

screen missions_menu():
    add "backgrounds/bg-dossiers.jpg"

    modal True
    tag missions

    use hud
    use scanlines

    # ── Заголовок + репутація ──
    vbox:
        align (0.5, 0.08)
        spacing 6
        text "МІСІЇ" size 14 color "#ffffff25" xalign 0.5 kerning 8
        text "Репутація Гекс" size 20 color "#a855f7" xalign 0.5

        hbox:
            xalign 0.5
            spacing 12
            text "[hex_rep]" size 28 color "#facc15" bold True
            # Наступний поріг
            python:
                _rank_thresholds = {2: 100, 3: 300, 4: 600, 5: 1000, 6: 1500}
                _next_threshold = _rank_thresholds.get(syndicate_rank + 1, 9999)
            text "/ [_next_threshold]" size 16 color "#ffffff30" yalign 1.0

        # Прогрес-бар
        frame:
            xalign 0.5
            xsize 500
            ysize 8
            background "#ffffff10"
            padding (0, 0, 0, 0)
            bar value StaticValue(hex_rep, _next_threshold):
                xmaximum 500
                left_bar Solid("#a855f7")
                right_bar Solid("#ffffff08")
                ysize 8

    # ── Сітка місій 3×2 (+ можлива аварійна) ──
    $ _mission_count = min(len(missions), 7)
    $ _cols = 3
    $ _rows = (_mission_count + _cols - 1) // _cols

    vpgrid:
        align (0.5, 0.55)
        cols _cols
        spacing 16
        xmaximum 1250

        for i in range(len(missions)):
            $ m = missions[i]
            $ dur_mins = max(1, m["level"]) * 60
            $ dur_hours = dur_mins // 60
            $ _is_redemption = m.get("is_redemption", False)
            $ _is_synergy = m.get("partner_count", 1) >= 2
            $ _chem_available = m["partner"] is not None and m["partner"] not in mission_chem_today

            button:
                xsize 380
                ysize 180
                if _is_redemption:
                    background "#ef444420"
                    hover_background "#ef444440"
                else:
                    background "#0d0d1acc"
                    hover_background "#a855f722"
                padding (16, 14)
                action Return(i)

                vbox:
                    spacing 5

                    # Назва місії
                    text "[m['name']]" size 18 color "#d8b4fe" bold True

                    # Рівень + час
                    hbox:
                        spacing 8
                        text "Рівень [m['level']]" size 14 color "#facc15"
                        text "[dur_hours] год" size 14 color "#22d3ee"

                    # Нагорода
                    if m['reward'] > 0:
                        hbox:
                            spacing 8
                            text "[m['reward']] крон" size 14 color "#22d3ee"
                            text "+[m['rep']] реп" size 14 color "#a855f7"
                    else:
                        text "Без нагороди" size 14 color "#ffffff30"

                    # Напарник + статус хімії
                    if m['partner']:
                        hbox:
                            spacing 8
                            text "[m['partner']]" size 14 color "#ffffff60"
                            if _chem_available:
                                text "+10" size 12 color "#22d3ee"
                            else:
                                text "зв'язок вичерпано" size 11 color "#ffffff30"

                        # Другий напарник (synergy raid)
                        if _is_synergy:
                            $ _p2 = m.get("partner2", "?")
                            text "+ [_p2]" size 14 color "#f0abfc"
                    else:
                        text "Соло місія" size 14 color "#ffffff30"

    # ── Назад ──
    button:
        style "hex_btn"
        xpos 0.96
        ypos 0.94
        xanchor 1.0
        yanchor 1.0
        action Return("back")
        text "Назад" size 18 color "#8888aa"
