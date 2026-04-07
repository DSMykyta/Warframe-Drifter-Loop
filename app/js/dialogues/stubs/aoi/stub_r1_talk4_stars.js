// Stub: Аоі — stars
DIALOGUE_ENTRIES.push({
  id: "stub_ao_stars",
  who: "Аоі",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Дивишся на зорі?", label: "stub_ao_stars" }]
});

registerScript("stub_ao_stars", [
  { type: "show", who: "ao", zorder: 1 },
  { type: "say", who: "mc", text: "Дивишся на зорі?" },
  { type: "say", who: "ao", text: "Так! Ось та, яскрава — це Вега. З сузір'я Ліри." },
  { type: "say", who: "ao", text: "Ліра — це музичний інструмент. Значить, навіть космос любить музику." },
  { type: "say", who: "mc", text: "Або це просто назва." },
  { type: "say", who: "ao", text: "Не руйнуй магію!" },
  { type: "end", text: "" }
]);
