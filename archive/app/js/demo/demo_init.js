// ═══════════════════════════════════════════════════
// ДЕМО ІНІЦІАЛІЗАЦІЯ
// ═══════════════════════════════════════════════════
//
// Замінює intro на демо-сценарій.
// Вимикає звичайні діалоги — тільки демо.
// Встановлює стан для перевірки ВСІХ механік.

var DEMO_MODE = true;

// Перехопити startNewGame для демо
var _origStartNewGame = startNewGame;
startNewGame = function() {
  // Скинути auto/skip
  if (typeof _disableAutoMode === "function") _disableAutoMode();
  if (typeof _disableSkipToggle === "function") _disableSkipToggle();
  if (typeof _textHistory !== "undefined") _textHistory = [];

  // Скинути стан
  resetState();
  if (typeof clearSceneSprites === "function") clearSceneSprites();

  // Встановити стартові умови для демо
  gameState.time.day = 1;
  gameState.time.minutes = 600; // 10:00
  gameState.money.amount = 2000;
  gameState.rank.syndicate_rank = 1;
  gameState.rank.hex_rep = 0;
  gameState.location.current = "security_desk";

  // Ініціалізувати тригери
  if (typeof initTriggerData === "function") initTriggerData();
  if (typeof buildDailyDeck === "function") buildDailyDeck();

  // Флаги для доступу
  setFlag("intro_done");
  setFlag("explore_done");
  setFlag("has_pager");
  setFlag("has_map");
  setFlag("garage_unlocked");
  setFlag("rooftop_unlocked");
  setFlag("comp_club_unlocked");
  setFlag("cafe_unlocked");
  setFlag("cafe_balcony_unlocked");
  setFlag("coffee_machine_found");

  // Додати предмети в інвентар
  gameState.inventory.items["toaster"] = 1;
  gameState.inventory.items["wireless_headphones"] = 1;
  gameState.inventory.items["medical_kit"] = 1;
  gameState.inventory.items["coffee_black"] = 3;
  gameState.inventory.items["coffee_espresso"] = 2;
  gameState.inventory.items["coffee_latte"] = 1;

  // Початкова хімія (без daily cap — напряму)
  gameState.chemistry.values["ar"] = 10;
  gameState.chemistry.values["el"] = 10;
  gameState.chemistry.values["lt"] = 10;
  gameState.chemistry.values["am"] = 10;
  gameState.chemistry.values["ao"] = 10;
  gameState.chemistry.values["qu"] = 10;

  // Генерувати місії
  if (typeof generateMissions === "function") generateMissions();

  // Показати game-screen, сховати все зайве
  showScreen("game-screen");
  hideHUD();
  if (typeof hidePager === "function") hidePager();
  if (typeof _hideMapButton === "function") _hideMapButton();

  // Сховати UI локації
  var dlg = document.querySelector(".dialogue");
  if (dlg) dlg.style.display = "none";
  var choices = document.querySelector(".choices");
  if (choices) choices.style.display = "none";

  // Flow flags
  _afterIntro = false;
  _afterExplore = false;

  // Запустити демо
  runScript("demo_start");
};

// Перебудувати deck коли демо діалог завершується
var _origOnSceneEnd = onSceneEnd;
onSceneEnd = function() {
  // Перебудувати колоду щоб нові demo діалоги стали доступні
  if (typeof buildDailyDeck === "function") buildDailyDeck();
  _origOnSceneEnd();
};
