// ═══════════════════════════════════════════════════
// КВІНСІ — ІНТРО: Скальдра, Русалка, Віктор + підстава з "бро"
// Порт з game/dialogues/quincy/quincy_intro.rpy
// ═══════════════════════════════════════════════════

DIALOGUE_ENTRIES.push({
  id: "quincy_intro",
  who: "Квінсі",
  conditions: { flag_false: ["quincy_intro_done"] },
  priority: 90,
  chance: 100,
  titles: [
    { text: "Привіт.", label: "quincy_intro_main" }
  ]
});

registerScript("quincy_intro_main", [
  { type: "show", who: "qu", zorder: 1 },
  { type: "say", who: "mc", text: "Привіт." },
  { type: "say", who: "qu", text: "Привіт? Серйозно?" },
  { type: "say", who: "qu", text: "В майбутньому весь сленг вимер чи шо?" },

  { type: "menu", choices: [
    { text: "В мене були інші пріоритети.", label: "quincy_greet_1" },
    { text: "А як треба було сказати?", label: "quincy_greet_2" },
    { text: "Йо.", label: "quincy_greet_3" }
  ]},

  { type: "label", id: "quincy_greet_1" },
  { type: "say", who: "mc", text: "В мене були інші пріоритети, ніж сленг." },
  { type: "say", who: "qu", text: "Fair enough. Але тут тобі доведеться підтягнутись, cuz." },
  { type: "chemistry", who: "qu", amount: 2 },
  { type: "jump", to: "quincy_base" },

  { type: "label", id: "quincy_greet_2" },
  { type: "say", who: "mc", text: "А як треба було сказати?" },
  { type: "say", who: "qu", text: "Та шо завгодно окрім «привіт» як бабуся до сусідки." },
  { type: "say", who: "qu", text: "Ладно, прощаю. Ти з іншого часу." },
  { type: "jump", to: "quincy_base" },

  { type: "label", id: "quincy_greet_3" },
  { type: "say", who: "mc", text: "Йо." },
  { type: "say", who: "qu", text: "О! Бачиш, вмієш коли хочеш!" },
  { type: "chemistry", who: "qu", amount: 4 },

  { type: "label", id: "quincy_base" },
  { type: "say", who: "qu", text: "Короче, Марті. Раз ти тут — маєш знати базу." },
  { type: "say", who: "mc", text: "Слухаю." },
  { type: "say", who: "qu", text: "За стінами молу — місто. Гьольванія." },
  { type: "say", who: "qu", text: "Було класне місце. Бари, музика, люди. А тепер..." },
  { type: "say", who: "qu", text: "Скальдра. Чув про них?" },

  { type: "menu", choices: [
    { text: "Ні. Що це?", label: "quincy_scaldra_1" },
    { text: "Щось чув від Артура.", label: "quincy_scaldra_2" }
  ]},

  { type: "label", id: "quincy_scaldra_1" },
  { type: "say", who: "mc", text: "Ні. Що це?" },
  { type: "say", who: "qu", text: "Заражені. Техногниль перетворює людей на... щось інше." },
  { type: "say", who: "qu", text: "Вони не зовсім мертві, не зовсім живі. Просто... злі. І швидкі." },
  { type: "say", who: "qu", text: "Раніше вони були сусідами, продавцями, друзями. Тепер — targets." },
  { type: "jump", to: "quincy_rusalka" },

  { type: "label", id: "quincy_scaldra_2" },
  { type: "say", who: "mc", text: "Щось чув. Заражені?" },
  { type: "say", who: "qu", text: "Заражені — це м'яко сказано. Вони тебе зжеруть якщо зазіваєшся." },

  { type: "label", id: "quincy_rusalka" },
  { type: "say", who: "qu", text: "А ще — Русалка." },
  { type: "say", who: "mc", text: "Русалка?" },
  { type: "say", who: "qu", text: "Жінка. Якщо це слово ще підходить." },
  { type: "say", who: "qu", text: "Контролює скальдру. Або вони контролюють її. Ніхто не знає точно." },
  { type: "say", who: "qu", text: "Живе десь у глибині міста. Ми її бачили пару разів. Краще б не бачили." },

  { type: "say", who: "mc", text: "А Віктор?" },
  { type: "say", who: "qu", text: "О, Віктора ти ще зустрінеш." },
  { type: "say", who: "qu", text: "Лікар. Або був лікарем. Зараз він... складний." },
  { type: "say", who: "qu", text: "Допомагає місцевим. Але в нього свої методи. І свої секрети." },
  { type: "say", who: "qu", text: "Артур йому не довіряє. Елеонор вважає його цікавим. Летті його ненавидить." },
  { type: "say", who: "qu", text: "Я? Я просто тримаю його на мушці коли він поряд. На всяк випадок." },
  { type: "chemistry", who: "qu", amount: 2 },

  { type: "menu", choices: [
    { text: "Дякую за інформацію.", label: "quincy_thanks" },
    { text: "Весела компанія зібралась.", label: "quincy_fun" }
  ]},

  { type: "label", id: "quincy_thanks" },
  { type: "say", who: "mc", text: "Дякую. Тепер хоч розумію де я опинився." },
  { type: "say", who: "qu", text: "Не дякуй. Тут всі мають знати правила гри." },
  { type: "jump", to: "quincy_bro_check" },

  { type: "label", id: "quincy_fun" },
  { type: "say", who: "mc", text: "Весела компанія зібралась." },
  { type: "say", who: "qu", text: "Lmao. Ти ще й половини не бачив, m8." },
  { type: "chemistry", who: "qu", amount: 2 },

  // Підстава з "бро" — тільки якщо Артур ще не пройдений
  { type: "label", id: "quincy_bro_check" },
  { type: "if", flag: "arthur_intro_done", jump: "quincy_intro_end" },

  { type: "say", who: "qu", text: "О, і ще." },
  { type: "say", who: "qu", text: "Ти ж ще не говорив з героєбоєм?" },
  { type: "say", who: "mc", text: "З ким?" },
  { type: "say", who: "qu", text: "З Артуром. Нашим великим лідером." },
  { type: "say", who: "qu", text: "Маленька порада, cuz. Він любить коли до нього звертаються по-свійськи." },
  { type: "say", who: "qu", text: "Типу «бро». Або «братан». Він тоді відразу розслабляється." },
  { type: "say", who: "qu", text: "Trust me on this one." },

  { type: "menu", choices: [
    { text: "Серйозно? Не схоже на нього.", label: "quincy_bro_doubt" },
    { text: "Окей, спробую.", label: "quincy_bro_ok" },
    { text: "Щось мені підказує що це погана ідея.", label: "quincy_bro_smart" }
  ]},

  { type: "label", id: "quincy_bro_doubt" },
  { type: "say", who: "mc", text: "Серйозно? Він виглядає як людина, яка НЕ любить «бро»." },
  { type: "say", who: "qu", text: "Ні-ні, це маска. Всередині він м'який як пончик." },
  { type: "say", who: "qu", text: "Спробуй. Що ти втрачаєш?" },
  { type: "set_flag", flag: "quincy_told_bro" },
  { type: "jump", to: "quincy_intro_end" },

  { type: "label", id: "quincy_bro_ok" },
  { type: "say", who: "mc", text: "Добре. Спробую." },
  { type: "say", who: "qu", text: "Gg. Скажеш мені потім як пройшло." },
  { type: "set_flag", flag: "quincy_told_bro" },
  { type: "chemistry", who: "qu", amount: 2 },
  { type: "jump", to: "quincy_intro_end" },

  { type: "label", id: "quincy_bro_smart" },
  { type: "say", who: "mc", text: "Щось мені підказує що це погана ідея." },
  { type: "say", who: "qu", text: "Ти розумніший ніж виглядаєш, Марті." },
  { type: "chemistry", who: "qu", amount: 4 },

  { type: "label", id: "quincy_intro_end" },
  { type: "set_flag", flag: "quincy_intro_done" },

  // Якщо немає пейджера — направити до Аміра
  { type: "if", flag: "has_pager", jump: "quincy_intro_done_final" },
  { type: "say", who: "qu", text: "Btw, зайди до Аміра. Він в аркадах." },
  { type: "say", who: "qu", text: "Він тобі щось причепить. Не питай — просто йди." },
  { type: "label", id: "quincy_intro_done_final" },
  { type: "end", text: "" }
]);
