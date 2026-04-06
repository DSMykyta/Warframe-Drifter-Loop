// ═══════════════════════════════════════════════════
// ІНТРО: Допит на футкорті + знайомство з Гексом
// Порт з game/scenes/intro.rpy
// ═══════════════════════════════════════════════════

registerScript("intro", [
  // ─── Чорний екран ───
  { type: "bg", file: "bg_black.png" },
  { type: "say", who: null, text: "..." },

  // ─── Футкорт: всі 6 вже сидять навпроти ───
  { type: "bg", file: "bg_foodcourt.webp" },
  { type: "show", who: "ao", at: 8,  zorder: 0 },
  { type: "show", who: "lt", at: 22, zorder: 0 },
  { type: "show", who: "el", at: 36, zorder: 0 },
  { type: "show", who: "ar", at: 50, zorder: 2 },
  { type: "show", who: "am", at: 64, zorder: 0 },
  { type: "show", who: "qu", at: 85, zorder: 0 },

  { type: "say", who: "am", text: "Ого. Тобто ти типу... Марті МакФлай?" },
  { type: "say", who: "qu", text: "Знущаєшся, мабуть?" },
  { type: "say", who: "ar", text: "Якщо це туфта — я Марті особисто згодую Техроту." },
  { type: "say", who: "ar", text: "Але часу нема." },
  { type: "say", who: "am", text: "Бомба... знаєш, воно сходиться." },

  // ─── ВИБІР 1: реакція на допит ───
  { type: "menu", choices: [
    {
      text: "З Новим Роком.",
      flag: "intro_dark_humor",
      chemistry: { "Квінсі": 2 },
      label: "after_choice_1"
    },
    {
      text: "Я не прошу вірити. Перевірте.",
      flag: "intro_asked_to_verify",
      chemistry: { "Артур": 2 },
      label: "after_choice_1"
    },
    {
      text: "[Нічого не сказати.]",
      flag: "intro_stayed_silent",
      chemistry: { "Артур": 1, "Квінсі": 1 },
      label: "intro_silent_reaction"
    }
  ]},

  // ─── Мовчанка — реакція ───
  { type: "label", id: "intro_silent_reaction" },
  { type: "say", who: "am", text: "Він... не буде відповідати?" },
  { type: "say", who: "ar", text: "Амір." },
  { type: "say", who: "am", text: "Все, мовчу." },

  // ─── Після першого вибору ───
  { type: "label", id: "after_choice_1" },
  { type: "say", who: "ar", text: "Добре, Марті. Ти нам, може, і потрібний." },
  { type: "say", who: "ar", text: "Але спробуєш ще раз залізти мені в голову—" },
  { type: "say", who: "ar", text: "—і Летті нічого буде зшивати." },
  { type: "say", who: "lt", text: "Si." },
  { type: "say", who: "ar", text: "Ми зрозуміли один одного?" },

  // ─── ВИБІР 2: відповідь Артуру ───
  { type: "menu", choices: [
    {
      text: "Так точно.",
      flag: "intro_military_response",
      chemistry: { "Артур": 2 },
      label: "after_choice_2"
    },
    {
      text: "Поки мене не прив'язують до стільців — так.",
      flag: "intro_sarcastic_response",
      chemistry: { "Квінсі": 2, "Амір": 1 },
      label: "intro_sarcastic_reaction"
    },
    {
      text: "Обіцяю.",
      flag: "intro_promised",
      chemistry: { "Елеонор": 2 },
      label: "after_choice_2"
    }
  ]},

  // ─── Саркастична реакція ───
  { type: "label", id: "intro_sarcastic_reaction" },
  { type: "say", who: "qu", text: "Ха." },
  { type: "say", who: "am", text: "Він мені подобається." },
  { type: "say", who: "ar", text: "Тобі всі подобаються, Амір." },

  // ─── Після другого вибору — Летті перев'язує ───
  { type: "label", id: "after_choice_2" },
  { type: "say", who: "lt", text: "Руку покажи." },
  { type: "say", who: "lt", text: "Чисто. Між кістками. Жити будеш." },
  { type: "say", who: "lt", text: "На жаль." },
  { type: "set_flag", flag: "lettie_bandaged_hand" },
  { type: "chemistry", values: { "Летті": 1 } },

  // ─── Аоі представляється ───
  { type: "say", who: "ao", text: "Я Аоі." },

  // ─── ВИБІР 3: відповідь Аоі ───
  { type: "menu", choices: [
    {
      text: "Дріфтер. Відносно приємно.",
      chemistry: { "Аоі": 2 },
      label: "after_choice_3"
    },
    {
      text: "[Потиснути руку.]",
      chemistry: { "Аоі": 1, "Артур": 1 },
      label: "intro_handshake_reaction"
    },
    {
      text: "Вибач за голову. Не було іншого способу.",
      chemistry: { "Аоі": 1 },
      label: "intro_apology_reaction"
    }
  ]},

  // ─── Потиснути руку ───
  { type: "label", id: "intro_handshake_reaction" },
  { type: "say", who: "ao", text: "Небалакучий тип." },
  { type: "jump", to: "after_choice_3" },

  // ─── Вибачення ───
  { type: "label", id: "intro_apology_reaction" },
  { type: "say", who: "ao", text: "Не мені вибачати. Але дякую що сказав." },

  // ─── Після третього вибору — знайомство решти ───
  { type: "label", id: "after_choice_3" },
  { type: "say", who: "am", text: "Амір! Технічна частина. І аркади." },
  { type: "say", who: "am", text: "Якщо потрібно щось полагодити або... ну..." },
  { type: "say", who: "ar", text: "Амір." },
  { type: "say", who: "am", text: "Тихо. Так." },
  { type: "chemistry", values: { "Амір": 1 } },

  { type: "say", who: "qu", text: "Квінсі. Тир. Без стуку не заходь." },
  { type: "say", who: "ar", text: "Бекрум. Коридор, другі двері. Завтра о восьмій." },
  { type: "say", who: "ao", text: "Музичний. Другий поверх. Якщо що." },
  { type: "say", who: "am", text: "Ну, бувай, Марті." },
  { type: "say", who: "lt", text: "Рану промий вранці. Водою. Не спирт." },

  // ─── Після допиту ───
  { type: "bg", file: "bg_black.png" },
  { type: "say", who: null, text: "Бекрум. Коридор, другі двері — як Артур сказав." },
  { type: "say", who: null, text: "Кинув речі. Рука ниє, але пов'язка тримається." },
  { type: "say", who: null, text: "Треба оглянути це місце." },

  // ─── Ініціалізація флагів ───
  { type: "set_flag", flag: "intro_done" },
  { type: "set_flag", flag: "met_arthur" },
  { type: "set_flag", flag: "met_aoi" },
  { type: "set_flag", flag: "met_amir" },
  { type: "set_flag", flag: "met_quincy" },
  { type: "set_flag", flag: "met_lettie" },
  { type: "set_flag", flag: "met_eleanor" },
  { type: "set_flag", flag: "nickname_marty" },

  // ─── Кінець інтро — перехід до explore_mall ───
  { type: "end", text: "" }
]);
