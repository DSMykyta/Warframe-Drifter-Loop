// Stub: Квінсі — nicknames
DIALOGUE_ENTRIES.push({
  id: "stub_qu_nicknames",
  who: "Квінсі",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Привіт, Квінсі.", label: "stub_qu_nicknames" }]
});

registerScript("stub_qu_nicknames", [
  { type: "show", who: "qu", zorder: 1 },
  { type: "say", who: "mc", text: "Привіт, Квінсі." },
  { type: "say", who: "qu", text: "Йоу, Марті. Чи пан Макфлай? Чи сер Петля?" },
  { type: "say", who: "mc", text: "Просто Марті." },
  { type: "say", who: "qu", text: "Нудно. Я буду називати тебе Петля. Без права оскарження." },
  { type: "end", text: "" }
]);
