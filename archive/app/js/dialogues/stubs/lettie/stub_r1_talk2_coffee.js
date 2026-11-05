// Stub: Летті — coffee
DIALOGUE_ENTRIES.push({
  id: "stub_lt_coffee",
  who: "lt",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Кава?", label: "stub_lt_coffee" }]
});

registerScript("stub_lt_coffee", [
  { type: "show", who: "lt", zorder: 1 },
  { type: "say", who: "mc", text: "Кава?" },
  { type: "say", who: "lt", text: "Четверта за сьогодні. Si, я рахую." },
  { type: "say", who: "lt", text: "Не дивись на мене так. Я медик, я знаю норму." },
  { type: "say", who: "lt", text: "Норма — стільки, скільки мені треба щоб не вбити когось." },
  { type: "end", text: "" }
]);
