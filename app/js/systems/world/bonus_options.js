// ═══════════════════════════════════════════════════
// ДИНАМІЧНІ ОПЦІЇ ДІАЛОГІВ — ПЛОСКА СИСТЕМА
// ═══════════════════════════════════════════════════
//
// Порт з bonus_options.rpy
//
// Будь-який діалог може отримати додаткові опції в меню
// на основі стану світу (флаги, хімія, одяг, інвентар).
//
// Опція НЕ прив'язана до конкретного діалогу — вона з'являється
// СКРІЗЬ де гравець говорить з цим NPC, якщо умова виконана.
//
// Структура запису:
// {
//     id: "arthur_metro_jacket_comment",
//     who: "Артур",                          <- з ким розмова
//     text: "О! Зачекай, це що та куртка?",  <- текст опції в меню
//     label: "arthur_metro_jacket_react",     <- label що викликається
//     conditions: { flag_true: [...], ... },  <- умови появи
//     outfit_check: ["Артур", "metro_jacket"], <- ОПЦІОНАЛЬНО
//     once: true                              <- зникає після використання
// }

// Глобальний реєстр динамічних опцій (сцени додають свої)
var BONUS_OPTIONS = [];


// Повертає список eligible бонусних опцій для NPC
function getBonusOptions(name) {
  var result = [];

  for (var i = 0; i < BONUS_OPTIONS.length; i++) {
    var opt = BONUS_OPTIONS[i];
    if (opt.who !== name) continue;

    // Перевірити чи вже використана
    if (opt.once && getFlag(opt.id + "_used")) continue;

    // Перевірити conditions
    var conds = opt.conditions || {};
    if (!checkStableConditions(conds)) continue;
    if (!checkDynamicConditions(conds)) continue;

    // Перевірити одяг (якщо вказано)
    if (opt.outfit_check) {
      var ocName = opt.outfit_check[0];
      var ocOutfit = opt.outfit_check[1];
      // gameState може мати систему одягу — перевірити через флаги
      if (getFlag("outfit_" + charFlag(ocName)) !== ocOutfit) continue;
    }

    // Перевірка кави: є кава + не давав сьогодні
    if (opt.id && opt.id.indexOf("coffee_give_") === 0) {
      if (!(hasAnyCoffee() && canGiveCoffeeTo(opt.who))) continue;
    }

    result.push(opt);
  }

  return result;
}


// Позначає бонусну опцію як використану
function markBonusUsed(optionId) {
  setFlag(optionId + "_used");
}


// ═══ Реєстрація бонусних опцій кави для всіх NPC ═══
// Ці опції з'являються коли гравець знайшов кавовий автомат

function _registerCoffeeBonusOptions() {
  // Ця функція викликається після завантаження CAST
  var castKeys = Object.keys(CAST);
  for (var i = 0; i < castKeys.length; i++) {
    var castName = CAST[castKeys[i]].name;
    var castId = charFlag(castName);
    BONUS_OPTIONS.push({
      id: "coffee_give_" + castId,
      who: castName,
      text: "\u0422\u0440\u0438\u043c\u0430\u0439. \u041f\u0440\u0438\u043d\u0456\u0441 \u043a\u0430\u0432\u0443.",  // Тримай. Приніс каву.
      label: "coffee_give_scene",
      conditions: {
        flag_true: ["coffee_machine_found"],
        flag_false: ["coffee_given_" + castId + "_today"]
      },
      once: false
    });
  }
}
