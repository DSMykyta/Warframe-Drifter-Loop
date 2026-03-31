# game/screens/screen_interact.rpy
# ═══════════════════════════════════════════════════
# МЕНЮ ВЗАЄМОДІЇ З NPC
# ═══════════════════════════════════════════════════
# Один eligible діалог → його titles (гілки) + bonus + подарунок + піти.
# titles = [("текст репліки", "label_гілки"), ...]

screen npc_interact_menu(npc_name, titles, bonus_opts, can_gift):
    modal True
    tag interact

    add Solid("#00000066")

    text "[npc_name]" size 28 color "#d8b4fe" bold True xalign 0.5 ypos 60

    vbox:
        align (0.5, 0.5)
        spacing 8
        xmaximum 700

        # Гілки діалогу
        # titles = [("текст", "label"), ...] або [("текст", "label", "flag"), ...]
        # Якщо є 3-й елемент — показувати тільки якщо store.flags.get(flag) == True
        for _entry in titles:
            $ _t_text = _entry[0]
            $ _t_label = _entry[1]
            $ _t_flag = _entry[2] if len(_entry) > 2 else None
            if _t_flag is None or store.flags.get(_t_flag):
                $ _t_style = "interact_btn" if _t_flag is None else "interact_btn_bonus"
                $ _t_text_style = "interact_btn_text" if _t_flag is None else "interact_btn_text_bonus"
                button:
                    style _t_style
                    action Return(("topic", _t_label))
                    text "[_t_text]" style _t_text_style

        # Бонусні опції
        for _bopt in bonus_opts:
            button:
                style "interact_btn_bonus"
                action Return(("bonus", _bopt["label"]))
                $ _btext = _bopt["text"]
                text "[_btext]" style "interact_btn_text_bonus"

        # Подарунок
        if can_gift:
            button:
                style "interact_btn"
                action Return("gift")
                text "Маю дещо для тебе" style "interact_btn_text"

        # Піти
        null height 12
        button:
            style "interact_btn_dismiss"
            action Return("dismiss")
            text "Незважай" style "interact_btn_text_dismiss"


style interact_btn:
    background "#0d0d1acc"
    hover_background "#a855f730"
    padding (24, 14, 24, 14)
    xfill True

style interact_btn_text:
    color "#d8b4fe"
    size 20
    xalign 0.0

style interact_btn_bonus:
    background "#facc1510"
    hover_background "#facc1530"
    padding (24, 14, 24, 14)
    xfill True

style interact_btn_text_bonus:
    color "#facc15"
    size 20
    xalign 0.0

style interact_btn_dismiss:
    background "#ffffff08"
    hover_background "#ffffff18"
    padding (24, 14, 24, 14)
    xfill True

style interact_btn_text_dismiss:
    color "#ffffff40"
    size 18
    xalign 0.5
