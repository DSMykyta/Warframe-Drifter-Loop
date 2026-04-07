// ═══════════════════════════════════════════════════
// ФЛАГИ
// ═══════════════════════════════════════════════════
//
// Центральна система флагів.
// setFlag → зберігає значення + день → оновлює UI.
// Будь-який UI елемент сам перевіряє свої флаги при refreshUI().

registerState("flags", {
  data: {},
});

function setFlag(name, value) {
  if (value === undefined) value = true;
  gameState.flags.data[name] = value;
  gameState.flags.data[name + "_day"] = gameState.time.day;
  _refreshUI();
}

function getFlag(name) {
  return gameState.flags.data[name] || false;
}

function clearFlag(name) {
  gameState.flags.data[name] = false;
  _refreshUI();
}

// Оновити весь UI після зміни флагу.
// Кожен елемент сам перевіряє свої флаги (has_pager, has_map, тощо).
function _refreshUI() {
  if (typeof showPager === "function") showPager();
  if (typeof updatePagerScreen === "function") updatePagerScreen();
  if (typeof _showMapButton === "function" && getFlag("has_map")) _showMapButton();
  if (typeof updateHUD === "function") updateHUD();
}
