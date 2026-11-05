// Stub: Аоі — music
DIALOGUE_ENTRIES.push({
  id: "stub_ao_music",
  who: "ao",
  conditions: {},
  priority: 1,
  chance: 100,
  titles: [{ text: "Що слухаєш?", label: "stub_ao_music" }]
});

registerScript("stub_ao_music", [
  { type: "show", who: "ao", zorder: 1 },
  { type: "say", who: "mc", text: "Що слухаєш?" },
  { type: "say", who: "ao", text: "Новий дист! Називається On-lyne. Японський синтпоп!" },
  { type: "say", who: "ao", text: "Така мелодія, що хочеться танцювати прямо тут." },
  { type: "say", who: "mc", text: "Тут коридор." },
  { type: "say", who: "ao", text: "Коридор — це сцена для тих, хто не боїться!" },
  { type: "end", text: "" }
]);
