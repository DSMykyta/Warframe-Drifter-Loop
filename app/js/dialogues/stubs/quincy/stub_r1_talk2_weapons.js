// Stub: Квінсі — weapons
DIALOGUE_ENTRIES.push({
  id: "stub_qu_weapons",
  who: "Квінсі",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Нова гвинтівка?", label: "stub_qu_weapons" }]
});

registerScript("stub_qu_weapons", [
  { type: "show", who: "qu", zorder: 1 },
  { type: "say", who: "mc", text: "Нова гвинтівка?" },
  { type: "say", who: "qu", text: "Стара. Але я поставив новий приціл." },
  { type: "say", who: "qu", text: "Тепер бачу, як Артур хмуриться з п'ятисот метрів." },
  { type: "say", who: "qu", text: "Технічно це апгрейд якості життя." },
  { type: "end", text: "" }
]);
