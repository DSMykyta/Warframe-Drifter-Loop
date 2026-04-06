// ═══════════════════════════════════════════════════
// ПЕЙДЖЕР — віджет повідомлень
// ═══════════════════════════════════════════════════
//
// Показує: статус (час/локація) або повідомлення від NPC.
// Клік — переключити режим.
// Флешить коли нове повідомлення.
// Випадкові повідомлення надсилаються під час гри.

var PAGER_MESSAGES = [];       // Завантажені повідомлення з CSV
var _pagerQueue = [];          // Черга непрочитаних
var _pagerMode = "status";     // "status" або "message"
var _pagerVisible = false;
var _pagerTimer = null;
var _pagerFlashing = false;


// ─── ЗАВАНТАЖЕННЯ ПОВІДОМЛЕНЬ З CSV ───

function loadPagerMessages(callback) {
  loadCSV("data/pager_messages.csv", function(rows) {
    PAGER_MESSAGES = rows;
    if (callback) callback();
  });
}


// ─── ІНІЦІАЛІЗАЦІЯ ПЕЙДЖЕРА ───

function initPager() {
  var pager = document.querySelector(".pager");
  if (!pager) return;

  // Клік на пейджер — переключити режим
  pager.addEventListener("click", function(e) {
    e.stopPropagation();
    togglePagerMode();
  });

  // Клік на popup — закрити
  var popup = document.querySelector(".pager-popup");
  if (popup) {
    popup.addEventListener("click", function(e) {
      e.stopPropagation();
      popup.style.display = "none";
    });
  }
}


// ─── ПОКАЗАТИ / СХОВАТИ ПЕЙДЖЕР ───

function showPager() {
  var pager = document.querySelector(".pager");
  if (!getFlag("has_pager")) {
    if (pager) pager.style.display = "none";
    return;
  }
  if (pager) pager.style.display = "flex";
  _pagerVisible = true;
  updatePagerScreen();
  startPagerInterval();
}

function hidePager() {
  var pager = document.querySelector(".pager");
  if (pager) pager.style.display = "none";
  _pagerVisible = false;
  stopPagerInterval();
}


// ─── ОНОВИТИ ЕКРАН ПЕЙДЖЕРА ───

function updatePagerScreen() {
  var screen = document.querySelector(".pager-screen");
  if (!screen) return;

  var hasPager = getFlag("has_pager");

  if (_pagerQueue.length > 0) {
    var msg = _pagerQueue[0];
    screen.innerHTML = '<div class="pager-who">' + msg.who + '</div>' +
      '<div class="pager-text">' + msg.text + '</div>';
    _pagerMode = "message";
  } else if (hasPager) {
    // Пейджер є але немає повідомлень — порожній екран
    _pagerMode = "status";
    screen.innerHTML = '<div class="pager-status-time" style="font-size:14px;color:rgba(255,255,255,0.3);">Немає повідомлень</div>';
  } else {
    // Пейджер ще не отриманий — сховати
    _pagerMode = "status";
    screen.innerHTML = '';
    var pager2 = document.querySelector(".pager");
    if (pager2) pager2.style.display = "none";
  }
}


// ─── ПЕРЕКЛЮЧИТИ РЕЖИМ ───

function togglePagerMode() {
  if (_pagerMode === "status" && _pagerQueue.length > 0) {
    _pagerMode = "message";
    _pagerFlashing = false;
    var pager = document.querySelector(".pager");
    if (pager) pager.classList.remove("pager-flash");
  } else if (_pagerMode === "message") {
    // Прочитане — видалити зі черги
    if (_pagerQueue.length > 0) _pagerQueue.shift();
    if (_pagerQueue.length > 0) {
      // Наступне повідомлення
      _pagerMode = "message";
    } else {
      _pagerMode = "status";
    }
  }
  updatePagerScreen();
}


// ─── НАДІСЛАТИ ПОВІДОМЛЕННЯ ───

function sendPagerMessage(who, text) {
  var charData = CAST_BY_NAME[who];
  var displayName = charData ? charData.name : who;

  _pagerQueue.push({ who: displayName, text: text });

  // Флеш пейджера
  _pagerFlashing = true;
  var pager = document.querySelector(".pager");
  if (pager) pager.classList.add("pager-flash");

  // Показати popup
  var popup = document.querySelector(".pager-popup");
  if (popup) {
    popup.innerHTML = '<div class="pager-popup-who">' + displayName + '</div>' +
      '<div class="pager-popup-text">' + text + '</div>';
    popup.style.display = "flex";
    setTimeout(function() { popup.style.display = "none"; }, 4000);
  }

  // Оновити екран якщо видно
  if (_pagerVisible) updatePagerScreen();
}


// ─── ВИПАДКОВЕ ПОВІДОМЛЕННЯ ───

function _sendRandomPagerMessage() {
  if (!_pagerVisible) return;
  if (PAGER_MESSAGES.length === 0) return;

  // 30% шанс кожного разу
  if (Math.random() > 0.3) return;

  // Вибрати випадкове повідомлення
  var idx = Math.floor(Math.random() * PAGER_MESSAGES.length);
  var msg = PAGER_MESSAGES[idx];

  // Конвертувати short в ім'я
  var name = charName(msg.who);
  if (name === msg.who && CAST[msg.who]) {
    name = CAST[msg.who].name;
  }

  sendPagerMessage(name, msg.text);
}


// ─── ІНТЕРВАЛ ПОВІДОМЛЕНЬ ───

function startPagerInterval() {
  stopPagerInterval();
  // Кожні 45 секунд реального часу — спроба надіслати повідомлення
  _pagerTimer = setInterval(_sendRandomPagerMessage, 45000);
}

function stopPagerInterval() {
  if (_pagerTimer) {
    clearInterval(_pagerTimer);
    _pagerTimer = null;
  }
}


// ─── ПЕРЕВІРКА HELP REQUEST ЧЕРЕЗ ПЕЙДЖЕР ───

function checkPagerHelpRequest() {
  var request = checkHelpRequests();
  if (request) {
    sendPagerMessage(request.who, request.message);
    // Зберегти активний запит
    gameState._activeHelpRequest = request;
  }
}
