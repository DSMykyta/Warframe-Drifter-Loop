// Stub: Артур — discipline
DIALOGUE_ENTRIES.push({
  id: "stub_ar_discipline",
  who: "Артур",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Як справи, командире?", label: "stub_ar_discipline" }]
});

registerScript("stub_ar_discipline", [
  { type: "show", who: "ar", zorder: 1 },
  { type: "say", who: "mc", text: "Як справи, командире?" },
  { type: "say", who: "ar", text: "Справи є завжди. Питання — чи ти до них готовий." },
  { type: "say", who: "ar", text: "Не стій без діла. Знайди чим зайнятися." },
  { type: "end", text: "" }
]);
