// Stub: Амір — electronics
DIALOGUE_ENTRIES.push({
  id: "stub_am_electronics",
  who: "Амір",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Що паяєш?", label: "stub_am_electronics" }]
});

registerScript("stub_am_electronics", [
  { type: "show", who: "am", zorder: 1 },
  { type: "say", who: "mc", text: "Що паяєш?" },
  { type: "say", who: "am", text: "Намагаюсь зробити з цього FM-приймача щось корисне." },
  { type: "say", who: "am", text: "Поки що ловить тільки статику і чиєсь радіо з кумбією." },
  { type: "say", who: "mc", text: "Може, залиш кумбію." },
  { type: "say", who: "am", text: "Знаєш що? Ти маєш рацію." },
  { type: "end", text: "" }
]);
