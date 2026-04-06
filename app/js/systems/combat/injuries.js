// ═══════════════════════════════════════════════════
// СИСТЕМА ТРАВМ v2
// ═══════════════════════════════════════════════════
//
// Порт з injuries.rpy
//
// Стак 0 — здоровий
// Стак 1 — легка травма. Може на місію. +5% шанс.
// Стак 2 — серйозна. Може на місію (гра попереджає). +10% шанс.
// Стак 3 — критичний. Тільки через місію.
//   NPC: переміщується в recovery_room, відсутній 2 дні.
//   Дріфтер: непритомний, emergency_skip 2 дні.
//
// Летті на місії = 0% шанс + знімає ВСІ стаки з усіх учасників.

// Базовий шанс травми за рівнем місії (%)
var INJURY_CHANCE = {
  1: 3,
  2: 5,
  3: 8,
  4: 12,
  5: 18,
  6: 25
};


registerState("injuries", {
  stacks: {},            // {"Артур": 2, "player": 1, ...}
  day_gained: {},        // {"Артур": [3, 5], ...} — дні коли отримав стаки
  recovery_until: {}     // {"Амір": 14} — день до якого NPC в палаті
});


// ═══ ЧИТАННЯ СТАКІВ ═══

function getInjuryStacks(name) {
  return gameState.injuries.stacks[name] || 0;
}

function isNpcInjured(name) {
  return getInjuryStacks(name) > 0;
}

function isPlayerInjured() {
  return getInjuryStacks("player") > 0;
}

function getInjuryText(target) {
  var stacks = getInjuryStacks(target);
  if (stacks === 0) return null;
  if (stacks === 1) return "\u041b\u0435\u0433\u043a\u0430 \u0442\u0440\u0430\u0432\u043c\u0430";       // Легка травма
  if (stacks === 2) return "\u0421\u0435\u0440\u0439\u043e\u0437\u043d\u0430 \u0442\u0440\u0430\u0432\u043c\u0430";  // Серйозна травма
  return "\u041a\u0440\u0438\u0442\u0438\u0447\u043d\u0430 \u0442\u0440\u0430\u0432\u043c\u0430";        // Критична травма
}


// ═══ ДОДАВАННЯ / ЗНЯТТЯ СТАКІВ ═══

// Додає один стак травми. Повертає нове значення.
function addInjuryStack(name) {
  var current = gameState.injuries.stacks[name] || 0;
  var newVal = Math.min(3, current + 1);
  gameState.injuries.stacks[name] = newVal;

  // Записати день отримання
  if (!gameState.injuries.day_gained[name]) {
    gameState.injuries.day_gained[name] = [];
  }
  gameState.injuries.day_gained[name].push(gameState.time.day);

  // Флаги для NPC
  if (name !== "player") {
    var charKey = charFlag(name);
    setFlag(charKey + "_injured");
    if (newVal >= 2) {
      setFlag(charKey + "_injured_severe");
    }
    if (newVal >= 3) {
      // NPC в палату на 2 дні
      gameState.injuries.recovery_until[name] = gameState.time.day + 2;
      setFlag(charKey + "_in_recovery");
    }
  } else {
    setFlag("player_injured");
    if (newVal >= 2) {
      setFlag("player_injured_severe");
    }
  }

  return newVal;
}


// Знімає один стак травми
function removeInjuryStack(name) {
  var current = gameState.injuries.stacks[name] || 0;
  if (current <= 0) return;

  var newVal = current - 1;
  gameState.injuries.stacks[name] = newVal;

  // Видалити найстаріший запис дня
  if (gameState.injuries.day_gained[name] && gameState.injuries.day_gained[name].length > 0) {
    gameState.injuries.day_gained[name].shift();
  }

  // Оновити флаги
  if (name !== "player") {
    var charKey = charFlag(name);
    if (newVal === 0) {
      clearFlag(charKey + "_injured");
    }
    if (newVal < 2) {
      clearFlag(charKey + "_injured_severe");
    }
  } else {
    if (newVal === 0) {
      clearFlag("player_injured");
    }
    if (newVal < 2) {
      clearFlag("player_injured_severe");
    }
  }
}


// Знімає ВСІ стаки. Використовується Летті на місії.
function removeAllStacks(name) {
  while (getInjuryStacks(name) > 0) {
    removeInjuryStack(name);
  }
}


// ═══ ПАЛАТА (recovery_room) ═══

// NPC в палаті (3 стаки, без свідомості)
function isNpcInRecovery(name) {
  var until = gameState.injuries.recovery_until[name] || 0;
  return gameState.time.day < until;
}

// NPC відсутній = в палаті
function isNpcAbsent(name) {
  return isNpcInRecovery(name);
}


// ═══ КИДОК НА ТРАВМУ ═══

// Кидає на травму для кожного учасника окремо.
// Летті = 0% + лікує всіх.
// Повертає dict {"player": true/false, ...} або null.
function rollMissionInjury(missionLevel, partnerName, partner2Name) {
  var participants = ["player"];
  if (partnerName) participants.push(partnerName);
  if (partner2Name) participants.push(partner2Name);

  // Летті на місії — повна імунність + лікування
  var lettiePresent = participants.indexOf("\u041b\u0435\u0442\u0442\u0456") >= 0; // Летті
  if (lettiePresent) {
    for (var lp = 0; lp < participants.length; lp++) {
      if (getInjuryStacks(participants[lp]) > 0) {
        removeAllStacks(participants[lp]);
      }
    }
    return null;
  }

  var baseChance = INJURY_CHANCE[missionLevel] || 10;
  var result = {};
  var anyHit = false;

  for (var i = 0; i < participants.length; i++) {
    var p = participants[i];

    // Індивідуальний шанс
    var stacks = getInjuryStacks(p);
    var stackBonus = stacks * 5;

    // Повторні місії з тим же NPC сьогодні
    var repeatBonus = 0;
    if (p !== "player" && gameState.missions.missions_today_with[p]) {
      var repeats = gameState.missions.missions_today_with[p];
      repeatBonus = Math.max(0, (repeats - 1)) * 5;
    }

    var chance = baseChance + stackBonus + repeatBonus;

    if ((Math.floor(Math.random() * 100) + 1) <= chance) {
      result[p] = true;
      anyHit = true;
    } else {
      result[p] = false;
    }
  }

  if (!anyHit) return null;
  return result;
}


// ═══ ЗАСТОСУВАННЯ ТРАВМ ═══

// Застосовує травми. Повертає {messages: [...], outcome: "normal"/"partner_evac"/"player_evac"/"both_evac"}
function applyMissionInjuries(result, partnerName, partner2Name) {
  var messages = [];
  var playerDown = false;
  var anyPartnerDown = false;

  // Гравець
  if (result["player"]) {
    var pStacks = addInjuryStack("player");
    if (pStacks >= 3) {
      playerDown = true;
      messages.push("\u0422\u0438 \u0432\u043f\u0430\u0432. \u0422\u0435\u043c\u0440\u044f\u0432\u0430."); // Ти впав. Темрява.
    } else {
      messages.push("\u0422\u0438 \u043e\u0442\u0440\u0438\u043c\u0430\u0432 \u0442\u0440\u0430\u0432\u043c\u0443. (\u0421\u0442\u0430\u043a\u0456\u0432: " + pStacks + "/3)"); // Ти отримав травму.
      addJournalEntry("\u0422\u0440\u0430\u0432\u043c\u0430 \u043d\u0430 \u043c\u0456\u0441\u0456\u0457. \u0421\u0442\u0430\u043a\u0456\u0432: " + pStacks + "/3.", "event");
    }
  }

  // Напарники
  var partners = [partnerName, partner2Name];
  for (var i = 0; i < partners.length; i++) {
    var pName = partners[i];
    if (!pName) continue;
    if (!result[pName]) continue;

    var nStacks = addInjuryStack(pName);
    if (nStacks >= 3) {
      anyPartnerDown = true;
      messages.push(pName + " \u0431\u0435\u0437 \u0441\u0432\u0456\u0434\u043e\u043c\u043e\u0441\u0442\u0456. \u041a\u0440\u0438\u0442\u0438\u0447\u043d\u0438\u0439 \u0441\u0442\u0430\u043d."); // без свідомості. Критичний стан.
      addJournalEntry(pName + " \u043a\u0440\u0438\u0442\u0438\u0447\u043d\u043e \u043f\u043e\u0440\u0430\u043d\u0435\u043d\u0438\u0439 \u043d\u0430 \u043c\u0456\u0441\u0456\u0457.", "event");
    } else {
      messages.push(pName + " \u043e\u0442\u0440\u0438\u043c\u0430\u0432 \u0442\u0440\u0430\u0432\u043c\u0443. (\u0421\u0442\u0430\u043a\u0456\u0432: " + nStacks + "/3)");
    }
  }

  // Визначити outcome
  var outcome = "normal";
  if (playerDown && anyPartnerDown) {
    outcome = "both_evac";
  } else if (playerDown) {
    outcome = "player_evac";
  } else if (anyPartnerDown) {
    outcome = "partner_evac";
  }

  return {messages: messages, outcome: outcome};
}


// ═══ EMERGENCY SKIP ═══

// Дріфтер непритомний. Скіп N днів.
// Обіцянки не штрафуються. NPC які мали обіцянки — прийдуть потім.
function emergencySkip(days) {
  setFlag("emergency_skip_active");

  // Зберегти хто мав обіцянки — вони прийдуть після
  gameState.injuries._emergency_visitors = [];
  var promises = gameState.promises.list;
  for (var i = 0; i < promises.length; i++) {
    var p = promises[i];
    if (p.day >= gameState.time.day && p.day < gameState.time.day + days) {
      if (gameState.injuries._emergency_visitors.indexOf(p.who) < 0) {
        gameState.injuries._emergency_visitors.push(p.who);
      }
    }
  }

  // Скіп днів
  for (var d = 0; d < days; d++) {
    nextDay();
  }

  clearFlag("emergency_skip_active");
  gameState.location.current = "medbay";

  // Зняти 1 стак гравця (Летті лікувала поки був непритомний)
  if (getInjuryStacks("player") > 0) {
    removeInjuryStack("player");
  }

  addJournalEntry(
    "\u041f\u0440\u043e\u043a\u0438\u043d\u0443\u0432\u0441\u044f \u0432 \u043c\u0435\u0434\u0432\u0456\u0434\u0434\u0456\u043b\u0456. \u041f\u0440\u043e\u043f\u0443\u0441\u0442\u0438\u0432 " + days + " \u0434\u043d.", // Прокинувся в медвідділі.
    "event"
  );
}


// Повертає масив імен NPC які прийшли поки Дріфтер був непритомний
function getEmergencyVisitors() {
  return gameState.injuries._emergency_visitors || [];
}

function clearEmergencyVisitors() {
  gameState.injuries._emergency_visitors = [];
}


// ═══ ЗАГОЄННЯ (nextDay) ═══

// Знімає стаки що "дозріли" — отримані 2+ дні тому.
// Стак день X -> є день X+1 -> зникає день X+2.
function checkInjuriesHeal() {
  var stacks = gameState.injuries.stacks;
  var names = Object.keys(stacks);

  for (var i = 0; i < names.length; i++) {
    var name = names[i];
    if (stacks[name] <= 0) continue;

    var days = gameState.injuries.day_gained[name] || [];
    var healed = 0;
    var remaining = [];

    for (var d = 0; d < days.length; d++) {
      if (gameState.time.day - days[d] >= 2) {
        healed++;
      } else {
        remaining.push(days[d]);
      }
    }

    gameState.injuries.day_gained[name] = remaining;
    for (var h = 0; h < healed; h++) {
      removeInjuryStack(name);
    }
  }

  // Перевірити recovery — повернути NPC зі стаком 1
  var recovery = gameState.injuries.recovery_until;
  var expired = [];
  for (var rName in recovery) {
    if (gameState.time.day >= recovery[rName]) {
      expired.push(rName);
      var charKey = charFlag(rName);
      clearFlag(charKey + "_in_recovery");
    }
  }
  for (var e = 0; e < expired.length; e++) {
    delete gameState.injuries.recovery_until[expired[e]];
  }
}


// Допоміжна функція — charFlag (латинський ID для флагів)
// Визначена в state.js як глобальна утиліта
function charFlag(name) {
  // Маппінг кирилиця -> латиниця
  var map = {
    "\u0410\u0440\u0442\u0443\u0440": "arthur",       // Артур
    "\u0415\u043b\u0435\u043e\u043d\u043e\u0440": "eleanor",     // Елеонор
    "\u041b\u0435\u0442\u0442\u0456": "lettie",       // Летті
    "\u0410\u043c\u0456\u0440": "amir",         // Амір
    "\u0410\u043e\u0456": "aoi",           // Аоі
    "\u041a\u0432\u0456\u043d\u0441\u0456": "quincy"        // Квінсі
  };
  return map[name] || name.toLowerCase();
}
