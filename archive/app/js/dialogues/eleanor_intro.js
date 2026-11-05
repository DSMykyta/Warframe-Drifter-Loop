// ═══════════════════════════════════════════════════
// ЕЛЕОНОР — ІНТРО: Телепатія, шок Дріфтера, журналістика
// Порт з game/dialogues/eleanor/eleanor_intro.rpy
// ═══════════════════════════════════════════════════
//
// Елеонор = Нікс. Техрот забрав їй голос.
// Вона НЕ МОЖЕ говорити — тільки телепатія.
// ВСІ її репліки = type: "telepathy"

DIALOGUE_ENTRIES.push({
  id: "eleanor_intro",
  who: "el",
  conditions: { flag_false: ["eleanor_intro_done"] },
  priority: 90,
  chance: 100,
  titles: [
    { text: "Привіт, Елеонор.", label: "eleanor_intro_main" }
  ]
});

registerScript("eleanor_intro_main", [
  { type: "show", who: "el", zorder: 1 },

  // Дріфтер підходить — Елеонор мовчить, дивиться
  { type: "say", who: "mc", text: "Привіт, Елеонор." },

  // Тиша. Вона не відповідає. Дріфтер чекає.
  { type: "say", who: "mc", text: "..." },

  // Раптом — голос в голові
  { type: "telepathy", text: "Привіт." },

  // Шок Дріфтера
  { type: "say", who: "mc", text: "Що..." },
  { type: "say", who: "mc", text: "Ти щойно... в моїй голові?" },

  { type: "telepathy", text: "Так. Вибач за незручність." },
  { type: "telepathy", text: "Я не можу говорити. Голос — перше що забрав Техрот." },
  { type: "telepathy", text: "Але натомість дав дещо інше." },

  { type: "say", who: "mc", text: "Телепатія." },

  { type: "telepathy", text: "Точніше — я думаю, а ти чуєш. Без фільтрів. Без масок." },
  { type: "telepathy", text: "Більшість людей це лякає." },

  { type: "menu", choices: [
    { text: "Це... незвично. Але не страшно.", label: "el_not_scary" },
    { text: "Чесно? Трохи лякає.", label: "el_scary" },
    { text: "[Мовчати. Просто слухати.]", label: "el_silent", chemistry: { "el": 4 } }
  ]},

  { type: "label", id: "el_not_scary" },
  { type: "say", who: "mc", text: "Це... незвично. Але не страшно." },
  { type: "telepathy", text: "Ти або хоробрий, або брешеш." },
  { type: "telepathy", text: "Обидва варіанти мене влаштовують." },
  { type: "chemistry", who: "el", amount: 2 },
  { type: "jump", to: "el_explain" },

  { type: "label", id: "el_scary" },
  { type: "say", who: "mc", text: "Чесно? Трохи лякає." },
  { type: "telepathy", text: "Звісно. Хтось говорить тобі в голову. Це має лякати." },
  { type: "telepathy", text: "Але подумай — що страшніше: голос, який ти чуєш, чи думки, яких не чуєш?" },
  { type: "chemistry", who: "el", amount: 2 },
  { type: "jump", to: "el_explain" },

  { type: "label", id: "el_silent" },
  { type: "telepathy", text: "Мовчиш." },
  { type: "telepathy", text: "Мовчазні люди — найнебезпечніші. Вони слухають." },
  { type: "telepathy", text: "Мені це подобається." },

  { type: "label", id: "el_explain" },
  { type: "telepathy", text: "Дозволь поясню." },
  { type: "telepathy", text: "Техрот пожирає моє тіло. Повільно. З апетитом." },
  { type: "telepathy", text: "Голос зник першим. Потім — відчуття в кінцівках." },
  { type: "telepathy", text: "Але натомість він дав мені доступ до найцікавішого органу — чужого мозку." },
  { type: "telepathy", text: "Не хвилюйся. Я не читаю думки без запрошення." },
  { type: "telepathy", text: "Ну... майже без запрошення." },

  { type: "say", who: "mc", text: "А раніше? До Техроту?" },

  { type: "telepathy", text: "Журналістка. Писала про людей, які ховаються за владою." },
  { type: "telepathy", text: "А потім прийшов Техрот. І я стала однією з тих, про кого пишуть." },

  { type: "menu", choices: [
    { text: "Ти довіряєш мені настільки?", label: "el_trust" },
    { text: "Як ти з цим живеш?", label: "el_cope" },
    { text: "Мені шкода.", label: "el_sorry" }
  ]},

  { type: "label", id: "el_trust" },
  { type: "say", who: "mc", text: "Ти довіряєш мені настільки? Ми ж щойно познайомились." },
  { type: "telepathy", text: "Довіра — це не часова функція. Це відчуття." },
  { type: "telepathy", text: "Я подивилась в тебе під час допиту. Коли Артур тримав меч біля твого горла." },
  { type: "telepathy", text: "І побачила когось, хто помирав стільки разів, що перестав боятися." },
  { type: "telepathy", text: "Це або мужність, або божевілля." },
  { type: "telepathy", text: "І те, і те мене цікавить." },
  { type: "chemistry", who: "el", amount: 4 },
  { type: "jump", to: "el_end" },

  { type: "label", id: "el_cope" },
  { type: "say", who: "mc", text: "Як ти з цим живеш? Без голосу, без..." },
  { type: "telepathy", text: "Без нормальності?" },
  { type: "telepathy", text: "Нормальність — це те, до чого звикли. Я звикла до цього." },
  { type: "telepathy", text: "І чесно? Слова завжди були неточними. Повними шуму." },
  { type: "telepathy", text: "Хвилі — чесніші." },
  { type: "chemistry", who: "el", amount: 2 },
  { type: "jump", to: "el_end" },

  { type: "label", id: "el_sorry" },
  { type: "say", who: "mc", text: "Мені шкода." },
  { type: "telepathy", text: "Не треба." },
  { type: "telepathy", text: "Жалість — це коли дивишся зверху вниз. А ти дивишся прямо." },
  { type: "telepathy", text: "Це рідкість." },
  { type: "chemistry", who: "el", amount: 2 },

  { type: "label", id: "el_end" },
  { type: "telepathy", text: "Марті." },
  { type: "say", who: "mc", text: "Так?" },
  { type: "telepathy", text: "Ми ще будемо розмовляти. Багато." },
  { type: "telepathy", text: "Я бачу в тобі щось неспокійне. Як дзеркало, в якому відображення рухається окремо від тебе." },
  { type: "telepathy", text: "Але про це потім." },
  { type: "telepathy", text: "Йди. В мене є над чим подумати." },

  { type: "set_flag", flag: "eleanor_intro_done" },

  // Якщо немає пейджера — направити до Аміра
  { type: "if", flag: "has_pager", jump: "eleanor_intro_done_final" },
  { type: "telepathy", text: "Ти ще без зв'язку." },
  { type: "telepathy", text: "Амір. Аркади. Він чекає на тебе." },
  { type: "label", id: "eleanor_intro_done_final" },
  { type: "end", text: "" }
]);
