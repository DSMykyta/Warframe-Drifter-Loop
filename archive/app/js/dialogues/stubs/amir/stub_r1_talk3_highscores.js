// Stub: Амір — high scores
DIALOGUE_ENTRIES.push({
  id: "stub_am_highscores",
  who: "am",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Новий рекорд?", label: "stub_am_highscores" }]
});

registerScript("stub_am_highscores", [
  { type: "show", who: "am", zorder: 1 },
  { type: "say", who: "mc", text: "Новий рекорд?" },
  { type: "say", who: "am", text: "МАЙЖЕ. Був на сьомому рівні, і тут Квінсі смикнув шнур з розетки." },
  { type: "say", who: "am", text: "Каже, випадково. АГА. ВИПАДКОВО." },
  { type: "say", who: "am", text: "Я йому цього ніколи не забуду." },
  { type: "end", text: "" }
]);
