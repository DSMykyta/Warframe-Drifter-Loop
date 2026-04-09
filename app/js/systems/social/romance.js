// ═══════════════════════════════════════════════════
// СИСТЕМА РОМАНСУ
// ═══════════════════════════════════════════════════
//
// Порт з romance.rpy
//
// Ексклюзивний романс — тільки з одним персонажем одночасно.
// Зізнання доступне коли chemistry >= 160 і friends_milestone пройдений.
// Розрив — -30 хімії. Флірт з іншим при партнері — наслідки.

registerState("romance", {
  dating: null   // null або ім'я (ексклюзивний романс)
});


// Починає романс з персонажем. Ексклюзивний.
// Потрібна хімія >= 160. Повертає true якщо успішно.
function startDating(name) {
  if (gameState.romance.dating !== null) return false;
  if ((gameState.chemistry.values[name] || 0) < 160) return false;

  gameState.romance.dating = name;
  setFlag("dating_" + charFlag(name));
  addJournalEntry(
    "\u041c\u0438 \u0437 " + charName(name) + " \u0442\u0435\u043f\u0435\u0440 \u0440\u0430\u0437\u043e\u043c. \u0426\u0435... \u043d\u0435\u0441\u043f\u043e\u0434\u0456\u0432\u0430\u043d\u043e. \u0410\u043b\u0435 \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e.",
    // Ми з {name} тепер разом. Це... несподівано. Але правильно.
    "romance"
  );
  return true;
}


// Розрив стосунків. -30 хімії.
function breakUp(name) {
  if (gameState.romance.dating !== name) return false;

  gameState.romance.dating = null;
  setFlag("breakup_" + charFlag(name));
  addChemistry(name, -30);
  addJournalEntry(
    "\u0420\u043e\u0437\u0440\u0438\u0432 \u0437 " + charName(name) + ". \u042f \u043d\u0435 \u0434\u0443\u043c\u0430\u0432 \u0449\u043e \u0431\u0443\u0434\u0435 \u0442\u0430\u043a \u0431\u043e\u043b\u044f\u0447\u0435.",
    // Розрив з {name}. Я не думав що буде так боляче.
    "romance"
  );
  return true;
}


// Перевіряє наслідки флірту з кимось при наявності партнера.
// Повертає: null (нема партнера / фліртуєш з партнером), "caught" або "private"
function checkFlirtConsequences(targetName) {
  if (gameState.romance.dating === null) return null;
  if (gameState.romance.dating === targetName) return null; // Фліртуєш з партнером — ок

  var partner = gameState.romance.dating;

  // Публічний флірт — перевірити чи партнер в локації
  var charsHere = getCharsAt(gameState.location.current);
  if (charsHere) {
    for (var i = 0; i < charsHere.length; i++) {
      if (charsHere[i] === partner) {
        // Партнер бачить — одразу конфлікт
        addChemistry(partner, -5);
        setFlag("flirt_caught_by_" + charFlag(partner));
        return "caught";
      }
    }
  }

  // Приватний — шанс через плітки
  addGossip("flirt_with_" + targetName, [targetName], 1);
  gameState.gossip.heat += 1;
  return "private";
}
