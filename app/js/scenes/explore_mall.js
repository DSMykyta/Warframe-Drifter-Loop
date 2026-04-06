// ═══════════════════════════════════════════════════
// СЦЕНА 2: Дрифтер досліджує мол, знаходить карту
// Порт з game/scenes/explore_mall.rpy
// ═══════════════════════════════════════════════════

registerScript("explore_mall", [
  // ─── Мол ───
  { type: "bg", file: "bg_mall.webp" },

  { type: "say", who: null, text: "Мол. Великий. Тихий." },
  { type: "say", who: null, text: "Музика з динаміків під стелею. Ледь чутно." },
  { type: "say", who: null, text: "Вивіски, ескалатори, магазини. Все на місці." },
  { type: "say", who: null, text: "Людей — ні." },
  { type: "say", who: null, text: "Треба зорієнтуватись." },

  // ─── Інфостійка ───
  { type: "bg", file: "bg_info_desk.webp" },

  { type: "say", who: null, text: "Інфостійка. Брошури, схеми евакуації." },
  { type: "say", who: null, text: "Карта молу. Ціла." },

  { type: "set_flag", flag: "has_map" },

  { type: "say", who: null, text: "Тир, аркади, медвідділ — периметр. Гараж — через комп-клуб. Дах — сходи з центру." },
  { type: "say", who: null, text: "Зрозуміло." },

  // ─── Розблокувати локації що видно на карті ───
  { type: "set_flag", flag: "garage_unlocked" },
  { type: "set_flag", flag: "comp_club_unlocked" },
  { type: "set_flag", flag: "rooftop_unlocked" },
  { type: "set_flag", flag: "balcony_unlocked" },
  { type: "set_flag", flag: "security_room_unlocked" },
  { type: "set_flag", flag: "parking_unlocked" },
  { type: "set_flag", flag: "cinema_unlocked" },
  { type: "set_flag", flag: "gym_unlocked" },
  { type: "set_flag", flag: "billiard_unlocked" },
  { type: "set_flag", flag: "barbershop_unlocked" },
  { type: "set_flag", flag: "photo_studio_unlocked" },
  { type: "set_flag", flag: "laundry_unlocked" },
  { type: "set_flag", flag: "wc_unlocked" },
  { type: "set_flag", flag: "warehouse_unlocked" },
  { type: "set_flag", flag: "utility_unlocked" },
  { type: "set_flag", flag: "pharmacy_unlocked" },
  { type: "set_flag", flag: "video_rental_unlocked" },
  { type: "set_flag", flag: "electronics_unlocked" },
  { type: "set_flag", flag: "jewelry_unlocked" },
  { type: "set_flag", flag: "bookshop_unlocked" },
  { type: "set_flag", flag: "room_2_unlocked" },
  // Пейджер від Аміра
  { type: "set_flag", flag: "has_pager" },

  // ─── Повернення в мол ───
  { type: "bg", file: "bg_mall.webp" },

  { type: "end", text: "" }
]);
