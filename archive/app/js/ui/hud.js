// ═══════════════════════════════════════════════════
// HUD — верхня панель
// ═══════════════════════════════════════════════════
//
// Видно під час ходьби по локаціях.
// Ховається під час діалогів.

function showHUD() {
  var hud = document.querySelector(".hud");
  if (hud) hud.style.display = "flex";
  updateHUD();
}

function hideHUD() {
  var hud = document.querySelector(".hud");
  if (hud) hud.style.display = "none";
}

function updateHUD() {
  var loc = document.querySelector(".hud-location");
  var time = document.querySelector(".hud-time");
  var rank = document.querySelector(".hud-rank");
  var money = document.querySelector(".hud-money");

  if (loc) loc.textContent = currentLocationName();
  if (time) time.textContent = "День " + gameState.time.day + " / " + getTimeString();
  if (rank) rank.textContent = "Ранг " + (gameState.rank ? gameState.rank.syndicate_rank : 1);
  if (money) money.textContent = gameState.money.amount + " крон";
}
