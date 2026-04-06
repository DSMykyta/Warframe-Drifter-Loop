// ═══════════════════════════════════════════════════
// СИСТЕМА ПЛІТОК
// ═══════════════════════════════════════════════════
//
// Порт з dispatcher.rpy (секція GOSSIP)
//
// Плітки поширюються через GOSSIP_ROUTES:
//   Аоі ↔ Летті, Артур ↔ Елеонор, Квінсі ↔ Амір
//
// Плітка створюється → чекає spread_delay днів → розповсюджується.
// gossip_heat >= 10 — тригерить awareness (NPC помічають).

// Маршрути пліток: хто кому розповідає
var GOSSIP_ROUTES = {
  "\u0410\u043e\u0456":     ["\u041b\u0435\u0442\u0442\u0456"],            // Аоі -> Летті
  "\u041b\u0435\u0442\u0442\u0456":   ["\u0410\u043e\u0456"],              // Летті -> Аоі
  "\u0410\u0440\u0442\u0443\u0440":   ["\u0415\u043b\u0435\u043e\u043d\u043e\u0440"],    // Артур -> Елеонор
  "\u0415\u043b\u0435\u043e\u043d\u043e\u0440": ["\u0410\u0440\u0442\u0443\u0440"],      // Елеонор -> Артур
  "\u041a\u0432\u0456\u043d\u0441\u0456":  ["\u0410\u043c\u0456\u0440"],          // Квінсі -> Амір
  "\u0410\u043c\u0456\u0440":    ["\u041a\u0432\u0456\u043d\u0441\u0456"]         // Амір -> Квінсі
};


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
