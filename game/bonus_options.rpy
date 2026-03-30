# game/bonus_options.rpy
# ═══════════════════════════════════════════════════════════════
# ДИНАМІЧНІ ОПЦІЇ ДІАЛОГІВ — ПЛОСКА СИСТЕМА
# ═══════════════════════════════════════════════════════════════
#
# Будь-який діалог може отримати додаткові опції в меню
# на основі стану світу (флаги, хімія, одяг, інвентар).
#
# Опція НЕ прив'язана до конкретного діалогу — вона з'являється
# СКРІЗЬ де гравець говорить з цим NPC, якщо умова виконана.
#
# ВИКОРИСТАННЯ В ДІАЛОГАХ:
#
#   menu:
#       "Звичайна опція 1":
#           jump branch_1
#       "Звичайна опція 2":
#           jump branch_2
#
#   # Після основного меню — перевірити динамічні опції
#   $ _bonus = get_bonus_options("Артур")
#   if _bonus:
#       # Показати друге меню з бонусними опціями
#       # (або вбудувати в перше через dynamic menu)
#
# АБО ПРОСТІШЕ — через Ren'Py `if` в menu:
#
#   menu:
#       "Опція 1":
#           ...
#       "Опція 2":
#           ...
#       "О! Та куртка з метро!" if store.flags.get("arthur_has_metro_jacket") and store.current_outfits.get("Артур") == "metro_jacket":
#           call arthur_metro_jacket_reaction
#
# ═══════════════════════════════════════════════════════════════

init -5 python:

    # Глобальний реєстр динамічних опцій
    BONUS_OPTIONS = []

    # Структура запису:
    # {
    #     "id": "arthur_metro_jacket_comment",
    #     "who": "Артур",                          ← з ким розмова
    #     "text": "О! Зачекай, це що та куртка?",  ← текст опції в меню
    #     "label": "arthur_metro_jacket_react",     ← label що викликається
    #     "conditions": {                           ← умови появи (той же формат що в DIALOGUE_ENTRIES)
    #         "flag_true": ["arthur_has_metro_jacket"],
    #     },
    #     "outfit_check": ("Артур", "metro_jacket"), ← ОПЦІОНАЛЬНО: з'являється тільки якщо NPC в цьому аутфіті
    #     "once": True,                              ← зникає після використання
    # }

    def get_bonus_options(name):
        """Повертає список eligible бонусних опцій для NPC."""
        result = []
        for opt in BONUS_OPTIONS:
            if opt["who"] != name:
                continue
            # Перевірити чи вже використана
            if opt.get("once") and store.flags.get(opt["id"] + "_used"):
                continue
            # Перевірити conditions
            conds = opt.get("conditions", {})
            if not check_stable_conditions(conds):
                continue
            if not check_dynamic_conditions(conds):
                continue
            # Перевірити одяг (якщо вказано)
            if "outfit_check" in opt:
                oc_name, oc_outfit = opt["outfit_check"]
                if store.current_outfits.get(oc_name) != oc_outfit:
                    continue
            result.append(opt)
        return result

    def mark_bonus_used(option_id):
        """Позначає бонусну опцію як використану."""
        set_flag(option_id + "_used")
