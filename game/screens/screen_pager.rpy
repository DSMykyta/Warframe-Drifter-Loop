# game/screens/screen_pager.rpy
# ═══════════════════════════════════════════════════
# ЕКРАН ПЕЙДЖЕРА
# ═══════════════════════════════════════════════════

screen pager():
    zorder 80
    $ _active = get_active_promises()
    $ _warning = promise_warning()

    if _active:
        frame:
            xpos 0.02
            ypos 0.85
            xanchor 0.0
            yanchor 1.0
            background "#0d0d1acc"
            padding (16, 10, 16, 10)
            xmaximum 350

            vbox:
                spacing 6
                text "ПЕЙДЖЕР" size 12 color "#facc15" bold True

                for _p in _active:
                    $ _p_time_from = "{:02d}:{:02d}".format(_p["from_min"] // 60, _p["from_min"] % 60)
                    $ _p_time_to = "{:02d}:{:02d}".format(_p["to_min"] // 60, _p["to_min"] % 60)
                    $ _p_loc = LOCATION_NAMES.get(_p["where"], _p["where"])
                    hbox:
                        spacing 6
                        if _warning and _warning["who"] == _p["who"]:
                            text "!" size 14 color "#ef4444" bold True
                        text "[_p[who]]" size 14 color "#d8b4fe"
                        text "[_p_loc]" size 13 color "#a5f3fc"
                        text "[_p_time_from]-[_p_time_to]" size 13 color "#ffffff60"
