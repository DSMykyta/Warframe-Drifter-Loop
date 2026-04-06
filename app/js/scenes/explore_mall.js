// ═══════════════════════════════════════════════════
// СЦЕНА 2: Дрифтер досліджує мол, знаходить карту
// Порт з game/scenes/explore_mall.rpy
// ═══════════════════════════════════════════════════

registerScript("explore_mall", [
  // ─── Мол ───
  { type: "bg", file: "bg_mall.png" },

  { type: "say", who: null, text: "Мол. Великий. Тихий." },
  { type: "say", who: null, text: "Музика з динаміків під стелею. Ледь чутно." },
  { type: "say", who: null, text: "Вивіски, ескалатори, магазини. Все на місці." },
  { type: "say", who: null, text: "Людей — ні." },
  { type: "say", who: null, text: "Треба зорієнтуватись." },

  // ─── Інфостійка ───
  { type: "bg", file: "bg_info_desk.png" },

  { type: "say", who: null, text: "Інфостійка. Брошури, схеми евакуації." },
  { type: "say", who: null, text: "Карта молу. Ціла." },

  { type: "set_flag", flag: "has_map" },

  { type: "say", who: null, text: "Тир, аркади, медвідділ — периметр. Гараж — через комп-клуб. Дах — сходи з центру." },
  { type: "say", who: null, text: "Зрозуміло." },

  // ─── Повернення в мол ───
  { type: "bg", file: "bg_mall.png" },

  { type: "end", text: "" }
]);
