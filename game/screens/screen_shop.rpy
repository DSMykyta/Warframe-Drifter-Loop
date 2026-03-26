# game/screen_shop.rpy
# Екран магазину — доступний з будь-якої локації, 0 хв

screen shop():
    tag menu
    modal True
    default current_cat = "gift"

    frame:
        xfill True yfill True
        style_prefix "shop"

        vbox:
            spacing 10
            xfill True

            hbox:
                xfill True
                text "МАГАЗИН" size 28
                text "Крони: [money]" size 20 xalign 1.0

            # Вкладки категорій
            hbox:
                spacing 15
                textbutton "Подарунки" action SetScreenVariable("current_cat", "gift")
                textbutton "Декор" action SetScreenVariable("current_cat", "decor")
                textbutton "Витратники" action SetScreenVariable("current_cat", "consumable")
                textbutton "Інформація" action SetScreenVariable("current_cat", "info")

            null height 10

            # Сітка товарів
            viewport:
                scrollbars "vertical"
                mousewheel True
                ysize 400

                vbox:
                    spacing 5
                    for item in get_catalog_by_category(current_cat):
                        $ _already = item["id"] in store.inventory and store.inventory[item["id"]] > 0
                        $ _can_buy = store.money >= item["price"] and not _already
                        # Декор та інфо — купується лише раз
                        $ _one_time = item["category"] in ("decor", "info")

                        hbox:
                            spacing 15
                            xfill True

                            text item["name"] size 16 yalign 0.5 xsize 350
                            $ _item_price = item["price"]
                            text "[_item_price] крон" size 14 yalign 0.5 xsize 100

                            if _already and _one_time:
                                text "Куплено" size 14 yalign 0.5 color "#888"
                            elif _can_buy:
                                textbutton "Купити" action Function(buy_item, item["id"]) yalign 0.5
                            elif not _can_buy and not _already:
                                text "Замало крон" size 14 yalign 0.5 color "#a55"

            null height 15

            textbutton "Закрити" action Return() xalign 0.5



# Екран інвентарю (для перегляду)
screen inventory_screen():
    tag menu
    modal True

    frame:
        xfill True yfill True

        vbox:
            spacing 10
            xfill True

            text "ІНВЕНТАР" size 28

            null height 10

            viewport:
                scrollbars "vertical"
                mousewheel True
                ysize 450

                vbox:
                    spacing 5
                    if not inventory:
                        text "Інвентар порожній." size 16 color "#888"
                    else:
                        for item_id, count in inventory.items():
                            hbox:
                                spacing 15
                                text get_item_name(item_id) size 16
                                if count > 1:
                                    text "x[count]" size 14 color "#aaa"

            null height 15

            textbutton "Закрити" action Return() xalign 0.5


# Label для відкриття магазину з гри
label open_shop:
    call screen shop
    return
