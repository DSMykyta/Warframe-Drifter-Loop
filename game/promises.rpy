# game/promises.rpy
# ═══════════════════════════════════════════════════
# СИСТЕМА ОБІЦЯНОК + ПЕЙДЖЕР
# ═══════════════════════════════════════════════════

init python:

    def create_promise(who, where, from_min, to_min, day, label):
        """Створює нову обіцянку."""
        store.promises.append({
            "who": who,
            "where": where,
            "from_min": from_min,
            "to_min": to_min,
            "day": day,
            "label": label,
            "fulfilled": False,
        })

    def check_broken_promises():
        """Перевіряє порушені обіцянки. Викликається в next_day()."""
        broken = []
        kept = []
        for p in store.promises:
            if p["day"] < store.day and not p.get("fulfilled"):
                # Порушена обіцянка
                add_chemistry(p["who"], -5)
                set_flag("broke_promise_" + p["who"].lower())
                broken.append(p)
            else:
                kept.append(p)
        # Видалити старі обіцянки
        store.promises = [p for p in store.promises if p["day"] >= store.day]

    def fulfill_promise(who):
        """Позначає обіцянку як виконану. +5 хімії."""
        for p in store.promises:
            if p["who"] == who and p["day"] == store.day and not p["fulfilled"]:
                p["fulfilled"] = True
                add_chemistry(who, 5)
                return True
        return False

    def has_active_promise(name, time_from, time_to):
        """Перевіряє чи є у персонажа обіцянка що перетинається з часом."""
        for p in store.promises:
            if p["who"] == name and p["day"] == store.day:
                if p["from_min"] < time_to and p["to_min"] > time_from:
                    return True
        return False

    def has_conflict(time_min):
        """Перевіряє чи є будь-яка обіцянка що конфліктує з часом."""
        for p in store.promises:
            if p["day"] == store.day:
                if p["from_min"] <= time_min < p["to_min"]:
                    return True
        return False

    def get_active_promises():
        """Повертає список активних обіцянок на сьогодні."""
        return [p for p in store.promises if p["day"] == store.day and not p["fulfilled"]]

    def promise_warning():
        """Перевіряє чи є обіцянка за 30 хвилин."""
        for p in store.promises:
            if p["day"] == store.day and not p["fulfilled"]:
                if 0 <= p["from_min"] - store.minutes <= 30:
                    return p
        return None


