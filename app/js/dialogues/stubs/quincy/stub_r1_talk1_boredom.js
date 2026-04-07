// Stub: Квінсі — boredom
DIALOGUE_ENTRIES.push({
  id: "stub_qu_boredom",
  who: "Квінсі",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Нудьгуєш?", label: "stub_qu_boredom" }]
});

registerScript("stub_qu_boredom", [
  { type: "show", who: "qu", zorder: 1 },
  { type: "say", who: "mc", text: "Нудьгуєш?" },
  { type: "say", who: "qu", text: "Нудьгую? Я ВМИРАЮ від нудьги." },
  { type: "say", who: "qu", text: "Останні три години я рахував плями на стелі. Сорок сім." },
  { type: "say", who: "qu", text: "Ну шо, Марті, розважиш мене чи як?" },
  { type: "end", text: "" }
]);
