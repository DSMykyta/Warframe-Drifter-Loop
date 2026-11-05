# game/quests/coffee/coffee_hooks.rpy
# ═══════════════════════════════════════════════════
# КВЕСТ КАВИ — ХУКИ ДЛЯ next_day()
# ═══════════════════════════════════════════════════
#
# Додати в day_logic.rpy в next_day() ПІСЛЯ build_daily_deck():
#
#   check_coffee_extract_deadline()
#   check_coffee_parts_pager()
#   check_coffee_amir_diy()
#   check_coffee_cafe_open()
#
# Додати в _daily_flags:
#   "coffee_given_arthur_today", "coffee_given_eleanor_today",
#   "coffee_given_lettie_today", "coffee_given_amir_today",
#   "coffee_given_aoi_today", "coffee_given_quincy_today",
#
# Також додати в screens.rpy location_ui кнопку автомата:
#
#   if current_location == "cafe" and store.flags.get("coffee_machine_found"):
#       button:
#           style "hex_btn"
#           action Return("coffee")
#           text "Автомат" size 18 color "#facc15"
#
# І в script.rpy location_loop обробник:
#
#   if _choice == "coffee":
#       $ hide_pager()
#       call coffee_machine_interact
#       $ show_pager()
#       jump location_loop
#
# Також додати в images.rpy:
#
#   image bg_cafe_coffee = "backgrounds/bg_cafe_coffee.png"
#
# І в BG_OVERRIDES:
#
#   "coffee_machine_found": {"cafe": "bg_cafe_coffee"},
