# game/screens/screen_pager_fix.rpy
# ═══════════════════════════════════════════════════
# ПЕЙДЖЕР — ВИПРАВЛЕНИЙ
# ═══════════════════════════════════════════════════

screen pager_hud():
    zorder 90

    if store.flags.get("has_pager"):
        fixed:
            xpos 1900
            ypos 1060
            xanchor 1.0
            yanchor 1.0
            xsize 400
            ysize 220

            add Solid("#477220", xsize=285, ysize=86) xpos 54 ypos 43

            fixed:
                xpos 54
                ypos 43
                xsize 285
                ysize 86

                $ _hud_time = get_time_display()
                $ _hud_loc = LOCATION_NAMES.get(current_location, current_location)

                if pager_mode == "request":
                    text "[pager_request_who]" xpos 6 ypos 4 size 18 color "#131f1f" bold True font "fonts/JetBrainsMono-Bold.ttf"
                    fixed:
                        xpos 6 ypos 22
                        xsize 240 ysize 58
                        text "[pager_request_text]" size 16 color "#131f1f" bold True font "fonts/JetBrainsMono-Bold.ttf"

                elif pager_mode == "message" and pager_messages:
                    $ _pi = min(pager_msg_index, len(pager_messages) - 1)
                    $ _pmsg_entry = pager_messages[_pi]
                    $ _pmsg_who = _pmsg_entry["who"]
                    $ _pmsg_text = _pmsg_entry["text"]
                    $ _pnum = _pi + 1
                    $ _ptotal = len(pager_messages)
                    text "[_pmsg_who]" xpos 6 ypos 4 size 18 color "#131f1f" bold True font "fonts/JetBrainsMono-Bold.ttf"
                    fixed:
                        xpos 6 ypos 22
                        xsize 240 ysize 58
                        text "[_pmsg_text]" size 16 color "#131f1f" bold True font "fonts/JetBrainsMono-Bold.ttf"
                    text "[_pnum]/[_ptotal]" xpos 251 ypos 63 size 18 color "#131f1f" bold True font "fonts/JetBrainsMono-Bold.ttf"

                else:
                    text "[_hud_loc]" xpos 6 ypos 8 size 20 color "#131f1f" font "fonts/JetBrainsMono-Regular.ttf"
                    text "[_hud_time]" xpos 6 ypos 38 size 36 color "#131f1f" bold True font "fonts/JetBrainsMono-Bold.ttf"
                    text "[hex_rep]" xpos 240 ypos 50 size 20 color "#131f1f" bold True font "fonts/JetBrainsMono-Bold.ttf"
                    if renpy.loadable("gui/icons/the-hex_pager.png"):
                        add "gui/icons/the-hex_pager.png" xpos 255 ypos 45 zoom 0.4

            add Crop((0, 0, 285, 86), "gui/overlay-effect.png") xpos 54 ypos 43
            add "gui/pager.png" zoom 0.4 align (0.0, 0.0)

            if pager_unread:
                add Solid("#ef4444", xsize=12, ysize=12) xpos 340 ypos 38

            # ═══ КНОПКИ — ТІЛЬКИ Function()! ═══

            button:
                xpos 60 ypos 139 xsize 80 ysize 28
                background Solid("#ffffff00")
                hover_background Solid("#ffffff30")
                if pager_mode == "message":
                    action Function(pager_prev_msg)
                elif pager_mode == "request":
                    action Function(_pager_accept)
                else:
                    action NullAction()

            button:
                xpos 153 ypos 139 xsize 80 ysize 28
                background Solid("#ffffff00")
                hover_background Solid("#ffffff30")
                if pager_mode == "request":
                    action NullAction()
                else:
                    action Function(pager_dismiss)

            button:
                xpos 246 ypos 139 xsize 80 ysize 28
                background Solid("#ffffff00")
                hover_background Solid("#ffffff30")
                if pager_mode == "message" and pager_messages:
                    action Function(pager_next_msg)
                elif pager_mode == "request":
                    action Function(_pager_decline)
                else:
                    action NullAction()
