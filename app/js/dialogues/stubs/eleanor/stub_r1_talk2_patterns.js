// Stub: Елеонор — patterns
DIALOGUE_ENTRIES.push({
  id: "stub_el_patterns",
  who: "Елеонор",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Бачиш щось цікаве?", label: "stub_el_patterns" }]
});

registerScript("stub_el_patterns", [
  { type: "show", who: "el", zorder: 1 },
  { type: "say", who: "mc", text: "Бачиш щось цікаве?" },
  { type: "say", who: "el", text: "Завжди. Все навколо — патерни." },
  { type: "say", who: "el", text: "Летті п'є каву о сьомій. Амір вмикає музику о восьмій. Квінсі жартує о дев'ятій." },
  { type: "telepathy", text: "А ти приходиш до мене, коли не знаєш куди себе подіти." },
  { type: "say", who: "el", text: "Це теж патерн." },
  { type: "end", text: "" }
]);
