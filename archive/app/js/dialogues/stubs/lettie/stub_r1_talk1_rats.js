// Stub: Летті — rats
DIALOGUE_ENTRIES.push({
  id: "stub_lt_rats",
  who: "lt",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Знову щури?", label: "stub_lt_rats" }]
});

registerScript("stub_lt_rats", [
  { type: "show", who: "lt", zorder: 1 },
  { type: "say", who: "mc", text: "Знову щури?" },
  { type: "say", who: "lt", text: "Babas вилізли з вентиляції. Треті за тиждень." },
  { type: "say", who: "lt", text: "Я поставила пастки, але ці розумніші за половину Гексу." },
  { type: "say", who: "mc", text: "За половину?" },
  { type: "say", who: "lt", text: "Я сказала що сказала." },
  { type: "end", text: "" }
]);
