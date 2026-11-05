// ═══════════════════════════════════════════════════
// РАНГ СИНДИКАТУ (ГЕКСУ)
// ═══════════════════════════════════════════════════
//
// Порт з vars.rpy: RANK_THRESHOLDS, can_rank_up(), try_rank_up()
//
// Ранг 1-6. Кожен наступний ранг вимагає певну кількість hex_rep.
// Репутація здобувається ТІЛЬКИ через місії.

// Пороги репутації для кожного рангу
var RANK_THRESHOLDS = {
  2: 30,
  3: 80,
  4: 150,
  5: 230,
  6: 300
};

registerState("rank", {
  syndicate_rank: 1,   // поточний ранг (1-6)
  hex_rep: 0           // репутація Гексу
});


// Чи можна підвищити ранг?
function canRankUp() {
  var next = gameState.rank.syndicate_rank + 1;
  if (next > 6) return false;
  var threshold = RANK_THRESHOLDS[next];
  if (threshold === undefined) return false;
  return gameState.rank.hex_rep >= threshold;
}


// Підвищити ранг якщо можливо. Повертає true якщо підвищив.
function tryRankUp() {
  if (!canRankUp()) return false;
  gameState.rank.syndicate_rank++;
  setFlag("rank_" + gameState.rank.syndicate_rank);
  // Ранг 3 — відкрити бар
  if (gameState.rank.syndicate_rank >= 3) {
    setFlag("syndicate_rank_3");
  }
  addJournalEntry(
    "Ранг Гексу підвищено до " + gameState.rank.syndicate_rank + ".",
    "event"
  );
  // Нові діалоги можуть стати доступними — перебудувати колоду
  buildDailyDeck();
  return true;
}


// Додати репутацію Гексу
function addHexRep(amount) {
  gameState.rank.hex_rep += amount;
}
