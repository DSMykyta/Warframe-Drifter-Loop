// ═══════════════════════════════════════════════════
// ФІНАЛ: День 31 — Перемога / Поразка
// ═══════════════════════════════════════════════════
//
// Порт з game/scenes/finale_win.rpy
//
// Перевірка: всі 6 NPC мають chemistry >= 120 (Друзі).
// Якщо так — перемога (реактор стабілізований, петля розірвана).
// Якщо ні — поразка (петля замикається).

function checkAllFriends() {
  for (var short in CAST) {
    if (!CAST[short].missions) continue;
    if ((gameState.chemistry.values[short] || 0) < 120) {
      return false;
    }
  }
  return true;
}


// ─── Попередження на день 30 ───

DIALOGUE_ENTRIES.push({
  id: "day30_warning",
  who: "ar",
  conditions: {
    day_min: 30,
    day_max: 31,
    flag_false: ["day30_warning_done"]
  },
  priority: 99,
  chance: 100,
  label: "day30_warning"
});

registerScript("day30_warning", [
  {type: "say", who: "ar", text: "Завтра — Новий Рік. Реактор."},
  {type: "say", who: "ar", text: "Якщо ми не готові... якщо ми не довіряємо одне одному повністю..."},
  {type: "say", who: "ar", text: "Не буде другого шансу."},
  {type: "set_flag", flag: "day30_warning_done"},
  {type: "end"}
]);


// ─── Перемога ───

registerScript("finale_victory", [
  {type: "say", who: null, text: "День 31. Новий Рік. Реактор."},
  {type: "say", who: null, text: "Гекс стоїть разом. Усі шестеро. І ти."},
  {type: "say", who: "ar", text: "Ми готові."},
  {type: "say", who: "el", text: "Я бачу в них впевненість. Справжню."},
  {type: "say", who: "lt", text: "Якщо хтось поранеться — я тут. Але краще б ніхто не поранився."},
  {type: "say", who: "am", text: "Системи стабільні. Реактор під контролем. Наскільки це можливо."},
  {type: "say", who: "ao", text: "Тисяча журавликів. Бажання — щоб ми всі вижили."},
  {type: "say", who: "qu", text: "Менше слів. Більше дій. Погнали."},
  {type: "say", who: null, text: "Реактор. Серце Гьольванії. Тисячі тонн нестабільної енергії."},
  {type: "say", who: null, text: "Але Гекс працює як єдиний організм. Кожен знає свою роль."},
  {type: "say", who: null, text: "Артур координує. Елеонор сканує. Летті підтримує. Амір контролює системи."},
  {type: "say", who: null, text: "Аоі знаходить слабке місце. Квінсі робить один точний постріл."},
  {type: "say", who: null, text: "Реактор стабілізований."},
  {type: "say", who: null, text: "Петля — розірвана."},
  {type: "say", who: null, text: "..."},
  {type: "say", who: null, text: "Ви стоїте на даху молу. Перше січня 2000 року."},
  {type: "say", who: null, text: "Перший ранок без петлі."},
  {type: "say", who: "ar", text: "Ми зробили це."},
  {type: "say", who: null, text: "Разом."},
  {type: "say", who: "ar", text: "Разом."},
  {type: "say", who: null, text: "WARFRAME: DRIFTER LOOP"},
  {type: "say", who: null, text: "Кінець."},
  {type: "say", who: null, text: "...Або початок?"},
  {type: "set_flag", flag: "_trigger_victory"},
  {type: "end", text: ""}
]);


// ─── Поразка визначена в finale_lose.js ───
