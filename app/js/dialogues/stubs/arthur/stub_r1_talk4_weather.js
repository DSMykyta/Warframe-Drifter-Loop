// Stub: Артур — weather
DIALOGUE_ENTRIES.push({
  id: "stub_ar_weather",
  who: "Артур",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Яка погода надворі?", label: "stub_ar_weather" }]
});

registerScript("stub_ar_weather", [
  { type: "show", who: "ar", zorder: 1 },
  { type: "say", who: "mc", text: "Яка погода надворі?" },
  { type: "say", who: "ar", text: "Вітер. Холодний." },
  { type: "say", who: "ar", text: "Непогано для патрулювання. Тримає в тонусі." },
  { type: "say", who: "mc", text: "А для відпочинку?" },
  { type: "say", who: "ar", text: "Відпочинок — це розкіш." },
  { type: "end", text: "" }
]);
