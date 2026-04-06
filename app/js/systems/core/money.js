// ═══════════════════════════════════════════════════
// ГРОШІ
// ═══════════════════════════════════════════════════

registerState("money", {
  amount: 0,
});

function addMoney(amount) {
  gameState.money.amount += amount;
}

function spendMoney(amount) {
  if (gameState.money.amount < amount) return false;
  gameState.money.amount -= amount;
  return true;
}
