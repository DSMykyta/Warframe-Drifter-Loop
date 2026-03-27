# game/inventory.rpy
# Каталог товарів та управління інвентарем

init -5 python:

    # ═══════════════════════════════════════════════
    # КАТАЛОГ МАГАЗИНУ
    # ═══════════════════════════════════════════════

    SHOP_CATALOG = [
        # ──── ПОДАРУНКИ: АРТУР (кухня та побут) ────
        {"id": "toaster", "name": "KineKitchen™ Toaster", "price": 300, "category": "gift"},
        {"id": "toaster_oven", "name": "KineKitchen™ Toaster Oven", "price": 350, "category": "gift"},
        {"id": "microwave", "name": "KineKitchen™ Microwave", "price": 400, "category": "gift"},
        {"id": "announce", "name": "Kinemantik™ Announce", "price": 300, "category": "gift"},
        {"id": "propane_tank", "name": "Green Gorilla™ Propane Tank", "price": 150, "category": "gift"},
        {"id": "keychains", "name": "KineBasik™ Asst. Metal Keychains", "price": 50, "category": "gift"},

        # ──── ПОДАРУНКИ: АОІ (музика, транспорт) ────
        {"id": "onlyne_album", "name": "On-lyne: The Boys R Back", "price": 300, "category": "gift"},
        {"id": "wireless_headphones", "name": "KineMagik!™ Wireless Headphones", "price": 400, "category": "gift"},
        {"id": "speaker_system", "name": "Kinemantik™ Speaker System", "price": 350, "category": "gift"},
        {"id": "scooticle", "name": "The Scooticle™", "price": 500, "category": "gift"},
        {"id": "gas_can", "name": "KineBasik™ Gas Can (Large)", "price": 80, "category": "gift"},
        {"id": "roadsigns", "name": "KineBasik™ Assorted Roadsigns", "price": 60, "category": "gift"},

        # ──── ПОДАРУНКИ: АМІР (техніка та ігри) ────
        {"id": "hockey_table", "name": "Kinemantik™ Hockey Table", "price": 450, "category": "gift"},
        {"id": "gpu_256", "name": "Kinemantik™ 256 GPU", "price": 250, "category": "gift"},
        {"id": "game_system", "name": "K.A.H.™ Game System", "price": 300, "category": "gift"},
        {"id": "game_monitor", "name": "K.A.H.™ Game Monitor", "price": 300, "category": "gift"},
        {"id": "tv_840hd", "name": "Kinemantik™ 840HD TV", "price": 350, "category": "gift"},

        # ──── ПОДАРУНКИ: КВІНСІ (електроніка, медіа) ────
        {"id": "video_camera", "name": "Kinemantik™ Digital Video Camera", "price": 400, "category": "gift"},
        {"id": "av_receiver", "name": "Kinemantik™ A/V Receiver", "price": 250, "category": "gift"},
        {"id": "speaker", "name": "Kinemantik™ Speaker", "price": 200, "category": "gift"},
        {"id": "cellphone", "name": "Kinemantik™ Cellphone", "price": 100, "category": "gift"},
        {"id": "poster", "name": "File-A-Style™ Insta-Print Poster", "price": 80, "category": "gift"},
        {"id": "vhs_series", "name": "'Circle of Comrades' Series on VHS", "price": 120, "category": "gift"},

        # ──── ПОДАРУНКИ: ЛЕТТІ (кава і побут) ────
        {"id": "coffee_machine", "name": "KineKitchen™ Coffee Machine", "price": 400, "category": "gift"},
        {"id": "medical_kit", "name": "KineBasik™ Medical Kit", "price": 200, "category": "gift"},
        {"id": "coffee_cups", "name": "File-A-Style™ Coffee Cups", "price": 80, "category": "gift"},
        {"id": "coffee_mug", "name": "KineBasik™ Coffee Mug", "price": 60, "category": "gift"},
        {"id": "pillows", "name": "KineBasik™ Pillows", "price": 100, "category": "gift"},
        {"id": "cardboard_box", "name": "KineBasik™ Cardboard Box", "price": 50, "category": "gift"},

        # ──── ПОДАРУНКИ: ЕЛЕОНОР (природа, канцелярія) ────
        {"id": "hanging_planter", "name": "KineBasik™ Hanging Planter", "price": 300, "category": "gift"},
        {"id": "notepad", "name": "File-a-Style™ Notepad", "price": 150, "category": "gift"},
        {"id": "binder", "name": "File-a-Style™ Binder", "price": 80, "category": "gift"},
        {"id": "pens", "name": "File-a-Style™ Pens", "price": 60, "category": "gift"},
        {"id": "pencils", "name": "File-a-Style™ Pencils", "price": 50, "category": "gift"},

        # ──── ДЕКОР БЕКРУМУ ────
        {"id": "arcade_machine", "name": "Аркадний автомат", "price": 800, "category": "decor"},
        {"id": "coffee_maker_decor", "name": "Кавоварка для бекруму", "price": 600, "category": "decor"},
        {"id": "bookshelf", "name": "Книжкова полиця", "price": 500, "category": "decor"},
        {"id": "dartboard", "name": "Мішень для дартсу", "price": 400, "category": "decor"},
        {"id": "neon_poster", "name": "Неоновий плакат", "price": 200, "category": "decor"},
        {"id": "led_lights", "name": "LED-освітлення", "price": 300, "category": "decor"},

        # ──── ВИТРАТНИКИ ────
        {"id": "medkit", "name": "Аптечка", "price": 100, "category": "consumable"},
        {"id": "energy_capsule", "name": "Енергокапсула", "price": 150, "category": "consumable"},

        # ──── ІНФОРМАЦІЯ ────
        {"id": "dossier_aoi", "name": "Файл ICR про Аоі", "price": 500, "category": "info"},
        {"id": "dossier_arthur", "name": "Файл ICR про Артура", "price": 500, "category": "info"},
        {"id": "dossier_eleanor", "name": "Файл ICR про Елеонор", "price": 500, "category": "info"},
        {"id": "dossier_lettie", "name": "Файл ICR про Летті", "price": 500, "category": "info"},
        {"id": "dossier_amir", "name": "Файл ICR про Аміра", "price": 500, "category": "info"},
        {"id": "dossier_quincy", "name": "Файл ICR про Квінсі", "price": 500, "category": "info"},
        {"id": "techrot_report", "name": "Звіт про Техрот", "price": 800, "category": "info"},
    ]

    # ═══════════════════════════════════════════════
    # ТАБЛИЦІ ПОДАРУНКІВ
    # ═══════════════════════════════════════════════

    # Хто що любить: {item_id: {character: chemistry_bonus}}
    # Баланс v2: loved=+12, liked=+7, small=+3
    GIFT_REACTIONS = {
        # Артур — кухня
        "toaster":        {"Артур": 12},
        "toaster_oven":   {"Артур": 12},
        "microwave":      {"Артур": 12},
        "announce":       {"Артур": 12},
        "propane_tank":   {"Артур": 7},
        "keychains":      {"Артур": 3},

        # Аоі — музика, транспорт
        "onlyne_album":       {"Аоі": 12},
        "wireless_headphones": {"Аоі": 12, "Амір": 12},
        "speaker_system":     {"Аоі": 12},
        "scooticle":          {"Аоі": 12},
        "gas_can":            {"Аоі": 3},
        "roadsigns":          {"Аоі": 3},

        # Амір — техніка, ігри
        "hockey_table":  {"Амір": 12},
        "gpu_256":       {"Амір": 7},
        "game_system":   {"Амір": 7},
        "game_monitor":  {"Амір": 7},
        "tv_840hd":      {"Амір": 7, "Квінсі": 3},

        # Квінсі — електроніка, медіа
        "video_camera":  {"Квінсі": 12},
        "av_receiver":   {"Квінсі": 7},
        "speaker":       {"Квінсі": 7},
        "cellphone":     {"Квінсі": 3},
        "poster":        {"Квінсі": 3},
        "vhs_series":    {"Квінсі": 3},

        # Летті — кава, побут
        "coffee_machine": {"Летті": 12},
        "medical_kit":    {"Летті": 7},
        "coffee_cups":    {"Летті": 3},
        "coffee_mug":     {"Летті": 3},
        "pillows":        {"Летті": 3, "Елеонор": 3},
        "cardboard_box":  {"Летті": 3},

        # Елеонор — природа, канцелярія
        "hanging_planter": {"Елеонор": 12},
        "notepad":         {"Елеонор": 7},
        "binder":          {"Елеонор": 3},
        "pens":            {"Елеонор": 3},
        "pencils":         {"Елеонор": 3},
    }

    # Образливі подарунки: {item_prefix_or_id: {character: (penalty, reaction_text)}}
    OFFENSIVE_GIFTS = {
        # Аоі ненавидить кухонне — стереотипи
        "toaster":      {"Аоі": (-5, "Це натяк? Що я жінка і маю місце на кухні?")},
        "toaster_oven": {"Аоі": (-5, "Кухонна техніка. Для мене. Серйозно?")},
        "microwave":    {"Аоі": (-5, "Мікрохвильовка. Яка... оригінальна ідея.")},

        # Квінсі не терпить натяків на слабкість
        "medical_kit":  {"Квінсі": (-3, "Думаєш я не впораюсь сам? Йди звідси.")},

        # Артур — дешеві сувеніри
        "keychains":    {"Артур": (-3, "...Ти серйозно? Краще б нічого не приносив.")},
        "roadsigns":    {"Артур": (-3, "Дорожні знаки. Дякую. Дуже... корисно.")},

        # Амір — книги/нудне
        "binder":       {"Амір": (-2, "О... дякую... я... поставлю на полицю. Десь.")},
        "notepad":      {"Амір": (-2, "Блокнот. Так. Запишу туди... щось.")},

        # Елеонор — техніка/гучне
        "speaker_system": {"Елеонор": (-5, "Ти знаєш що в мене в голові? І ти несеш ЦЕ?")},
        "speaker":        {"Елеонор": (-3, "Гучне. Саме те, чого мені не вистачало. Ні.")},
        "hockey_table":   {"Елеонор": (-5, "Хокейний стіл. Для мене. Ти взагалі мене знаєш?")},

        # Летті — духи/косметика (стереотипи)
        "hanging_planter": {"Летті": (-3, "Квітка. Для лікаря. Який не має часу навіть каву допити.")},
        "pillows":         {"Летті": (-2, "Подушки. Думаєш я тут сплю? ...Ну, іноді. Але це не привід.")},
    }

    # ═══════════════════════════════════════════════
    # ДЕКОР ЕФЕКТИ
    # ═══════════════════════════════════════════════

    DECOR_EFFECTS = {
        "arcade_machine":     {"flag": "decor_arcade", "trigger_char": "Амір"},
        "coffee_maker_decor": {"flag": "decor_coffee", "trigger_char": "Летті"},
        "bookshelf":          {"flag": "decor_bookshelf", "trigger_char": "Елеонор"},
        "dartboard":          {"flag": "decor_dartboard", "trigger_char": "Квінсі"},
        "neon_poster":        {"flag": "decor_neon"},
        "led_lights":         {"flag": "decor_led"},
    }

    # ═══════════════════════════════════════════════
    # ФУНКЦІЇ ІНВЕНТАРЮ
    # ═══════════════════════════════════════════════

    def buy_item(item_id):
        """Купує предмет з каталогу. Повертає True якщо успішно."""
        item = None
        for i in SHOP_CATALOG:
            if i["id"] == item_id:
                item = i
                break
        if not item:
            return False
        if store.money < item["price"]:
            return False
        store.money -= item["price"]
        # Додати в інвентар
        if item_id in store.inventory:
            store.inventory[item_id] += 1
        else:
            store.inventory[item_id] = 1
        # Декор — одразу активувати
        if item["category"] == "decor" and item_id in DECOR_EFFECTS:
            eff = DECOR_EFFECTS[item_id]
            set_flag(eff["flag"])
        # Інформація — одразу активувати флаг
        if item["category"] == "info":
            set_flag("has_" + item_id)
        return True

    def get_item_name(item_id):
        """Повертає назву предмета за id."""
        for i in SHOP_CATALOG:
            if i["id"] == item_id:
                return i["name"]
        return item_id

    def get_item_price(item_id):
        """Повертає ціну предмета."""
        for i in SHOP_CATALOG:
            if i["id"] == item_id:
                return i["price"]
        return 0

    def get_catalog_by_category(cat):
        """Повертає список товарів категорії."""
        return [i for i in SHOP_CATALOG if i["category"] == cat]
