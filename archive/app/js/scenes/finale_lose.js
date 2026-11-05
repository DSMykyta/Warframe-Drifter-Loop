// ═══════════════════════════════════════════════════
// ФІНАЛ: ПОРАЗКА (ЧАСОВА ПЕТЛЯ)
// Порт з game/scenes/finale_lose.rpy
// ═══════════════════════════════════════════════════

registerScript("finale_defeat", [
  { type: "scene", bg: "bg_black.png" },

  { type: "think", text: "День 31. Новий Рік. Реактор." },

  { type: "think", text: "Ви стоїте перед реактором. Але щось не так." },

  { type: "think", text: "Погляди не зустрічаються. Руки не впевнені. Слова — порожні." },

  { type: "show", who: "ar", zorder: 1 },
  { type: "say", who: "ar", text: "Ми... спробуємо." },

  { type: "say", who: "mc", text: "Артуре..." },

  { type: "say", who: "ar", text: "Я знаю. Я теж це відчуваю." },

  { type: "hide", who: "ar" },
  { type: "scene", bg: "bg_black.png" },

  { type: "think", text: "Реактор нестабільний. Команда не синхронізована." },

  { type: "think", text: "Хтось помиляється. Потім інший. Ланцюгова реакція." },

  { type: "think", text: "Вибух." },

  { type: "think", text: "..." },

  { type: "think", text: "Темрява." },

  { type: "think", text: "..." },

  { type: "think", text: "Будильник. Ранок." },

  { type: "think", text: "Знову." },

  // Зберегти persistent
  { type: "set_flag", flag: "_trigger_loop_end" },

  { type: "think", text: "Щось залишилось. Тінь спогаду. Дежавю." },

  { type: "think", text: "Може, цього разу..." },

  { type: "end", text: "" }
]);
