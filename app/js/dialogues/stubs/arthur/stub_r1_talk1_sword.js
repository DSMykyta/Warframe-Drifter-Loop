// Stub: Артур — sword cleaning
DIALOGUE_ENTRIES.push({
  id: "stub_ar_sword",
  who: "Артур",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Чистиш меч?", label: "stub_ar_sword" }]
});

registerScript("stub_ar_sword", [
  { type: "show", who: "ar", zorder: 1 },
  { type: "say", who: "mc", text: "Чистиш меч?" },
  { type: "say", who: "ar", text: "Щодня. Без винятків." },
  { type: "say", who: "ar", text: "Зброя, яку не доглядають, підводить в найгірший момент." },
  { type: "say", who: "ar", text: "Як і люди." },
  { type: "end", text: "" }
]);
