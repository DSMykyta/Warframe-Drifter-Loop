// ═══════════════════════════════════════════════════
// ГАЛЕРЕЯ — CG ТРЕКІНГ
// ═══════════════════════════════════════════════════
//
// Порт з persistent.cg_unlocked
// Використовує persistent.js для збереження між петлями.

// Каталог CG (додавати нові тут)
var CG_CATALOG = [
  // {id: "cg_finale_victory", name: "Перемога", category: "cg", thumb: "assets/cg/finale_victory_thumb.png", full: "assets/cg/finale_victory.png"},
  // {id: "cg_coffee_machine", name: "Кавомашина", category: "cg", thumb: "assets/cg/coffee_machine_thumb.png", full: "assets/cg/coffee_machine.png"},
];

// Каталог персонажів (автоматично з CAST)
function _buildCharacterGallery() {
  var result = [];
  for (var short in CAST) {
    var ch = CAST[short];
    result.push({
      id: "char_" + short,
      name: ch.name,
      category: "characters",
      thumb: "assets/sprites/" + (ch.sprite || short) + "/knee-test.png"
    });
  }
  return result;
}

// Рендер галереї
function renderGallery() {
  var grid = document.getElementById("gallery-grid");
  if (!grid) return;

  var tabs = document.querySelectorAll(".gallery-tab");
  var activeTab = "cg";
  for (var t = 0; t < tabs.length; t++) {
    if (tabs[t].classList.contains("active")) {
      activeTab = tabs[t].textContent.toLowerCase();
      break;
    }
  }

  grid.innerHTML = "";

  if (activeTab === "cg") {
    if (CG_CATALOG.length === 0) {
      grid.innerHTML = '<div style="color:#ffffff40;padding:40px;text-align:center;">CG будуть додані пізніше.</div>';
      return;
    }
    for (var i = 0; i < CG_CATALOG.length; i++) {
      var cg = CG_CATALOG[i];
      var unlocked = (typeof isCGUnlocked === "function") && isCGUnlocked(cg.id);
      var div = document.createElement("div");
      div.className = "gallery-item" + (unlocked ? "" : " locked");
      if (unlocked && cg.thumb) {
        div.style.backgroundImage = "url('" + cg.thumb + "')";
        div.style.backgroundSize = "cover";
      }
      div.innerHTML = '<div class="gallery-item-name">' + (unlocked ? cg.name : "???") + '</div>';
      grid.appendChild(div);
    }
  } else if (activeTab.indexOf("персонаж") >= 0) {
    var chars = _buildCharacterGallery();
    for (var c = 0; c < chars.length; c++) {
      var ch = chars[c];
      var cdiv = document.createElement("div");
      cdiv.className = "gallery-item";
      cdiv.style.backgroundImage = "url('" + ch.thumb + "')";
      cdiv.style.backgroundSize = "cover";
      cdiv.innerHTML = '<div class="gallery-item-name">' + ch.name + '</div>';
      grid.appendChild(cdiv);
    }
  } else {
    grid.innerHTML = '<div style="color:#ffffff40;padding:40px;text-align:center;">Локації будуть додані пізніше.</div>';
  }
}

// Підключити таби галереї
document.addEventListener("DOMContentLoaded", function() {
  var tabs = document.querySelectorAll(".gallery-tab");
  for (var i = 0; i < tabs.length; i++) {
    tabs[i].addEventListener("click", function() {
      var allTabs = document.querySelectorAll(".gallery-tab");
      for (var j = 0; j < allTabs.length; j++) allTabs[j].classList.remove("active");
      this.classList.add("active");
      renderGallery();
    });
  }
});
