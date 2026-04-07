// ═══════════════════════════════════════════════════
// АМІР — ІНТРО: Пейджер + туторіал + Марті
// Порт з game/dialogues/amir/amir_intro.rpy
// ═══════════════════════════════════════════════════

DIALOGUE_ENTRIES.push({
  id: "amir_intro",
  who: "Амір",
  conditions: { flag_false: ["amir_intro_done"] },
  priority: 90,
  chance: 100,
  titles: [
    { text: "Йо, Амір.", label: "amir_intro_main" },
    { text: "Привіт, круте місце.", chemistry: { "am": 1 }, label: "amir_intro_main" }
  ]
});

registerScript("amir_intro_main", [
  { type: "show", who: "am", zorder: 1 },

  // ═══ ПОВТОРНА ПЕТЛЯ — скорочено ═══
  { type: "if", loop_restart: true, jump: "amir_loop_restart" },

  // ═══ ПЕРША ПЕТЛЯ ═══
  { type: "say", who: "am", text: "О! Марті! Якраз тебе шукав." },
  { type: "say", who: "am", text: "Тримай." },
  { type: "set_flag", flag: "has_pager" },
  { type: "say", who: "am", text: "Це пейджер. Ну, як телефон. Тільки гірше. Набагато гірше." },

  { type: "menu", choices: [
    { text: "Що це за цеглина?", label: "amir_brick" },
    { text: "Дякую... а нащо він мені?", label: "amir_why" }
  ]},

  { type: "label", id: "amir_brick" },
  { type: "say", who: "mc", text: "Що це за цеглина?" },
  { type: "say", who: "am", text: "ХА! Це ж пейджер! Ти шо, з майбутнього??" },
  { type: "say", who: "mc", text: "..." },
  { type: "say", who: "am", text: "О. Точно. Ти ж реально з майбутнього." },
  { type: "say", who: "am", text: "Окей, окей. Пояснюю." },
  { type: "jump", to: "amir_explain" },

  { type: "label", id: "amir_why" },
  { type: "say", who: "mc", text: "Дякую... а нащо він мені?" },
  { type: "say", who: "am", text: "О, тобі він ДУЖЕ потрібен. Повір. Пояснюю." },

  // ═══ ПОЯСНЕННЯ ПЕЙДЖЕРА ═══
  { type: "label", id: "amir_explain" },
  { type: "say", who: "am", text: "Бачиш екранчик? Зелений такий, мерехтить." },
  { type: "say", who: "am", text: "Там час, день, де ти зараз, скільки грошей, репутація Гексу — базові речі." },
  { type: "say", who: "am", text: "Але головне — повідомлення." },
  { type: "say", who: "am", text: "У кожного з нас є такий. Люди пишуть, ти читаєш." },
  { type: "say", who: "am", text: "Типу... о, дивись!" },

  // Тестові повідомлення
  { type: "pager", who: "Аоі", text: "Я знайшла новий дист On-lyne!" },

  { type: "say", who: "am", text: "Бач? Аоі вже щось написала. І Артур теж — як завжди." },

  { type: "pager", who: "Артур", text: "Не смій вмикати на весь торгівельний центр." },

  { type: "say", who: "am", text: "Натисни центральну кнопку — побачиш повідомлення. Давай, спробуй." },

  // ═══ ПАУЗА: чекаємо кнопку пейджера ═══
  { type: "wait_pager", left: "amir_btn_wrong_left", center: "amir_btn_center", right: "amir_btn_wrong_right" },

  { type: "label", id: "amir_btn_center" },
  { type: "say", who: "am", text: "Бачиш? Перемикає між статусом і повідомленнями." },
  { type: "say", who: "am", text: "Можеш гортати — зелена і червона кнопки." },
  { type: "say", who: "am", text: "А центральна знов — назад на статус." },
  { type: "jump", to: "amir_request_tutorial" },

  { type: "label", id: "amir_btn_wrong_left" },
  { type: "say", who: "am", text: "Ні-ні, це зелена. Центральна — та що посередині." },
  { type: "say", who: "am", text: "Але не страшно, розберешся. Центральна перемикає, бокові гортають." },
  { type: "jump", to: "amir_request_tutorial" },

  { type: "label", id: "amir_btn_wrong_right" },
  { type: "say", who: "am", text: "Це червона. Центральна — посередині." },
  { type: "say", who: "am", text: "Але окей, суть зрозуміла. Центральна перемикає, бокові гортають." },

  // ═══ ЗАПИТ ДОПОМОГИ ═══
  { type: "label", id: "amir_request_tutorial" },
  { type: "say", who: "am", text: "А тепер дивись. Іноді приходить не просто повідомлення, а запит на допомогу." },
  { type: "say", who: "am", text: "Треба відповісти: так чи ні." },

  { type: "pager_request", who: "Летті", text: "Допоможи перенести коробки медикаментів?" },

  { type: "say", who: "am", text: "О! Летті просить допомогти перенести коробки." },
  { type: "say", who: "am", text: "Зелена кнопка зліва — прийняти. Червона справа — відхилити." },
  { type: "say", who: "am", text: "Зараз відхили — я ще не закінчив пояснювати." },

  // ═══ ПАУЗА: чекаємо відповідь на запит ═══
  { type: "wait_pager", left: "amir_req_accept", center: "amir_req_center", right: "amir_req_decline" },

  { type: "label", id: "amir_req_decline" },
  { type: "say", who: "am", text: "Ось. Відхилено." },
  { type: "say", who: "am", text: "Але запам'ятай — якщо вільний і хтось просить, йди. Бо це репутація." },
  { type: "say", who: "am", text: "А репутація — це довіра. А довіра тут — валюта." },
  { type: "chemistry", who: "am", amount: 2 },
  { type: "jump", to: "amir_after_request" },

  { type: "label", id: "amir_req_center" },
  { type: "say", who: "am", text: "...Це центральна. Ти просто закрив запит." },
  { type: "say", who: "am", text: "Ну... технічно теж варіант. Просто проігнорив." },
  { type: "say", who: "am", text: "Краще відповідай. Ігнор теж помітять." },
  { type: "chemistry", who: "am", amount: 1 },
  { type: "jump", to: "amir_after_request" },

  { type: "label", id: "amir_req_accept" },
  { type: "say", who: "am", text: "Стій-стій! Я ж сказав — відхили!" },
  { type: "say", who: "am", text: "Летті тепер думає що ти йдеш допомагати." },
  { type: "say", who: "mc", text: "..." },
  { type: "say", who: "am", text: "...Ладно, нічого. Скажу їй що ти випадково натиснув." },
  { type: "say", who: "am", text: "Запам'ятай: зелена — підтверджуєш. Червона — відмовляєш." },
  { type: "chemistry", who: "am", amount: 2 },

  // ═══ ПІСЛЯ ЗАПИТУ ═══
  { type: "label", id: "amir_after_request" },
  { type: "say", who: "am", text: "А! І ще." },
  { type: "say", who: "am", text: "Якщо домовився з кимось зустрітись — пейджер нагадає. Щоб не забув." },
  { type: "say", who: "am", text: "Бо якщо забудеш... ну... люди тут не дуже це прощають." },

  // ═══ МАРТІ ═══
  { type: "say", who: "mc", text: "До речі, Аміре." },
  { type: "say", who: "mc", text: "Хто такий Марті? Чому ви мене так називаєте?" },
  { type: "say", who: "am", text: "О-о-о, брат. Ти не знаєш??" },
  { type: "say", who: "am", text: "Марті МакФлай! Фільм! «Назад у Майбутнє»!" },
  { type: "say", who: "am", text: "Хлопець потрапляє в минуле, все ламає, потім фіксить." },
  { type: "say", who: "am", text: "Ти ж теж з майбутнього і все тут ламаєш, ні?" },

  { type: "menu", choices: [
    { text: "Я ще нічого не зламав.", label: "amir_marty_1" },
    { text: "Грубо. Але смішно.", label: "amir_marty_2" },
    { text: "Мені все одно як мене називають.", label: "amir_marty_3" }
  ]},

  { type: "label", id: "amir_marty_1" },
  { type: "say", who: "mc", text: "Я ще нічого не зламав." },
  { type: "say", who: "am", text: "Поки що. ПОКИ ЩО, Марті." },
  { type: "say", who: "am", text: "Але серйозно — це комплімент. Марті класний." },
  { type: "chemistry", who: "am", amount: 2 },
  { type: "jump", to: "amir_movies" },

  { type: "label", id: "amir_marty_2" },
  { type: "say", who: "mc", text: "Грубо. Але смішно." },
  { type: "say", who: "am", text: "ДЯКУЮ. Я старався." },
  { type: "chemistry", who: "am", amount: 4 },
  { type: "jump", to: "amir_movies" },

  { type: "label", id: "amir_marty_3" },
  { type: "say", who: "mc", text: "Мені все одно як мене називають." },
  { type: "say", who: "am", text: "...Ну добре. Але ти все одно Марті." },

  { type: "label", id: "amir_movies" },
  { type: "say", who: "am", text: "Слухай, а ти кіно любиш?" },

  { type: "menu", choices: [
    { text: "Майже не дивився.", label: "amir_movie_1" },
    { text: "Люблю, але не до кіна.", label: "amir_movie_2" },
    { text: "Ні.", label: "amir_movie_3" }
  ]},

  { type: "label", id: "amir_movie_1" },
  { type: "say", who: "mc", text: "Якщо чесно, я майже не дивився фільмів. Ну... обставини." },
  { type: "say", who: "am", text: "ШООО?! Це ж ЗЛОЧИН!" },
  { type: "say", who: "am", text: "Окей, все. Ми сідаємо і дивимось. Обов'язково." },
  { type: "set_flag", flag: "amir_movie_night_promised" },
  { type: "chemistry", who: "am", amount: 4 },
  { type: "jump", to: "amir_intro_end" },

  { type: "label", id: "amir_movie_2" },
  { type: "say", who: "mc", text: "Люблю. Але зараз не найкращий час для кіновечорів." },
  { type: "say", who: "am", text: "Час ЗАВЖДИ є для кіна, Марті. Запам'ятай це." },
  { type: "set_flag", flag: "amir_movie_night_promised" },
  { type: "chemistry", who: "am", amount: 2 },
  { type: "jump", to: "amir_intro_end" },

  { type: "label", id: "amir_movie_3" },
  { type: "say", who: "mc", text: "Ні, не моя тема." },
  { type: "say", who: "am", text: "...Ми це виправимо. Повір мені." },
  { type: "set_flag", flag: "amir_movie_night_promised" },

  { type: "label", id: "amir_intro_end" },
  { type: "set_flag", flag: "amir_intro_done" },
  { type: "end", text: "" },

  // ═══ ПОВТОРНА ПЕТЛЯ — скорочено, без туторіалу і Марті ═══
  { type: "label", id: "amir_loop_restart" },
  { type: "say", who: "mc", text: "Та я знаю, Аміре." },
  { type: "say", who: "am", text: "...Шо?" },
  { type: "say", who: "mc", text: "Не зважай. Дякую." },
  { type: "say", who: "am", text: "Окей... дивний ти, Марті." },
  { type: "set_flag", flag: "has_pager" },
  { type: "say", who: "am", text: "Ну все. Пейджер є, карта є. Давай, не загуби нічого." },
  { type: "set_flag", flag: "amir_intro_done" },
  { type: "end", text: "" }
]);
