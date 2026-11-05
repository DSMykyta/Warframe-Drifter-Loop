// Stub: Квінсі — trolling
DIALOGUE_ENTRIES.push({
  id: "stub_qu_trolling",
  who: "qu",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Що ти знову зробив?", label: "stub_qu_trolling" }]
});

registerScript("stub_qu_trolling", [
  { type: "show", who: "qu", zorder: 1 },
  { type: "say", who: "mc", text: "Що ти знову зробив?" },
  { type: "say", who: "qu", text: "Я? Нічого. Взагалі нічого." },
  { type: "say", who: "qu", text: "Ну хіба що переставив усі чашки Артура дном догори." },
  { type: "say", who: "qu", text: "Але це арт. Він не оцінить, але нащадки запам'ятають." },
  { type: "end", text: "" }
]);
