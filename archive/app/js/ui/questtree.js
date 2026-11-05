// ═══════════════════════════════════════════════════
// ДЕРЕВО КВЕСТІВ — візуальне відображення прогресу
// ═══════════════════════════════════════════════════
//
// Показує всі квестові лінії з етапами.
// Пройдені гілки — відкриті. Непройдені — заблюрені.
// Поточний етап — підсвічений.

// ═══ ВИЗНАЧЕННЯ КВЕСТОВИХ ЛІНІЙ ═══
//
// Кожен квест — масив етапів.
// Етап: { id, name, description, flag, children }
// flag — прапорець що позначає завершення етапу
// children — дочірні гілки (для розгалужень)

var QUEST_TREE = [
  {
    id: "main",
    name: "ОСНОВНА ПЕТЛЯ",
    icon: "∞",
    stages: [
      { id: "intro", name: "Допит", desc: "Прибуття в мол. Знайомство з Гексом.", flag: "intro_done" },
      { id: "explore", name: "Розвідка", desc: "Дослідити мол Гьольвані.", flag: "explore_done" },
      { id: "pager", name: "Пейджер", desc: "Отримати пейджер від Артура.", flag: "has_pager" },
      { id: "map", name: "Карта", desc: "Знайти карту молу.", flag: "has_map" },
      { id: "garage", name: "Гараж", desc: "Розблокувати гараж для місій.", flag: "garage_unlocked" },
      { id: "rank2", name: "Ранг 2", desc: "Підвищити ранг Гексу до 2.", flag: "rank_2" },
      { id: "rank3", name: "Ранг 3", desc: "Ранг 3 — відкрити бар.", flag: "syndicate_rank_3" },
      { id: "rank4", name: "Ранг 4", desc: "Ранг 4 — місії рівня 6.", flag: "rank_4" },
      { id: "rank5", name: "Ранг 5", desc: "Ранг 5 — елітні операції.", flag: "rank_5" },
      { id: "rank6", name: "Ранг 6", desc: "Максимальний ранг.", flag: "rank_6" },
      { id: "finale", name: "День 31", desc: "Фінальна подія петлі.", flag: "_trigger_victory",
        branches: [
          { id: "victory", name: "Перемога", desc: "Реактор стабілізований.", flag: "_trigger_victory" },
          { id: "defeat", name: "Поразка", desc: "Петля замикається.", flag: "_trigger_loop_end" }
        ]
      }
    ]
  },
  {
    id: "arthur",
    name: "АРТУР",
    icon: "⚔",
    stages: [
      { id: "ar_meet", name: "Знайомство", desc: "Зустрів Артура — лідера Гексу.", flag: "arthur_intro_done" },
      { id: "ar_trust", name: "Довіра", desc: "Артур довіряє тобі.", flag: "arthur_trusts" },
      { id: "ar_fight", name: "Сварка", desc: "Конфлікт між Артуром та Елеонор.", flag: "arthur_eleanor_fight_active",
        branches: [
          { id: "ar_resolved", name: "Примирення", desc: "Вирішити конфлікт.", flag: "arthur_fight_resolved" },
          { id: "ar_unresolved", name: "Розрив", desc: "Конфлікт не вирішено.", flag: "arthur_fight_failed" }
        ]
      },
      { id: "ar_friends", name: "Друзі", desc: "Хімія 120+.", flag: "arthur_friends_milestone" },
      { id: "ar_romance", name: "Романс", desc: "Хімія 160+.", flag: "dating_arthur" }
    ]
  },
  {
    id: "eleanor",
    name: "ЕЛЕОНОР",
    icon: "◈",
    stages: [
      { id: "el_meet", name: "Знайомство", desc: "Зустрів Елеонор — телепатку.", flag: "eleanor_intro_done" },
      { id: "el_voices", name: "Голоси", desc: "Дізнатись про голоси в голові.", flag: "eleanor_voices_known" },
      { id: "el_trust", name: "Довіра", desc: "Елеонор відкривається.", flag: "eleanor_trusts" },
      { id: "el_friends", name: "Друзі", desc: "Хімія 120+.", flag: "eleanor_friends_milestone" },
      { id: "el_romance", name: "Романс", desc: "Хімія 160+.", flag: "dating_eleanor" }
    ]
  },
  {
    id: "lettie",
    name: "ЛЕТТІ",
    icon: "✚",
    stages: [
      { id: "lt_meet", name: "Знайомство", desc: "Зустрів Летті — медика.", flag: "lettie_intro_done" },
      { id: "lt_bandage", name: "Перев'язка", desc: "Летті перев'язала руку.", flag: "lettie_bandaged_hand" },
      { id: "lt_trust", name: "Довіра", desc: "Летті перестає саркастизувати.", flag: "lettie_trusts" },
      { id: "lt_friends", name: "Друзі", desc: "Хімія 120+.", flag: "lettie_friends_milestone" },
      { id: "lt_romance", name: "Романс", desc: "Хімія 160+.", flag: "dating_lettie" }
    ]
  },
  {
    id: "amir",
    name: "АМІР",
    icon: "⚡",
    stages: [
      { id: "am_meet", name: "Знайомство", desc: "Зустрів Аміра — техніка.", flag: "amir_intro_done" },
      { id: "am_nickname", name: "Прізвисько", desc: "Амір назвав тебе Марті.", flag: "nickname_marty" },
      { id: "am_trust", name: "Довіра", desc: "Амір ділиться планами.", flag: "amir_trusts" },
      { id: "am_friends", name: "Друзі", desc: "Хімія 120+.", flag: "amir_friends_milestone" },
      { id: "am_romance", name: "Романс", desc: "Хімія 160+.", flag: "dating_amir" }
    ]
  },
  {
    id: "aoi",
    name: "АОІ",
    icon: "♪",
    stages: [
      { id: "ao_meet", name: "Знайомство", desc: "Зустрів Аоі — логістику.", flag: "aoi_intro_done" },
      { id: "ao_hand", name: "Рука", desc: "Аоі простягнула руку першою.", flag: "aoi_handshake" },
      { id: "ao_trust", name: "Довіра", desc: "Аоі відкривається.", flag: "aoi_trusts" },
      { id: "ao_friends", name: "Друзі", desc: "Хімія 120+.", flag: "aoi_friends_milestone" },
      { id: "ao_romance", name: "Романс", desc: "Хімія 160+.", flag: "dating_aoi" }
    ]
  },
  {
    id: "quincy",
    name: "КВІНСІ",
    icon: "◎",
    stages: [
      { id: "qu_meet", name: "Знайомство", desc: "Зустрів Квінсі — снайпера.", flag: "quincy_intro_done" },
      { id: "qu_range", name: "Тир", desc: "Квінсі запросив в тир.", flag: "quincy_range_invite" },
      { id: "qu_trust", name: "Довіра", desc: "Квінсі перестає тролити.", flag: "quincy_trusts" },
      { id: "qu_friends", name: "Друзі", desc: "Хімія 120+.", flag: "quincy_friends_milestone" },
      { id: "qu_romance", name: "Романс", desc: "Хімія 160+.", flag: "dating_quincy" }
    ]
  },
  {
    id: "coffee_quest",
    name: "КАВОВИЙ КВЕСТ",
    icon: "☕",
    stages: [
      { id: "cq_find", name: "Знахідка", desc: "Знайти кавомашину.", flag: "coffee_machine_found" },
      { id: "cq_milk", name: "Молоко", desc: "Розблокувати молочні напої.", flag: "milk_drinks_unlocked" },
      { id: "cq_cap", name: "Капучіно", desc: "Розблокувати капучіно.", flag: "milk_cappuccino_unlocked" },
      { id: "cq_cafe", name: "Кав'ярня", desc: "Відкрити кав'ярню.", flag: "cafe_unlocked" }
    ]
  }
];


// ═══ РЕНДЕР ДЕРЕВА КВЕСТІВ ═══

function renderQuestTree() {
  var container = document.getElementById("quest-tree-container");
  if (!container) return;
  container.innerHTML = "";

  for (var q = 0; q < QUEST_TREE.length; q++) {
    var quest = QUEST_TREE[q];
    var questEl = document.createElement("div");
    questEl.className = "qt-quest";

    // Заголовок квесту
    var header = document.createElement("div");
    header.className = "qt-quest-header";
    header.innerHTML = '<span class="qt-icon">' + (quest.icon || "") + '</span>' +
      '<span class="qt-quest-name">' + quest.name + '</span>' +
      '<span class="qt-progress">' + _getQuestProgress(quest) + '</span>';
    questEl.appendChild(header);

    // Лінія етапів
    var timeline = document.createElement("div");
    timeline.className = "qt-timeline";

    var lastCompleted = -1;
    for (var s = 0; s < quest.stages.length; s++) {
      var stage = quest.stages[s];
      var completed = _isStageCompleted(stage);
      var isNext = !completed && lastCompleted === s - 1;
      if (completed) lastCompleted = s;

      var stageEl = _renderStage(stage, completed, isNext, s === 0);
      timeline.appendChild(stageEl);

      // Гілки (branches)
      if (stage.branches && stage.branches.length > 0) {
        var branchContainer = document.createElement("div");
        branchContainer.className = "qt-branches";
        for (var b = 0; b < stage.branches.length; b++) {
          var branch = stage.branches[b];
          var bCompleted = _isStageCompleted(branch);
          var bIsNext = completed && !bCompleted;
          var branchEl = _renderStage(branch, bCompleted, bIsNext, false);
          branchEl.classList.add("qt-branch");
          branchContainer.appendChild(branchEl);
        }
        timeline.appendChild(branchContainer);
      }

      // З'єднувальна лінія (крім останнього)
      if (s < quest.stages.length - 1 && (!stage.branches || stage.branches.length === 0)) {
        var connector = document.createElement("div");
        connector.className = "qt-connector" + (completed ? " completed" : "");
        timeline.appendChild(connector);
      }
    }

    questEl.appendChild(timeline);
    container.appendChild(questEl);
  }
}


// Рендер одного етапу
function _renderStage(stage, completed, isNext, isFirst) {
  var el = document.createElement("div");

  if (completed) {
    el.className = "qt-stage completed";
  } else if (isNext || isFirst) {
    el.className = "qt-stage current";
  } else {
    el.className = "qt-stage locked";
  }

  var dot = document.createElement("div");
  dot.className = "qt-dot";
  if (completed) dot.innerHTML = "✓";
  el.appendChild(dot);

  var info = document.createElement("div");
  info.className = "qt-stage-info";

  var nameEl = document.createElement("div");
  nameEl.className = "qt-stage-name";
  nameEl.textContent = completed || isNext || isFirst ? stage.name : "???";
  info.appendChild(nameEl);

  var descEl = document.createElement("div");
  descEl.className = "qt-stage-desc";
  descEl.textContent = completed || isNext || isFirst ? stage.desc : "";
  info.appendChild(descEl);

  el.appendChild(info);
  return el;
}


// Перевірити чи етап пройдений
function _isStageCompleted(stage) {
  if (!stage.flag) return false;
  // Перевірити хімію для friends/romance етапів
  if (stage.flag.indexOf("friends_milestone") >= 0) {
    var charName = _extractCharName(stage.id);
    if (charName && gameState.chemistry && gameState.chemistry.values[charName] >= 120) return true;
  }
  if (stage.flag.indexOf("dating_") === 0) {
    return gameState.romance && gameState.romance.dating === _flagToName(stage.flag.replace("dating_", ""));
  }
  return getFlag(stage.flag);
}


// Прогрес квесту (текст)
function _getQuestProgress(quest) {
  var total = quest.stages.length;
  var done = 0;
  for (var i = 0; i < quest.stages.length; i++) {
    if (_isStageCompleted(quest.stages[i])) done++;
  }
  return done + "/" + total;
}


// Допоміжне: витягти ім'я персонажа з ID етапу
function _extractCharName(stageId) {
  var map = {
    "ar_": "ar", "el_": "el", "lt_": "lt",
    "am_": "am", "ao_": "ao", "qu_": "qu"
  };
  for (var prefix in map) {
    if (stageId.indexOf(prefix) === 0) return map[prefix];
  }
  return null;
}


// Допоміжне: charFlag → ім'я
function _flagToName(flagName) {
  // Convert full Latin flag name to short ID for comparison
  var map = {
    "arthur": "ar", "eleanor": "el", "lettie": "lt",
    "amir": "am", "aoi": "ao", "quincy": "qu"
  };
  return map[flagName] || flagName;
}
