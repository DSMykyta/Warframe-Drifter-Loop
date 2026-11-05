# game/coffee.rpy
# ═══════════════════════════════════════════════════
# КАВОВИЙ АВТОМАТ — кав'ярня
# ═══════════════════════════════════════════════════

init -5 python:

    # ═══ ТИПИ КАВИ ═══

    COFFEE_MENU_BASE = [
        {"id": "coffee_black", "name": "Чорна кава", "price": 5, "desc": "Гаряча. Гірка. Чесна."},
        {"id": "coffee_espresso", "name": "Подвійний еспресо", "price": 25, "desc": "Удар. Для тих хто не спав."},
    ]

    COFFEE_MENU_MILK = [
        {"id": "coffee_latte", "name": "Лате", "price": 15, "desc": "М'яка, з молоком.", "requires_milk": True},
        {"id": "coffee_cocoa", "name": "Какао", "price": 15, "desc": "Солодке, густе, тепле.", "requires_milk": True},
        {"id": "coffee_cappuccino", "name": "Капучіно", "price": 20, "desc": "Піна, молоко, кава. Класика.", "requires_fresh": True},
    ]

    def get_available_coffees():
        """Повертає список доступних напоїв з урахуванням молока."""
        result = list(COFFEE_MENU_BASE)
        if store.flags.get("milk_drinks_unlocked"):
            for c in COFFEE_MENU_MILK:
                if c.get("requires_fresh") and not store.flags.get("milk_cappuccino_unlocked"):
                    continue
                result.append(c)
        return result

    # Хто що любить
    COFFEE_PREFERENCES = {
        "Артур":   "coffee_espresso",
        "Летті":   "coffee_latte",
        "Аоі":     "coffee_cocoa",
        "Амір":    "coffee_espresso",
        "Квінсі":  "coffee_black",
        "Елеонор": "coffee_latte",
    }

    # ═══ ФУНКЦІЇ ═══

    def has_any_coffee():
        for c in get_available_coffees():
            if store.inventory.get(c["id"], 0) > 0:
                return True
        return False

    def get_coffee_list():
        result = []
        for c in get_available_coffees():
            qty = store.inventory.get(c["id"], 0)
            if qty > 0:
                result.append({"id": c["id"], "name": c["name"], "qty": qty})
        return result

    def buy_coffee(coffee_id):
        for c in get_available_coffees():
            if c["id"] == coffee_id:
                if store.money >= c["price"]:
                    store.money -= c["price"]
                    store.inventory[coffee_id] = store.inventory.get(coffee_id, 0) + 1
                    return True
                return False
        return False

    def drink_coffee(coffee_id):
        if store.inventory.get(coffee_id, 0) <= 0:
            return None
        store.inventory[coffee_id] -= 1
        if store.inventory[coffee_id] <= 0:
            del store.inventory[coffee_id]
        return coffee_id

    def give_coffee_to(name, coffee_id):
        if store.inventory.get(coffee_id, 0) <= 0:
            return 0
        store.inventory[coffee_id] -= 1
        if store.inventory[coffee_id] <= 0:
            del store.inventory[coffee_id]
        set_flag("coffee_given_{}_today".format(char_flag(name)))
        preferred = COFFEE_PREFERENCES.get(name)
        if coffee_id == preferred:
            return 4
        return 2

    def can_give_coffee_to(name):
        if not has_any_coffee():
            return False
        flag = "coffee_given_{}_today".format(char_flag(name))
        return not store.flags.get(flag)


# ═══ БОНУСНІ ОПЦІЇ — "Тримай, каву приніс" ═══

init python:
    for _coffee_npc in CAST:
        BONUS_OPTIONS.append({
            "id": "coffee_give_{}".format(char_flag(_coffee_npc)),
            "who": _coffee_npc,
            "text": "Тримай. Приніс каву.",
            "label": "coffee_give_scene",
            "conditions": {
                "flag_true": ["coffee_machine_found"],
                "flag_false": ["coffee_given_{}_today".format(char_flag(_coffee_npc))],
            },
            "once": False,
        })


# ═══ ЕКРАН АВТОМАТУ ═══

screen coffee_machine():
    modal True
    add Solid("#00000088")

    vbox:
        align (0.5, 0.5)
        spacing 12
        xmaximum 600

        text "КАВОВИЙ АВТОМАТ" size 28 color "#facc15" bold True xalign 0.5

        null height 8

        for _c in get_available_coffees():
            $ _c_id = _c["id"]
            $ _c_name = _c["name"]
            $ _c_price = _c["price"]
            $ _c_desc = _c["desc"]
            $ _c_afford = store.money >= _c_price

            button:
                xfill True
                padding (20, 12, 20, 12)
                if _c_afford:
                    background Solid("#a855f712")
                    hover_background Solid("#a855f725")
                    action Return(("buy", _c_id))
                else:
                    background Solid("#ffffff06")
                    action NullAction()

                hbox:
                    spacing 16
                    yalign 0.5
                    vbox:
                        spacing 2
                        text "[_c_name]" size 18 color ("#d8b4fe" if _c_afford else "#ffffff30") bold True
                        text "[_c_desc]" size 13 color ("#ffffff40" if _c_afford else "#ffffff18")
                    text "[_c_price] крон" size 16 color ("#facc15" if _c_afford else "#ffffff20") yalign 0.5

        null height 8

        if has_any_coffee():
            text "В РУКАХ:" size 14 color "#ffffff30" xalign 0.5

            for _inv_c in get_coffee_list():
                $ _inv_id = _inv_c["id"]
                $ _inv_name = _inv_c["name"]
                $ _inv_qty = _inv_c["qty"]
                button:
                    xfill True
                    padding (20, 10, 20, 10)
                    background Solid("#22d3ee10")
                    hover_background Solid("#22d3ee25")
                    action Return(("drink", _inv_id))

                    hbox:
                        spacing 16
                        yalign 0.5
                        text "Випити [_inv_name]" size 16 color "#a5f3fc"
                        text "×[_inv_qty]" size 14 color "#ffffff40" yalign 0.5

        null height 12

        button:
            xfill True
            padding (20, 12, 20, 12)
            background Solid("#ffffff08")
            hover_background Solid("#ffffff18")
            action Return("leave")
            text "Відійти" size 16 color "#ffffff40" xalign 0.5


# ═══ LABELS ═══

label coffee_machine_interact:
    call screen coffee_machine
    $ _coffee_choice = _return

    if _coffee_choice == "leave":
        return

    if isinstance(_coffee_choice, tuple):

        if _coffee_choice[0] == "buy":
            $ _bought_id = _coffee_choice[1]
            $ _bought_ok = buy_coffee(_bought_id)
            if _bought_ok:
                python:
                    _bought_name = ""
                    for _cm in get_available_coffees():
                        if _cm["id"] == _bought_id:
                            _bought_name = _cm["name"]
                            break
                "Автомат гуде, щось булькає... [_bought_name]. Готово."
            else:
                "Не вистачає грошей."
            jump coffee_machine_interact

        if _coffee_choice[0] == "drink":
            $ _drink_id = _coffee_choice[1]
            $ _drank = drink_coffee(_drink_id)
            if _drank is not None:
                $ advance_time(10)
                if _drink_id == "coffee_espresso":
                    if store.minutes > 540:
                        $ store.minutes = max(480, store.minutes - 60)
                        $ store.hour = store.minutes // 60
                        "Подвійний еспресо. Як удар. Сонливість зникає."
                    else:
                        "Подвійний еспресо. Гіркий. Чесний. Працює."
                elif _drink_id == "coffee_cocoa":
                    "Какао. Солодке, густе, тепле. На хвилину — все нормально."
                elif _drink_id == "coffee_latte":
                    "Лате. М'яко. Тихо. Десять хвилин для себе."
                elif _drink_id == "coffee_cappuccino":
                    "Капучіно. Піна на губах. Майже як вдома. Майже."
                else:
                    "Чорна кава. Гаряче. Гірко. Достатньо."

                # Шанс на banter
                $ _cafe_chars = get_chars_at("cafe")
                if _cafe_chars and renpy.random.randint(1, 100) <= 40:
                    $ _cafe_npc = renpy.random.choice(_cafe_chars)
                    if _cafe_npc == "Аоі":
                        "Аоі сідає навпроти. Теж з чашкою. Мовчить. Нормально."
                    elif _cafe_npc == "Летті":
                        "Летті підходить. Сідає. Нічого не каже. Просто поруч."
                    elif _cafe_npc == "Амір":
                        "Амір з'являється нізвідки. «Оо, теж каву? Дай ковтнути!»"
                    elif _cafe_npc == "Квінсі":
                        "Квінсі кивнув здалеку. Це в нього — привітання."
                    elif _cafe_npc == "Артур":
                        "Артур проходить повз. Зупиняється. «Добрий вибір.» Йде далі."
                    elif _cafe_npc == "Елеонор":
                        "Елеонор сидить з книгою. Піднімає очі. Посміхається. Повертається до читання."

            jump coffee_machine_interact

    return


label coffee_give_scene:
    $ _coffee_target = _interact_target
    $ _my_coffees = get_coffee_list()

    if not _my_coffees:
        "В тебе нема кави."
        return

    menu:
        "Чорна кава" if store.inventory.get("coffee_black", 0) > 0:
            $ _give_id = "coffee_black"
        "Лате" if store.inventory.get("coffee_latte", 0) > 0:
            $ _give_id = "coffee_latte"
        "Какао" if store.inventory.get("coffee_cocoa", 0) > 0:
            $ _give_id = "coffee_cocoa"
        "Подвійний еспресо" if store.inventory.get("coffee_espresso", 0) > 0:
            $ _give_id = "coffee_espresso"
        "Капучіно" if store.inventory.get("coffee_cappuccino", 0) > 0:
            $ _give_id = "coffee_cappuccino"
        "Не зараз":
            return

    $ _chem_bonus = give_coffee_to(_coffee_target, _give_id)
    $ _is_preferred = (_give_id == COFFEE_PREFERENCES.get(_coffee_target))

    if _coffee_target == "Летті":
        if _is_preferred:
            "Летті бере чашку. П'є. Мовчить."
            "...довго мовчить."
            le "...Дякую."
        else:
            le "...Дякую."

    elif _coffee_target == "Артур":
        if _is_preferred:
            ar "Подвійний?"
            mc "Так."
            ar "Добре."
        else:
            ar "Дякую."

    elif _coffee_target == "Аоі":
        if _is_preferred:
            ao "О! Какао?! Ти серйозно?!"
            ao "ДЯКУЮЮ!"
        else:
            ao "О! Дякую!"

    elif _coffee_target == "Амір":
        am "Оо, брат! Рятуєш!"
        if _is_preferred:
            am "Подвійний?! Ти знаєш мої потреби!"

    elif _coffee_target == "Квінсі":
        if _is_preferred:
            qu "...чорна?"
            qu "...cheers."
        else:
            "Квінсі бере. Кивнув."

    elif _coffee_target == "Елеонор":
        if _is_preferred:
            el "Ти запам'ятав що я п'ю?"
        else:
            el "Дякую. Мило з твого боку."

    $ add_chemistry(_coffee_target, _chem_bonus)
    $ reset_interaction(_coffee_target)

    return
