// ═══════════════════════════════════════════════════
// ТЕКСТОВА ІСТОРІЯ (БЕКЛО́Г)
// ═══════════════════════════════════════════════════
//
// Зберігає останні 200 реплік. Відкривається через
// quick menu, колесо миші вгору, або клавішу L.

var _textHistory = [];
var _textHistoryMax = 200;

function pushToHistory(who, text, type) {
  var entry = {
    who: who || null,
    name: who ? charName(who) : null,
    text: text,
    type: type || "say"
  };
  _textHistory.push(entry);
  if (_textHistory.length > _textHistoryMax) {
    _textHistory.shift();
  }
}

function showBacklog() {
  var overlay = document.getElementById("overlay-backlog");
  if (!overlay) return;
  overlay.style.display = "flex";

  var main = overlay.querySelector("main");
  main.innerHTML = "";

  if (_textHistory.length === 0) {
    var empty = document.createElement("div");
    empty.className = "backlog-empty";
    empty.textContent = "Історія порожня";
    main.appendChild(empty);
    return;
  }

  var list = document.createElement("div");
  list.className = "backlog-list";

  for (var i = 0; i < _textHistory.length; i++) {
    var entry = _textHistory[i];
    var row = document.createElement("div");
    row.className = "backlog-entry backlog-" + entry.type;

    if (entry.name) {
      var nameEl = document.createElement("span");
      nameEl.className = "backlog-name";
      nameEl.textContent = entry.name;
      row.appendChild(nameEl);
    }

    var textEl = document.createElement("span");
    textEl.className = "backlog-text";
    textEl.textContent = entry.text;
    row.appendChild(textEl);

    list.appendChild(row);
  }

  main.appendChild(list);
  // Скролити до кінця (найновіші внизу)
  setTimeout(function() { main.scrollTop = main.scrollHeight; }, 0);
}

function hideBacklog() {
  var overlay = document.getElementById("overlay-backlog");
  if (overlay) overlay.style.display = "none";
}
