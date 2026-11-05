// Stub: Летті — supplies
DIALOGUE_ENTRIES.push({
  id: "stub_lt_supplies",
  who: "lt",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Вистачає медикаментів?", label: "stub_lt_supplies" }]
});

registerScript("stub_lt_supplies", [
  { type: "show", who: "lt", zorder: 1 },
  { type: "say", who: "mc", text: "Вистачає медикаментів?" },
  { type: "say", who: "lt", text: "Ніколи не вистачає. Це закон медицини." },
  { type: "say", who: "lt", text: "Бинти закінчуються, антисептик на донці, аспірин — на вагу золота." },
  { type: "say", who: "lt", text: "Але поки руки є — працюємо. Si?" },
  { type: "end", text: "" }
]);
