// ═══════════════════════════════════════════════════
// ХІМІЯ (ВІДНОСИНИ)
// ═══════════════════════════════════════════════════
//
// Імена беруться з characters.js автоматично.
// Не треба нічого прописувати тут.

var DAILY_CHEMISTRY_CAP = 15;

registerState("chemistry", { values: {}, gainedToday: {} });

function addChemistry(name, amount) {
  if (CAST[name]) name = CAST[name].name;
  if (amount <= 0) {
    gameState.chemistry.values[name] = Math.max(0, (gameState.chemistry.values[name] || 0) + amount);
    return amount;
  }
  var old = gameState.chemistry.values[name] || 0;
  var gained = gameState.chemistry.gainedToday[name] || 0;
  var remaining = Math.max(0, DAILY_CHEMISTRY_CAP - gained);
  var actual = Math.min(amount, remaining);
  if (actual <= 0) return 0;
  gameState.chemistry.values[name] = old + actual;
  gameState.chemistry.gainedToday[name] = gained + actual;
  return actual;
}

function getChemRank(name) {
  var pts = gameState.chemistry.values[name] || 0;
  if (pts >= 160) return "Кохання";
  if (pts >= 120) return "Друзі";
  if (pts >= 90)  return "Близько";
  if (pts >= 60)  return "Довіра";
  if (pts >= 35)  return "Подобається";
  if (pts >= 15)  return "Привітно";
  return "Нейтрально";
}
