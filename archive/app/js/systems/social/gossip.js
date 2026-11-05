// ═══════════════════════════════════════════════════
// СИСТЕМА ПЛІТОК
// ═══════════════════════════════════════════════════
//
// Порт з dispatcher.rpy (секція GOSSIP)
//
// Плітки поширюються через GOSSIP_ROUTES:
//   ao ↔ lt, ar ↔ el, qu ↔ am
//
// Плітка створюється → чекає spread_delay днів → розповсюджується.
// gossip_heat >= 10 — тригерить awareness (NPC помічають).

// Маршрути пліток: генеруються автоматично з CAST.gossip_to
var GOSSIP_ROUTES = {};

function _buildGossipRoutes() {
  GOSSIP_ROUTES = {};
  for (var id in CAST) {
    if (CAST[id].gossip_to) {
      GOSSIP_ROUTES[id] = [CAST[id].gossip_to];
    }
  }
}


registerState("gossip", {
  active: [],   // [{fact, knowers, day_created, spread_delay}, ...]
  heat: 0       // при >= 10 тригерить awareness
});


// Створює нову плітку.
// fact = ідентифікатор (рядок), initial_knowers = масив імен, spread_delay = днів до поширення
function addGossip(fact, initialKnowers, spreadDelay) {
  if (spreadDelay === undefined) spreadDelay = 2;

  gameState.gossip.active.push({
    fact: fact,
    knowers: initialKnowers.slice(),  // копія
    day_created: gameState.time.day,
    spread_delay: spreadDelay
  });
}


// Поширює плітки через GOSSIP_ROUTES. Викликається в nextDay().
function spreadGossip() {
  var gossipList = gameState.gossip.active;

  for (var i = 0; i < gossipList.length; i++) {
    var g = gossipList[i];

    // Чекати spread_delay днів
    if (gameState.time.day - g.day_created < (g.spread_delay || 2)) continue;

    var newKnowers = [];
    for (var k = 0; k < g.knowers.length; k++) {
      var knower = g.knowers[k];
      var targets = GOSSIP_ROUTES[knower] || [];

      for (var t = 0; t < targets.length; t++) {
        var target = targets[t];
        if (g.knowers.indexOf(target) < 0 && newKnowers.indexOf(target) < 0) {
          newKnowers.push(target);
          // Встановити флаг: gossip_{fact}_known_by_{char_id}
          setFlag("gossip_" + g.fact + "_known_by_" + charFlag(target));
          gameState.gossip.heat += 2;
        }
      }
    }

    // Додати нових knowers
    for (var n = 0; n < newKnowers.length; n++) {
      g.knowers.push(newKnowers[n]);
    }
  }
}
