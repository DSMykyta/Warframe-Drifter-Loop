// ═══════════════════════════════════════════════════
// ПЕЙДЖЕР
// ═══════════════════════════════════════════════════
//
// Поведінка:
//
// ПОВІДОМЛЕННЯ:
//   Приходить → LCD активний 5 сек → тьмяніє → статус.
//   Центральна кнопка: перегляд повідомлень за сьогодні.
//   Бокові: гортають повідомлення.
//
// ЗАПИТ НА ДОПОМОГУ:
//   Приходить → LCD активний 5 сек → тьмяніє.
//   Запит НЕ зникає — замінює статус, висить до:
//     - гравець натисне ліву (так) або праву (ні)
//     - або пройде 1 ігрова година
//   Центральна: перегляд простих повідомлень (не чіпає запит).
//
// СТАНИ LCD:
//   idle    — тьмяний, показує статус АБО pending запит
//   active  — яскравий, показує повідомлення/запит (5 сек або перегляд)

var PAGER_MESSAGES = [];
var _pagerVisible = false;
var _pagerTimer = null;
var _pagerInboxIndex = 0;

registerState("pager", {
  inbox: [],       // повідомлення за сьогодні — зберігаються до nextDay
});

// Запит
var _pagerRequest = null;        // {who, text, arrivedAt} або null
var _pagerRequestAcceptLabel = null;
var _pagerRequestDeclineLabel = null;

// Стан LCD
var _pagerLcdMode = "idle";      // "idle" | "active"
var _pagerView = "status";       // "status" | "message" | "request_flash"
var _pagerFlashTimer = null;

// Pending response (для dialogue engine)
var _pagerResponse = null;
var _pagerPendingLabel = null;
var _pagerPendingWho = null;


// ─── ЗАВАНТАЖЕННЯ ───

function loadPagerMessages(callback) {
  loadCSV("data/pager_messages.csv", function(rows) {
    PAGER_MESSAGES = rows;
    if (callback) callback();
  });
}


// ─── ІНІЦІАЛІЗАЦІЯ ───

function initPager() {
  var btnLeft = document.querySelector(".pager-btn-left");
  var btnCenter = document.querySelector(".pager-btn-center");
  var btnRight = document.querySelector(".pager-btn-right");

  if (btnLeft) btnLeft.addEventListener("click", function(e) {
    e.stopPropagation();
    _pagerClickSound();
    // Запит — прийняти
    if (_pagerRequest) { _pagerAccept(); }
    // Повідомлення — попереднє
    else if (_pagerView === "message") {
      _pagerInboxIndex = Math.max(0, _pagerInboxIndex - 1);
      _renderLCD();
    }
    // Рушій чекає кнопку — повідомити ПІСЛЯ дії пейджера
    if (typeof _waitingForPager !== "undefined" && _waitingForPager) {
      onPagerButton("left");
    }
  });

  if (btnCenter) btnCenter.addEventListener("click", function(e) {
    e.stopPropagation();
    _pagerClickSound();
    // Перемикання: статус ↔ повідомлення
    if (_pagerView === "message") {
      _pagerView = "status";
      _pagerLcdMode = "idle";
    } else if (gameState.pager.inbox.length > 0) {
      _pagerView = "message";
      _pagerLcdMode = "active";
      _pagerInboxIndex = gameState.pager.inbox.length - 1;
    }
    if (!_pagerRequest) _renderLCD();
    // Рушій чекає
    if (typeof _waitingForPager !== "undefined" && _waitingForPager) {
      onPagerButton("center");
    }
  });

  if (btnRight) btnRight.addEventListener("click", function(e) {
    e.stopPropagation();
    _pagerClickSound();
    // Запит — відхилити
    if (_pagerRequest) { _pagerDecline(); }
    // Повідомлення — наступне
    else if (_pagerView === "message") {
      _pagerInboxIndex = Math.min(gameState.pager.inbox.length - 1, _pagerInboxIndex + 1);
      _renderLCD();
    }
    // Рушій чекає
    if (typeof _waitingForPager !== "undefined" && _waitingForPager) {
      onPagerButton("right");
    }
  });

  // Popup клік — закрити
  var popup = document.querySelector(".pager-popup");
  if (popup) {
    popup.addEventListener("click", function(e) {
      e.stopPropagation();
      popup.style.display = "none";
    });
  }
}


// ─── ПОКАЗАТИ / СХОВАТИ ───

function showPager() {
  var pager = document.querySelector(".pager");
  if (!getFlag("has_pager")) {
    if (pager) pager.style.display = "none";
    return;
  }
  if (pager) pager.style.display = "block";
  _pagerVisible = true;
  _renderLCD();
  startPagerInterval();
}

function hidePager() {
  var pager = document.querySelector(".pager");
  if (pager) pager.style.display = "none";
  _pagerVisible = false;
  stopPagerInterval();
}

function updatePagerScreen() {
  _renderLCD();
}


// ─── РЕНДЕР LCD ───

function _renderLCD() {
  var lcd = document.querySelector(".pager-lcd");
  if (!lcd) return;
  var pagerEl = document.querySelector(".pager");

  // CSS клас active/idle
  if (pagerEl) {
    if (_pagerLcdMode === "active") {
      pagerEl.classList.add("active");
    } else {
      pagerEl.classList.remove("active");
    }
  }

  // Перегляд повідомлень
  if (_pagerView === "message" && gameState.pager.inbox.length > 0) {
    var idx = Math.min(_pagerInboxIndex, gameState.pager.inbox.length - 1);
    var msg = gameState.pager.inbox[idx];
    lcd.innerHTML =
      '<div class="pager-lcd-who">' + msg.who + '</div>' +
      '<div class="pager-lcd-text">' + msg.text + '</div>' +
      '<div class="pager-lcd-counter">' + (idx + 1) + '/' + gameState.pager.inbox.length + '</div>';
    return;
  }

  // Pending запит — замінює статус
  if (_pagerRequest) {
    lcd.innerHTML =
      '<div class="pager-lcd-who">' + _pagerRequest.who + '</div>' +
      '<div class="pager-lcd-text">' + _pagerRequest.text + '</div>';
    return;
  }

  // Статус
  var time = typeof getTimeString === "function" ? getTimeString() : "--:--";
  var loc = typeof currentLocationName === "function" ? currentLocationName() : "???";
  var rep = gameState.rank ? gameState.rank.hex_rep || 0 : 0;

  lcd.innerHTML =
    '<div class="pager-lcd-loc">' + loc + '</div>' +
    '<div class="pager-lcd-time">' + time + '</div>' +
    '<div class="pager-lcd-rep">' + rep + '</div>' +
    '<img class="pager-lcd-hex" src="assets/icons/the-hex_pager.png" onerror="this.style.display=\'none\'">';
}


// ─── НАДІСЛАТИ ПОВІДОМЛЕННЯ ───

function sendPagerMessage(who, text) {
  var displayName = charName(who);

  var msg = { who: displayName, text: text };
  gameState.pager.inbox.push(msg);

  // LCD активний 5 сек з повідомленням
  _pagerView = "message";
  _pagerLcdMode = "active";
  _pagerInboxIndex = gameState.pager.inbox.length - 1;
  _renderLCD();

  _pagerBeepSound();

  // Через 5 сек — тьмяніє, повертається до статусу
  clearTimeout(_pagerFlashTimer);
  _pagerFlashTimer = setTimeout(function() {
    if (_pagerView === "message") {
      _pagerView = "status";
      _pagerLcdMode = "idle";
      _renderLCD();
    }
  }, 5000);
}


// ─── НАДІСЛАТИ ЗАПИТ ───

function sendPagerRequest(who, text, acceptLabel, declineLabel) {
  _pagerRequest = {
    who: charName(who),
    text: text,
    arrivedAt: gameState.time.minutes
  };
  _pagerRequestAcceptLabel = acceptLabel || null;
  _pagerRequestDeclineLabel = declineLabel || null;

  // LCD активний 5 сек
  _pagerView = "status"; // запит замінює статус
  _pagerLcdMode = "active";
  _renderLCD();

  _pagerBeepSound();

  // Через 5 сек — тьмяніє, але запит залишається
  clearTimeout(_pagerFlashTimer);
  _pagerFlashTimer = setTimeout(function() {
    _pagerLcdMode = "idle";
    _renderLCD();
  }, 5000);
}


// ─── ACCEPT / DECLINE ───

function _pagerAccept() {
  if (!_pagerRequest) return;
  _pagerResponse = "accept";
  _pagerPendingLabel = _pagerRequestAcceptLabel;
  _pagerPendingWho = _pagerRequest.who;
  _clearRequest();
}

function _pagerDecline() {
  if (!_pagerRequest) return;
  _pagerResponse = "decline";
  _pagerPendingLabel = _pagerRequestDeclineLabel;
  _pagerPendingWho = _pagerRequest.who;
  _clearRequest();
}

function _clearRequest() {
  _pagerRequest = null;
  _pagerRequestAcceptLabel = null;
  _pagerRequestDeclineLabel = null;
  _pagerLcdMode = "idle";
  _pagerView = "status";
  _renderLCD();
}


// ─── ПЕРЕВІРКА ТАЙМАУТУ ЗАПИТУ (1 ігрова година) ───

function checkPagerRequestTimeout() {
  if (!_pagerRequest) return;
  if (gameState.time.minutes - _pagerRequest.arrivedAt >= 60) {
    // Таймаут — запит зник, вважається ігнором
    _pagerResponse = "decline";
    _pagerPendingLabel = _pagerRequestDeclineLabel;
    _pagerPendingWho = _pagerRequest.who;
    _clearRequest();
  }
}


// ─── PENDING RESPONSE (для dialogue engine) ───

function hasPendingPager() {
  return _pagerResponse !== null;
}

function consumePagerResponse() {
  var resp = _pagerResponse;
  var label = _pagerPendingLabel;
  var who = _pagerPendingWho;
  _pagerResponse = null;
  _pagerPendingLabel = null;
  _pagerPendingWho = null;
  return { response: resp, label: label, who: who };
}


// ─── POPUP ───

function _showPopup(who, text) {
  var popup = document.querySelector(".pager-popup");
  if (!popup) return;
  popup.innerHTML = '<div class="pager-popup-who">' + who + '</div>' +
    '<div class="pager-popup-text">' + text + '</div>';
  popup.style.display = "flex";
  // Popup закривається тільки кліком (handler вже в initPager)
}


// ─── ВИПАДКОВЕ ПОВІДОМЛЕННЯ ───

function _sendRandomPagerMessage() {
  if (!_pagerVisible) return;
  if (PAGER_MESSAGES.length === 0) return;
  if (Math.random() > 0.3) return;

  var idx = Math.floor(Math.random() * PAGER_MESSAGES.length);
  var msg = PAGER_MESSAGES[idx];
  sendPagerMessage(charName(msg.who), msg.text);
}

function startPagerInterval() {
  stopPagerInterval();
  _pagerTimer = setInterval(function() {
    _sendRandomPagerMessage();
    checkPagerRequestTimeout();
    // Перевірити обіцянки (попередження за 30 хв)
    _checkPromiseWarning();
  }, 45000);
}

// Перевірити чи є обіцянка за 30 хв — попередити через пейджер
function _checkPromiseWarning() {
  if (typeof promiseWarning !== "function") return;
  var p = promiseWarning();
  if (!p) return;
  // Не дублювати — перевірити флаг
  var warnFlag = "promise_warned_" + p.who + "_" + p.day;
  if (typeof getFlag === "function" && getFlag(warnFlag)) return;
  if (typeof setFlag === "function") setFlag(warnFlag);
  sendPagerMessage(p.who, "Нагадування: зустріч через 30 хв.");
}

function stopPagerInterval() {
  if (_pagerTimer) { clearInterval(_pagerTimer); _pagerTimer = null; }
}


// ─── ЗВУКИ ───

function _pagerBeepSound() {
  try { var a = new Audio("assets/pager/pager_beep.mp3"); a.volume = 0.4; a.play(); } catch(e) {}
}

function _pagerClickSound() {
  try { var a = new Audio("assets/pager/pager_click.mp3"); a.volume = 0.3; a.play(); } catch(e) {}
}


// ─── HELP REQUEST ───

function checkPagerHelpRequest() {
  if (typeof checkHelpRequests !== "function") return;
  var request = checkHelpRequests();
  if (request) {
    sendPagerRequest(request.who, request.message, request.acceptLabel || null, request.declineLabel || null);
  }
}
