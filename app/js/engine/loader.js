// ═══════════════════════════════════════════════════
// ЗАВАНТАЖУВАЧ ДАНИХ
// ═══════════════════════════════════════════════════
//
// Читає CSV файли і реєструє дані в рушії.
// CSV → масив об'єктів → реєстрація.

// Розібрати CSV текст в масив об'єктів
function parseCSV(text) {
  var lines = text.trim().split("\n");
  var headers = lines[0].split(",");
  var result = [];
  for (var i = 1; i < lines.length; i++) {
    var values = lines[i].split(",");
    var obj = {};
    for (var j = 0; j < headers.length; j++) {
      var val = values[j] || "";
      // Числа → числа
      if (val === "0" || val === "1") val = parseInt(val);
      obj[headers[j]] = val;
    }
    result.push(obj);
  }
  return result;
}

// Завантажити CSV файл
function loadCSV(url, callback) {
  var xhr = new XMLHttpRequest();
  xhr.open("GET", url, true);
  xhr.onload = function() {
    if (xhr.status === 200) {
      callback(parseCSV(xhr.responseText));
    }
  };
  xhr.send();
}

// Завантажити персонажів з CSV і зареєструвати
function loadCharacters(callback) {
  loadCSV("data/characters.csv", function(rows) {
    for (var i = 0; i < rows.length; i++) {
      var r = rows[i];
      c(r.short, r.name, r.full, r.missions, r.chemistry, r.telepathy);
      if (CAST[r.short]) {
        CAST[r.short].sprite = r.sprite || null;
        CAST[r.short].home = r.home || "mall";
      }
    }
    if (callback) callback();
  });
}
