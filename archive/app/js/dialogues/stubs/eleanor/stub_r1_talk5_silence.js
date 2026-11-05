// Stub: Елеонор — silence
DIALOGUE_ENTRIES.push({
  id: "stub_el_silence",
  who: "el",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Можна просто посидіти?", label: "stub_el_silence" }]
});

registerScript("stub_el_silence", [
  { type: "show", who: "el", zorder: 1 },
  { type: "say", who: "mc", text: "Можна просто посидіти?" },
  { type: "telepathy", text: "Можна." },
  { type: "telepathy", text: "Дякую, що не питаєш як справи." },
  { type: "telepathy", text: "...Посидь." },
  { type: "end", text: "" }
]);
