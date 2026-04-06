// ═══════════════════════════════════════════════════
// ІГРОВИЙ ЦИКЛ
// ═══════════════════════════════════════════════════
//
// Порядок гри:
// 1. НОВА ПЕТЛЯ → resetState → intro → explore_mall → location loop
// 2. Локація: showLocation → NPC/карта/сон
// 3. Сон: nextDay → нові місії → новий день → showLocation
// 4. Повторювати до дня 31

var _afterIntro = false;   // Чи потрібно запустити explore_mall після intro
var _afterExplore = false; // Чи потрібно перейти в location loop після explore_mall

function startNewGame() {
  // Скинути весь стан
  resetState();

  // Початкові значення для першого дня
  gameState.time.day = 1;
  gameState.time.minutes = 660; // 11:00 — допит
  gameState.location.current = "foodcourt";
  gameState.money.amount = 0;

  // Ініціалізувати trigger data (потрібно після CAST завантажено)
  if (typeof initTriggerData === "function") initTriggerData();

  // Побудувати колоду діалогів
  if (typeof buildDailyDeck === "function") buildDailyDeck();

  // Показати ігровий екран
  showScreen("game-screen");
  hideHUD();
  if (typeof hidePager === "function") hidePager();
  _hideMapButton();

  // Позначити що після інтро треба перейти в explore_mall
  _afterIntro = true;
  _afterExplore = false;

  // Запустити інтро
  if (SCRIPTS["intro"]) {
    runScript("intro");
  } else {
    console.warn("[game] No intro script! Skipping to location loop.");
    _startLocationLoop();
  }
}


// Викликається коли будь-яка сцена закінчується (end node + клік)
function onSceneEnd() {
  if (_afterIntro) {
    _afterIntro = false;

    // Додати записи в щоденник та думки (як в intro.rpy)
    if (typeof addJournalEntry === "function") {
      addJournalEntry("Допит. Розв'язали. Марті. Завтра о восьмій.", "event");
    }
    if (typeof addInsight === "function") {
      addInsight("hex_exists", "Шестеро в молі. Гекс.");
      addInsight("arthur_leads", "Артур — лідер. Меч наскрізь через долоню — між кістками.");
      addInsight("nickname_marty", "Амір назвав Марті. Прижилось.");
      addInsight("aoi_logistics", "Аоі — логістика. Перша простягнула руку.");
      addInsight("quincy_sniper", "Квінсі. Тир. Без стуку.");
      addInsight("amir_tech", "Амір — технік. Аркади.");
      if (getFlag("lettie_bandaged_hand")) {
        addInsight("lettie_medic", "Летті — медик. Перев'язала без питань.");
      }
    }

    // Запустити explore_mall
    if (SCRIPTS["explore_mall"]) {
      _afterExplore = true;
      runScript("explore_mall");
    } else {
      _startLocationLoop();
    }
    return;
  }

  if (_afterExplore) {
    _afterExplore = false;
    _startLocationLoop();
    return;
  }

  // Звичайне завершення сцени — повернутись до локації
  _returnToLocation();
}


// Почати основний цикл гри (exploration loop)
function _startLocationLoop() {
  // Встановити локацію і час для першого дня
  gameState.location.current = "backroom";
  gameState.time.minutes = 660; // 11:00

  // Генерувати місії
  if (typeof generateMissions === "function") {
    generateMissions();
  }

  // Побудувати колоду діалогів
  if (typeof buildDailyDeck === "function") {
    buildDailyDeck();
  }

  // Автозбереження
  if (typeof autoSave === "function") autoSave();

  // Показати локацію
  _returnToLocation();
}


// Повернутись до UI локації (після будь-якого діалогу)
function _returnToLocation() {
  showHUD();
  updateHUD();
  if (typeof showPager === "function") showPager();
  showLocation();

  // Перевірити help requests через пейджер
  if (typeof checkPagerHelpRequest === "function") {
    setTimeout(checkPagerHelpRequest, 3000);
  }
}
