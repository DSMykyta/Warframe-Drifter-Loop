// ═══════════════════════════════════════════════════
// АОІ — ІНТРО: On-lyne, музика, логістика
// Порт з game/dialogues/aoi/aoi_intro.rpy
// ═══════════════════════════════════════════════════

DIALOGUE_ENTRIES.push({
  id: "aoi_intro",
  who: "ao",
  conditions: { flag_false: ["aoi_intro_done"] },
  priority: 95,
  chance: 100,
  label: "aoi_intro"
});

registerScript("aoi_intro", [
  { type: "show", who: "ao", zorder: 1 },
  { type: "say", who: "ao", text: "О! Ти!" },
  { type: "say", who: "ao", text: "Привіт-привіт! Я Аоі!" },
  { type: "say", who: "ao", text: "Слухай, поки ти тут — скажи чесно." },
  { type: "say", who: "ao", text: "Ти чув On-lyne?" },
  { type: "say", who: "mc", text: "On-lyne?" },
  { type: "say", who: "ao", text: "Гурт! Вони скрізь! Плакати, радіо, автомати з напоями — всюди їхня пісня." },
  { type: "say", who: "ao", text: "Ну, одна пісня. Але яка!" },
  { type: "say", who: "ao", text: "«Boys R Back»!" },

  { type: "menu", choices: [
    { text: "Наспівай.", label: "aoi_sing" },
    { text: "Здається чув щось в молі.", label: "aoi_heard" },
    { text: "В майбутньому музика інша.", label: "aoi_future" }
  ]},

  { type: "label", id: "aoi_sing" },
  { type: "say", who: "mc", text: "Наспівай, може впізнаю." },
  { type: "say", who: "ao", text: "Ем..." },
  { type: "say", who: "ao", text: "Ні. Ні-ні-ні. Я не співаю при людях." },
  { type: "say", who: "ao", text: "Але повір — почуєш і не зможеш забути. В хорошому сенсі!" },
  { type: "chemistry", who: "ao", amount: 4 },
  { type: "jump", to: "aoi_after_choice" },

  { type: "label", id: "aoi_heard" },
  { type: "say", who: "mc", text: "Здається щось грало з динаміків коли я ходив по молу." },
  { type: "say", who: "ao", text: "ТАК! Це вони! Бачиш, вони СКРІЗЬ!" },
  { type: "chemistry", who: "ao", amount: 2 },
  { type: "jump", to: "aoi_after_choice" },

  { type: "label", id: "aoi_future" },
  { type: "say", who: "mc", text: "В майбутньому музика... трохи інша." },
  { type: "say", who: "ao", text: "Інша як? Краща? Гірша? Є синтезатори??" },
  { type: "say", who: "mc", text: "Є... орбітери. З вбудованим радіо." },
  { type: "say", who: "ao", text: "Я не знаю що таке орбітер, але якщо там є радіо — я хочу один." },
  { type: "chemistry", who: "ao", amount: 2 },

  { type: "label", id: "aoi_after_choice" },
  { type: "say", who: "ao", text: "Знаєш що мені подобається в On-lyne?" },
  { type: "say", who: "ao", text: "Вони грають так, ніби все нормально. Ніби немає Техроту, скальдри, нічого." },
  { type: "say", who: "ao", text: "Просто хлопці з гітарами і надією." },
  { type: "say", who: "ao", text: "Іноді цього достатньо." },
  { type: "say", who: "mc", text: "..." },
  { type: "say", who: "ao", text: "Ой, я розговорилась! Вибач." },
  { type: "say", who: "ao", text: "Я Аоі. Логістика, координація, магнітні здібності." },
  { type: "say", who: "ao", text: "Якщо потрібно знайти щось або когось — приходь до мене. Я в музичному магазині." },
  { type: "say", who: "ao", text: "І якщо хочеш послухати On-lyne разом — теж приходь!" },

  { type: "set_flag", flag: "aoi_intro_done" },

  // Якщо немає пейджера — направити до Аміра
  { type: "if", flag: "has_pager", jump: "aoi_intro_done_final" },
  { type: "say", who: "ao", text: "А! Ти ще не був у Аміра?" },
  { type: "say", who: "ao", text: "Він в аркадах. Обов'язково зайди — в нього є штука яка тобі дуже потрібна!" },
  { type: "label", id: "aoi_intro_done_final" },
  { type: "end", text: "" }
]);
