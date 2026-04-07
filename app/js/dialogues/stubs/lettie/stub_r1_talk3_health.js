// Stub: Летті — health
DIALOGUE_ENTRIES.push({
  id: "stub_lt_health",
  who: "Летті",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Як моє здоров'я?", label: "stub_lt_health" }]
});

registerScript("stub_lt_health", [
  { type: "show", who: "lt", zorder: 1 },
  { type: "say", who: "mc", text: "Як моє здоров'я?" },
  { type: "say", who: "lt", text: "Живий. Це вже непогано за нашими стандартами." },
  { type: "say", who: "lt", text: "Їж нормально, спи більше, не лізь куди не просять." },
  { type: "say", who: "mc", text: "Це медична порада?" },
  { type: "say", who: "lt", text: "Це наказ, corazoncito." },
  { type: "end", text: "" }
]);
