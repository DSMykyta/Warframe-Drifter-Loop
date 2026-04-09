// Stub: Артур — silence
DIALOGUE_ENTRIES.push({
  id: "stub_ar_silence",
  who: "ar",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Все тихо сьогодні.", label: "stub_ar_silence" }]
});

registerScript("stub_ar_silence", [
  { type: "show", who: "ar", zorder: 1 },
  { type: "say", who: "mc", text: "Все тихо сьогодні." },
  { type: "say", who: "ar", text: "Тиша — це добре." },
  { type: "say", who: "ar", text: "Коли тихо — значить ніхто не помирає." },
  { type: "say", who: "ar", text: "Поки що." },
  { type: "end", text: "" }
]);
