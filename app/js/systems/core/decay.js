// ═══════════════════════════════════════════════════
// РОЗПАД СТОСУНКІВ (DECAY)
// ═══════════════════════════════════════════════════
//
// Порт з dispatcher.rpy: apply_decay(), reset_interaction(), check_mission_neglect()
//
// Якщо гравець не спілкується з NPC — хімія поступово зменшується.
// Баланс v2: decay починається з дня 7, grace period 2 дні.
//
// Також — штраф за ігнорування місій (days_without_mission).

registerState("decay", {
  days_since_interaction: {},   // {"Артур": 5, ...} — днів без контакту
  paused_until: 0               // день до якого decay на паузі
});


// Зменшує хімію якщо давно не взаємодіяв.
// Викликається в nextDay().
function applyDecay() {
  if (gameState.time.day <= gameState.decay.paused_until) return;

  var names = Object.keys(CAST);
  for (var i = 0; i < names.length; i++) {
    var name = names[i];
    var d = gameState.decay.days_since_interaction[name] || 0;

    if (d >= 14) {
      addChemistry(name, -3);
    } else if (d >= 10) {
      addChemistry(name, -2);
    } else if (d >= 7) {
      addChemistry(name, -1);
    }

    // Інкремент лічильника
    gameState.decay.days_since_interaction[name] = d + 1;
  }
}


// Скидає лічильник днів без взаємодії.
// Викликати коли гравець поговорив, дав каву, подарунок тощо.
function resetInteraction(name) {
  gameState.decay.days_since_interaction[name] = 0;
}


// Перевіряє чи гравець ігнорує місії.
// Баланс v2: одноразові штрафи з ресетом лічильника.
function checkMissionNeglect() {
  var d = gameState.missions.days_without_mission;

  if (d >= 6) {
    // Критичний ігнор — штраф всім NPC
    var names = Object.keys(CAST);
    for (var i = 0; i < names.length; i++) {
      addChemistry(names[i], -3);
    }
    setFlag("mission_neglect_critical");
    gameState.missions.days_without_mission = 0;  // Ресет — новий цикл
  } else if (d === 5) {
    // Попередження — м'якший штраф
    var names2 = Object.keys(CAST);
    for (var j = 0; j < names2.length; j++) {
      addChemistry(names2[j], -2);
    }
    setFlag("mission_neglect_warning");
  }
}


// Після кожної успішної місії — скинути лічильник
function onMissionComplete() {
  gameState.missions.days_without_mission = 0;
}
