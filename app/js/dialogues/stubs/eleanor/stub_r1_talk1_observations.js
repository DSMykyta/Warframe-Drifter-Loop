// Stub: Елеонор — observations
DIALOGUE_ENTRIES.push({
  id: "stub_el_observations",
  who: "Елеонор",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Про що думаєш?", label: "stub_el_observations" }]
});

registerScript("stub_el_observations", [
  { type: "show", who: "el", zorder: 1 },
  { type: "say", who: "mc", text: "Про що думаєш?" },
  { type: "say", who: "el", text: "Про те, як люди ходять. У кожного свій ритм." },
  { type: "say", who: "el", text: "Артур марширує. Квінсі тинається. Аоі стрибає." },
  { type: "telepathy", text: "А ти ходиш так, ніби земля під тобою може зникнути." },
  { type: "say", who: "el", text: "Це спостереження, не діагноз." },
  { type: "end", text: "" }
]);
