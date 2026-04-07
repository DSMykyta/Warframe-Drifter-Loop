// ═══════════════════════════════════════════════════
// ЕЛЕОНОР — ІНТРО: Телепатія, філософія, журналістика
// Порт з game/dialogues/eleanor/eleanor_intro.rpy
// ═══════════════════════════════════════════════════

DIALOGUE_ENTRIES.push({
  id: "eleanor_intro",
  who: "Елеонор",
  conditions: { flag_false: ["eleanor_intro_done"] },
  priority: 90,
  chance: 100,
  titles: [
    { text: "Привіт, Елеонор.", label: "eleanor_intro_main" }
  ]
});

registerScript("eleanor_intro_main", [
  { type: "show", who: "el", zorder: 1 },
  { type: "say", who: "mc", text: "Привіт, Елеонор." },
  { type: "say", who: "el", text: "А." },
  { type: "say", who: "el", text: "Привіт." },
  { type: "say", who: "el", text: "Ти знаєш, є щось надзвичайно кумедне в тому, як ти підходиш до людей." },
  { type: "say", who: "el", text: "Ти кажеш «привіт» так, ніби це слово ще щось означає." },
  { type: "say", who: "el", text: "Ніби воно не було зношене до діри мільярдами ротів до тебе." },
  { type: "say", who: "el", text: "І це, як не дивно, — зворушливо." },
  { type: "say", who: "el", text: "Бо ти кажеш його щиро. Без задньої думки. Без стратегії." },
  { type: "say", who: "el", text: "Просто — «привіт». Як дитина, яка ще вірить що цього достатньо." },
  { type: "telepathy", text: "Можливо, це й достатньо." },
  { type: "say", who: "el", text: "Вибач. Я маю звичку думати вголос." },
  { type: "say", who: "el", text: "Точніше — думати В ТЕБЕ вголос. Це інша річ." },

  { type: "menu", choices: [
    { text: "Що це було?", label: "el_what" },
    { text: "Телепатія. Артур згадував.", label: "el_knew" },
    { text: "[Просто слухати.]", label: "el_silent" }
  ]},

  { type: "label", id: "el_what" },
  { type: "say", who: "mc", text: "Що це щойно було? Я почув тебе... але ти не говорила." },
  { type: "say", who: "el", text: "Телепатія. Спасибі Техроту." },
  { type: "say", who: "el", text: "Він пожирає моє тіло. Повільно, з апетитом. Але натомість дав мені доступ до найцікавішого органу з усіх — чужого мозку." },
  { type: "say", who: "el", text: "Не хвилюйся. Я не читаю думки без запрошення." },
  { type: "say", who: "el", text: "Ну... майже без запрошення." },
  { type: "chemistry", who: "el", amount: 2 },
  { type: "jump", to: "el_explain" },

  { type: "label", id: "el_knew" },
  { type: "say", who: "mc", text: "Телепатія. Артур щось казав." },
  { type: "say", who: "el", text: "Артур багато про що каже. Переважно — наказовим тоном." },
  { type: "say", who: "el", text: "Але так. Це мій маленький талант. Або прокляття. Залежить від ракурсу." },
  { type: "chemistry", who: "el", amount: 2 },
  { type: "jump", to: "el_explain" },

  { type: "label", id: "el_silent" },
  { type: "say", who: "el", text: "Мовчиш. Цікаво." },
  { type: "telepathy", text: "Мовчазні люди — найнебезпечніші. Вони слухають." },
  { type: "say", who: "el", text: "Мені це подобається." },
  { type: "chemistry", who: "el", amount: 4 },

  { type: "label", id: "el_explain" },
  { type: "say", who: "el", text: "Дозволь мені пояснити одну річ." },
  { type: "say", who: "el", text: "Більшість людей тут спілкуються як люди. Рот, звуки, повітря." },
  { type: "say", who: "el", text: "Це неефективно. Неточно. Повно шуму." },
  { type: "say", who: "el", text: "Коли ти говориш словами — ти редагуєш. Обираєш що сказати, що приховати." },
  { type: "say", who: "el", text: "Це мистецтво. Я поважаю це мистецтво. Я сама була журналісткою." },
  { type: "say", who: "el", text: "Але телепатія — це інше." },
  { type: "telepathy", text: "Це — чесність. Без фільтрів. Без масок." },
  { type: "telepathy", text: "Коли я говорю так — ти чуєш мене справжню." },
  { type: "say", who: "el", text: "Я не завжди буду говорити так. Це стомлює. І лякає людей." },
  { type: "say", who: "el", text: "Але іноді — коли мені захочеться бути чесною — ти почуєш хвилі." },
  { type: "say", who: "el", text: "І тоді — слухай уважно. Бо те, що я кажу хвилями, я більше не повторю словами." },

  { type: "menu", choices: [
    { text: "Ти довіряєш мені настільки?", label: "el_trust" },
    { text: "Яка ти була як журналістка?", label: "el_journalist" },
    { text: "Це лякає.", label: "el_scary" }
  ]},

  { type: "label", id: "el_trust" },
  { type: "say", who: "mc", text: "Ти довіряєш мені настільки? Ми ж щойно познайомились." },
  { type: "say", who: "el", text: "Довіра — це не часова функція. Це відчуття." },
  { type: "say", who: "el", text: "Я подивилась в тебе під час допиту. Коли Артур тримав меч біля твого горла." },
  { type: "say", who: "el", text: "І побачила когось, хто помирав стільки разів, що перестав боятися." },
  { type: "telepathy", text: "Це або мужність, або божевілля." },
  { type: "telepathy", text: "І те, і те мене цікавить." },
  { type: "chemistry", who: "el", amount: 4 },
  { type: "jump", to: "el_end" },

  { type: "label", id: "el_journalist" },
  { type: "say", who: "mc", text: "Журналістка? Де?" },
  { type: "say", who: "el", text: "О, скрізь. Де є несправедливість — там є історія. Де є історія — там була я." },
  { type: "say", who: "el", text: "Я писала про людей, які ховаються за владою." },
  { type: "say", who: "el", text: "А потім прийшов Техрот. І я стала однією з тих, про кого пишуть." },
  { type: "say", who: "el", text: "Іронія — моя улюблена літературна форма." },
  { type: "chemistry", who: "el", amount: 2 },
  { type: "jump", to: "el_end" },

  { type: "label", id: "el_scary" },
  { type: "say", who: "mc", text: "Чесно? Це трохи лякає." },
  { type: "say", who: "el", text: "Звісно, що лякає. Хтось говорить тобі в голову. Це має лякати." },
  { type: "say", who: "el", text: "Але подумай — що страшніше: голос, який ти чуєш, чи думки, яких не чуєш?" },
  { type: "say", who: "el", text: "Я хоча б чесна зі своїми." },
  { type: "chemistry", who: "el", amount: 2 },

  { type: "label", id: "el_end" },
  { type: "say", who: "el", text: "Марті." },
  { type: "say", who: "mc", text: "Так?" },
  { type: "say", who: "el", text: "Ми ще будемо розмовляти. Багато." },
  { type: "say", who: "el", text: "Я бачу в тобі щось... неспокійне. Як дзеркало, в якому відображення рухається окремо від тебе." },
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
