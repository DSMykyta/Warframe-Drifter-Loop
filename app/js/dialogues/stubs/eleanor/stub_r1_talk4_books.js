// Stub: Елеонор — books
DIALOGUE_ENTRIES.push({
  id: "stub_el_books",
  who: "Елеонор",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Що читаєш?", label: "stub_el_books" }]
});

registerScript("stub_el_books", [
  { type: "show", who: "el", zorder: 1 },
  { type: "say", who: "mc", text: "Що читаєш?" },
  { type: "say", who: "el", text: "Камю. Знову." },
  { type: "say", who: "el", text: "Є щось заспокійливе в тому, коли хтось написав про абсурд краще за тебе." },
  { type: "telepathy", text: "Означає, що ти не одна це бачиш." },
  { type: "say", who: "el", text: "Раджу спробувати. Хоча б для настрою." },
  { type: "end", text: "" }
]);
