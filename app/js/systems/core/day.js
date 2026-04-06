// ═══════════════════════════════════════════════════
// ЦИКЛ ДНІВ — ПОВНА ВЕРСІЯ
// ═══════════════════════════════════════════════════
//
// Порт з day_logic.rpy: next_day() + всі підсистеми
//
// Як в Ren'Py:
// Гравець натискає "спати" -> nextDay() -> новий день
//
// Порядок виконання (як в оригіналі):
//  1. Штраф за пізній сон
//  2. Інкрементувати день
//  3. Скинути щоденні лічильники
//  4. days_without_mission++
//  5. check_broken_promises (якщо не emergency skip)
//  6. check_mission_neglect
//  7. apply_decay
//  7a. check_injuries_heal
//  7b. Скинути одноденні флаги
//  8. generate_missions
//  9. try_rank_up
// 10. check_expired_events
// 11. build_daily_deck
// 12. spread_gossip
// 13. autoSave

function nextDay() {
  // ═══ 1. Штраф за пізній сон ═══
  var penalty = Math.max(0, gameState.time.minutes - 1440);  // хвилини після 24:00
  var wakeUp = Math.min(720, 480 + penalty);                  // кеп на 12:00

  // ═══ 2. Інкрементувати день ═══
  gameState.time.day++;
  gameState.time.minutes = wakeUp;

  // ═══ 3. Скинути щоденні лічильники ═══

  // Хімія: скинути daily cap
  for (var name in gameState.chemistry.gainedToday) {
    gameState.chemistry.gainedToday[name] = 0;
  }

  // Диспетчер: скинути talked_today, tags_used_today
  gameState.dispatcher.talked_today = [];
  gameState.dispatcher.tags_used_today = {};

  // Подарунки: скинути gifted_today
  gameState.gifts.gifted_today = [];

  // Місії: скинути missions_today_with
  gameState.missions.missions_today_with = {};

  // ═══ 4. Лічильник днів без місій ═══
  gameState.missions.days_without_mission++;

  // ═══ 5. Перевірка порушених обіцянок (не під час emergency skip) ═══
  if (!getFlag("emergency_skip_active")) {
    checkBrokenPromises();
  }

  // ═══ 6. Штраф за ігнорування місій ═══
  checkMissionNeglect();

  // ═══ 7. Розпад стосунків ═══
  applyDecay();

  // ═══ 7a. Загоєння травм ═══
  checkInjuriesHeal();

  // ═══ 7b. Скинути одноденні флаги ═══
  var dailyFlags = [
    "lettie_healed_today",
    "amir_saw_bruises", "aoi_saw_injury", "arthur_saw_injury", "quincy_saw_injury",
    "helped_someone_today",
    "helped_lettie_today", "helped_amir_today", "helped_arthur_today",
    "helped_aoi_today", "helped_quincy_today", "helped_eleanor_today",
    "coffee_given_arthur_today", "coffee_given_eleanor_today",
    "coffee_given_lettie_today", "coffee_given_amir_today",
    "coffee_given_aoi_today", "coffee_given_quincy_today"
  ];
  for (var i = 0; i < dailyFlags.length; i++) {
    if (getFlag(dailyFlags[i])) {
      clearFlag(dailyFlags[i]);
    }
  }

  // ═══ 8. Генерація місій ═══
  generateMissions();

  // ═══ 9. Перевірка rank-up ═══
  tryRankUp();

  // ═══ 10. Обробити протухлі івенти (перед deck — ставить флаги) ═══
  checkExpiredEvents();

  // ═══ 11. Побудувати колоду eligible діалогів на день ═══
  buildDailyDeck();

  // ═══ 12. Поширити плітки ═══
  spreadGossip();

  // ═══ 13. Кавовий квест: хуки ═══
  if (typeof checkCoffeeExtractDeadline === "function") checkCoffeeExtractDeadline();
  if (typeof checkCoffeePartsPager === "function") checkCoffeePartsPager();
  if (typeof checkCoffeeAmirDiy === "function") checkCoffeeAmirDiy();
  if (typeof checkCoffeeCafeFind === "function") checkCoffeeCafeFind();
  if (typeof checkCoffeeCafeOpen === "function") checkCoffeeCafeOpen();

  // ═══ 14. Переміщення в бекрум (прокинувся) ═══
  gameState.location.current = "backroom";

  // ═══ 15. ��втозбереження ═══
  autoSave();
}
