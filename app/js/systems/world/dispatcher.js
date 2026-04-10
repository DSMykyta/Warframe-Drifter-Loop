// ═══════════════════════════════════════════════════
// ДИСПЕТЧЕР ДІАЛОГІВ — ЯДРО
// ═══════════════════════════════════════════════════
//
// Порт з dispatcher.rpy: condition-based dialogue system
//
// Кожен діалог в грі реєструється в DIALOGUE_ENTRIES.
// Диспетчер обирає один eligible діалог за пріоритетом/шансом.
//
// Дві перевірки:
// 1. Стабільні (check_stable_conditions) — раз на день при build_daily_deck
// 2. Динамічні (check_dynamic_conditions) — при кожному get_dialogue

// ═══ ГОЛОВНІ БАЗИ ═══

var DIALOGUE_ENTRIES = [];        // Кожен діалог в грі — запис тут
var BANTER_ENTRIES = [];          // Фонові репліки (0 хв)
var MISSION_DIALOGUE_ENTRIES = []; // Місійні міні-діалоги

// Валідація: перевірити дублікати при push
var _origPush = Array.prototype.push;
function _validateEntryPush(arr, arrName) {
  return function(entry) {
    if (!entry.id) {
      console.error("[" + arrName + "] Entry without id:", entry);
      return arr.length;
    }
    for (var i = 0; i < arr.length; i++) {
      if (arr[i].id === entry.id) {
        console.warn("[" + arrName + "] Duplicate id '" + entry.id + "', overwriting");
        arr[i] = entry;
        return arr.length;
      }
    }
    return _origPush.call(arr, entry);
  };
}
DIALOGUE_ENTRIES.push = _validateEntryPush(DIALOGUE_ENTRIES, "DIALOGUE");
BANTER_ENTRIES.push = _validateEntryPush(BANTER_ENTRIES, "BANTER");
MISSION_DIALOGUE_ENTRIES.push = _validateEntryPush(MISSION_DIALOGUE_ENTRIES, "MISSION_DLG");


// ═══ ЗАГЛУШКИ — ТЕМИ ═══

var STUB_TOPICS = {
  "ar": [                    // ar
    "square_food", "keys", "danko", "sword_cleaning",
    "weather", "cooking", "drinks", "sleep", "silence", "quincy_annoying"
  ],
  "ao": [                                 // ao
    "origami", "music", "bubbletea", "bikes", "sleep",
    "weather", "quincy_noise", "mall_stores", "dreams", "stars"
  ],
  "am": [                           // am
    "games", "electronics", "future", "food", "sleep",
    "weather", "high_score", "mall_people", "energy", "jokes"
  ],
  "qu": [               // qu
    "weapons", "silence", "trolling", "training", "sleep",
    "weather", "amir_loud", "film", "accuracy", "boredom"
  ],
  "lt": [                     // lt
    "rats", "coffee", "health", "sarcasm", "sleep",
    "weather", "patients", "silence", "research", "cynicism"
  ],
  "el": [         // el
    "philosophy", "observations", "writing", "plants", "sleep",
    "weather", "patterns", "books", "quiet", "riddles"
  ]
};


registerState("dispatcher", {
  daily_deck: {},          // {"ar": [entry1, ...]} — фільтрована колода на день
  talked_today: [],        // ["ar", "ao"] — з ким сьогодні говорили
  seen_dialogues: [],      // ["arthur_middle_name", ...] — побачені діалоги
  stub_pools: {},          // {"ar": ["topic1", ...]} — пули заглушок
  tags_used_today: {},     // {"ar": ["heavy_lore"], ...} — cooldown теги
  expired_events: []       // ["arthur_eleanor_rooftop_fight", ...] — протухлі
});


// ═══════════════════════════════════════════════
// ПЕРЕВІРКА УМОВ
// ═══════════════════════════════════════════════

// Стабільні умови — перевіряються раз на день при build_daily_deck.
function checkStableConditions(conds) {
  if (!conds) return true;

  // chemistry_min: [name, val]
  if (conds.chemistry_min) {
    var cmName = conds.chemistry_min[0];
    var cmVal = conds.chemistry_min[1];
    if ((gameState.chemistry.values[cmName] || 0) < cmVal) return false;
  }

  // chemistry_max: [name, val]
  if (conds.chemistry_max) {
    var cxName = conds.chemistry_max[0];
    var cxVal = conds.chemistry_max[1];
    if ((gameState.chemistry.values[cxName] || 0) >= cxVal) return false;
  }

  // flag_true: ["flag1", "flag2"]
  if (conds.flag_true) {
    for (var i = 0; i < conds.flag_true.length; i++) {
      if (!getFlag(conds.flag_true[i])) return false;
    }
  }

  // flag_false: ["flag1", "flag2"]
  if (conds.flag_false) {
    for (var j = 0; j < conds.flag_false.length; j++) {
      if (getFlag(conds.flag_false[j])) return false;
    }
  }

  // rank_min: число
  if (conds.rank_min !== undefined) {
    if (gameState.rank.syndicate_rank < conds.rank_min) return false;
  }

  // rank_max: число
  if (conds.rank_max !== undefined) {
    if (gameState.rank.syndicate_rank >= conds.rank_max) return false;
  }

  // day_min: число
  if (conds.day_min !== undefined) {
    if (gameState.time.day < conds.day_min) return false;
  }

  // day_max: число
  if (conds.day_max !== undefined) {
    if (gameState.time.day >= conds.day_max) return false;
  }

  // dating: null або ім'я
  if (conds.dating !== undefined) {
    if (gameState.romance.dating !== conds.dating) return false;
  }

  return true;
}


// Динамічні умови — перевіряються при кожному get_dialogue.
function checkDynamicConditions(conds) {
  if (!conds) return true;

  // time_min / time_from
  var tMin = (conds.time_min !== undefined) ? conds.time_min : conds.time_from;
  if (tMin !== undefined && tMin !== null) {
    if (gameState.time.minutes < tMin) return false;
  }

  // time_max / time_to
  var tMax = (conds.time_max !== undefined) ? conds.time_max : conds.time_to;
  if (tMax !== undefined && tMax !== null) {
    if (gameState.time.minutes >= tMax) return false;
  }

  // location: "id"
  if (conds.location !== undefined) {
    if (gameState.location.current !== conds.location) return false;
  }

  // talked_today: true/false (+ who)
  if (conds.talked_today !== undefined) {
    var tName = conds.who || "";
    var talked = gameState.dispatcher.talked_today;
    var hasTalked = talked.indexOf(tName) >= 0;
    if (conds.talked_today && !hasTalked) return false;
    if (!conds.talked_today && hasTalked) return false;
  }

  // mission_partner: "ім'я"
  if (conds.mission_partner !== undefined) {
    if ((gameState.missions.current_partner || null) !== conds.mission_partner) return false;
  }

  // mission_partner2: "ім'я"
  if (conds.mission_partner2 !== undefined) {
    if ((gameState.missions.current_partner2 || null) !== conds.mission_partner2) return false;
  }

  // chars_at_location: ["ім'я1", "ім'я2"]
  if (conds.chars_at_location) {
    var here = getCharsAt(gameState.location.current);
    for (var i = 0; i < conds.chars_at_location.length; i++) {
      if (here.indexOf(conds.chars_at_location[i]) < 0) return false;
    }
  }

  // chemistry_min (dynamic re-check)
  if (conds.chemistry_min) {
    var cmName = conds.chemistry_min[0];
    var cmVal = conds.chemistry_min[1];
    if ((gameState.chemistry.values[cmName] || 0) < cmVal) return false;
  }

  // chemistry_max (dynamic re-check)
  if (conds.chemistry_max) {
    var cxName = conds.chemistry_max[0];
    var cxVal = conds.chemistry_max[1];
    if ((gameState.chemistry.values[cxName] || 0) >= cxVal) return false;
  }

  return true;
}


// ═══════════════════════════════════════════════
// DAILY DECK — ОПТИМІЗАЦІЯ
// ═══════════════════════════════════════════════

// Раз на день: фільтрує DIALOGUE_ENTRIES по стабільних умовах.
function buildDailyDeck() {
  gameState.dispatcher.daily_deck = {};

  for (var i = 0; i < DIALOGUE_ENTRIES.length; i++) {
    var entry = DIALOGUE_ENTRIES[i];

    // Вже побачені та не повторювані — пропустити
    if (gameState.dispatcher.seen_dialogues.indexOf(entry.id) >= 0 && !entry.repeatable) {
      continue;
    }

    // Стабільні умови
    if (!checkStableConditions(entry.conditions || {})) continue;

    var name = entry.who;
    if (!gameState.dispatcher.daily_deck[name]) {
      gameState.dispatcher.daily_deck[name] = [];
    }
    gameState.dispatcher.daily_deck[name].push(entry);
  }
}


// Точкове оновлення після критичного флагу.
function updateDeck(name) {
  gameState.dispatcher.daily_deck[name] = [];

  for (var i = 0; i < DIALOGUE_ENTRIES.length; i++) {
    var entry = DIALOGUE_ENTRIES[i];
    if (entry.who !== name) continue;
    if (gameState.dispatcher.seen_dialogues.indexOf(entry.id) >= 0 && !entry.repeatable) {
      continue;
    }
    if (!checkStableConditions(entry.conditions || {})) continue;
    gameState.dispatcher.daily_deck[name].push(entry);
  }
}


// ═══════════════════════════════════════════════
// ДИСПЕТЧЕР ДІАЛОГІВ
// ═══════════════════════════════════════════════

// Обирає ОДИН eligible діалог для NPC (за пріоритетом/шансом).
// Повертає entry dict або null.
function getActiveDialogue(name) {
  var deck = gameState.dispatcher.daily_deck[name] || [];
  var eligible = [];

  for (var i = 0; i < deck.length; i++) {
    var entry = deck[i];
    if (!entry.label && !entry.titles) continue;
    if (gameState.dispatcher.seen_dialogues.indexOf(entry.id) >= 0 && !entry.repeatable) continue;
    if (!checkDynamicConditions(entry.conditions || {})) continue;

    // Cooldown перевірка
    if (entry.cooldown_tag) {
      var used = gameState.dispatcher.tags_used_today[name] || [];
      if (used.indexOf(entry.cooldown_tag) >= 0) continue;
    }
    eligible.push(entry);
  }

  if (eligible.length === 0) return null;

  // Найвищий пріоритет
  var maxPri = -Infinity;
  for (var j = 0; j < eligible.length; j++) {
    if (eligible[j].priority > maxPri) maxPri = eligible[j].priority;
  }
  var top = [];
  for (var k = 0; k < eligible.length; k++) {
    if (eligible[k].priority === maxPri) top.push(eligible[k]);
  }

  // Chance — кидок кубика
  var passed = [];
  for (var m = 0; m < top.length; m++) {
    var ch = top[m].chance !== undefined ? top[m].chance : 100;
    if (ch >= 100 || (Math.floor(Math.random() * 100) + 1) <= ch) {
      passed.push(top[m]);
    }
  }

  // Якщо chance провалено — пробуємо нижчий пріоритет
  if (passed.length === 0) {
    var remaining = [];
    for (var n = 0; n < eligible.length; n++) {
      if (eligible[n].priority < maxPri) remaining.push(eligible[n]);
    }
    if (remaining.length > 0) {
      var nextPri = -Infinity;
      for (var p = 0; p < remaining.length; p++) {
        if (remaining[p].priority > nextPri) nextPri = remaining[p].priority;
      }
      for (var q = 0; q < remaining.length; q++) {
        if (remaining[q].priority === nextPri) {
          var ch2 = remaining[q].chance !== undefined ? remaining[q].chance : 100;
          if (ch2 >= 100 || (Math.floor(Math.random() * 100) + 1) <= ch2) {
            passed.push(remaining[q]);
          }
        }
      }
    }
  }

  if (passed.length === 0) return null;
  return passed[Math.floor(Math.random() * passed.length)];
}


// Перевіряє чи є forced діалог від NPC в локації.
function checkForcedDialogue(location) {
  var charsHere = getCharsAt(location);
  var eligible = [];
  for (var ci = 0; ci < charsHere.length; ci++) {
    var name = charsHere[ci];
    var deck = gameState.dispatcher.daily_deck[name] || [];
    for (var i = 0; i < deck.length; i++) {
      var entry = deck[i];
      if (!entry.label) continue;
      if (gameState.dispatcher.seen_dialogues.indexOf(entry.id) >= 0) continue;
      if (!checkDynamicConditions(entry.conditions || {})) continue;
      eligible.push(entry);
    }
  }
  if (eligible.length === 0) return null;
  var maxPri = -Infinity;
  for (var j = 0; j < eligible.length; j++) {
    var p = eligible[j].priority !== undefined ? eligible[j].priority : 1;
    if (p > maxPri) maxPri = p;
  }
  var top = [];
  for (var k = 0; k < eligible.length; k++) {
    var pp = eligible[k].priority !== undefined ? eligible[k].priority : 1;
    if (pp === maxPri) top.push(eligible[k]);
  }
  return top[Math.floor(Math.random() * top.length)];
}


// Головна функція: шукає в Daily Deck, повертає entry (з titles або label) або null.
function getDialogue(name) {
  var deck = gameState.dispatcher.daily_deck[name] || [];
  var eligible = [];

  for (var i = 0; i < deck.length; i++) {
    var entry = deck[i];
    if (gameState.dispatcher.seen_dialogues.indexOf(entry.id) >= 0 && !entry.repeatable) continue;
    if (!checkDynamicConditions(entry.conditions || {})) continue;

    // Cooldown перевірка
    if (entry.cooldown_tag) {
      var used = gameState.dispatcher.tags_used_today[name] || [];
      if (used.indexOf(entry.cooldown_tag) >= 0) continue;
    }
    eligible.push(entry);
  }

  if (eligible.length === 0) return null;

  // Найвищий пріоритет
  var maxPri = -Infinity;
  for (var j = 0; j < eligible.length; j++) {
    if (eligible[j].priority > maxPri) maxPri = eligible[j].priority;
  }
  var top = [];
  for (var k = 0; k < eligible.length; k++) {
    if (eligible[k].priority === maxPri) top.push(eligible[k]);
  }

  // Chance — кидок кубика
  var passed = [];
  for (var m = 0; m < top.length; m++) {
    var ch = top[m].chance !== undefined ? top[m].chance : 100;
    if (ch >= 100 || (Math.floor(Math.random() * 100) + 1) <= ch) {
      passed.push(top[m]);
    }
  }

  // Якщо chance провалено — нижчий пріоритет
  if (passed.length === 0) {
    var remaining = [];
    for (var n = 0; n < eligible.length; n++) {
      if (eligible[n].priority < maxPri) remaining.push(eligible[n]);
    }
    if (remaining.length > 0) {
      var nextPri = -Infinity;
      for (var p = 0; p < remaining.length; p++) {
        if (remaining[p].priority > nextPri) nextPri = remaining[p].priority;
      }
      for (var q = 0; q < remaining.length; q++) {
        if (remaining[q].priority === nextPri) {
          var ch2 = remaining[q].chance !== undefined ? remaining[q].chance : 100;
          if (ch2 >= 100 || (Math.floor(Math.random() * 100) + 1) <= ch2) {
            passed.push(remaining[q]);
          }
        }
      }
    }
  }

  if (passed.length === 0) return null;
  return passed[Math.floor(Math.random() * passed.length)];
}


// Перевіряє BANTER_ENTRIES для локації. Повертає entry або null.
function getBanter(location) {
  var charsHere = getCharsAt(location);
  var eligible = [];

  for (var i = 0; i < BANTER_ENTRIES.length; i++) {
    var entry = BANTER_ENTRIES[i];
    if (gameState.dispatcher.seen_dialogues.indexOf(entry.id) >= 0) continue;

    // Фільтр по локації (null/undefined = будь-де)
    var entryLoc = entry.location !== undefined ? entry.location : null;
    if (entryLoc !== null && entryLoc !== location) continue;

    // Перевірка NPC (одиночний або парний)
    if (entry.who) {
      if (charsHere.indexOf(entry.who) < 0) continue;
    } else if (entry.chars) {
      var allHere = true;
      for (var c = 0; c < entry.chars.length; c++) {
        if (charsHere.indexOf(entry.chars[c]) < 0) {
          allHere = false;
          break;
        }
      }
      if (!allHere) continue;
    } else {
      continue;
    }

    var conds = entry.conditions || {};
    if (!checkStableConditions(conds)) continue;
    if (!checkDynamicConditions(conds)) continue;
    eligible.push(entry);
  }

  if (eligible.length === 0) return null;

  // Найвищий пріоритет
  var maxPri = -Infinity;
  for (var j = 0; j < eligible.length; j++) {
    var p = eligible[j].priority !== undefined ? eligible[j].priority : 1;
    if (p > maxPri) maxPri = p;
  }
  var top = [];
  for (var k = 0; k < eligible.length; k++) {
    var pp = eligible[k].priority !== undefined ? eligible[k].priority : 1;
    if (pp === maxPri) top.push(eligible[k]);
  }

  var winner = top[Math.floor(Math.random() * top.length)];

  // Позначити як побачений
  gameState.dispatcher.seen_dialogues.push(winner.id);

  // Встановити flag_false флаги щоб banter не повторювався
  var bConds = winner.conditions || {};
  if (bConds.flag_false) {
    for (var f = 0; f < bConds.flag_false.length; f++) {
      setFlag(bConds.flag_false[f]);
    }
  }

  return winner;
}


// Місійний міні-діалог для напарника. Повертає label або null.
function getMissionDialogue(partner) {
  var eligible = [];

  for (var i = 0; i < MISSION_DIALOGUE_ENTRIES.length; i++) {
    var entry = MISSION_DIALOGUE_ENTRIES[i];
    if (entry.who !== partner) continue;
    if (gameState.dispatcher.seen_dialogues.indexOf(entry.id) >= 0) continue;
    var conds = entry.conditions || {};
    if (!checkStableConditions(conds)) continue;
    if (!checkDynamicConditions(conds)) continue;
    eligible.push(entry);
  }

  if (eligible.length === 0) return null;

  var maxPri = -Infinity;
  for (var j = 0; j < eligible.length; j++) {
    var p = eligible[j].priority !== undefined ? eligible[j].priority : 1;
    if (p > maxPri) maxPri = p;
  }
  var top = [];
  for (var k = 0; k < eligible.length; k++) {
    var pp = eligible[k].priority !== undefined ? eligible[k].priority : 1;
    if (pp === maxPri) top.push(eligible[k]);
  }

  var passed = [];
  for (var m = 0; m < top.length; m++) {
    var ch = top[m].chance !== undefined ? top[m].chance : 100;
    if (ch >= 100 || (Math.floor(Math.random() * 100) + 1) <= ch) {
      passed.push(top[m]);
    }
  }

  if (passed.length === 0) return null;
  return passed[Math.floor(Math.random() * passed.length)].label;
}


// ═══════════════════════════════════════════════
// ЗАГЛУШКИ
// ═══════════════════════════════════════════════

// Стан гравця для заглушок
function getPlayerState() {
  if (gameState.time.minutes >= 1380) return "tired";    // після 23:00
  if (gameState.missions.days_without_mission >= 3) return "stressed";
  return "normal";
}


// Модульна заглушка: тема з пулу + локація + стан.
function getStub(name) {
  var pool = gameState.dispatcher.stub_pools[name];

  // Якщо пул порожній — заповнити з STUB_TOPICS і перемішати
  if (!pool || pool.length === 0) {
    var topics = STUB_TOPICS[name] || [];
    var shuffled = topics.slice();
    for (var si = shuffled.length - 1; si > 0; si--) {
      var sj = Math.floor(Math.random() * (si + 1));
      var tmp = shuffled[si]; shuffled[si] = shuffled[sj]; shuffled[sj] = tmp;
    }
    gameState.dispatcher.stub_pools[name] = shuffled;
    pool = gameState.dispatcher.stub_pools[name];
  }
  if (!pool || pool.length === 0) return "generic_stub";

  // Випадкова тема з пулу
  var idx = Math.floor(Math.random() * pool.length);
  var topic = pool[idx];
  pool.splice(idx, 1);

  var loc = gameState.location.current;
  var state = getPlayerState();

  // Спробувати специфічний label: stub_Name_topic_loc_state
  var label = "stub_" + name + "_" + topic + "_" + loc + "_" + state;
  if (SCRIPTS && SCRIPTS[label]) return label;

  // Менш специфічний: stub_Name_topic
  label = "stub_" + name + "_" + topic;
  if (SCRIPTS && SCRIPTS[label]) return label;

  return "generic_stub";
}


// ═══════════════════════════════════════════════
// ПРОТУХАЮЧІ ІВЕНТИ
// ═══════════════════════════════════════════════

// Обробляє протухлі івенти. Викликається в nextDay().
function checkExpiredEvents() {
  for (var i = 0; i < DIALOGUE_ENTRIES.length; i++) {
    var entry = DIALOGUE_ENTRIES[i];
    if (entry.expires_in_days === undefined) continue;
    if (gameState.dispatcher.seen_dialogues.indexOf(entry.id) >= 0) continue;
    if (gameState.dispatcher.expired_events.indexOf(entry.id) >= 0) continue;

    var conds = entry.conditions || {};
    if (!checkStableConditions(conds)) continue;

    // Визначити коли став eligible
    var flagList = conds.flag_true || [];
    var becameDay = 1;
    if (flagList.length > 0) {
      becameDay = gameState.flags.data[flagList[0] + "_day"] || gameState.time.day;
    }

    if (gameState.time.day - becameDay > entry.expires_in_days) {
      // Протух — виконати наслідки
      var onExp = entry.on_expire || {};

      if (onExp.flags_set) {
        for (var f = 0; f < onExp.flags_set.length; f++) {
          setFlag(onExp.flags_set[f]);
        }
      }

      if (onExp.chemistry_change) {
        for (var cn in onExp.chemistry_change) {
          addChemistry(cn, onExp.chemistry_change[cn]);
        }
      }

      if (onExp.gossip_heat) {
        gameState.gossip.heat += onExp.gossip_heat;
      }

      gameState.dispatcher.expired_events.push(entry.id);
    }
  }
}


// Позначити діалог як побачений
function markDialogueSeen(dialogueId) {
  if (gameState.dispatcher.seen_dialogues.indexOf(dialogueId) < 0) {
    gameState.dispatcher.seen_dialogues.push(dialogueId);
  }
}


// Позначити що говорили сьогодні з NPC
function markTalkedToday(name) {
  if (gameState.dispatcher.talked_today.indexOf(name) < 0) {
    gameState.dispatcher.talked_today.push(name);
  }
}
