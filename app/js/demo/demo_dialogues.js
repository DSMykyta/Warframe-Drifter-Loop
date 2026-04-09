// ═══════════════════════════════════════════════════
// ДЕМО: ТЕСТ ДІАЛОГОВОГО РУШІЯ
// ═══════════════════════════════════════════════════
//
// Крок 1: say, telepathy, think, show/hide, bg, scene
// Крок 2: menu з виборами (locked, bonus, seen)
// Крок 3: chemistry, flags, time
// Крок 4: call/return, jump
// Крок 5: pager, wait_pager
// Крок 6: effect (shake, flash)
// Крок 7: transitions (dissolve, fade)

// ─── СТАРТ ДЕМО ───
registerScript("demo_start", [
  {type: "scene", bg: "bg_security_desk.webp", text: "ДЕМО: ДІАЛОГОВИЙ РУШІЙ"},

  // SAY — наратор
  {type: "say", who: null, text: "Це наратор. Текст без імені. Друкується по буквах."},

  // SAY — гравець (mc)
  {type: "say", who: "mc", text: "Це фраза гравця. Без плашки імені."},

  // SHOW + SAY — NPC
  {type: "show", who: "ar", at: "center", zorder: 1},
  {type: "say", who: "ar", text: "Це Артур. Перевірка імені та кольору."},

  // Другий спрайт — перевірка групи
  {type: "show", who: "el", at: "left", zorder: 0},
  {type: "say", who: "el", text: "Це Елеонор. Два спрайти на сцені. Артур затемнений."},
  {type: "say", who: "ar", text: "Тепер я говорю. Елеонор затемнена."},

  // HIDE
  {type: "hide", who: "el"},
  {type: "say", who: "ar", text: "Елеонор сховалась. Тільки я на сцені."},

  // TELEPATHY
  {type: "telepathy", who: "el", text: "Це телепатія. Трясучийся текст. Голос Елеонор в голові."},

  // THINK
  {type: "think", text: "Це внутрішня думка гравця. Курсив. Чистий текст."},

  // BG зміна без очистки спрайтів
  {type: "bg", file: "bg_backroom.webp"},
  {type: "say", who: "ar", text: "Фон змінився на бекрум, але я залишився."},

  // SCENE — повна заміна
  {type: "scene", bg: "bg_arcade.webp"},
  {type: "say", who: null, text: "Повна зміна сцени. Спрайти очищені. Фон — аркади."},

  // CHEMISTRY в say ноді
  {type: "show", who: "am"},
  {type: "say", who: "am", text: "Цей рядок дає +3 хімії Аміру.", chemistry: {"am": 3}},

  // FLAG в say ноді
  {type: "say", who: "am", text: "Цей рядок ставить флаг demo_flag_test.", flag: "demo_flag_test"},

  // TIME в say ноді
  {type: "say", who: "am", text: "Цей рядок просуває час на 30 хв.", time: 30},

  // HIDE + перехід до меню
  {type: "hide", who: "am"},
  {type: "say", who: null, text: "Зараз буде меню виборів."},

  // ─── MENU ───
  {type: "menu", choices: [
    {text: "Звичайний вибір", label: "demo_choice_normal", chemistry: {"ar": 2}},
    {text: "Бонусний вибір (жовтий)", label: "demo_choice_bonus", bonus: true},
    {text: "Заблокований (потрібен прапорець)", label: "demo_choice_locked", condition: {flag: "nonexistent_flag"}},
    {text: "Вже обраний (сірий)", label: "demo_choice_seen", flag: "demo_flag_test"}
  ]},

  // Labels для виборів
  {type: "label", id: "demo_choice_normal"},
  {type: "say", who: null, text: "Обрано звичайний. +2 хімії Артуру."},
  {type: "jump", to: "demo_after_menu"},

  {type: "label", id: "demo_choice_bonus"},
  {type: "say", who: null, text: "Обрано бонусний."},
  {type: "jump", to: "demo_after_menu"},

  {type: "label", id: "demo_choice_locked"},
  {type: "say", who: null, text: "Це не мало бути доступним!"},
  {type: "jump", to: "demo_after_menu"},

  {type: "label", id: "demo_choice_seen"},
  {type: "say", who: null, text: "Обрано вже побачений вибір."},

  // ─── AFTER MENU: IF/JUMP ───
  {type: "label", id: "demo_after_menu"},
  {type: "say", who: null, text: "Перевірка IF: чи встановлений demo_flag_test?"},
  {type: "if", flag: "demo_flag_test", jump: "demo_flag_yes", else_jump: "demo_flag_no"},

  {type: "label", id: "demo_flag_yes"},
  {type: "say", who: null, text: "IF пройшов: флаг demo_flag_test = true."},
  {type: "jump", to: "demo_call_test"},

  {type: "label", id: "demo_flag_no"},
  {type: "say", who: null, text: "IF не пройшов: флаг не встановлений."},

  // ─── CALL / RETURN ───
  {type: "label", id: "demo_call_test"},
  {type: "say", who: null, text: "Зараз CALL до підскрипту demo_sub. Потім RETURN сюди."},
  {type: "call", script: "demo_sub"},
  {type: "say", who: null, text: "Повернулись з demo_sub через RETURN. Call/Return працює."},

  // ─── PAGER ───
  {type: "say", who: null, text: "Зараз пейджер отримає повідомлення."},
  {type: "pager", who: "lt", text: "Тест пейджера. Летті пише."},
  {type: "say", who: null, text: "Повідомлення надіслано. Подивись на пейджер."},

  // PAGER REQUEST + WAIT
  {type: "say", who: null, text: "Зараз пейджер-запит. Натисни ЛІВУ або ПРАВУ кнопку."},
  {type: "pager_request", who: "am", text: "Допоможи з аркадним автоматом?", accept: "demo_pager_yes", decline: "demo_pager_no"},
  {type: "wait_pager", left: "demo_pager_yes", right: "demo_pager_no"},

  {type: "label", id: "demo_pager_yes"},
  {type: "say", who: null, text: "Прийнято запит. Ліва кнопка працює."},
  {type: "jump", to: "demo_effects"},

  {type: "label", id: "demo_pager_no"},
  {type: "say", who: null, text: "Відхилено запит. Права кнопка працює."},

  // ─── EFFECTS ───
  {type: "label", id: "demo_effects"},
  {type: "say", who: null, text: "Зараз ефект SHAKE."},
  {type: "effect", name: "shake", intensity: 15, duration: 600},
  {type: "say", who: null, text: "Shake готово. Зараз FLASH."},
  {type: "effect", name: "flash", color: "#fff", duration: 400},
  {type: "say", who: null, text: "Flash готово. Зараз TINT (червоний)."},
  {type: "effect", name: "tint", color: "#f00", opacity: 0.3, duration: 800},

  // ─── TRANSITIONS ───
  {type: "say", who: null, text: "Зараз перехід DISSOLVE."},
  {type: "with", transition: "dissolve", duration: 600},
  {type: "scene", bg: "bg_medbay.webp"},
  {type: "say", who: null, text: "Dissolve + нова сцена. Зараз FADE."},
  {type: "with", transition: "fade", duration: 600},
  {type: "scene", bg: "bg_foodcourt.webp"},
  {type: "say", who: null, text: "Fade + нова сцена."},

  // ─── CHEMISTRY IF ───
  {type: "say", who: null, text: "Перевірка chemistry_min: Амір >= 5?"},
  {type: "if", chemistry_min: ["am", 5], jump: "demo_chem_yes", else_jump: "demo_chem_no"},

  {type: "label", id: "demo_chem_yes"},
  {type: "say", who: null, text: "Хімія Аміра >= 5. Правильно."},
  {type: "jump", to: "demo_engine_done"},

  {type: "label", id: "demo_chem_no"},
  {type: "say", who: null, text: "Хімія Аміра < 5. Щось не так."},

  // ─── КІНЕЦЬ ДІАЛОГОВОГО ТЕСТУ ───
  {type: "label", id: "demo_engine_done"},
  {type: "set_flag", flag: "demo_engine_passed"},
  {type: "say", who: null, text: "ДІАЛОГОВИЙ РУШІЙ: ВСІ ТЕСТИ ПРОЙДЕНІ."},
  {type: "say", who: null, text: "Повернення до локації. Натисни на NPC для тесту titles/forced/banter."},
  {type: "say", who: null, text: "Артур: titles меню. Елеонор: forced діалог (автоматично). Квінсі: обіцянка."},
  {type: "end", text: ""}
]);

// Підскрипт для CALL/RETURN
registerScript("demo_sub", [
  {type: "say", who: null, text: "Ми в підскрипті demo_sub. Зараз RETURN."},
  {type: "return"}
]);
