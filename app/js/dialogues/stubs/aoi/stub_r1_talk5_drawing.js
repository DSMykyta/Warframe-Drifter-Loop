// Stub: Аоі — drawing
DIALOGUE_ENTRIES.push({
  id: "stub_ao_drawing",
  who: "Аоі",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Що малюєш?", label: "stub_ao_drawing" }]
});

registerScript("stub_ao_drawing", [
  { type: "show", who: "ao", zorder: 1 },
  { type: "say", who: "mc", text: "Що малюєш?" },
  { type: "say", who: "ao", text: "Нас! Увесь Гекс. У стилі чібі." },
  { type: "say", who: "ao", text: "Артур вийшов трошки сердитий, але це ж точно." },
  { type: "say", who: "mc", text: "А я там є?" },
  { type: "say", who: "ao", text: "Звісно! Ти в центрі. З великими очима." },
  { type: "end", text: "" }
]);
