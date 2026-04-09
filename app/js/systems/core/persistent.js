// ═══════════════════════════════════════════════════
// PERSISTENT — КРОС-ПЕТЛЕВА ПЕРСИСТЕНЦІЯ
// ═══════════════════════════════════════════════════
//
// Порт з vars.rpy: persistent.* — дані що зберігаються між петлями (NG+).
// Використовує окремий ключ в localStorage, НЕ залежить від gameState.
//
// persistent.loop_count      — скільки разів гравець пройшов гру
// persistent.completed       — чи була хоч одна перемога
// persistent.all_friends     — чи були всі 6 друзями
// persistent.cg_unlocked     — набір відкритих CG
// persistent.insights_log    — факти з попередніх петель
// persistent.previous_journal — щоденник попередньої петлі
// persistent.romanced_*      — хто був романтичним партнером

var PERSISTENT_KEY = "drifter_persistent";

var persistent = {
  loop_count: 0,
  completed: false,
  all_friends: false,
  cg_unlocked: [],
  endings_seen: [],      // ["victory_all_friends", "victory_partial", "defeat"]
  insights_log: [],
  previous_journal: [],
  romanced: {}           // {"Артур": true, "Аоі": true, ...}
};


// Завантажити persistent з localStorage
function loadPersistent() {
  var raw = localStorage.getItem(PERSISTENT_KEY);
  if (!raw) return;
  try {
    var data = JSON.parse(raw);
    for (var key in data) {
      if (key in persistent) {
        persistent[key] = data[key];
      }
    }
  } catch (e) {
    // corrupted — ignore
  }
}


// Зберегти persistent в localStorage
function savePersistent() {
  localStorage.setItem(PERSISTENT_KEY, JSON.stringify(persistent));
}


// Перевірити чи це NG+
function isNgPlus() {
  return persistent.completed === true;
}


// Перевірити чи це рестарт петлі
function isLoopRestart() {
  return persistent.loop_count > 0;
}


// Скільки петель пройдено
function getLoopCount() {
  return persistent.loop_count;
}


// Чи був роман з NPC в попередній петлі
function wasRomanced(name) {
  return persistent.romanced[name] === true;
}


// Зберегти insights з попередньої петлі
function getPreviousInsights() {
  return persistent.insights_log || [];
}


// Зберегти journal з попередньої петлі
function getPreviousJournal() {
  return persistent.previous_journal || [];
}


// Викликається при завершенні петлі (перемога або поразка)
function onLoopEnd(victory) {
  // Зберегти journal
  persistent.previous_journal = (gameState.insights && gameState.insights.journal)
    ? JSON.parse(JSON.stringify(gameState.insights.journal))
    : [];

  // Зберегти insights
  persistent.insights_log = (gameState.insights && gameState.insights.log)
    ? JSON.parse(JSON.stringify(gameState.insights.log))
    : [];

  // Зберегти роман
  if (gameState.romance && gameState.romance.dating) {
    persistent.romanced[gameState.romance.dating] = true;
  }

  if (victory) {
    persistent.completed = true;
    // Перевірити all_friends
    var allFriends = true;
    for (var name in gameState.chemistry.values) {
      if (gameState.chemistry.values[name] < 120) {
        allFriends = false;
        break;
      }
    }
    persistent.all_friends = allFriends;

    // Трекер закінчень
    var endingId = allFriends ? "victory_all_friends" : "victory_partial";
    if (persistent.endings_seen.indexOf(endingId) < 0) {
      persistent.endings_seen.push(endingId);
    }
  } else {
    if (persistent.endings_seen.indexOf("defeat") < 0) {
      persistent.endings_seen.push("defeat");
    }
  }

  persistent.loop_count++;
  savePersistent();
}


// Розблокувати CG
function unlockCG(cgId) {
  if (persistent.cg_unlocked.indexOf(cgId) < 0) {
    persistent.cg_unlocked.push(cgId);
    savePersistent();
  }
}


// Перевірити чи CG розблоковано
function isCGUnlocked(cgId) {
  return persistent.cg_unlocked.indexOf(cgId) >= 0;
}


// Завантажити при старті
loadPersistent();
