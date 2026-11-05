// ═══════════════════════════════════════════════════
// ЧАС І ДЕНЬ
// ═══════════════════════════════════════════════════

registerState("time", {
  day: 1,
  minutes: 480,   // 08:00
});

function advanceTime(mins) {
  gameState.time.minutes += mins;
  if (typeof updateHUD === "function") updateHUD();
}

function getHour() {
  return Math.floor(gameState.time.minutes / 60);
}

function getTimeString() {
  var h = Math.floor(gameState.time.minutes / 60);
  var m = gameState.time.minutes % 60;
  return String(h).padStart(2, "0") + ":" + String(m).padStart(2, "0");
}

function getDayString() {
  return gameState.time.day + " грудня";
}

function isNight() {
  // Ніч = після 24:00 (1440 хв). Але після nextDay minutes скидаються до 480-720.
  // Тому перевіряємо тільки поточний день: >= 22:00 (1320) = пізній вечір
  return gameState.time.minutes >= 1380;
}
