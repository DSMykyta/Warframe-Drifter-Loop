// Stub: Елеонор — writing
DIALOGUE_ENTRIES.push({
  id: "stub_el_writing",
  who: "Елеонор",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Знову пишеш?", label: "stub_el_writing" }]
});

registerScript("stub_el_writing", [
  { type: "show", who: "el", zorder: 1 },
  { type: "say", who: "mc", text: "Знову пишеш?" },
  { type: "say", who: "el", text: "Записую. Не плутай." },
  { type: "say", who: "el", text: "Письменник вигадує. Журналіст фіксує. Я — фіксую." },
  { type: "say", who: "el", text: "Хтось має пам'ятати те, що відбувається тут. Навіть якщо ніхто не прочитає." },
  { type: "end", text: "" }
]);
