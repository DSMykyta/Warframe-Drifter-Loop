// ═══════════════════════════════════════════════════
// СИСТЕМА ОБІЦЯНОК
// ═══════════════════════════════════════════════════
//
// Порт з promises.rpy
//
// Обіцянка = зустріч з NPC в конкретному місці і часі.
// Виконана = +5 хімії. Порушена = -5 хімії + флаг.
// Під час emergency skip обіцянки не штрафуються.

registerState("promises", {
  list: []   // [{who, where, from_min, to_min, day, label, fulfilled}, ...]
});


// Створює нову обіцянку
function createPromise(who, where, fromMin, toMin, day, label) {
  gameState.promises.list.push({
    who: who,
    where: where,
    from_min: fromMin,
    to_min: toMin,
    day: day,
    label: label,
    fulfilled: false
  });
}


// Перевіряє порушені обіцянки. Викликається в nextDay().
function checkBrokenPromises() {
  var promises = gameState.promises.list;

  for (var i = 0; i < promises.length; i++) {
    var p = promises[i];
    if (p.day < gameState.time.day && !p.fulfilled) {
      // Порушена обіцянка — штраф
      addChemistry(p.who, -5);
      setFlag("broke_promise_" + charFlag(p.who));
    }
  }

  // Видалити старі обіцянки (день вже минув)
  var remaining = [];
  for (var j = 0; j < promises.length; j++) {
    if (promises[j].day >= gameState.time.day) {
      remaining.push(promises[j]);
    }
  }
  gameState.promises.list = remaining;
}


// Позначає обіцянку як виконану. +5 хімії.
function fulfillPromise(who) {
  var promises = gameState.promises.list;
  for (var i = 0; i < promises.length; i++) {
    var p = promises[i];
    if (p.who === who && p.day === gameState.time.day && !p.fulfilled) {
      p.fulfilled = true;
      addChemistry(who, 5);
      return true;
    }
  }
  return false;
}


// Перевіряє чи є у персонажа обіцянка що перетинається з часом
function hasActivePromise(name, timeFrom, timeTo) {
  var promises = gameState.promises.list;
  for (var i = 0; i < promises.length; i++) {
    var p = promises[i];
    if (p.who === name && p.day === gameState.time.day) {
      if (p.from_min < timeTo && p.to_min > timeFrom) {
        return true;
      }
    }
  }
  return false;
}


// Перевіряє чи є будь-яка обіцянка що конфліктує з часом
function hasConflict(timeMin) {
  var promises = gameState.promises.list;
  for (var i = 0; i < promises.length; i++) {
    var p = promises[i];
    if (p.day === gameState.time.day) {
      if (p.from_min <= timeMin && timeMin < p.to_min) {
        return true;
      }
    }
  }
  return false;
}


// Повертає список активних обіцянок на сьогодні
function getActivePromises() {
  var result = [];
  var promises = gameState.promises.list;
  for (var i = 0; i < promises.length; i++) {
    if (promises[i].day === gameState.time.day && !promises[i].fulfilled) {
      result.push(promises[i]);
    }
  }
  return result;
}


// Перевіряє чи є обіцянка за 30 хвилин (попередження)
function promiseWarning() {
  var promises = gameState.promises.list;
  for (var i = 0; i < promises.length; i++) {
    var p = promises[i];
    if (p.day === gameState.time.day && !p.fulfilled) {
      var diff = p.from_min - gameState.time.minutes;
      if (diff >= 0 && diff <= 30) {
        return p;
      }
    }
  }
  return null;
}
