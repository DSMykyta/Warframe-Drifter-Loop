// ═══════════════════════════════════════════════════
// ЧАС І ДЕНЬ
// ═══════════════════════════════════════════════════

registerState("time", {
  day: 1,
  minutes: 480,   // 08:00
});

function advanceTime(mins) {
  gameState.time.minutes += mins;
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
  return gameState.time.minutes >= 1440;
}
