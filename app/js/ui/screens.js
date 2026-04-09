// ═══════════════════════════════════════════════════
// ПЕРЕКЛЮЧЕННЯ ЕКРАНІВ
// ═══════════════════════════════════════════════════
//
// Всі екрани: main-menu, load-screen, settings-screen, gallery-screen, game-screen
// При переході — заголовок друкується по буквах
// При виході — стирається по буквах, потім перехід

var ALL_SCREENS = ["main-menu", "load-screen", "settings-screen", "gallery-screen", "game-screen", "quest-tree-screen"];
var _previousScreen = null; // Трекінг попереднього екрану для правильного "НАЗАД"

// Показати екран (миттєво)
function showScreen(id) {
  // Запам'ятати поточний активний екран перед переключенням
  for (var i = 0; i < ALL_SCREENS.length; i++) {
    var el = document.querySelector("#" + ALL_SCREENS[i]);
    if (el && el.style.display !== "none") {
      _previousScreen = ALL_SCREENS[i];
      break;
    }
  }

  ALL_SCREENS.forEach(function(s) {
    document.querySelector("#" + s).style.display = "none";
  });
  document.querySelector("#" + id).style.display = "flex";

  // Друкувати заголовок (тільки прямий h1 екрану, не оверлеїв)
  var h1 = document.querySelector("#" + id + " > header > h1");
  if (h1) titleTypeIn(h1);
}

// Вийти з екрану (стерти заголовок, потім перейти)
function goBack(fromId, toId) {
  // Якщо toId — main-menu, але ми прийшли з гри — повернутись до гри
  if (toId === "main-menu" && _previousScreen === "game-screen") {
    toId = "game-screen";
  }

  var h1 = document.querySelector("#" + fromId + " > header > h1");
  if (h1 && h1.getAttribute("data-word")) {
    titleTypeOut(h1, function() {
      showScreen(toId);
    });
  } else {
    showScreen(toId);
  }
}
