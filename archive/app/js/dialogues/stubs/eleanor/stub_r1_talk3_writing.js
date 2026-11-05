// Stub: Елеонор — writing
DIALOGUE_ENTRIES.push({
  id: "stub_el_writing",
  who: "el",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Знову пишеш?", label: "stub_el_writing" }]
});

registerScript("stub_el_writing", [
  { type: "show", who: "el", zorder: 1 },
  { type: "say", who: "mc", text: "Знову пишеш?" },
  { type: "telepathy", text: "Записую. Не плутай." },
  { type: "telepathy", text: "Письменник вигадує. Журналіст фіксує. Я — фіксую." },
  { type: "telepathy", text: "Хтось має пам'ятати те, що відбувається тут. Навіть якщо ніхто не прочитає." },
  { type: "end", text: "" }
]);
