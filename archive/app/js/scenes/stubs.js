// ═══════════════════════════════════════════════════
// ЗАГЛУШКИ ДІАЛОГІВ — пул коротких реплік для NPC
// Кожен NPC має мінімум 5 заглушок за різними темами
// ═══════════════════════════════════════════════════


// ────────────────────────────────────
// АРТУР — короткий, військовий, готує
// ────────────────────────────────────

registerScript("stub_ar_square_food", [
  { type: "say", who: "ar", text: "Щось готую. Не чіпай." },
  { type: "say", who: "ar", text: "...Бульйон. Якщо цікаво." },
  { type: "end", text: "" }
]);

registerScript("stub_ar_keys", [
  { type: "say", who: "ar", text: "Ключі від складу бачив?" },
  { type: "say", who: "mc", text: "Ні." },
  { type: "say", who: "ar", text: "Шукай. Мені до вечора треба." },
  { type: "end", text: "" }
]);

registerScript("stub_ar_danko", [
  { type: "say", who: "ar", text: "Не стій стовпом. Або допомагай, або не заважай." },
  { type: "end", text: "" }
]);

registerScript("stub_ar_sword_cleaning", [
  { type: "say", who: "ar", text: "Меч чистити треба кожен день. Це дисципліна." },
  { type: "say", who: "ar", text: "Тебе це також стосується." },
  { type: "end", text: "" }
]);

registerScript("stub_ar_weather", [
  { type: "say", who: "ar", text: "Дощ. Знову." },
  { type: "say", who: "ar", text: "Не найкращий день для виходу." },
  { type: "end", text: "" }
]);

registerScript("stub_ar_cooking", [
  { type: "say", who: "ar", text: "На вечерю — плов. Не запізнюйся." },
  { type: "end", text: "" }
]);

registerScript("stub_ar_drinks", [
  { type: "say", who: "ar", text: "Вода. Пий воду. Не газовану дрянь з автомату." },
  { type: "end", text: "" }
]);

registerScript("stub_ar_sleep", [
  { type: "say", who: "ar", text: "Спати треба. Без сну — помилки. Помилки — втрати." },
  { type: "end", text: "" }
]);

registerScript("stub_ar_silence", [
  { type: "say", who: "ar", text: "..." },
  { type: "say", who: "ar", text: "Якщо нема що сказати — не кажи." },
  { type: "end", text: "" }
]);

registerScript("stub_ar_quincy_annoying", [
  { type: "say", who: "ar", text: "Квінсі знов стріляв о третій ночі." },
  { type: "say", who: "ar", text: "Поговори з ним. Мене він не слухає." },
  { type: "end", text: "" }
]);


// ────────────────────────────────────
// ЕЛЕОНОР — задумлива, телепатка, журналістка
// ────────────────────────────────────

registerScript("stub_el_philosophy", [
  { type: "say", who: "el", text: "Знаєш, час тут інакший. Тече, але не рухається." },
  { type: "say", who: "el", text: "Може тому ми тут застрягли." },
  { type: "end", text: "" }
]);

registerScript("stub_el_observations", [
  { type: "say", who: "el", text: "Ти сьогодні інший. Щось сталось?" },
  { type: "say", who: "mc", text: "Ні." },
  { type: "say", who: "el", text: "Не обов'язково відповідати. Я і так бачу." },
  { type: "end", text: "" }
]);

registerScript("stub_el_writing", [
  { type: "say", who: "el", text: "Пишу. Нотатки, спостереження. Звичка журналіста." },
  { type: "say", who: "el", text: "Колись це буде важливо. Або ні. Але я пишу." },
  { type: "end", text: "" }
]);

registerScript("stub_el_plants", [
  { type: "say", who: "el", text: "Рослини тут дивні. Ростуть без сонця." },
  { type: "say", who: "el", text: "Як і ми, мабуть." },
  { type: "end", text: "" }
]);

registerScript("stub_el_sleep", [
  { type: "say", who: "el", text: "Я не сплю добре. Голоси не зупиняються на ніч." },
  { type: "say", who: "el", text: "Але ти не хвилюйся. Я звикла." },
  { type: "end", text: "" }
]);

registerScript("stub_el_weather", [
  { type: "say", who: "el", text: "Погода зовні... я вже не пам'ятаю яка вона." },
  { type: "end", text: "" }
]);

registerScript("stub_el_patterns", [
  { type: "say", who: "el", text: "Ти помічав закономірності? Як все повторюється?" },
  { type: "say", who: "el", text: "Не відповідай. Просто подумай." },
  { type: "end", text: "" }
]);

registerScript("stub_el_books", [
  { type: "say", who: "el", text: "В книгарні знайшла Маркеса. Зачитана до дірок." },
  { type: "say", who: "el", text: "Хтось тут читав до нас." },
  { type: "end", text: "" }
]);

registerScript("stub_el_quiet", [
  { type: "say", who: "el", text: "Тихо. Добре." },
  { type: "say", who: "el", text: "Побудь тут. Не треба говорити." },
  { type: "end", text: "" }
]);

registerScript("stub_el_riddles", [
  { type: "say", who: "el", text: "Чому двері зліва завжди зачинені, а праві — ні?" },
  { type: "say", who: "el", text: "Тут все має значення. Або нічого не має." },
  { type: "end", text: "" }
]);


// ────────────────────────────────────
// ЛЕТТІ — саркастична, медик, кава
// ────────────────────────────────────

registerScript("stub_lt_rats", [
  { type: "say", who: "lt", text: "Бачив щурів? Жирних." },
  { type: "say", who: "lt", text: "Якщо побачиш — не чіпай. Серйозно." },
  { type: "end", text: "" }
]);

registerScript("stub_lt_coffee", [
  { type: "say", who: "lt", text: "Каву. Хоч якусь. Мені байдуже яку." },
  { type: "say", who: "lt", text: "...Гаряча щоб була." },
  { type: "end", text: "" }
]);

registerScript("stub_lt_health", [
  { type: "say", who: "lt", text: "Покажи руку." },
  { type: "say", who: "lt", text: "Ти нормально їси? Бо виглядаєш паршиво." },
  { type: "end", text: "" }
]);

registerScript("stub_lt_sarcasm", [
  { type: "say", who: "lt", text: "О, ти. Живий. Яка несподіванка." },
  { type: "end", text: "" }
]);

registerScript("stub_lt_sleep", [
  { type: "say", who: "lt", text: "Іди спати. Це не прохання, це діагноз." },
  { type: "end", text: "" }
]);

registerScript("stub_lt_weather", [
  { type: "say", who: "lt", text: "Погода. Не знаю. Тут немає вікон." },
  { type: "say", who: "lt", text: "І це мене влаштовує." },
  { type: "end", text: "" }
]);

registerScript("stub_lt_patients", [
  { type: "say", who: "lt", text: "Знаєш скільки разів я зшивала Квінсі?" },
  { type: "say", who: "lt", text: "Сім. Сім разів." },
  { type: "end", text: "" }
]);

registerScript("stub_lt_silence", [
  { type: "say", who: "lt", text: "Ш-ш-ш. Зайнята." },
  { type: "end", text: "" }
]);

registerScript("stub_lt_research", [
  { type: "say", who: "lt", text: "Дослідження. Не питай яке. Не скажу." },
  { type: "end", text: "" }
]);

registerScript("stub_lt_cynicism", [
  { type: "say", who: "lt", text: "Знаєш що найгірше в цьому місці?" },
  { type: "say", who: "lt", text: "Все." },
  { type: "say", who: "lt", text: "Ні, жартую. Найгірше — кава." },
  { type: "end", text: "" }
]);


// ────────────────────────────────────
// АМІР — ентузіаст, технік, ігри
// ────────────────────────────────────

registerScript("stub_am_games", [
  { type: "say", who: "am", text: "Марті! Скільки пальців треба для Mortal Kombat?" },
  { type: "say", who: "am", text: "Десять. І нерви. Багато нервів." },
  { type: "end", text: "" }
]);

registerScript("stub_am_electronics", [
  { type: "say", who: "am", text: "Лагодив блок живлення. Три рази вдарило." },
  { type: "say", who: "am", text: "Але працює!" },
  { type: "end", text: "" }
]);

registerScript("stub_am_future", [
  { type: "say", who: "am", text: "Як думаєш, скільки ми тут будемо?" },
  { type: "say", who: "am", text: "...Не відповідай. Я не хочу знати." },
  { type: "end", text: "" }
]);

registerScript("stub_am_food", [
  { type: "say", who: "am", text: "Чіпси в автоматі закінчились вчора." },
  { type: "say", who: "am", text: "Це трагедія, Марті. Серйозно." },
  { type: "end", text: "" }
]);

registerScript("stub_am_sleep", [
  { type: "say", who: "am", text: "Не спав до четвертої. Новий рівень в Pac-Man." },
  { type: "say", who: "am", text: "Вартувало." },
  { type: "end", text: "" }
]);

registerScript("stub_am_weather", [
  { type: "say", who: "am", text: "Хмарно?" },
  { type: "say", who: "mc", text: "Не знаю." },
  { type: "say", who: "am", text: "Я теж. Тут нема вікон. Забув." },
  { type: "end", text: "" }
]);

registerScript("stub_am_high_score", [
  { type: "say", who: "am", text: "Марті! Новий рекорд в Tetris! 847291!" },
  { type: "say", who: "am", text: "...Квінсі побив вчора. 850000. Ненавиджу." },
  { type: "end", text: "" }
]);

registerScript("stub_am_mall_people", [
  { type: "say", who: "am", text: "Раніше тут були люди. Тисячі." },
  { type: "say", who: "am", text: "А тепер нас шестеро. Ну, семеро з тобою." },
  { type: "end", text: "" }
]);

registerScript("stub_am_energy", [
  { type: "say", who: "am", text: "Мені потрібен енергетик. Або три." },
  { type: "say", who: "am", text: "Автомат видає тільки колу. Трагедія продовжується." },
  { type: "end", text: "" }
]);

registerScript("stub_am_jokes", [
  { type: "say", who: "am", text: "Знаєш чому програмісти не виходять на вулицю?" },
  { type: "say", who: "am", text: "Бо там NullPointerException." },
  { type: "say", who: "am", text: "...Ніхто не сміється. Як завжди." },
  { type: "end", text: "" }
]);


// ────────────────────────────────────
// АОІ — тиха, музика, орігамі
// ────────────────────────────────────

registerScript("stub_ao_origami", [
  { type: "say", who: "ao", text: "Журавлик. Сьогодні двадцять третій." },
  { type: "say", who: "ao", text: "До тисячі — далеко." },
  { type: "end", text: "" }
]);

registerScript("stub_ao_music", [
  { type: "say", who: "ao", text: "Слухаю. Не заважай." },
  { type: "say", who: "ao", text: "...Якщо хочеш — сідай. Мовчки." },
  { type: "end", text: "" }
]);

registerScript("stub_ao_bubbletea", [
  { type: "say", who: "ao", text: "Bubble tea. Там, в автоматі. Якщо знайдеш — мені таро." },
  { type: "end", text: "" }
]);

registerScript("stub_ao_bikes", [
  { type: "say", who: "ao", text: "В гаражі є скутер. Зламаний." },
  { type: "say", who: "ao", text: "Якщо знайдеш запчастини — я полагоджу." },
  { type: "end", text: "" }
]);

registerScript("stub_ao_sleep", [
  { type: "say", who: "ao", text: "Поганий сон?" },
  { type: "say", who: "ao", text: "Я теж." },
  { type: "end", text: "" }
]);

registerScript("stub_ao_weather", [
  { type: "say", who: "ao", text: "Тихо сьогодні." },
  { type: "end", text: "" }
]);

registerScript("stub_ao_quincy_noise", [
  { type: "say", who: "ao", text: "Квінсі в тирі. Знову." },
  { type: "say", who: "ao", text: "Через три стіни чутно. Вражає." },
  { type: "end", text: "" }
]);

registerScript("stub_ao_mall_stores", [
  { type: "say", who: "ao", text: "Книгарня на другому. Туди мало хто ходить." },
  { type: "say", who: "ao", text: "Саме тому — моя улюблена." },
  { type: "end", text: "" }
]);

registerScript("stub_ao_dreams", [
  { type: "say", who: "ao", text: "Сниться океан. Щоночі." },
  { type: "say", who: "ao", text: "Не знаю що це значить." },
  { type: "end", text: "" }
]);

registerScript("stub_ao_stars", [
  { type: "say", who: "ao", text: "На даху видно зірки. Якщо не хмарно." },
  { type: "say", who: "ao", text: "Раджу." },
  { type: "end", text: "" }
]);


// ────────────────────────────────────
// КВІНСІ — тролінг, англійський сленг, снайпер
// ────────────────────────────────────

registerScript("stub_qu_weapons", [
  { type: "say", who: "qu", text: "Чистив гвинтівку. Не підходь." },
  { type: "say", who: "qu", text: "Жартую. Підходь. Але повільно." },
  { type: "end", text: "" }
]);

registerScript("stub_qu_silence", [
  { type: "say", who: "qu", text: "..." },
  { type: "say", who: "qu", text: "Чого стоїш?" },
  { type: "end", text: "" }
]);

registerScript("stub_qu_trolling", [
  { type: "say", who: "qu", text: "Знаєш що я зробив зранку?" },
  { type: "say", who: "mc", text: "Ні." },
  { type: "say", who: "qu", text: "I'm not gonna tell ya." },
  { type: "end", text: "" }
]);

registerScript("stub_qu_training", [
  { type: "say", who: "qu", text: "800 метрів. Вітер зліва. Одна куля." },
  { type: "say", who: "qu", text: "Хочеш спробувати?" },
  { type: "say", who: "qu", text: "Та ні, ти не хочеш." },
  { type: "end", text: "" }
]);

registerScript("stub_qu_sleep", [
  { type: "say", who: "qu", text: "Спав як мертвий." },
  { type: "say", who: "qu", text: "Це... не метафора. Я реально не ворушився 8 годин." },
  { type: "end", text: "" }
]);

registerScript("stub_qu_weather", [
  { type: "say", who: "qu", text: "Rain." },
  { type: "say", who: "qu", text: "Hate it." },
  { type: "end", text: "" }
]);

registerScript("stub_qu_amir_loud", [
  { type: "say", who: "qu", text: "Амір оре з аркад. Знову програв." },
  { type: "say", who: "qu", text: "Lovely." },
  { type: "end", text: "" }
]);

registerScript("stub_qu_film", [
  { type: "say", who: "qu", text: "Дивився фільм. Поганий. Два рази." },
  { type: "say", who: "qu", text: "Не питай чому." },
  { type: "end", text: "" }
]);

registerScript("stub_qu_accuracy", [
  { type: "say", who: "qu", text: "97.3%. Мій відсоток влучань." },
  { type: "say", who: "qu", text: "2.7% — то я мигнув." },
  { type: "end", text: "" }
]);

registerScript("stub_qu_boredom", [
  { type: "say", who: "qu", text: "Нудно." },
  { type: "say", who: "qu", text: "Absolutely. Boring." },
  { type: "say", who: "qu", text: "Йди звідси поки я не почав стріляти по банках." },
  { type: "end", text: "" }
]);


// ────────────────────────────────────
// ЗАГАЛЬНА ЗАГЛУШКА — якщо нічого не знайдено
// ────────────────────────────────────

registerScript("generic_stub", [
  { type: "say", who: null, text: "Мовчанка. Іноді це — найкраща розмова." },
  { type: "end", text: "" }
]);


// ────────────────────────────────────
// КАВА — сцена дарування кави NPC
// ────────────────────────────────────

registerScript("coffee_give_scene", [
  { type: "say", who: "mc", text: "Тримай. Приніс каву." },
  { type: "label", id: "coffee_react" },
  { type: "end", text: "" }
]);
