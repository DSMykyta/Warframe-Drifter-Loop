// Stub: Елеонор — observations
DIALOGUE_ENTRIES.push({
  id: "stub_el_observations",
  who: "el",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Про що думаєш?", label: "stub_el_observations" }]
});

registerScript("stub_el_observations", [
  { type: "show", who: "el", zorder: 1 },
  { type: "say", who: "mc", text: "Про що думаєш?" },
  { type: "telepathy", text: "Про те, як люди ходять. У кожного свій ритм." },
  { type: "telepathy", text: "Артур марширує. Квінсі тинається. Аоі стрибає." },
  { type: "telepathy", text: "А ти ходиш так, ніби земля під тобою може зникнути." },
  { type: "telepathy", text: "Це спостереження, не діагноз." },
  { type: "end", text: "" }
]);
