// Stub: Летті — patients
DIALOGUE_ENTRIES.push({
  id: "stub_lt_patients",
  who: "lt",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Багато пацієнтів?", label: "stub_lt_patients" }]
});

registerScript("stub_lt_patients", [
  { type: "show", who: "lt", zorder: 1 },
  { type: "say", who: "mc", text: "Багато пацієнтів?" },
  { type: "say", who: "lt", text: "Квінсі приходив з подряпиною і просив знеболююче." },
  { type: "say", who: "lt", text: "Я дала йому пластир і сказала не бути babas." },
  { type: "say", who: "lt", text: "Він образився. Це означає, що він здоровий." },
  { type: "end", text: "" }
]);
