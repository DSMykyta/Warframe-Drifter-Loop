// Stub: Амір — future tech
DIALOGUE_ENTRIES.push({
  id: "stub_am_futuretech",
  who: "am",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Знову про майбутнє?", label: "stub_am_futuretech" }]
});

registerScript("stub_am_futuretech", [
  { type: "show", who: "am", zorder: 1 },
  { type: "say", who: "mc", text: "Знову про майбутнє?" },
  { type: "say", who: "am", text: "Марті, скажи чесно. У вас там є літаючі дошки?" },
  { type: "say", who: "mc", text: "Ні." },
  { type: "say", who: "am", text: "Майбутнє офіційно розчарувало мене." },
  { type: "end", text: "" }
]);
