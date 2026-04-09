// ═══════════════════════════════════════════════════
// ЕКРАН ЗАВАНТАЖЕННЯ — список збережень
// ═══════════════════════════════════════════════════
//
// Ліва колонка: список слотів (авто + 1-20)
// Права колонка: деталі обраного збереження
// Кнопки: ЗАВАНТАЖИТИ / ВИДАЛИТИ

var _selectedSlot = null;

// Рендер списку збережень
function renderLoadScreen() {
  var slotsEl = document.querySelector("#load-screen .load-slots");
  var detailsEl = document.querySelector("#load-screen .load-details");
  if (!slotsEl || !detailsEl) return;

  _selectedSlot = null;

  // Зібрати всі збереження
  var saves = {};
  var autoRaw = localStorage.getItem(SAVE_PREFIX + "auto");
  if (autoRaw) {
    saves["auto"] = JSON.parse(autoRaw)._meta || {};
  }
  for (var i = 1; i <= MAX_SLOTS; i++) {
    var raw = localStorage.getItem(SAVE_PREFIX + i);
    if (raw) {
      saves[i] = JSON.parse(raw)._meta || {};
    }
  }

  // Рендер слотів
  var html = '';

  // Авто-слот
  html += _renderSlotRow("auto", "АВТО", saves["auto"]);

  // Слоти 1-20
  for (var s = 1; s <= MAX_SLOTS; s++) {
    html += _renderSlotRow(s, "СЛОТ " + s, saves[s]);
  }

  slotsEl.innerHTML = html;

  // Початковий стан деталей
  detailsEl.innerHTML = '<div class="load-details-empty">Оберіть збереження зліва</div>';
}


// Рядок одного слота
function _renderSlotRow(slot, label, meta) {
  var isEmpty = !meta;
  var cls = "load-slot";
  if (isEmpty) cls += " empty";

  var dateStr = '';
  if (meta && meta._ctime) {
    var d = new Date(meta._ctime);
    dateStr = _padZero(d.getDate()) + '.' +
      _padZero(d.getMonth() + 1) + '.' +
      d.getFullYear() + ' ' +
      _padZero(d.getHours()) + ':' +
      _padZero(d.getMinutes());
  }

  var desc = (meta && meta._save_name) ? meta._save_name : '';

  var onclick = isEmpty ? '' : ' onclick="_selectSaveSlot(\'' + slot + '\')"';

  return '<button class="' + cls + '"' + onclick + '>' +
    '<span class="load-slot-label">' + label + (desc ? ' — ' + desc : '') + '</span>' +
    (dateStr ? '<span class="load-slot-date">' + dateStr + '</span>' : '') +
    '</button>';
}


// Обрати слот
function _selectSaveSlot(slot) {
  _selectedSlot = slot;

  // Підсвітити обраний
  var allSlots = document.querySelectorAll("#load-screen .load-slot");
  for (var i = 0; i < allSlots.length; i++) {
    allSlots[i].classList.remove("selected");
  }
  // Знайти потрібний — по порядку (0=авто, 1-20=слоти)
  var idx = (slot === "auto") ? 0 : parseInt(slot);
  if (allSlots[idx]) allSlots[idx].classList.add("selected");

  // Показати деталі
  var detailsEl = document.querySelector("#load-screen .load-details");
  if (!detailsEl) return;

  var raw = localStorage.getItem(SAVE_PREFIX + slot);
  if (!raw) {
    detailsEl.innerHTML = '<div class="load-details-empty">Збереження пошкоджене або видалене</div>';
    return;
  }

  var data = JSON.parse(raw);
  var meta = data._meta || {};

  var html = '<div class="load-details-info">';

  // Назва збереження
  if (meta._save_name) {
    html += '<div class="detail-row"><span class="detail-label">Опис</span>' +
      '<span class="detail-value">' + _escapeHtml(meta._save_name) + '</span></div>';
  }

  // Дата
  if (meta._ctime) {
    var d = new Date(meta._ctime);
    var dateStr = _padZero(d.getDate()) + '.' +
      _padZero(d.getMonth() + 1) + '.' +
      d.getFullYear() + ' ' +
      _padZero(d.getHours()) + ':' +
      _padZero(d.getMinutes()) + ':' +
      _padZero(d.getSeconds());
    html += '<div class="detail-row"><span class="detail-label">Збережено</span>' +
      '<span class="detail-value">' + dateStr + '</span></div>';
  }

  // Ігрові дані
  if (data.time) {
    html += '<div class="detail-row"><span class="detail-label">День</span>' +
      '<span class="detail-value">' + (data.time.day || '?') + '</span></div>';
  }
  if (data.location && data.location.current && LOCATION_NAMES[data.location.current]) {
    html += '<div class="detail-row"><span class="detail-label">Локація</span>' +
      '<span class="detail-value">' + LOCATION_NAMES[data.location.current] + '</span></div>';
  }
  if (data.money) {
    html += '<div class="detail-row"><span class="detail-label">Крони</span>' +
      '<span class="detail-value">' + data.money.amount + '</span></div>';
  }
  if (data.rank) {
    html += '<div class="detail-row"><span class="detail-label">Ранг</span>' +
      '<span class="detail-value">' + data.rank.syndicate_rank + '</span></div>';
  }

  html += '</div>';

  // Кнопки
  html += '<div class="load-actions">';
  html += '<button class="btn btn-load" onclick="_loadSelectedSlot()">ЗАВАНТАЖИТИ</button>';
  html += '<button class="btn btn-delete" onclick="_deleteSelectedSlot()">ВИДАЛИТИ</button>';
  html += '</div>';

  detailsEl.innerHTML = html;
}


// Завантажити обраний слот
function _loadSelectedSlot() {
  if (_selectedSlot === null) return;

  function _doLoad() {
    // Скинути auto/skip та бекло́г перед завантаженням
    if (typeof _disableAutoMode === "function") _disableAutoMode();
    if (typeof _disableSkipToggle === "function") _disableSkipToggle();
    if (typeof _textHistory !== "undefined") _textHistory = [];
    if (load(_selectedSlot)) {
      showScreen("game-screen");
      // Перевірити чи був діалог — якщо так, відновити сцену
      if (gameState.dialogue_engine && gameState.dialogue_engine.scriptName && currentScript) {
        showHUD();
        updateHUD();
        if (typeof showPager === "function") showPager();
        execute(pc);
      } else {
        showLocation();
      }
    }
  }

  // Якщо гра активна — підтвердження
  if (typeof _isGameActive === "function" && _isGameActive() && typeof confirmDialog === "function") {
    confirmDialog("Завантажити? Незбережений прогрес буде втрачено.", _doLoad);
  } else {
    _doLoad();
  }
}


// Видалити обраний слот
function _deleteSelectedSlot() {
  if (_selectedSlot === null) return;
  if (_selectedSlot === "auto") return; // Автозбереження не можна видалити
  if (typeof confirmDialog === "function") {
    confirmDialog("Видалити це збереження?", function() {
      deleteSave(_selectedSlot);
      renderLoadScreen();
    });
  } else {
    deleteSave(_selectedSlot);
    renderLoadScreen();
  }
}


// Доповнення нулем
function _padZero(n) {
  return n < 10 ? '0' + n : '' + n;
}

// Екранування HTML (захист від XSS)
function _escapeHtml(str) {
  var div = document.createElement("div");
  div.appendChild(document.createTextNode(str));
  return div.innerHTML;
}
