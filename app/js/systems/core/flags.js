// ═══════════════════════════════════════════════════
// ФЛАГИ
// ═══════════════════════════════════════════════════

registerState("flags", {
  data: {},
});

function setFlag(name, value) {
  if (value === undefined) value = true;
  gameState.flags.data[name] = value;
  gameState.flags.data[name + "_day"] = gameState.time.day;
}

function getFlag(name) {
  return gameState.flags.data[name] || false;
}

function clearFlag(name) {
  gameState.flags.data[name] = false;
}
