// ═══════════════════════════════════════════════════
// СЦЕНА 2: Дрифтер досліджує мол, знаходить карту
// Порт з game/scenes/explore_mall.rpy
// ═══════════════════════════════════════════════════

registerScript("explore_mall", [
  { type: "bg", file: "bg_mall.webp" },

  // Повторна петля — скорочено
  { type: "if", loop_restart: true, jump: "explore_restart" },

  // ═══ ПЕРША ПЕТЛЯ ═══
  { type: "think", text: "Мол. Великий. Тихий." },
  { type: "think", text: "Музика з динаміків під стелею. Ледь чутно." },
  { type: "think", text: "Вивіски, ескалатори, магазини. Все на місці." },
  { type: "think", text: "Людей — ні." },
  { type: "think", text: "Треба зорієнтуватись." },

  { type: "bg", file: "bg_info_desk.webp" },

  { type: "think", text: "Інфостійка. Брошури, схеми евакуації." },
  { type: "think", text: "Карта молу. Ціла." },

  { type: "set_flag", flag: "has_map" },

  { type: "think", text: "Тир, аркади, медвідділ — периметр. Гараж — через комп-клуб. Дах — сходи з центру." },
  { type: "think", text: "Зрозуміло." },

  { type: "end", text: "" },

  // ═══ ПОВТОРНА ПЕТЛЯ ═══
  { type: "label", id: "explore_restart" },
  { type: "think", text: "Мол. Знову." },

  { type: "bg", file: "bg_info_desk.webp" },
  { type: "think", text: "Карта на стійці. Там само." },

  { type: "set_flag", flag: "has_map" },

  { type: "end", text: "" }
]);
