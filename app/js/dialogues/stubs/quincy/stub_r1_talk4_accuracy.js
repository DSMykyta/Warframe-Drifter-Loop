// Stub: Квінсі — accuracy
DIALOGUE_ENTRIES.push({
  id: "stub_qu_accuracy",
  who: "qu",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Як влучність?", label: "stub_qu_accuracy" }]
});

registerScript("stub_qu_accuracy", [
  { type: "show", who: "qu", zorder: 1 },
  { type: "say", who: "mc", text: "Як влучність?" },
  { type: "say", who: "qu", text: "Сто відсотків. Як завжди." },
  { type: "say", who: "mc", text: "Серйозно?" },
  { type: "say", who: "qu", text: "Ну, якщо не рахувати ті рази, коли я промазав. Але ті не рахуються." },
  { type: "end", text: "" }
]);
