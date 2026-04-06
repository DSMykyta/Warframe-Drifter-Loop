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
  for (var name in gameState.chemistry.values) {
    if (gameState.chemistry.values[name] < 120) {
      return false;
    }
  }
  return true;
}


// ─── Попередження на день 30 ───

DIALOGUE_ENTRIES.push({
  id: "day30_warning",
  who: "Артур",
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
  {type: "say", who: "Артур", text: "Завтра — Новий Рік. Реактор."},
  {type: "say", who: "Артур", text: "Якщо ми не готові... якщо ми не довіряємо одне одному повністю..."},
  {type: "say", who: "Артур", text: "Не буде другого шансу."},
  {type: "set_flag", flag: "day30_warning_done"},
  {type: "end"}
]);


// ─── Перемога ───

registerScript("finale_victory", [
  {type: "say", who: null, text: "День 31. Новий Рік. Реактор."},
  {type: "say", who: null, text: "Гекс стоїть разом. Усі шестеро. І ти."},
  {type: "say", who: "Артур", text: "Ми готові."},
  {type: "say", who: "Елеонор", text: "Я бачу в них впевненість. Справжню."},
  {type: "say", who: "Летті", text: "Якщо хтось поранеться — я тут. Але краще б ніхто не поранився."},
  {type: "say", who: "Амір", text: "Системи стабільні. Реактор під контролем. Наскільки це можливо."},
  {type: "say", who: "Аоі", text: "Тисяча журавликів. Бажання — щоб ми всі вижили."},
  {type: "say", who: "Квінсі", text: "Менше слів. Більше дій. Погнали."},
  {type: "say", who: null, text: "Реактор. Серце Гьольванії. Тисячі тонн нестабільної енергії."},
  {type: "say", who: null, text: "Але Гекс працює як єдиний організм. Кожен знає свою роль."},
  {type: "say", who: null, text: "Артур координує. Елеонор сканує. Летті підтримує. Амір контролює системи."},
  {type: "say", who: null, text: "Аоі знаходить слабке місце. Квінсі робить один точний постріл."},
  {type: "say", who: null, text: "Реактор стабілізований."},
  {type: "say", who: null, text: "Петля — розірвана."},
  {type: "say", who: null, text: "..."},
  {type: "say", who: null, text: "Ви стоїте на даху молу. Перше січня 2000 року."},
  {type: "say", who: null, text: "Перший ранок без петлі."},
  {type: "say", who: "Артур", text: "Ми зробили це."},
  {type: "say", who: null, text: "Разом."},
  {type: "say", who: "Артур", text: "Разом."},
  {type: "say", who: null, text: "WARFRAME: DRIFTER LOOP"},
  {type: "say", who: null, text: "Кінець."},
  {type: "say", who: null, text: "...Або початок?"},
  {type: "end"}
]);


// ─── Поразка ───

registerScript("finale_defeat", [
  {type: "say", who: null, text: "День 31. Новий Рік. Реактор."},
  {type: "say", who: null, text: "Гекс стоїть... але чогось не вистачає."},
  {type: "say", who: null, text: "Довіри. Зв'язку. Того що робить команду — командою."},
  {type: "say", who: "Артур", text: "Ми... спробуємо."},
  {type: "say", who: null, text: "Але всі знають — цього не достатньо."},
  {type: "say", who: null, text: "Реактор нестабільний. Енергія б'є хвилями."},
  {type: "say", who: null, text: "Команда не працює як єдине ціле. Занадто багато тріщин."},
  {type: "say", who: null, text: "Спалах. Біль. Темрява."},
  {type: "say", who: null, text: "..."},
  {type: "say", who: null, text: "Ви прокидаєтесь. Перше грудня. Знову."},
  {type: "say", who: null, text: "Петля замикається."},
  {type: "say", who: null, text: "Але в голові — тихий голос: 'Цього разу я зроблю інакше.'"},
  {type: "end"}
]);
