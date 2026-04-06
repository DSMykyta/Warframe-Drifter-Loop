// ═══════════════════════════════════════════════════
// ПЕРЕКЛЮЧЕННЯ ЕКРАНІВ
// ═══════════════════════════════════════════════════
//
// Всі екрани: main-menu, load-screen, settings-screen, gallery-screen, game-screen
// При переході — заголовок друкується по буквах
// При виході — стирається по буквах, потім перехід

var ALL_SCREENS = ["main-menu", "load-screen", "settings-screen", "gallery-screen", "game-screen"];

// Показати екран (миттєво)
function showScreen(id) {
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
  var h1 = document.querySelector("#" + fromId + " > header > h1");
  if (h1 && h1.getAttribute("data-word")) {
    titleTypeOut(h1, function() {
      showScreen(toId);
    });
  } else {
    showScreen(toId);
  }
}
