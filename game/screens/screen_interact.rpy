# game/screens/screen_interact.rpy
# ═══════════════════════════════════════════════════
# МЕНЮ ВЗАЄМОДІЇ З NPC
# ═══════════════════════════════════════════════════
# Показується при клікові на персонажа в локації.
# Збирає: репліки-входи з eligible діалогів + бонусні опції + подарунок + піти.

screen npc_interact_menu(npc_name, topics, bonus_opts, can_gift):
    modal True
    tag interact

    # Напівпрозорий фон
    add Solid("#00000066")

    # Ім'я NPC зверху
    text "[npc_name]" size 28 color "#d8b4fe" bold True xalign 0.5 ypos 60

    # Меню опцій по центру
    vbox:
        align (0.5, 0.5)
        spacing 8
        xmaximum 700

        # Репліки-входи з діалогів
        for _topic in topics:
            button:
                style "interact_btn"
                action Return(("topic", _topic["label"], _topic["id"]))
                text "[_topic[text]]" style "interact_btn_text"

        # Бонусні опції (динамічні)
        for _bopt in bonus_opts:
            button:
                style "interact_btn_bonus"
                action Return(("bonus", _bopt["label"]))
                text "[_bopt[text]]" style "interact_btn_text_bonus"

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


# ═══ СТИЛІ ═══

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
