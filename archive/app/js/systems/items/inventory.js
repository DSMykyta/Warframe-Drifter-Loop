// ═══════════════════════════════════════════════════
// ІНВЕНТАР ТА МАГАЗИН
// ═══════════════════════════════════════════════════
//
// Порт з inventory.rpy: SHOP_CATALOG, buy_item(), get_item_name()
//
// Каталог товарів — подарунки, декор, витратники, інформація.
// Кожен предмет має id, назву, ціну та категорію.

var SHOP_CATALOG = [
  // ──── ПОДАРУНКИ: АРТУР (кухня та побут) ────
  {id: "toaster",       name: "KineKitchen\u2122 Toaster",              price: 300, category: "gift"},
  {id: "toaster_oven",  name: "KineKitchen\u2122 Toaster Oven",         price: 350, category: "gift"},
  {id: "microwave",     name: "KineKitchen\u2122 Microwave",            price: 400, category: "gift"},
  {id: "announce",      name: "Kinemantik\u2122 Announce",              price: 300, category: "gift"},
  {id: "propane_tank",  name: "Green Gorilla\u2122 Propane Tank",       price: 150, category: "gift"},
  {id: "keychains",     name: "KineBasik\u2122 Asst. Metal Keychains",  price: 50,  category: "gift"},

  // ──── ПОДАРУНКИ: АОІ (музика, транспорт) ────
  {id: "onlyne_album",        name: "On-lyne: The Boys R Back",             price: 300, category: "gift"},
  {id: "wireless_headphones",  name: "KineMagik!\u2122 Wireless Headphones", price: 400, category: "gift"},
  {id: "speaker_system",      name: "Kinemantik\u2122 Speaker System",      price: 350, category: "gift"},
  {id: "scooticle",           name: "The Scooticle\u2122",                   price: 500, category: "gift"},
  {id: "gas_can",             name: "KineBasik\u2122 Gas Can (Large)",       price: 80,  category: "gift"},
  {id: "roadsigns",           name: "KineBasik\u2122 Assorted Roadsigns",    price: 60,  category: "gift"},

  // ──── ПОДАРУНКИ: АМІР (техніка та ігри) ────
  {id: "hockey_table", name: "Kinemantik\u2122 Hockey Table",   price: 450, category: "gift"},
  {id: "gpu_256",      name: "Kinemantik\u2122 256 GPU",        price: 250, category: "gift"},
  {id: "game_system",  name: "K.A.H.\u2122 Game System",        price: 300, category: "gift"},
  {id: "game_monitor", name: "K.A.H.\u2122 Game Monitor",       price: 300, category: "gift"},
  {id: "tv_840hd",     name: "Kinemantik\u2122 840HD TV",       price: 350, category: "gift"},

  // ──── ПОДАРУНКИ: КВІНСІ (електроніка, медіа) ────
  {id: "video_camera", name: "Kinemantik\u2122 Digital Video Camera", price: 400, category: "gift"},
  {id: "av_receiver",  name: "Kinemantik\u2122 A/V Receiver",         price: 250, category: "gift"},
  {id: "speaker",      name: "Kinemantik\u2122 Speaker",              price: 200, category: "gift"},
  {id: "cellphone",    name: "Kinemantik\u2122 Cellphone",            price: 100, category: "gift"},
  {id: "poster",       name: "File-A-Style\u2122 Insta-Print Poster", price: 80,  category: "gift"},
  {id: "vhs_series",   name: "'Circle of Comrades' Series on VHS",    price: 120, category: "gift"},

  // ──── ПОДАРУНКИ: ЛЕТТІ (кава і побут) ────
  {id: "coffee_machine", name: "KineKitchen\u2122 Coffee Machine",  price: 400, category: "gift"},
  {id: "medical_kit",    name: "KineBasik\u2122 Medical Kit",       price: 200, category: "gift"},
  {id: "coffee_cups",    name: "File-A-Style\u2122 Coffee Cups",    price: 80,  category: "gift"},
  {id: "coffee_mug",     name: "KineBasik\u2122 Coffee Mug",        price: 60,  category: "gift"},
  {id: "pillows",        name: "KineBasik\u2122 Pillows",           price: 100, category: "gift"},
  {id: "cardboard_box",  name: "KineBasik\u2122 Cardboard Box",     price: 50,  category: "gift"},

  // ──── ПОДАРУНКИ: ЕЛЕОНОР (природа, канцелярія) ────
  {id: "hanging_planter", name: "KineBasik\u2122 Hanging Planter", price: 300, category: "gift"},
  {id: "notepad",         name: "File-a-Style\u2122 Notepad",      price: 150, category: "gift"},
  {id: "binder",          name: "File-a-Style\u2122 Binder",       price: 80,  category: "gift"},
  {id: "pens",            name: "File-a-Style\u2122 Pens",         price: 60,  category: "gift"},
  {id: "pencils",         name: "File-a-Style\u2122 Pencils",      price: 50,  category: "gift"},

  // ──── ДЕКОР БЕКРУМУ ────
  {id: "arcade_machine",     name: "Аркадний автомат",        price: 800, category: "decor"},
  {id: "coffee_maker_decor", name: "Кавоварка для бекруму",   price: 600, category: "decor"},
  {id: "bookshelf",          name: "Книжкова полиця",         price: 500, category: "decor"},
  {id: "dartboard",          name: "Мішень для дартсу",       price: 400, category: "decor"},
  {id: "neon_poster",        name: "Неоновий плакат",         price: 200, category: "decor"},
  {id: "led_lights",         name: "LED-освітлення",          price: 300, category: "decor"},

  // ──── ВИТРАТНИКИ ────
  {id: "medkit",          name: "Аптечка",       price: 100, category: "consumable"},
  {id: "energy_capsule",  name: "Енергокапсула", price: 150, category: "consumable"},

  // ──── ІНФОРМАЦІЯ ────
  {id: "dossier_aoi",     name: "Файл ICR про Аоі",     price: 500, category: "info"},
  {id: "dossier_arthur",  name: "Файл ICR про Артура",   price: 500, category: "info"},
  {id: "dossier_eleanor", name: "Файл ICR про Елеонор",  price: 500, category: "info"},
  {id: "dossier_lettie",  name: "Файл ICR про Летті",    price: 500, category: "info"},
  {id: "dossier_amir",    name: "Файл ICR про Аміра",    price: 500, category: "info"},
  {id: "dossier_quincy",  name: "Файл ICR про Квінсі",   price: 500, category: "info"},
  {id: "techrot_report",  name: "Звіт про Техрот",       price: 800, category: "info"},
];


// Ефекти декору — встановлюють флаги при покупці
var DECOR_EFFECTS = {
  "arcade_machine":     {flag: "decor_arcade",    trigger_char: "\u0410\u043c\u0456\u0440"},   // Амір
  "coffee_maker_decor": {flag: "decor_coffee",    trigger_char: "\u041b\u0435\u0442\u0442\u0456"}, // Летті
  "bookshelf":          {flag: "decor_bookshelf", trigger_char: "\u0415\u043b\u0435\u043e\u043d\u043e\u0440"}, // Елеонор
  "dartboard":          {flag: "decor_dartboard", trigger_char: "\u041a\u0432\u0456\u043d\u0441\u0456"}, // Квінсі
  "neon_poster":        {flag: "decor_neon"},
  "led_lights":         {flag: "decor_led"},
};


registerState("inventory", {
  items: {}   // {"item_id": кількість}
});


// Купити предмет з каталогу. Повертає true якщо успішно.
function buyItem(itemId) {
  var item = null;
  for (var i = 0; i < SHOP_CATALOG.length; i++) {
    if (SHOP_CATALOG[i].id === itemId) {
      item = SHOP_CATALOG[i];
      break;
    }
  }
  if (!item) return false;
  if (gameState.money.amount < item.price) return false;

  // Списати гроші
  gameState.money.amount -= item.price;

  // Додати в інвентар
  if (gameState.inventory.items[itemId]) {
    gameState.inventory.items[itemId]++;
  } else {
    gameState.inventory.items[itemId] = 1;
  }

  // Декор — одразу активувати флаг
  if (item.category === "decor" && DECOR_EFFECTS[itemId]) {
    setFlag(DECOR_EFFECTS[itemId].flag);
  }

  // Інформація — одразу активувати флаг
  if (item.category === "info") {
    setFlag("has_" + itemId);
  }

  return true;
}


// Назва предмета за id
function getItemName(itemId) {
  for (var i = 0; i < SHOP_CATALOG.length; i++) {
    if (SHOP_CATALOG[i].id === itemId) {
      return SHOP_CATALOG[i].name;
    }
  }
  return itemId;
}


// Ціна предмета за id
function getItemPrice(itemId) {
  for (var i = 0; i < SHOP_CATALOG.length; i++) {
    if (SHOP_CATALOG[i].id === itemId) {
      return SHOP_CATALOG[i].price;
    }
  }
  return 0;
}


// Список товарів за категорією
function getCatalogByCategory(cat) {
  var result = [];
  for (var i = 0; i < SHOP_CATALOG.length; i++) {
    if (SHOP_CATALOG[i].category === cat) {
      result.push(SHOP_CATALOG[i]);
    }
  }
  return result;
}


// Кількість предмета в інвентарі
function getItemCount(itemId) {
  return gameState.inventory.items[itemId] || 0;
}


// Чи є предмет в інвентарі
function hasItem(itemId) {
  return getItemCount(itemId) > 0;
}


// Забрати предмет з інвентарю (1 шт). Повертає true якщо успішно.
function removeItem(itemId) {
  var count = gameState.inventory.items[itemId] || 0;
  if (count <= 0) return false;
  count--;
  if (count <= 0) {
    delete gameState.inventory.items[itemId];
  } else {
    gameState.inventory.items[itemId] = count;
  }
  return true;
}
