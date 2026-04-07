// ═══════════════════════════════════════════════════
// ЛЕТТІ — ІНТРО: Травми, медвідділ, щури
// Порт з game/dialogues/lettie/lettie_intro.rpy
// ═══════════════════════════════════════════════════

DIALOGUE_ENTRIES.push({
  id: "lettie_intro",
  who: "Летті",
  conditions: { flag_false: ["lettie_intro_done"] },
  priority: 90,
  chance: 100,
  titles: [
    { text: "Привіт, Летті.", label: "lettie_intro_main" }
  ]
});

registerScript("lettie_intro_main", [
  { type: "show", who: "lt", zorder: 1 },
  { type: "say", who: "mc", text: "Привіт, Летті." },
  { type: "say", who: "lt", text: "Ага." },
  { type: "say", who: "mc", text: "..." },
  { type: "say", who: "lt", text: "Шо стоїш? Якщо прийшов — сідай. Якщо ні — не заважай." },

  { type: "menu", choices: [
    { text: "Сідаю.", label: "lettie_sit" },
    { text: "Я на хвилинку.", label: "lettie_minute" }
  ]},

  { type: "label", id: "lettie_sit" },
  { type: "say", who: "mc", text: "Сідаю." },
  { type: "say", who: "lt", text: "Ну от і добре." },
  { type: "chemistry", who: "lt", amount: 2 },
  { type: "jump", to: "lettie_medbay" },

  { type: "label", id: "lettie_minute" },
  { type: "say", who: "mc", text: "Я тільки на хвилинку." },
  { type: "say", who: "lt", text: "Тут всі «на хвилинку». А потім я їх зшиваю." },

  { type: "label", id: "lettie_medbay" },
  { type: "say", who: "lt", text: "Слухай, babas. Раз ти тут — давай одразу." },
  { type: "say", who: "lt", text: "Бачиш це?" },
  { type: "say", who: "lt", text: "Це медвідділ. Мій медвідділ. Тут я лікую людей." },
  { type: "say", who: "lt", text: "І тебе, коли накосячиш на місії." },
  { type: "say", who: "mc", text: "Коли?" },
  { type: "say", who: "lt", text: "Не «якщо». Коли. Повір." },
  { type: "say", who: "lt", text: "На місіях є шанс отримати травму. І ти, і напарник." },
  { type: "say", who: "lt", text: "Травми — це стаки. Один стак — подряпини. Два — серйозно. Три..." },
  { type: "say", who: "lt", text: "...три і ти лежиш тут, а я вирішую чи зможу тебе зібрати." },

  { type: "menu", choices: [
    { text: "Як уникнути травм?", label: "lettie_avoid" },
    { text: "А якщо вже поранився?", label: "lettie_heal" }
  ]},

  { type: "label", id: "lettie_avoid" },
  { type: "say", who: "mc", text: "Є спосіб уникнути?" },
  { type: "say", who: "lt", text: "Si. Бери мене з собою." },
  { type: "say", who: "lt", text: "Коли я на місії — шанс травми нуль. Для всіх." },
  { type: "say", who: "mc", text: "Серйозно?" },
  { type: "say", who: "lt", text: "Я не жартую про медицину, babas. Ніколи." },
  { type: "chemistry", who: "lt", amount: 4 },
  { type: "jump", to: "lettie_extra" },

  { type: "label", id: "lettie_heal" },
  { type: "say", who: "mc", text: "А якщо вже отримав травму?" },
  { type: "say", who: "lt", text: "Приходь сюди. Я зніму один стак. Раз на день." },
  { type: "say", who: "lt", text: "Або чекай — стаки проходять самі через два дні. Якщо не додаш нових." },
  { type: "chemistry", who: "lt", amount: 2 },

  { type: "label", id: "lettie_extra" },
  { type: "say", who: "lt", text: "І ще." },
  { type: "say", who: "lt", text: "Чим більше місій з одним напарником за день — тим вище шанс травми." },
  { type: "say", who: "lt", text: "Не перепрацьовуй людей. Вони не залізні." },
  { type: "say", who: "lt", text: "Ну... більшість не залізні." },
  { type: "say", who: "mc", text: "А хто залізний?" },
  { type: "say", who: "lt", text: "Квінсі. Буквально. Але це не привід." },
  { type: "chemistry", who: "lt", amount: 2 },

  { type: "say", who: "lt", text: "А тепер..." },
  { type: "say", who: "lt", text: "Познайомся з Анітою." },
  { type: "say", who: "mc", text: "З ким?" },
  { type: "say", who: "lt", text: "Аніта. Моя нова corazoncito." },
  { type: "say", who: "lt", text: "Вона ще маленька. Але вже з характером." },

  { type: "menu", choices: [
    { text: "Вона мила.", label: "lettie_rat_1" },
    { text: "Ти тримаєш щура в медвідділі?", label: "lettie_rat_2" },
    { text: "В мене алергія.", label: "lettie_rat_3" }
  ]},

  { type: "label", id: "lettie_rat_1" },
  { type: "say", who: "mc", text: "Вона мила." },
  { type: "say", who: "lt", text: "Не кажи їй це. В неї зірковий синдром і так." },
  { type: "chemistry", who: "lt", amount: 4 },
  { type: "jump", to: "lettie_intro_end" },

  { type: "label", id: "lettie_rat_2" },
  { type: "say", who: "mc", text: "Ти тримаєш щура в медвідділі? Поруч з пацієнтами?" },
  { type: "say", who: "lt", text: "Аніта стерильніша за більшість пацієнтів, babas." },
  { type: "say", who: "lt", text: "І точно приємніша." },
  { type: "chemistry", who: "lt", amount: 2 },
  { type: "jump", to: "lettie_intro_end" },

  { type: "label", id: "lettie_rat_3" },
  { type: "say", who: "mc", text: "В мене алергія на щурів." },
  { type: "say", who: "lt", text: "Ні в тебе нема." },
  { type: "say", who: "mc", text: "Звідки ти знаєш?" },
  { type: "say", who: "lt", text: "Я медик. Я знаю." },

  { type: "label", id: "lettie_intro_end" },
  { type: "set_flag", flag: "lettie_intro_done" },

  // Якщо немає пейджера — направити до Аміра
  { type: "if", flag: "has_pager", jump: "lettie_intro_done_final" },
  { type: "say", who: "lt", text: "І ще, babas." },
  { type: "say", who: "lt", text: "Іди до Аміра. Аркади. Він дасть тобі пейджер." },
  { type: "say", who: "lt", text: "Без нього тут як без рук. Буквально." },
  { type: "label", id: "lettie_intro_done_final" },
  { type: "end", text: "" }
]);
