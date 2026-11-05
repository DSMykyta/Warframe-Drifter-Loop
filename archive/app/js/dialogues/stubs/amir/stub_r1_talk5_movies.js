// Stub: Амір — movies
DIALOGUE_ENTRIES.push({
  id: "stub_am_movies",
  who: "am",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Що дивишся?", label: "stub_am_movies" }]
});

registerScript("stub_am_movies", [
  { type: "show", who: "am", zorder: 1 },
  { type: "say", who: "mc", text: "Що дивишся?" },
  { type: "say", who: "am", text: "Термінатор 2. Вчетверте цього тижня." },
  { type: "say", who: "am", text: "Кожного разу помічаю нову деталь. Це ГЕНІАЛЬНО." },
  { type: "say", who: "mc", text: "Може, спробуєш щось нове?" },
  { type: "say", who: "am", text: "Навіщо? Досконалість не потребує замін." },
  { type: "end", text: "" }
]);
