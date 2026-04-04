# missions.rpy
# ═══════════════════════════════════════════════════
# МЕНЕДЖЕР МІСІЙ ТА НАГОРОД
# ═══════════════════════════════════════════════════
#
# Пул напарників спільний — кожен NPC може бути на ОДНІЙ місії.
# Парна місія забирає 2 з пулу.
# Місія 5 = ранг 2+, місія 6 = ранг 4+.
# Спеціальні місії — condition-based, як DIALOGUE_ENTRIES.

init python:
    import random

    mission_names_pool = [
        "Тихе проникнення",
        "Розвідка території",
        "Супровід каравану",
        "Рятувальна операція",
        "Злам ворожої системи",
        "Знешкодження бомби",
        "Захист рубежів",
        "Нічний патруль",
        "Саботаж",
        "Перехоплення даних",
    ]

    # Нагороди за рівнем
    MISSION_REWARDS = {
        1: {"reward": 120, "rep": 2},
        2: {"reward": 200, "rep": 3},
        3: {"reward": 300, "rep": 5},
        4: {"reward": 420, "rep": 7},
        5: {"reward": 550, "rep": 9},
        6: {"reward": 700, "rep": 12},
    }

    # Мінімальний ранг для місії
    MISSION_RANK_REQ = {
        1: 1,
        2: 1,
        3: 1,
        4: 1,
        5: 2,   # відкривається на ранзі 2
        6: 4,   # відкривається на ранзі 4
    }

    # ═══ СПЕЦІАЛЬНІ МІСІЇ — condition-based ═══
    SPECIAL_MISSION_ENTRIES = []

    def get_special_missions():
        """Повертає список eligible спеціальних місій."""
        result = []
        for entry in SPECIAL_MISSION_ENTRIES:
            if entry["id"] in store.seen_dialogues:
                continue
            conds = entry.get("conditions", {})
            if not check_stable_conditions(conds):
                continue
            # Chance
            ch = entry.get("chance", 100)
            if ch < 100 and random.randint(1, 100) > ch:
                continue
            result.append(entry)
        return result

    def generate_missions():
        """Генерує місії на день.
        Пріоритет: квестові спецмісії → звичайні → аварійна.
        Пул напарників спільний — кожен NPC на одній місії максимум."""
        names = list(mission_names_pool)
        random.shuffle(names)

        # Пул напарників (без тих хто в палаті — 3 стаки)
        pool = [p for p in CAST if not is_npc_in_recovery(p)]
        random.shuffle(pool)

        store.missions = []

        # ═══ 1. СПЕЦМІСІЇ ПЕРШИМИ — квест має пріоритет ═══
        for special in get_special_missions():
            sp_partner = special.get("partner")
            sp_partner2 = special.get("partner2")
            # Забрати напарників спецмісії з пулу
            if sp_partner and sp_partner in pool:
                pool.remove(sp_partner)
            if sp_partner2 and sp_partner2 in pool:
                pool.remove(sp_partner2)
            sp_mission = {
                "name": special.get("name", "СПЕЦОПЕРАЦІЯ"),
                "level": special.get("level", 3),
                "reward": special.get("reward", 0),
                "rep": special.get("rep", 0),
                "partner": sp_partner,
                "partner2": sp_partner2,
                "partner_count": special.get("partner_count", 0),
                "is_special": True,
                "special_id": special["id"],
                "special_label": special.get("label"),
            }
            store.missions.append(sp_mission)

        # ═══ 2. ЗВИЧАЙНІ МІСІЇ — кількість за рівнями ═══
        max_level = len(MISSION_REWARDS)
        for i in range(max_level):
            level = i + 1
            mr = MISSION_REWARDS.get(level, {"reward": 100 * level, "rep": level})
            name = names[i % len(names)]

            # Перевірка рангу — пропустити якщо не відкрито
            rank_req = MISSION_RANK_REQ.get(level, 1)
            if store.syndicate_rank < rank_req:
                continue

            # Напарник з пулу (забирається!)
            partner = None
            if pool:
                partner = pool.pop(0)

            mission = {
                "name": name,
                "level": level,
                "reward": mr["reward"],
                "rep": mr["rep"],
                "partner": partner,
                "partner2": None,
                "partner_count": 1 if partner else 0,
            }

            # 15% шанс на парну місію (рівень 3+, є напарник, є ще хтось в пулі)
            if partner and level >= 3 and pool and random.randint(1, 100) <= 15:
                mission["partner2"] = pool.pop(0)
                mission["partner_count"] = 2
                mission["name"] = mission["name"] + " [ПАРНА]"

            store.missions.append(mission)

        # ═══ 3. АВАРІЙНА МІСІЯ — якщо neglect критичний ═══
        if store.days_without_mission >= 5:
            # Лідер загону як напарник
            _redemption_partner = CAST[0] if CAST else None
            store.missions.append({
                "name": "АВАРІЙНА ОПЕРАЦІЯ",
                "level": 4,
                "reward": 0,
                "rep": 0,
                "partner": _redemption_partner,
                "partner2": None,
                "partner_count": 1 if _redemption_partner else 0,
                "is_redemption": True,
            })


# ═══════════════════════════════════════════════════
# ЗМІННІ
# ═══════════════════════════════════════════════════

default missions = []
default selected_mission = 0

# Генеруємо перший набір місій при запуску
init 1 python:
    def _start_generate_missions():
        generate_missions()

    config.start_callbacks.append(_start_generate_missions)
