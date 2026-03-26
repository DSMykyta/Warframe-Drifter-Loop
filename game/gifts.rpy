# game/gifts.rpy
# Система подарунків — 1 подарунок на персонажа на день, 10 хв

init -5 python:

    def give_gift(character, item_id):
        """Дарує предмет персонажу. Повертає (bonus, reaction_text, is_offensive)."""
        # Перевірити чи вже дарував сьогодні
        if character in store.gifted_today:
            return (0, "Ти вже дарував мені сьогодні.", False)

        # Перевірити чи є предмет
        if item_id not in store.inventory or store.inventory[item_id] <= 0:
            return (0, "У тебе немає цього предмету.", False)

        # Забрати з інвентарю
        store.inventory[item_id] -= 1
        if store.inventory[item_id] <= 0:
            del store.inventory[item_id]

        # Позначити що дарував сьогодні
        store.gifted_today.add(character)

        # Час на подарунок
        advance_time(10)

        # Перевірка на образливий подарунок
        if item_id in OFFENSIVE_GIFTS and character in OFFENSIVE_GIFTS[item_id]:
            penalty, reaction = OFFENSIVE_GIFTS[item_id][character]
            store.chemistry[character] = max(0, store.chemistry[character] + penalty)
            # Ставимо флаг
            flag_name = "bad_gift_{}_{}".format(character.lower(), item_id)
            set_flag(flag_name)
            add_gossip("bad_gift_" + item_id, [character], spread_delay=1)
            return (penalty, reaction, True)

        # Перевірка на улюблений подарунок
        if item_id in GIFT_REACTIONS and character in GIFT_REACTIONS[item_id]:
            bonus = GIFT_REACTIONS[item_id][character]
            store.chemistry[character] += bonus
            reset_interaction(character)
            # Ставимо флаг для спеціальних реакцій на улюблені подарунки
            good_flag = "gifted_{}_{}".format(character.lower(), item_id)
            set_flag(good_flag)
            if bonus >= 20:
                return (bonus, "...Це саме те, що мені потрібно. Дякую.", False)
            elif bonus >= 10:
                return (bonus, "О, непогано. Дякую.", False)
            else:
                return (bonus, "Дякую, приємно.", False)

        # Нейтральний подарунок — +0
        return (0, "Дякую... мабуть.", False)


    # add_gossip() визначена в dispatcher.rpy — єдина версія
    # Сигнатура: add_gossip(fact, initial_knowers, spread_delay=2)


# ═══════════════════════════════════════════════
# LABEL для подарункового підменю
# ═══════════════════════════════════════════════

label gift_submenu(who):
    # Показує список предметів з інвентарю для вибору

    $ _gift_items = [(item_id, get_item_name(item_id)) for item_id, count in inventory.items() if count > 0]

    if not _gift_items:
        "Інвентар порожній."
        return

    if who in gifted_today:
        "Ти вже дарував [who] сьогодні."
        return

    call screen gift_selection(who, _gift_items)

    if isinstance(_return, str):
        $ _gift_result = give_gift(who, _return)
        $ _bonus = _gift_result[0]
        $ _reaction = _gift_result[1]
        $ _is_bad = _gift_result[2]

        "[who]: \"[_reaction]\""

        if _is_bad:
            "Здається, це був поганий вибір... ([_bonus] хімії)"
        elif _bonus > 0:
            "Подарунок сподобався! (+[_bonus] хімії)"
        else:
            "Нейтральна реакція."

    return


# Екран вибору подарунку
screen gift_selection(who, items):
    tag menu
    modal True

    frame:
        xfill True yfill True

        vbox:
            spacing 10

            text "Подарувати [who]:" size 24

            null height 10

            viewport:
                scrollbars "vertical"
                mousewheel True
                ysize 400

                vbox:
                    spacing 5
                    for item_id, item_name in items:
                        textbutton item_name action Return(item_id)

            null height 15

            textbutton "Нічого" action Return(None) xalign 0.5
