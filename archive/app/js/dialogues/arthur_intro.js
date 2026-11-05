// ═══════════════════════════════════════════════════
// АРТУР — ІНТРО: Місії, правила, погрози
// Порт з game/dialogues/arthur/arthur_intro.rpy
// + arthur_intro_bro.rpy
// ═══════════════════════════════════════════════════

DIALOGUE_ENTRIES.push({
  id: "arthur_intro",
  who: "ar",
  conditions: { flag_false: ["arthur_intro_done"] },
  priority: 90,
  chance: 100,
  titles: [
    { text: "Привіт.", label: "arthur_intro_normal" }
  ]
});

BONUS_OPTIONS.push({
  id: "arthur_bro_greeting",
  who: "ar",
  text: "Хай, бро.",
  label: "arthur_intro_bro",
  conditions: { flag_true: ["quincy_told_bro"], flag_false: ["arthur_intro_done"] },
  once: true
});

// ─── Бро-гілка ───
registerScript("arthur_intro_bro", [
  { type: "show", who: "ar", zorder: 1 },
  { type: "say", who: "mc", text: "Хай, бро." },
  { type: "say", who: "ar", text: "..." },
  { type: "say", who: "ar", text: "Як ти мене назвав?" },
  { type: "say", who: "mc", text: "Ну... бро. Квінсі сказав що ти—" },
  { type: "say", who: "ar", text: "Квінсі." },
  { type: "say", who: "ar", text: "Звісно." },
  { type: "say", who: "ar", text: "Послухай мене уважно." },
  { type: "say", who: "ar", text: "Я тобі не «бро». Не «братан». Не «чувак»." },
  { type: "say", who: "ar", text: "Я — Артур. Командир цієї групи." },
  { type: "say", who: "ar", text: "Ти можеш звати мене Артур. Або «сер». Або нічого." },
  { type: "say", who: "ar", text: "Це зрозуміло?" },
  { type: "menu", choices: [
    { text: "Зрозуміло. Вибач.", label: "arthur_bro_apologize" },
    { text: "[Мовчати.]", label: "arthur_bro_silent" }
  ]},
  { type: "label", id: "arthur_bro_apologize" },
  { type: "say", who: "mc", text: "Зрозуміло. Вибач." },
  { type: "say", who: "ar", text: "Не вибачайся переді мною. Вибачайся перед собою за те що послухав Квінсі." },
  { type: "chemistry", who: "ar", amount: -2 },
  { type: "jump", to: "arthur_bro_after" },

  { type: "label", id: "arthur_bro_silent" },
  { type: "say", who: "mc", text: "..." },
  { type: "say", who: "ar", text: "Мовчання — теж відповідь. Прийнятна." },

  { type: "label", id: "arthur_bro_after" },
  { type: "set_flag", flag: "arthur_bro_incident" },
  { type: "say", who: "ar", text: "А тепер до справи." },
  { type: "jump", to: "arthur_intro_missions" }
]);

// ─── Нормальне інтро ───
registerScript("arthur_intro_normal", [
  { type: "show", who: "ar", zorder: 1 },
  { type: "say", who: "mc", text: "Привіт." },
  { type: "say", who: "ar", text: "Привіт, Марті." },
  { type: "say", who: "ar", text: "Ти вчасно. Мені треба тобі дещо пояснити." },
  { type: "jump", to: "arthur_intro_missions" }
]);

// ─── Місії ───
registerScript("arthur_intro_missions", [
  { type: "say", who: "ar", text: "Місії. Це головне, чим ми тут займаємось." },
  { type: "say", who: "ar", text: "Щодня генеруються завдання. Різного рівня складності." },
  { type: "say", who: "ar", text: "Рівень один — розвідка. Рівень шість — ти або вони." },
  { type: "say", who: "ar", text: "Нагорода залежить від рівня. Гроші, репутація." },
  { type: "say", who: "ar", text: "Для місій потрібно йти в гараж. Там дошка завдань." },
  { type: "say", who: "ar", text: "Кожна місія має напарника — когось з Гексу. Працюєте разом." },
  { type: "say", who: "ar", text: "Репутація — це довіра Гексу до тебе. Чим більше — тим більше можливостей." },
  { type: "say", who: "ar", text: "Питання?" },

  { type: "menu", choices: [
    { text: "А якщо пропустити місію?", label: "arthur_q_skip" },
    { text: "Хто буде напарником?", label: "arthur_q_partner" },
    { text: "Нема питань.", label: "arthur_intro_end" }
  ]},

  { type: "label", id: "arthur_q_skip" },
  { type: "say", who: "mc", text: "А якщо я вирішу пропустити?" },
  { type: "say", who: "ar", text: "Один-два дні — нічого. Три — починають питання." },
  { type: "say", who: "ar", text: "П'ять — всі починають сумніватись чи ти взагалі тут потрібен." },
  { type: "say", who: "ar", text: "Я не загрожую. Я попереджаю." },
  { type: "chemistry", who: "ar", amount: 2 },

  { type: "menu", choices: [
    { text: "Хто буде напарником?", label: "arthur_q_partner" },
    { text: "Нема питань.", label: "arthur_intro_end" }
  ]},

  { type: "label", id: "arthur_q_partner" },
  { type: "say", who: "mc", text: "Напарник — це завжди хтось конкретний?" },
  { type: "say", who: "ar", text: "Кожна місія призначає напарника. Одного з Гексу." },
  { type: "say", who: "ar", text: "Працюєте разом. Захищаєте одне одного." },
  { type: "say", who: "ar", text: "Підставиш напарника — підставиш мого бійця. А це — особисте." },
  { type: "chemistry", who: "ar", amount: 2 },
  { type: "jump", to: "arthur_intro_end" },

  { type: "label", id: "arthur_intro_end" },
  { type: "say", who: "ar", text: "Добре. Гараж — через комп'ютерний клуб. Побачиш вивіску." },
  { type: "menu", choices: [
    { text: "Не підведу.", label: "arthur_end_promise" },
    { text: "Зрозумів.", label: "arthur_end_ok" }
  ]},

  { type: "label", id: "arthur_end_promise" },
  { type: "say", who: "mc", text: "Не підведу." },
  { type: "say", who: "ar", text: "Побачимо." },
  { type: "chemistry", who: "ar", amount: 2 },
  { type: "jump", to: "arthur_intro_flags" },

  { type: "label", id: "arthur_end_ok" },
  { type: "say", who: "mc", text: "Зрозумів." },
  { type: "say", who: "ar", text: "Добре." },

  { type: "label", id: "arthur_intro_flags" },
  { type: "set_flag", flag: "arthur_intro_done" },
  { type: "set_flag", flag: "garage_unlocked" },
  { type: "say", who: "ar", text: "Гараж тепер відкритий. Підеш коли будеш готовий — там дошка з місіями." },

  // Якщо немає пейджера — направити до Аміра
  { type: "if", flag: "has_pager", jump: "arthur_intro_done_final" },
  { type: "say", who: "ar", text: "І зайди до Аміра. Він в аркадах. Має щось для тебе." },
  { type: "say", who: "ar", text: "Це наказ, не прохання." },
  { type: "label", id: "arthur_intro_done_final" },
  { type: "end", text: "" }
]);
