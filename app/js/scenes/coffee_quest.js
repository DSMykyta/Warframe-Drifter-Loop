// ═══════════════════════════════════════════════════
// КВЕСТ КАВИ — ВСІ 8 ЕТАПІВ + ХУКИ
// ═══════════════════════════════════════════════════
//
// Порт з game/quests/coffee/*.rpy
//
// Етапи:
// 1. Знахідка на місії (Амір або Квінсі)
// 2. Розмова з Аоі (бонусна опція)
// 3. Спецмісія: витягти кавомашину з Аоі
// 4. Аоі знаходить місце для кав'ярні
// 5. Склади Скальдри — деталі (данжн)
// 6. Амір запускає кав'ярню (групова сцена)
// 7. Молочна місія
// 8. Молочне меню розблоковано


// ═══════════════════════════════════════════════════
// ХУКИ ДЛЯ nextDay()
// ═══════════════════════════════════════════════════

function checkCoffeeExtractDeadline() {
  if (!getFlag("coffee_extract_available")) return;
  if (getFlag("coffee_machine_extracted")) return;
  if (getFlag("coffee_extract_reminded")) return;
  var deadline = gameState.flags.data["_coffee_extract_deadline"] || 0;
  if (gameState.time.day > deadline) {
    if (typeof sendPagerMessage === "function") {
      sendPagerMessage("Аоі", "Ми ще йдемо за кавомашиною?");
    }
    setFlag("coffee_extract_reminded");
  }
}

function checkCoffeePartsPager() {
  if (!getFlag("coffee_machine_extracted")) return;
  if (getFlag("coffee_parts_pager_sent")) return;
  if (!getFlag("coffee_parts_mission_pending")) return;
  if (gameState.time.minutes < 720) return;
  if (typeof sendPagerMessage === "function") {
    sendPagerMessage("Амір", "Марті! Кавомашина майже готова. Потрібні деталі зі складів Скальдри.");
  }
  setFlag("coffee_parts_pager_sent");
  setFlag("coffee_parts_mission_available");
  if (typeof generateMissions === "function") generateMissions();
}

function checkCoffeeAmirDiy() {
  if (getFlag("coffee_parts_got")) return;
  if (!getFlag("coffee_parts_failed") && !getFlag("coffee_parts_declined")) return;
  if (getFlag("coffee_amir_found_parts")) return;
  var targetDay = gameState.flags.data["_coffee_amir_diy_day"] || 0;
  if (gameState.time.day >= targetDay && targetDay > 0) {
    setFlag("coffee_amir_found_parts");
    setFlag("coffee_parts_got");
    if (typeof sendPagerMessage === "function") {
      sendPagerMessage("Амір", "МАРТІ! Я ЗНАЙШОВ ДЕТАЛІ! Кавомашина буде!!!");
    }
    if (typeof addJournalEntry === "function") {
      addJournalEntry("Амір знайшов деталі для кавомашини сам.", "event");
    }
  }
}

function checkCoffeeCafeOpen() {
  if (getFlag("cafe_unlocked")) return;
  if (!getFlag("coffee_parts_got")) return;
  setFlag("cafe_unlocked");
  setFlag("cafe_balcony_unlocked");
  setFlag("coffee_machine_found");
  setFlag("coffee_group_scene_pending");
  if (typeof sendPagerMessage === "function") {
    sendPagerMessage("Амір", "КАВ'ЯРНЯ ПРАЦЮЄ!!! ПРИХОДЬ!!!");
  }
  if (typeof addJournalEntry === "function") {
    addJournalEntry("Кав'ярня відкрита! Амір запустив кавомашину.", "event");
  }
}

function checkCoffeeCafeFind() {
  if (!getFlag("coffee_machine_extracted")) return;
  if (getFlag("cafe_find_pager_sent")) return;
  setFlag("cafe_unlocked");
  setFlag("cafe_balcony_unlocked");
  setFlag("cafe_find_scene_available");
  if (typeof sendPagerMessage === "function") {
    sendPagerMessage("Аоі", "Знайшла місце для кавомашини на другому поверсі біля балкону!");
  }
  setFlag("cafe_find_pager_sent");
}


// ═══════════════════════════════════════════════════
// МІСІЙНІ ДІАЛОГИ (ЕТАП 1)
// ═══════════════════════════════════════════════════

MISSION_DIALOGUE_ENTRIES.push({
  id: "coffee_find_machine",
  who: "Амір",
  conditions: {
    flag_false: ["coffee_find_machine_done", "coffee_quest_started", "coffee_quest_refused"],
    chemistry_min: ["Амір", 10]
  },
  priority: 60,
  chance: 100,
  label: "coffee_find_machine"
});

MISSION_DIALOGUE_ENTRIES.push({
  id: "coffee_find_machine_q",
  who: "Квінсі",
  conditions: {
    flag_false: ["coffee_find_machine_done", "coffee_quest_started", "coffee_quest_refused"],
    chemistry_min: ["Квінсі", 10]
  },
  priority: 60,
  chance: 100,
  label: "coffee_find_machine_quincy"
});


// ═══════════════════════════════════════════════════
// ДІАЛОГОВІ ЗАПИСИ (ЕТАП 6 — група, ЕТАП 4 — кафе)
// ═══════════════════════════════════════════════════

DIALOGUE_ENTRIES.push({
  id: "coffee_group_opening",
  who: "Амір",
  conditions: {
    flag_true: ["coffee_group_scene_pending"],
    flag_false: ["coffee_group_scene_done"],
    location: "cafe"
  },
  priority: 95,
  chance: 100,
  forced: true,
  label: "coffee_group_scene"
});

DIALOGUE_ENTRIES.push({
  id: "coffee_cafe_find_scene",
  who: "Аоі",
  conditions: {
    flag_true: ["cafe_find_scene_available"],
    flag_false: ["cafe_location_found"],
    location: "cafe"
  },
  priority: 95,
  chance: 100,
  forced: true,
  label: "cafe_find_scene"
});


// ═══════════════════════════════════════════════════
// БОНУСНІ ОПЦІЇ КАВОВОГО КВЕСТУ
// ═══════════════════════════════════════════════════

if (typeof BONUS_OPTIONS !== "undefined") {
  BONUS_OPTIONS.push({
    id: "coffee_tell_aoi",
    who: "Аоі",
    text: "Слухай, ми дещо знайшли на місії...",
    label: "coffee_tell_aoi_scene",
    conditions: {
      flag_true: ["coffee_quest_started"],
      flag_false: ["coffee_aoi_agreed"]
    },
    once: true
  });

  BONUS_OPTIONS.push({
    id: "coffee_extract_remind",
    who: "Аоі",
    text: "Про ту кавомашину — ти ще готова?",
    label: "coffee_extract_remind_scene",
    conditions: {
      flag_true: ["coffee_extract_delayed"],
      flag_false: ["coffee_machine_extracted"]
    },
    once: true
  });

  BONUS_OPTIONS.push({
    id: "coffee_apology_amir",
    who: "Амір",
    text: "Слухай, вибач що не дістав ті деталі...",
    label: "coffee_apology_amir_scene",
    conditions: {
      flag_true: ["coffee_parts_failed"],
      flag_false: ["coffee_apology_done"]
    },
    once: true
  });

  BONUS_OPTIONS.push({
    id: "milk_quest_ask_amir",
    who: "Амір",
    text: "Про молоко для кавомашини — я готовий.",
    label: "milk_quest_start_delayed",
    conditions: {
      flag_true: ["milk_quest_delayed", "coffee_group_scene_done"],
      flag_false: ["milk_quest_started"]
    },
    once: true
  });
}


// ═══════════════════════════════════════════════════
// СПЕЦМІСІЇ
// ═══════════════════════════════════════════════════

SPECIAL_MISSION_ENTRIES.push({
  id: "coffee_extract_mission",
  name: "Витягти кавомашину",
  level: 2,
  conditions: {
    flag_true: ["coffee_extract_available"],
    flag_false: ["coffee_machine_extracted"]
  },
  chance: 100,
  partner: "Аоі",
  reward: 50,
  rep: 1,
  label: "coffee_extract_scene"
});

SPECIAL_MISSION_ENTRIES.push({
  id: "coffee_parts_mission",
  name: "Склади Скальдри — деталі",
  level: 3,
  conditions: {
    flag_true: ["coffee_parts_mission_available"],
    flag_false: ["coffee_parts_mission_done"]
  },
  chance: 100,
  partner: null,
  reward: 200,
  rep: 3,
  label: "coffee_warehouse_dungeon"
});

SPECIAL_MISSION_ENTRIES.push({
  id: "coffee_milk_mission",
  name: "Пошук молока",
  level: 2,
  conditions: {
    flag_true: ["milk_quest_started"],
    flag_false: ["milk_mission_done"]
  },
  chance: 100,
  partner: null,
  reward: 100,
  rep: 2,
  label: "coffee_milk_scene"
});


// ═══════════════════════════════════════════════════
// СКРИПТИ ДІАЛОГІВ
// ═══════════════════════════════════════════════════

// Етап 1: Знахідка з Аміром
registerScript("coffee_find_machine", [
  {type: "say", who: "Амір", text: "Стій-стій-стій."},
  {type: "say", who: "Амір", text: "Бач оте? Під балкою."},
  {type: "say", who: null, text: "Під завалом — щось хромоване."},
  {type: "say", who: "Амір", text: "Це ж... ні. Це КАВОМАШИНА, Марті!"},
  {type: "say", who: null, text: "Амір штовхає балку. Не рухається."},
  {type: "say", who: "Амір", text: "Затиснута. Тонна металу зверху."},
  {type: "menu", choices: [
    {text: "Це багато мороки. Потім.", label: "coffee_find_refuse"},
    {text: "О. Ідея є.", label: "coffee_find_accept"}
  ]}
]);

registerScript("coffee_find_refuse", [
  {type: "say", who: null, text: "«Аміре, ми на місії. Потім.»"},
  {type: "say", who: "Амір", text: "...Ну добре. Але я запам'ятаю де це."},
  {type: "set_flag", flag: "coffee_quest_refused"},
  {type: "set_flag", flag: "coffee_find_machine_done"},
  {type: "end"}
]);

registerScript("coffee_find_accept", [
  {type: "say", who: null, text: "«Зачекай. Якщо підняти балку...»"},
  {type: "say", who: "Амір", text: "Одному? Та вона вагу трьох людей."},
  {type: "say", who: null, text: "«Не одному. Треба когось хто може метал зсунути.»"},
  {type: "say", who: "Амір", text: "О! Аоі! Вона ж Маг — металом рухає як нічого!"},
  {type: "say", who: "Амір", text: "Марті, ти ГЕНІЙ. Повернемось і розкажемо їй."},
  {type: "set_flag", flag: "coffee_quest_started"},
  {type: "set_flag", flag: "coffee_find_machine_done"},
  {type: "chemistry", who: "Амір", amount: 4},
  {type: "end"}
]);

// Етап 1: Знахідка з Квінсі
registerScript("coffee_find_machine_quincy", [
  {type: "say", who: null, text: "Квінсі зупиняється."},
  {type: "say", who: "Квінсі", text: "...hm."},
  {type: "say", who: null, text: "Під завалом — хромований край."},
  {type: "say", who: "Квінсі", text: "Looks like it."},
  {type: "say", who: null, text: "Квінсі штовхає балку ногою. Ніяк."},
  {type: "say", who: "Квінсі", text: "Важка. Треба когось, mate."},
  {type: "menu", choices: [
    {text: "Це багато мороки. Потім.", label: "coffee_find_refuse"},
    {text: "О. Ідея є.", label: "coffee_find_accept_q"}
  ]}
]);

registerScript("coffee_find_accept_q", [
  {type: "say", who: null, text: "«Квінсі, якщо привести когось хто може метал зсунути...»"},
  {type: "say", who: "Квінсі", text: "Аоі. Вона пів молу розібрала коли ми тут селились."},
  {type: "say", who: "Квінсі", text: "Скажи їй. I don't do conversations."},
  {type: "set_flag", flag: "coffee_quest_started"},
  {type: "set_flag", flag: "coffee_find_machine_done"},
  {type: "chemistry", who: "Квінсі", amount: 2},
  {type: "end"}
]);

// Етап 2: Розмова з Аоі
registerScript("coffee_tell_aoi_scene", [
  {type: "say", who: "Аоі", text: "Що знайшли?"},
  {type: "say", who: null, text: "«Кавомашину. Під завалами, на одній з ділянок.»"},
  {type: "say", who: "Аоі", text: "...Кавомашину?"},
  {type: "say", who: null, text: "«Хромовану. Здається робочу. Але вона під купою металу.»"},
  {type: "say", who: "Аоі", text: "Металеві балки?"},
  {type: "say", who: null, text: "«Так. Тонна мінімум.»"},
  {type: "say", who: "Аоі", text: "Я можу зсунути балки. Але мені потрібен хтось поруч — підстрахувати."},
  {type: "say", who: "Аоі", text: "Підемо разом?"},
  {type: "menu", choices: [
    {text: "Домовились.", label: "coffee_aoi_agree"},
    {text: "Це не небезпечно?", label: "coffee_aoi_careful"}
  ]}
]);

registerScript("coffee_aoi_agree", [
  {type: "say", who: "Аоі", text: "Добре. Я підготуюсь."},
  {type: "set_flag", flag: "coffee_aoi_agreed"},
  {type: "set_flag", flag: "coffee_extract_available"},
  {type: "chemistry", who: "Аоі", amount: 3},
  {type: "end"}
]);

registerScript("coffee_aoi_careful", [
  {type: "say", who: "Аоі", text: "Я обережна. Завжди. Але вдвох — безпечніше."},
  {type: "say", who: "Аоі", text: "Добре. Я підготуюсь."},
  {type: "set_flag", flag: "coffee_aoi_agreed"},
  {type: "set_flag", flag: "coffee_extract_available"},
  {type: "chemistry", who: "Аоі", amount: 2},
  {type: "end"}
]);

// Етап 3: Спецмісія витягнення
registerScript("coffee_extract_scene", [
  {type: "say", who: null, text: "Аоі вже на місці."},
  {type: "say", who: "Аоі", text: "Бачиш? Три балки."},
  {type: "say", who: null, text: "Хромований край кавомашини під завалом."},
  {type: "say", who: "Аоі", text: "Нижня — несуча. Зсуну верхні дві, нижня впаде сама."},
  {type: "say", who: null, text: "Аоі підносить руки. Метал стогне."},
  {type: "say", who: null, text: "Перша балка повільно зсувається вбік. Падає."},
  {type: "say", who: "Аоі", text: "Одна."},
  {type: "say", who: null, text: "Друга — заржавіла, вросла в стіну."},
  {type: "say", who: null, text: "Аоі стискає кулаки. Метал тріщить, гнеться..."},
  {type: "say", who: null, text: "Балка з'їжджає вбік."},
  {type: "say", who: "Аоі", text: "Є."},
  {type: "say", who: null, text: "Під брудом — хромована кавомашина. Ціла."},
  {type: "say", who: "Аоі", text: "...Вона ціла. Дивно. Все навколо зруйноване, а вона — ні."},
  {type: "menu", choices: [
    {text: "Ти молодець.", label: "coffee_extract_praise"},
    {text: "Амір буде в захваті.", label: "coffee_extract_amir"}
  ]}
]);

registerScript("coffee_extract_praise", [
  {type: "say", who: null, text: "«Ти молодець. Без тебе б не вийшло.»"},
  {type: "say", who: "Аоі", text: "...Дякую."},
  {type: "chemistry", who: "Аоі", amount: 4},
  {type: "say", who: "Аоі", text: "Я віднесу Аміру. А ти... дякую. За те що покликав мене."},
  {type: "set_flag", flag: "coffee_machine_extracted"},
  {type: "set_flag", flag: "coffee_parts_mission_pending"},
  {type: "chemistry", who: "Аоі", amount: 2},
  {type: "end"}
]);

registerScript("coffee_extract_amir", [
  {type: "say", who: "Аоі", text: "Він буде НЕСТЕРПНИЙ. Але... так. Я теж рада."},
  {type: "chemistry", who: "Аоі", amount: 3},
  {type: "say", who: "Аоі", text: "Я віднесу Аміру. А ти... дякую. За те що покликав мене."},
  {type: "set_flag", flag: "coffee_machine_extracted"},
  {type: "set_flag", flag: "coffee_parts_mission_pending"},
  {type: "chemistry", who: "Аоі", amount: 2},
  {type: "end"}
]);

// Етап 4: Кафе знайдено
registerScript("cafe_find_scene", [
  {type: "say", who: "Аоі", text: "Ось. Дивись."},
  {type: "say", who: null, text: "Стійка, крісла під чохлами, вітрина."},
  {type: "say", who: "Аоі", text: "Тут була кав'ярня. До всього цього. Я прибрала."},
  {type: "menu", choices: [
    {text: "Затишно. Навіть з пилом.", label: "cafe_find_nice"},
    {text: "Ти сама все прибрала?", label: "cafe_find_impressed"},
    {text: "Тут досі брудно.", label: "cafe_find_rude"}
  ]}
]);

registerScript("cafe_find_nice", [
  {type: "say", who: "Аоі", text: "Правда? Ходила повз сто разів. А потім подумала — навіщо це пустує?"},
  {type: "chemistry", who: "Аоі", amount: 3},
  {type: "say", who: "Аоі", text: "Як тільки Амір запустить машину — тут буде кав'ярня. Справжня."},
  {type: "set_flag", flag: "cafe_location_found"},
  {type: "end"}
]);

registerScript("cafe_find_impressed", [
  {type: "say", who: "Аоі", text: "Ну... метал зсунула. Решту руками. Не хотіла чекати."},
  {type: "chemistry", who: "Аоі", amount: 4},
  {type: "say", who: "Аоі", text: "Як тільки Амір запустить машину — тут буде кав'ярня. Справжня."},
  {type: "set_flag", flag: "cafe_location_found"},
  {type: "end"}
]);

registerScript("cafe_find_rude", [
  {type: "say", who: "Аоі", text: "...Я знаю. Я прибирала пів ночі."},
  {type: "say", who: "Аоі", text: "Вибач. Я думала тобі сподобається."},
  {type: "chemistry", who: "Аоі", amount: -3},
  {type: "set_flag", flag: "cafe_find_rude"},
  {type: "set_flag", flag: "cafe_location_found"},
  {type: "end"}
]);

// Етап 5: Склади Скальдри (спрощений данжн)
registerScript("coffee_warehouse_dungeon", [
  {type: "say", who: null, text: "Склади Скальдри. Промзона. Три корпуси за парканом."},
  {type: "say", who: null, text: "Потрібні клапан тиску і нагрівальний елемент."},
  {type: "menu", choices: [
    {text: "Головний вхід — швидко, але ризиковано", label: "coffee_wh_front"},
    {text: "Бічний прохід — через дірку в паркані", label: "coffee_wh_side"},
    {text: "Через дах — довше, але непомітно", label: "coffee_wh_roof"}
  ]}
]);

registerScript("coffee_wh_front", [
  {type: "say", who: null, text: "Паркан низький, ворота напіввідчинені. Зайшов напряму."},
  {type: "say", who: null, text: "Камера на стовпі повертається. Повільно."},
  {type: "menu", choices: [
    {text: "Проскочити між поворотами", label: "coffee_wh_stealth_ok"},
    {text: "Йти спокійно, не ховаючись", label: "coffee_wh_spotted"}
  ]}
]);

registerScript("coffee_wh_stealth_ok", [
  {type: "say", who: null, text: "Вичекав. Побіг. Встиг. Всередині. Тихо."},
  {type: "say", who: null, text: "Другий поверх. Табличка: 'Побутове обладнання — кімната 2Б-04'."},
  {type: "say", who: null, text: "Коробка 'Кавообладнання — запасні частини'. Клапан тиску. Нагрівальний елемент. Все."},
  {type: "say", who: null, text: "Назад. Тихо. Чисто."},
  {type: "say", who: null, text: "Деталі в рюкзаку. Ніхто не бачив. Чисто."},
  {type: "set_flag", flag: "coffee_parts_got"},
  {type: "set_flag", flag: "coffee_parts_stealth"},
  {type: "set_flag", flag: "coffee_parts_mission_done"},
  {type: "chemistry", who: "Амір", amount: 4},
  {type: "end"}
]);

registerScript("coffee_wh_spotted", [
  {type: "say", who: null, text: "Камера повернулась. Червоний діод мигнув."},
  {type: "say", who: null, text: "Десь глибоко в будівлі щось клацнуло."},
  {type: "say", who: null, text: "Другий поверх. Знайшов деталі, але тебе бачили."},
  {type: "say", who: null, text: "Кроки. Ближче. Хтось йде коридором."},
  {type: "menu", choices: [
    {text: "Сховатись і перечекати", label: "coffee_wh_hide_ok"},
    {text: "Бігти до виходу", label: "coffee_wh_run"}
  ]}
]);

registerScript("coffee_wh_hide_ok", [
  {type: "say", who: null, text: "За стелажем. Дихання затримане. Кроки пройшли повз."},
  {type: "say", who: null, text: "Деталі є. Але тебе бачили. Наступного разу буде складніше."},
  {type: "set_flag", flag: "coffee_parts_got"},
  {type: "set_flag", flag: "coffee_parts_mission_done"},
  {type: "chemistry", who: "Амір", amount: 3},
  {type: "end"}
]);

registerScript("coffee_wh_run", [
  {type: "say", who: null, text: "Біжиш. Коридор, сходи, двері. Встиг."},
  {type: "say", who: null, text: "Деталі є. Але тебе бачили."},
  {type: "set_flag", flag: "coffee_parts_got"},
  {type: "set_flag", flag: "coffee_parts_mission_done"},
  {type: "chemistry", who: "Амір", amount: 3},
  {type: "end"}
]);

registerScript("coffee_wh_side", [
  {type: "say", who: null, text: "Знайшов пролом. Протиснувся. Тихо. Камери сюди не дістають."},
  {type: "say", who: null, text: "Другий поверх. Кімната 2Б-04. Коробка 'Кавообладнання'. Все тут."},
  {type: "say", who: null, text: "Деталі в рюкзаку. Ніхто не бачив."},
  {type: "set_flag", flag: "coffee_parts_got"},
  {type: "set_flag", flag: "coffee_parts_stealth"},
  {type: "set_flag", flag: "coffee_parts_mission_done"},
  {type: "chemistry", who: "Амір", amount: 4},
  {type: "end"}
]);

registerScript("coffee_wh_roof", [
  {type: "say", who: null, text: "Пожежна драбина. Іржава, але тримає."},
  {type: "say", who: null, text: "Дах. Люк. Відкритий. Спустився на другий поверх — саме туди де треба."},
  {type: "say", who: null, text: "Кімната 2Б-04. Коробка. Клапан тиску. Нагрівальний елемент. Є."},
  {type: "say", who: null, text: "Назад через дах. Ніхто не бачив."},
  {type: "set_flag", flag: "coffee_parts_got"},
  {type: "set_flag", flag: "coffee_parts_stealth"},
  {type: "set_flag", flag: "coffee_parts_mission_done"},
  {type: "chemistry", who: "Амір", amount: 4},
  {type: "end"}
]);

// Етап 5b: Вибачення
registerScript("coffee_apology_amir_scene", [
  {type: "say", who: "Амір", text: "Та стій, стій."},
  {type: "say", who: "Амір", text: "Ти пішов. На склади. Один. Заради кавомашини."},
  {type: "say", who: "Амір", text: "Це вже більше ніж треба було."},
  {type: "say", who: "Амір", text: "Не парся, Марті. Ти зробив більше ніж будь-хто б зробив."},
  {type: "set_flag", flag: "coffee_apology_done"},
  {type: "chemistry", who: "Амір", amount: 3},
  {type: "end"}
]);

// Етап 6: Групова сцена
registerScript("coffee_group_scene", [
  {type: "say", who: "Амір", text: "ВСЕ! ВСІМ ТИХО!"},
  {type: "say", who: "Амір", text: "Дами і джентльмени. Квінсі."},
  {type: "say", who: "Квінсі", text: "Wow. Hilarious."},
  {type: "say", who: "Амір", text: "Дозвольте представити..."},
  {type: "say", who: null, text: "Кавомашина. Хромована, вичищена."},
  {type: "say", who: "Амір", text: "ТА-ДАМ! Робоча. Кавомашина. В нашому молі."},
  {type: "say", who: "Артур", text: "Ти серйозно зібрав нас заради кавомашини."},
  {type: "say", who: "Амір", text: "Артуре. КАВА. Справжня. Гаряча. Не та бурда з пакетиків."},
  {type: "say", who: "Елеонор", text: "Насправді, я вражена. Хто її знайшов?"},
  {type: "say", who: "Амір", text: "Марті знайшов! На місії. А Аоі витягла з-під завалів."},
  {type: "say", who: "Летті", text: "Вона хоча б чиста?"},
  {type: "say", who: "Амір", text: "Я промив тричі! Все стерильно!"},
  {type: "say", who: "Летті", text: "...Прийнятно."},
  {type: "say", who: "Амір", text: "ВІД ЛЕТТІ ЦЕ КОМПЛІМЕНТ!"},
  {type: "menu", choices: [
    {text: "А латте можна?", label: "coffee_group_milk"},
    {text: "Як вона працює?", label: "coffee_group_how"},
    {text: "Непогано, Аміре.", label: "coffee_group_praise"}
  ]}
]);

registerScript("coffee_group_milk", [
  {type: "say", who: "Амір", text: "О-о-о. Молоко. Проблема. Машина може, але в нас нема молока."},
  {type: "say", who: "Аоі", text: "Я бачила сухе молоко на складі поруч з консервами."},
  {type: "say", who: "Амір", text: "Марті? Береш квест на молоко?"},
  {type: "menu", choices: [
    {text: "Беру.", label: "coffee_group_milk_yes"},
    {text: "Потім.", label: "coffee_group_milk_later"}
  ]}
]);

registerScript("coffee_group_milk_yes", [
  {type: "say", who: "Амір", text: "КРАСАВА! Знайдеш молоко — лате, какао, капучіно, все буде!"},
  {type: "set_flag", flag: "milk_quest_started"},
  {type: "chemistry", who: "Амір", amount: 2},
  {type: "say", who: "Амір", text: "Ну все! Кав'ярня офіційно відкрита!"},
  {type: "say", who: "Квінсі", text: "Nobody asked for a ceremony, mate."},
  {type: "set_flag", flag: "coffee_group_scene_done"},
  {type: "end"}
]);

registerScript("coffee_group_milk_later", [
  {type: "say", who: "Амір", text: "Теж варіант. Але якщо надумаєш — скажи."},
  {type: "set_flag", flag: "milk_quest_delayed"},
  {type: "say", who: "Амір", text: "Ну все! Кав'ярня офіційно відкрита!"},
  {type: "say", who: "Квінсі", text: "Nobody asked for a ceremony, mate."},
  {type: "set_flag", flag: "coffee_group_scene_done"},
  {type: "end"}
]);

registerScript("coffee_group_how", [
  {type: "say", who: "Амір", text: "О! Натискаєш кнопку — зверху чорна кава. Міцна, гірка."},
  {type: "say", who: "Амір", text: "Є ще еспресо — подвійний удар. Для справжніх людей."},
  {type: "say", who: "Амір", text: "Ну все! Кав'ярня офіційно відкрита!"},
  {type: "say", who: "Квінсі", text: "Nobody asked for a ceremony, mate."},
  {type: "set_flag", flag: "coffee_group_scene_done"},
  {type: "end"}
]);

registerScript("coffee_group_praise", [
  {type: "say", who: "Амір", text: "НЕПОГАНО?! Це ШЕДЕВР!"},
  {type: "say", who: "Артур", text: "Це кавомашина."},
  {type: "say", who: "Артур", text: "Подвійний еспресо є?"},
  {type: "say", who: "Амір", text: "...Є."},
  {type: "say", who: "Артур", text: "Тоді нормально."},
  {type: "chemistry", who: "Артур", amount: 1},
  {type: "say", who: "Амір", text: "Ну все! Кав'ярня офіційно відкрита!"},
  {type: "say", who: "Квінсі", text: "Nobody asked for a ceremony, mate."},
  {type: "set_flag", flag: "coffee_group_scene_done"},
  {type: "end"}
]);

// Етап 5b: Молочний квест старт (відкладений)
registerScript("milk_quest_start_delayed", [
  {type: "say", who: "Амір", text: "О! Нарешті!"},
  {type: "say", who: "Амір", text: "Місія на дошці. Сухе молоко — на складах біля консервів."},
  {type: "say", who: "Амір", text: "Але якщо знайдеш щось краще — бери."},
  {type: "set_flag", flag: "milk_quest_started"},
  {type: "chemistry", who: "Амір", amount: 2},
  {type: "end"}
]);

// Етап 7: Молочна місія
registerScript("coffee_milk_scene", [
  {type: "say", who: null, text: "Склад поруч з консервами. Стелажі. Коробки. Пил."},
  {type: "say", who: null, text: "Картонна коробка з написом: 'СУХЕ МОЛОКО — 24 шт.' Дві пачки всередині."},
  {type: "menu", choices: [
    {text: "Взяти сухе і йти", label: "coffee_milk_dry"},
    {text: "Пошукати ще", label: "coffee_milk_search"}
  ]}
]);

registerScript("coffee_milk_dry", [
  {type: "say", who: null, text: "Дві пачки сухого молока в рюкзак. Достатньо."},
  {type: "say", who: null, text: "Сухе молоко доставлене. Краще ніж нічого."},
  {type: "set_flag", flag: "milk_type_dry"},
  {type: "set_flag", flag: "milk_drinks_unlocked"},
  {type: "set_flag", flag: "milk_mission_done"},
  {type: "chemistry", who: "Амір", amount: 2},
  {type: "end"}
]);

registerScript("coffee_milk_search", [
  {type: "say", who: null, text: "Далі. Холодильник. Старий, промисловий. Не працює."},
  {type: "say", who: null, text: "Всередині — пластикові пляшки. 'Пастеризоване молоко'."},
  {type: "menu", choices: [
    {text: "Взяти пастеризоване", label: "coffee_milk_pasteurized"},
    {text: "Шукати далі", label: "coffee_milk_deep"}
  ]}
]);

registerScript("coffee_milk_pasteurized", [
  {type: "say", who: null, text: "Три пляшки. Запечатані. Може пощастить."},
  {type: "say", who: null, text: "Пастеризоване молоко доставлене. Непогано."},
  {type: "set_flag", flag: "milk_type_pasteurized"},
  {type: "set_flag", flag: "milk_drinks_unlocked"},
  {type: "set_flag", flag: "milk_mission_done"},
  {type: "chemistry", who: "Амір", amount: 3},
  {type: "end"}
]);

registerScript("coffee_milk_deep", [
  {type: "say", who: null, text: "За стелажами — двері. 'Персонал'. Маленька кімната. Холодильник. Гуде."},
  {type: "say", who: null, text: "Цей працює. Свіже молоко. Справжнє. Ще добре."},
  {type: "menu", choices: [
    {text: "Взяти свіже (найкраще)", label: "coffee_milk_fresh"},
    {text: "Занадто ризиковано. Взяти пастеризоване.", label: "coffee_milk_pasteurized"}
  ]}
]);

registerScript("coffee_milk_fresh", [
  {type: "say", who: null, text: "Дві пляшки свіжого. Треба донести швидко."},
  {type: "say", who: null, text: "Свіже молоко доставлене. Амір буде в екстазі."},
  {type: "set_flag", flag: "milk_type_fresh"},
  {type: "set_flag", flag: "milk_drinks_unlocked"},
  {type: "set_flag", flag: "milk_cappuccino_unlocked"},
  {type: "set_flag", flag: "milk_mission_done"},
  {type: "chemistry", who: "Амір", amount: 4},
  {type: "end"}
]);

// Нагадування Аоі
registerScript("coffee_extract_remind_scene", [
  {type: "say", who: "Аоі", text: "Я завжди готова. Місія доступна. Коли скажеш."},
  {type: "chemistry", who: "Аоі", amount: 1},
  {type: "end"}
]);
