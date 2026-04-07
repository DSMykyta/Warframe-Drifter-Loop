// Stub: Аоі — origami
DIALOGUE_ENTRIES.push({
  id: "stub_ao_origami",
  who: "Аоі",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Що складаєш?", label: "stub_ao_origami" }]
});

registerScript("stub_ao_origami", [
  { type: "show", who: "ao", zorder: 1 },
  { type: "say", who: "mc", text: "Що складаєш?" },
  { type: "say", who: "ao", text: "Журавлика! Кажуть, якщо скласти тисячу — збудеться бажання." },
  { type: "say", who: "mc", text: "Скільки вже?" },
  { type: "say", who: "ao", text: "Сім. Але я вірю в процес!" },
  { type: "end", text: "" }
]);
