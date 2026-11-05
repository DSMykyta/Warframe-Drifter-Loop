// Stub: Аоі — bubble tea
DIALOGUE_ENTRIES.push({
  id: "stub_ao_bubbletea",
  who: "ao",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Знову бабл-ті?", label: "stub_ao_bubbletea" }]
});

registerScript("stub_ao_bubbletea", [
  { type: "show", who: "ao", zorder: 1 },
  { type: "say", who: "mc", text: "Знову бабл-ті?" },
  { type: "say", who: "ao", text: "Тут є автомат! Таро зі смаком манго!" },
  { type: "say", who: "ao", text: "Летті каже, що це суцільний цукор і я зіпсую зуби." },
  { type: "say", who: "ao", text: "Але щастя важливіше за зуби." },
  { type: "end", text: "" }
]);
