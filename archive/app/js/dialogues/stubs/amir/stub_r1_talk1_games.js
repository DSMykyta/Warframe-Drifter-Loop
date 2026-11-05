// Stub: Амір — games
DIALOGUE_ENTRIES.push({
  id: "stub_am_games",
  who: "am",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Що граєш?", label: "stub_am_games" }]
});

registerScript("stub_am_games", [
  { type: "show", who: "am", zorder: 1 },
  { type: "say", who: "mc", text: "Що граєш?" },
  { type: "say", who: "am", text: "О! Знайшов старий картридж з Contra!" },
  { type: "say", who: "am", text: "Тридцять життів і я все одно помираю на третьому рівні." },
  { type: "say", who: "am", text: "Це як метафора мого життя, тільки з піксельними вибухами." },
  { type: "end", text: "" }
]);
