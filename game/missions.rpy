# missions.rpy
# ═══════════════════════════════════════════════════
# МЕНЕДЖЕР МІСІЙ ТА НАГОРОД
# ═══════════════════════════════════════════════════

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

    def generate_missions():
        """Генерує 6 місій на день. 15% шанс на парну (synergy raid).
        NPC з 2+ стаками травм не потрапляють в пул напарників.
        Місії можуть бути без напарника."""
        names = list(mission_names_pool)
        random.shuffle(names)
        # Фільтрувати NPC з 2+ стаками травм
        all_partners = list(store.chemistry.keys())
        eligible_partners = [p for p in all_partners if get_injury_stacks(p) < 2]
        random.shuffle(eligible_partners)
        store.missions = []

        for i in range(6):
            level = i + 1
            reward = 100 * level
            rep = level
            name = names[i % len(names)]

            # Напарник або None якщо нікого немає
            if eligible_partners:
                partner = eligible_partners[i % len(eligible_partners)]
            else:
                partner = None

            mission = {
                "name": name,
                "level": level,
                "reward": reward,
                "rep": rep,
                "partner": partner,
                "partner_count": 1 if partner else 0,
            }

            # 15% шанс на парну місію (synergy raid)
            if partner and level >= 3 and random.randint(1, 100) <= 15:
                other_partners = [p for p in eligible_partners if p != partner]
                if other_partners:
                    mission["partner2"] = random.choice(other_partners)
                    mission["partner_count"] = 2
                    mission["name"] = mission["name"] + " [ПАРНА]"

            store.missions.append(mission)

        # Аварійна місія (redemption) якщо neglect критичний
        if store.days_without_mission >= 5:
            store.missions.append({
                "name": "АВАРІЙНА ОПЕРАЦІЯ",
                "level": 4,
                "reward": 0,
                "rep": 0,
                "partner": "Артур",
                "partner_count": 1,
                "is_redemption": True,
            })

# Значення по замовчуванню
default missions = []
default selected_mission = 0

# Генеруємо перший набір місій при запуску
init 1 python:
    def _start_generate_missions():
        generate_missions()

    config.start_callbacks.append(_start_generate_missions)
