// Stub: Артур — cooking
DIALOGUE_ENTRIES.push({
  id: "stub_ar_cooking",
  who: "Артур",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Щось готуєш?", label: "stub_ar_cooking" }]
});

registerScript("stub_ar_cooking", [
  { type: "show", who: "ar", zorder: 1 },
  { type: "say", who: "mc", text: "Щось готуєш?" },
  { type: "say", who: "ar", text: "Рис. Рис завжди працює." },
  { type: "say", who: "ar", text: "Не потребує фантазії. Потребує дисципліну." },
  { type: "say", who: "mc", text: "Звучить як ти." },
  { type: "say", who: "ar", text: "Саме так." },
  { type: "end", text: "" }
]);
