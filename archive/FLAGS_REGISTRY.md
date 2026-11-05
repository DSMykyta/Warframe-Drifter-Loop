# РЕЄСТР ФЛАГІВ — Drifter Loop

Кожен флаг, де він ставиться, що означає, і де використовується як тригер.

**Правило:** при створенні нового флагу — додай його сюди. Іменування: `NAMING_CONVENTIONS.md`.

---

## ІНТРО

| Флаг | Файл | Контекст | Тригер для |
|------|------|----------|------------|
| `intro_done` | scenes/intro.rpy | Інтро пройдено | script.rpy — пропуск інтро |
| `intro_dark_humor` | scenes/intro.rpy | Гравець: "З Новим Роком" | — |
| `intro_asked_to_verify` | scenes/intro.rpy | Гравець: "Перевірте" | — |
| `intro_stayed_silent` | scenes/intro.rpy | Гравець промовчав | — |
| `intro_military_response` | scenes/intro.rpy | Гравець: "Так точно" | — |
| `intro_sarcastic_response` | scenes/intro.rpy | Гравець пожартував про стілець | — |
| `intro_promised` | scenes/intro.rpy | Гравець: "Обіцяю" | — |
| `nickname_marty` | scenes/intro.rpy | Тільки петля 1 — думки про прізвисько | Гілка "хто такий Марті" |
| `lettie_bandaged_hand` | scenes/intro.rpy | Летті перев'язала руку | intro — інсайт lettie_medic |

## ЗНАЙОМСТВА

| Флаг | Файл | Контекст | Тригер для |
|------|------|----------|------------|
| `met_arthur` | scenes/intro.rpy | Зустрів Артура | — |
| `met_aoi` | scenes/intro.rpy | Зустрів Аоі | — |
| `met_amir` | scenes/intro.rpy | Зустрів Аміра | — |
| `met_quincy` | scenes/intro.rpy | Зустрів Квінсі | — |
| `met_lettie` | scenes/intro.rpy | Зустрів Летті | — |
| `met_eleanor` | scenes/intro.rpy | Зустрів Елеонор | — |

## АРТУР — ДІАЛОГИ

| Флаг | Файл | Контекст | Тригер для |
|------|------|----------|------------|
| `arthur_intro_done` | dialogues/arthur/arthur_intro.rpy | Інтро-діалог | Всі діалоги Артура, парні, місійні |
| `arthur_about_team_done` | dialogues/arthur/arthur_about_team.rpy | Про команду | arthur_middle_name |
| `arthur_daily_routine_done` | dialogues/arthur/arthur_daily_routine.rpy | Розпорядок дня | — |
| `arthur_atomicycle_done` | dialogues/arthur/arthur_atomicycle.rpy | Атомоцикл | — |
| `arthur_cooking_done` | dialogues/arthur/arthur_cooking.rpy | Про готування | arthur_drinks_invite, group_backroom_dinner |
| `arthur_middle_name_done` | dialogues/arthur/arthur_middle_name.rpy | По-батькові | arthur_skana_story |
| `arthur_drinks_invite_done` | dialogues/arthur/arthur_drinks_invite.rpy | Запросив у бар | arthur_skana_story |
| `arthur_skana_story_done` | dialogues/arthur/arthur_skana_story.rpy | Історія Скани | arthur_eleanor_secret |
| `arthur_eleanor_secret_done` | dialogues/arthur/arthur_eleanor_secret.rpy | Секрет Елеонор | arthur_icr_trauma |
| `arthur_icr_trauma_done` | dialogues/arthur/arthur_icr_trauma.rpy | ICR травма | arthur_future |
| `arthur_future_done` | dialogues/arthur/arthur_future.rpy | Про майбутнє | — |
| `arthur_leadership_burden_done` | dialogues/arthur/arthur_leadership_burden.rpy | Тягар лідерства | — |
| `arthur_trust_milestone_done` | dialogues/arthur/arthur_trust_milestone.rpy | Milestone хімія 60 | — |
| `arthur_friends_milestone_done` | dialogues/arthur/arthur_friends_milestone.rpy | Milestone хімія 120 | romance_confession |

## ЕЛЕОНОР — ДІАЛОГИ

| Флаг | Файл | Контекст | Тригер для |
|------|------|----------|------------|
| `eleanor_intro_done` | dialogues/eleanor/eleanor_intro.rpy | Інтро-діалог | Всі діалоги Елеонор |
| `eleanor_journalism_done` | dialogues/eleanor/eleanor_journalism.rpy | Журналістика | eleanor_journalism_past |
| `eleanor_journalism_past_done` | dialogues/eleanor/eleanor_journalism_past.rpy | Минуле журналістки | — |
| `eleanor_control_done` | dialogues/eleanor/eleanor_control.rpy | Контроль | eleanor_control_issues |
| `eleanor_control_issues_done` | dialogues/eleanor/eleanor_control_issues.rpy | Проблеми контролю | — |
| `eleanor_observations_done` | dialogues/eleanor/eleanor_observations.rpy | Спостереження | eleanor_techrot_hints |
| `eleanor_techrot_hints_done` | dialogues/eleanor/eleanor_techrot_hints.rpy | Підказки Техроту | eleanor_techrot_reveal |
| `eleanor_techrot_reveal_done` | dialogues/eleanor/eleanor_techrot_reveal.rpy | Техрот розкрито | — |
| `eleanor_twin_perspective_done` | dialogues/eleanor/eleanor_twin_perspective.rpy | Близнюки | — |
| `eleanor_petersham_tease_done` | dialogues/eleanor/eleanor_petersham_tease.rpy | Жарт Петершем | — |
| `eleanor_vulnerability_done` | dialogues/eleanor/eleanor_vulnerability.rpy | Вразливість | — |
| `eleanor_trust_milestone_done` | dialogues/eleanor/eleanor_trust_milestone.rpy | Milestone 60 | — |
| `eleanor_friends_milestone_done` | dialogues/eleanor/eleanor_friends_milestone.rpy | Milestone 120 | romance_confession |

## ЛЕТТІ — ДІАЛОГИ

| Флаг | Файл | Контекст | Тригер для |
|------|------|----------|------------|
| `lettie_intro_done` | dialogues/lettie/lettie_intro.rpy | Інтро-діалог | Всі діалоги Летті |
| `lettie_rats_done` | dialogues/lettie/lettie_rats.rpy | Щури | lettie_rat_names |
| `lettie_rat_names_done` | dialogues/lettie/lettie_rat_names.rpy | Імена щурів | — |
| `lettie_coffee_done` | dialogues/lettie/lettie_coffee.rpy | Кава | lettie_coffee_addiction |
| `lettie_coffee_addiction_done` | dialogues/lettie/lettie_coffee_addiction.rpy | Залежність | — |
| `lettie_medical_ethics_done` | dialogues/lettie/lettie_medical_ethics.rpy | Медична етика | lettie_why_medic |
| `lettie_cynicism_done` | dialogues/lettie/lettie_cynicism.rpy | Цинізм | — |
| `lettie_why_medic_done` | dialogues/lettie/lettie_why_medic.rpy | Чому медик | lettie_medbay_checkup |
| `lettie_medbay_checkup_done` | dialogues/lettie/lettie_medbay_checkup.rpy | Огляд | lettie_breakdown |
| `lettie_breakdown_done` | dialogues/lettie/lettie_breakdown.rpy | Зрив | — |
| `lettie_trust_milestone_done` | dialogues/lettie/lettie_trust_milestone.rpy | Milestone 60 | — |
| `lettie_friends_milestone_done` | dialogues/lettie/lettie_friends_milestone.rpy | Milestone 120 | romance_confession |

## АМІР — ДІАЛОГИ

| Флаг | Файл | Контекст | Тригер для |
|------|------|----------|------------|
| `amir_intro_done` | dialogues/amir/amir_intro.rpy | Інтро-діалог | Всі діалоги Аміра |
| `amir_gaming_done` | dialogues/amir/amir_gaming.rpy | Ігри | amir_high_score |
| `amir_electronics_done` | dialogues/amir/amir_electronics.rpy | Електроніка | amir_loyalty |
| `amir_nightmares_hint_done` | dialogues/amir/amir_nightmares_hint.rpy | Підказка кошмарів | amir_nightmares |
| `amir_nightmares_done` | dialogues/amir/amir_nightmares.rpy | Кошмари | amir_past_life |
| `amir_loyalty_done` | dialogues/amir/amir_loyalty.rpy | Лояльність | amir_loyalty_deep |
| `amir_loyalty_deep_done` | dialogues/amir/amir_loyalty_deep.rpy | Глибока лояльність | — |
| `amir_high_score_done` | dialogues/amir/amir_high_score.rpy | Рекорд | — |
| `amir_past_life_done` | dialogues/amir/amir_past_life.rpy | Минуле | — |
| `amir_trust_milestone_done` | dialogues/amir/amir_trust_milestone.rpy | Milestone 60 | — |
| `amir_friends_milestone_done` | dialogues/amir/amir_friends_milestone.rpy | Milestone 120 | romance_confession |

## АОІ — ДІАЛОГИ

| Флаг | Файл | Контекст | Тригер для |
|------|------|----------|------------|
| `aoi_intro_done` | dialogues/aoi/aoi_intro.rpy | Інтро-діалог | Всі діалоги Аоі |
| `aoi_origami_done` | dialogues/aoi/aoi_origami.rpy | Орігамі | aoi_onlyne_music |
| `aoi_onlyne_music_done` | dialogues/aoi/aoi_onlyne_music.rpy | Музика | aoi_music_meaning |
| `aoi_bubbletea_done` | dialogues/aoi/aoi_bubbletea.rpy | Бабл-ті | aoi_bubbletea_promise |
| `aoi_bubbletea_promise_done` | dialogues/aoi/aoi_bubbletea_promise.rpy | Обіцянка | — |
| `aoi_logistics_done` | dialogues/aoi/aoi_logistics.rpy | Логістика | aoi_noticed_arthur |
| `aoi_music_meaning_done` | dialogues/aoi/aoi_music_meaning.rpy | Значення музики | — |
| `aoi_noticed_arthur_done` | dialogues/aoi/aoi_noticed_arthur.rpy | Помітила Артура | aoi_icr_past |
| `aoi_icr_past_done` | dialogues/aoi/aoi_icr_past.rpy | ICR минуле | aoi_full_story |
| `aoi_full_story_done` | dialogues/aoi/aoi_full_story.rpy | Повна історія | aoi_vulnerability |
| `aoi_vulnerability_done` | dialogues/aoi/aoi_vulnerability.rpy | Вразливість | — |
| `aoi_trust_milestone_done` | dialogues/aoi/aoi_trust_milestone.rpy | Milestone 60 | — |
| `aoi_friends_milestone_done` | dialogues/aoi/aoi_friends_milestone.rpy | Milestone 120 | romance_confession |

## КВІНСІ — ДІАЛОГИ

| Флаг | Файл | Контекст | Тригер для |
|------|------|----------|------------|
| `quincy_intro_done` | dialogues/quincy/quincy_intro.rpy | Інтро-діалог | Всі діалоги Квінсі |
| `quincy_camera_done` | dialogues/quincy/quincy_camera.rpy | Камера | quincy_sarcasm |
| `quincy_sarcasm_done` | dialogues/quincy/quincy_sarcasm.rpy | Сарказм | quincy_training |
| `quincy_training_done` | dialogues/quincy/quincy_training.rpy | Тренування | quincy_vhs |
| `quincy_vhs_done` | dialogues/quincy/quincy_vhs.rpy | VHS | quincy_vhs_meaning |
| `quincy_vhs_meaning_done` | dialogues/quincy/quincy_vhs_meaning.rpy | Значення VHS | quincy_sniper_philosophy |
| `quincy_sniper_philosophy_done` | dialogues/quincy/quincy_sniper_philosophy.rpy | Філософія | quincy_loneliness |
| `quincy_loneliness_done` | dialogues/quincy/quincy_loneliness.rpy | Самотність | quincy_past |
| `quincy_past_done` | dialogues/quincy/quincy_past.rpy | Минуле | — |
| `quincy_trust_milestone_done` | dialogues/quincy/quincy_trust_milestone.rpy | Milestone 60 | — |
| `quincy_friends_milestone_done` | dialogues/quincy/quincy_friends_milestone.rpy | Milestone 120 | romance_confession |

## МІСІЇ

| Флаг | Файл | Контекст | Тригер для |
|------|------|----------|------------|
| `mission_arthur_praised` | events/missions/arthur_mission_5.rpy | Похвалив гравця | — |
| `mission_amir_found_components` | events/missions/amir_mission_3.rpy | Знайшов компоненти | — |
| `mission_quincy_acknowledged_teamwork` | events/missions/quincy_mission_5.rpy | Визнав команду | — |
| `mission_lettie_showed_concern` | events/missions/lettie_mission_5.rpy | Турбота | — |
| `mission_eleanor_noticed_detail` | events/missions/eleanor_mission_5.rpy | Помітила деталь | — |
| `mission_aoi_found_passage` | events/missions/aoi_mission_4.rpy | Знайшла прохід | — |

## ГРУПОВІ СЦЕНИ

| Флаг | Файл | Контекст | Тригер для |
|------|------|----------|------------|
| `group_bar_night_done` | events/group/bar_night.rpy | Вечір у барі | — |
| `group_arcade_tournament_done` | events/group/arcade_tournament.rpy | Турнір | — |
| `group_backroom_dinner_done` | events/group/backroom_dinner.rpy | Вечеря | — |
| `group_rooftop_stargazing_done` | events/group/rooftop_stargazing.rpy | Зірки | — |
| `group_cooking_together_offered` | events/group/backroom_dinner.rpy | Артур запропонував готувати | — |
| `group_bar_tonight_active` | (ставиться діалогом) | Сьогодні вечірка | triggers.rpy — всі NPC в бар |

## ПАРНІ СЦЕНИ

| Флаг | Файл | Контекст | Тригер для |
|------|------|----------|------------|
| `pair_amir_aoi_arcade_seen` | events/pairs/amir_aoi_arcade.rpy | Амір+Аоі в аркадах | — |
| `pair_aoi_lettie_medbay_seen` | events/pairs/aoi_lettie_medbay.rpy | Аоі+Летті в медвідділі | — |
| `pair_arthur_quincy_rooftop_seen` | events/pairs/arthur_quincy_rooftop.rpy | Артур+Квінсі на даху | — |
| `pair_eleanor_lettie_info_seen` | events/pairs/eleanor_lettie_info.rpy | Елеонор+Летті в інфо | — |

## ПОДАРУНКИ

| Флаг | Файл | Контекст | Тригер для |
|------|------|----------|------------|
| `gift_arthur_keychains_done` | events/gifts/arthur_gift_reactions.rpy | Поганий подарунок | Блокує повтор |
| `gift_arthur_roadsigns_done` | events/gifts/arthur_gift_reactions.rpy | Поганий подарунок | Блокує повтор |
| `gift_aoi_toaster_done` | events/gifts/aoi_gift_reactions.rpy | Поганий подарунок | Блокує повтор |
| `gift_aoi_toaster_oven_done` | events/gifts/aoi_gift_reactions.rpy | Поганий подарунок | Блокує повтор |
| `gift_aoi_microwave_done` | events/gifts/aoi_gift_reactions.rpy | Поганий подарунок | Блокує повтор |
| `gift_amir_binder_done` | events/gifts/amir_gift_reactions.rpy | Поганий подарунок | Блокує повтор |
| `gift_amir_notepad_done` | events/gifts/amir_gift_reactions.rpy | Поганий подарунок | Блокує повтор |
| `gift_eleanor_speaker_system_done` | events/gifts/eleanor_gift_reactions.rpy | Поганий подарунок | Блокує повтор |
| `gift_eleanor_speaker_done` | events/gifts/eleanor_gift_reactions.rpy | Поганий подарунок | Блокує повтор |
| `gift_eleanor_hockey_table_done` | events/gifts/eleanor_gift_reactions.rpy | Поганий подарунок | Блокує повтор |
| `gift_quincy_medical_kit_done` | events/gifts/quincy_gift_reactions.rpy | Поганий подарунок | Блокує повтор |
| `gift_lettie_coffee_machine_done` | events/gifts/lettie_gift_reactions.rpy | Подякувала за кавоварку | Блокує повтор |

## ТРИГЕРИ (тимчасові стани)

| Флаг | Файл | Контекст | Тригер для |
|------|------|----------|------------|
| `arthur_eleanor_fight_active` | (ставиться діалогом) | Сварка | triggers.rpy — Артур на дах, Елеонор в бекрум |
| `arthur_fight_resolved` | (ставиться діалогом) | Сварку вирішено | triggers.rpy — знімає тригер сварки |
| `aoi_ingredients_active` | (ставиться діалогом) | Шукає інгредієнти | triggers.rpy — Аоі на футкорт |
| `quincy_angry_active` | (ставиться діалогом) | Злий на гравця | triggers.rpy — Квінсі на дах |

## AWARENESS / ПЛІТКИ

| Флаг | Файл | Контекст | Тригер для |
|------|------|----------|------------|
| `spending_time_arthur_lettie_noticed` | events/awareness/spending_time_arthur.rpy | Летті помітила | — |
| `spending_time_arthur_quincy_noticed` | events/awareness/spending_time_arthur.rpy | Квінсі помітив | — |
| `spending_time_aoi_eleanor_noticed` | events/awareness/spending_time_aoi.rpy | Елеонор помітила | — |
| `spending_time_aoi_amir_noticed` | events/awareness/spending_time_aoi.rpy | Амір помітив | — |
| `neglect_warning_{ім'я}` | events/awareness/neglect_awareness.rpy | Попередження занедбання | — |
| `gossip_warning_{ім'я}` | events/awareness/gossip_reactions.rpy | Плітки дійшли | — |

## РОМАНС

| Флаг | Файл | Контекст | Тригер для |
|------|------|----------|------------|
| `dating_{ім'я}` | romance.rpy | Зустрічається | conditions: dating |
| `breakup_{ім'я}` | romance.rpy | Розрив | — |
| `flirt_caught_by_{ім'я}` | romance.rpy | Партнер бачив флірт | — |
| `romance_confession_{ім'я}_done` | romance.rpy | Зізнання пройдено | — |

## ФІНАЛ / NG+

| Флаг | Файл | Контекст | Тригер для |
|------|------|----------|------------|
| `day30_warning_done` | scenes/finale_win.rpy | Артур попередив | — |
| `arthur_dejavu_noticed` | scenes/loop_restart.rpy | NG+ дежавю | — |
| `arthur_name_known_ng` | scenes/loop_restart.rpy | NG+ знав ім'я | — |
| `eleanor_dejavu_sense_done` | scenes/loop_restart.rpy | NG+ Елеонор відчула | — |
| `ng_quincy_arthur_icr_done` | scenes/loop_restart.rpy | NG+ діалог | — |
| `ng_lettie_eleanor_techrot_done` | scenes/loop_restart.rpy | NG+ діалог | — |
| `ng_amir_lettie_patient_done` | scenes/loop_restart.rpy | NG+ діалог | — |
| `ng_arthur_aoi_past_done` | scenes/loop_restart.rpy | NG+ діалог | — |
| `ng_aoi_amir_nightmares_done` | scenes/loop_restart.rpy | NG+ діалог | — |
| `ng_eleanor_quincy_film_done` | scenes/loop_restart.rpy | NG+ діалог | — |
| `ng_shared_arthur_info` | scenes/loop_restart.rpy | NG+ поділився інфо | — |
