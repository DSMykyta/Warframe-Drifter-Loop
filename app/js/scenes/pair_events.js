// ═══════════════════════════════════════════════════
// ПАРНІ ІВЕНТИ — BANTER
// ═══════════════════════════════════════════════════
//
// Порт з game/events/pairs/*.rpy
// 4 парні діалоги між NPC, тригеряться при вході в локацію.

// ─── Амір + Аоі: Комп'ютерний клуб ───

BANTER_ENTRIES.push({
  id: "amir_aoi_arcade",
  location: "comp_club",
  chars: ["Аоі", "Амір"],
  conditions: {
    flag_false: ["pair_amir_aoi_arcade_seen"]
  },
  priority: 2,
  label: "amir_aoi_arcade"
});

registerScript("amir_aoi_arcade", [
  {type: "say", who: "Амір", text: "Аоі! Один раунд. Я знайшов нову комбо."},
  {type: "say", who: "Аоі", text: "Твоя остання 'нова комбо' тривала дві секунди."},
  {type: "say", who: "Амір", text: "Ця — три! Прогрес!"},
  {type: "say", who: "Аоі", text: "...Добре. Один раунд."},
  {type: "say", who: null, text: "Через хвилину Амір програє."},
  {type: "say", who: "Амір", text: "Як. ЯК."},
  {type: "say", who: "Аоі", text: "Ти завжди атакуєш першим. Це передбачувано."},
  {type: "set_flag", flag: "pair_amir_aoi_arcade_seen"},
  {type: "end"}
]);


// ─── Аоі + Летті: Медпункт ───

BANTER_ENTRIES.push({
  id: "aoi_lettie_medbay",
  location: "medbay",
  chars: ["Аоі", "Летті"],
  conditions: {
    flag_false: ["pair_aoi_lettie_medbay_seen"]
  },
  priority: 2,
  label: "aoi_lettie_medbay"
});

registerScript("aoi_lettie_medbay", [
  {type: "say", who: "Аоі", text: "Летті. Я принесла чай."},
  {type: "say", who: "Летті", text: "Чай? Ти знаєш, що я п'ю тільки каву."},
  {type: "say", who: "Аоі", text: "Знаю. Тому принесла чай. Тобі потрібен сон, а не черговий кофеїн."},
  {type: "say", who: "Летті", text: "..."},
  {type: "say", who: "Летті", text: "Нахабна. Але... дякую."},
  {type: "say", who: "Аоі", text: "Будь ласка."},
  {type: "say", who: "Летті", text: "Тільки нікому не кажи, що я це випила."},
  {type: "set_flag", flag: "pair_aoi_lettie_medbay_seen"},
  {type: "end"}
]);


// ─── Артур + Квінсі: Дах ───

BANTER_ENTRIES.push({
  id: "arthur_quincy_rooftop",
  location: "rooftop",
  chars: ["Артур", "Квінсі"],
  conditions: {
    flag_false: ["pair_arthur_quincy_rooftop_seen"]
  },
  priority: 2,
  label: "arthur_quincy_rooftop"
});

registerScript("arthur_quincy_rooftop", [
  {type: "say", who: "Артур", text: "Квінсі. Доповідай по периметру."},
  {type: "say", who: "Квінсі", text: "Чисто. Як завжди. Ти щоразу питаєш."},
  {type: "say", who: "Артур", text: "І буду питати. Це протокол."},
  {type: "say", who: "Квінсі", text: "Протокол для загону з шести людей у покинутому молі?"},
  {type: "say", who: "Артур", text: "Особливо для загону з шести людей у покинутому молі."},
  {type: "say", who: "Квінсі", text: "...Справедливо."},
  {type: "set_flag", flag: "pair_arthur_quincy_rooftop_seen"},
  {type: "end"}
]);


// ─── Елеонор + Летті: Інфо-кімната ───

BANTER_ENTRIES.push({
  id: "eleanor_lettie_info",
  location: "security_desk",
  chars: ["Елеонор", "Летті"],
  conditions: {
    flag_false: ["pair_eleanor_lettie_info_seen"]
  },
  priority: 2,
  label: "eleanor_lettie_info"
});

registerScript("eleanor_lettie_info", [
  {type: "say", who: "Елеонор", text: "Летті, у мене питання. Суто професійне."},
  {type: "say", who: "Летті", text: "Якщо про здоров'я — прийди в медпункт. Якщо про щось інше — я не зацікавлена."},
  {type: "say", who: "Елеонор", text: "Про записи. Ти ведеш медичний журнал?"},
  {type: "say", who: "Летті", text: "Так. Чому?"},
  {type: "say", who: "Елеонор", text: "Мені цікаво порівняти наші нотатки. Я бачу закономірності у поведінці людей, ти — у їхньому здоров'ї."},
  {type: "say", who: "Летті", text: "Хочеш сказати, що поведінка і здоров'я пов'язані? Яке відкриття."},
  {type: "say", who: "Елеонор", text: "Хочу сказати, що разом ми побачимо більше."},
  {type: "say", who: "Летті", text: "...Може. Поговоримо пізніше."},
  {type: "set_flag", flag: "pair_eleanor_lettie_info_seen"},
  {type: "end"}
]);
