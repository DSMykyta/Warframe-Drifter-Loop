# КОНВЕНЦІЇ ІМЕНУВАННЯ — Drifter Loop

Ім'я = інформація. Не відкриваючи файл і не дивлячись в реєстр — зрозуміти що це.

---

## 1. ФЛАГИ

Формат: `{хто}_{що}_{стан}`

### Суфікси стану

| Суфікс | Значення | Приклад |
|--------|----------|---------|
| `_done` | Діалог/сцена пройдена, не повторюється | `arthur_intro_done` |
| `_seen` | Гравець бачив (banter, парна сцена) | `pair_amir_aoi_arcade_seen` |
| `_active` | Щось зараз відбувається (тимчасовий стан) | `arthur_eleanor_fight_active` |
| `_resolved` | Конфлікт/ситуацію вирішено | `arthur_fight_resolved` |
| `_known` | Гравець дізнався факт | `arthur_icr_known` |
| `_given` | Подарунок/предмет вручено | `lettie_coffee_machine_given` |
| `_refused` | Гравець відмовив | `arthur_drinks_refused` |
| `_accepted` | Гравець погодився | `arthur_drinks_accepted` |
| `_warned` | Попередження видано | `neglect_arthur_warned` |

### Префікси за категорією

| Префікс | Категорія | Приклад |
|---------|-----------|---------|
| `{char}_` | Діалог/подія персонажа | `arthur_cooking_done` |
| `intro_` | Вибір в інтро | `intro_dark_humor` |
| `met_` | Знайомство | `met_arthur` |
| `ng_` | NG+ контент | `ng_quincy_arthur_icr_done` |
| `gift_` | Реакція на подарунок | `gift_arthur_keychains_done` |
| `gossip_` | Плітки | `gossip_arthur_flirt_warned` |
| `neglect_` | Занедбання | `neglect_amir_warned` |
| `mission_` | Подія на місії | `mission_arthur_praised` |
| `pair_` | Парна сцена | `pair_amir_aoi_arcade_seen` |
| `group_` | Групова подія | `group_bar_night_done` |
| `romance_` | Романс | `romance_arthur_confession_done` |
| `dating_` | Зустрічається з | `dating_arthur` |
| `breakup_` | Розрив | `breakup_arthur` |

### Правила

1. **Завжди англійська, lowercase, underscore** — `arthur_cooking_done`, не `Arthur_Cooking_Done`
2. **Персонаж першим** (якщо стосується одного) — `arthur_cooking_done`, не `cooking_arthur_done`
3. **Два персонажі — алфавітний порядок** — `pair_amir_aoi`, не `pair_aoi_amir`
4. **Вибір гравця — дія гравця** — `intro_dark_humor`, `intro_stayed_silent` (що гравець зробив)
5. **Не скорочувати** — `arthur_leadership_burden_done`, не `ar_lead_burd`
6. **Тимчасові стани — `_active`** — знімаються коли ситуація завершена

### Приклади читання

```
arthur_cooking_done         → Артур розповів про готування, діалог пройдений
intro_stayed_silent         → В інтро гравець промовчав
pair_arthur_quincy_seen     → Парну сцену Артур+Квінсі побачено
gift_aoi_toaster_done       → Реакція Аоі на тостер пройдена
neglect_amir_warned         → Попередження про занедбання Аміра видано
ng_eleanor_dejavu_done      → NG+ дежавю Елеонор пройдено
gossip_flirt_caught         → Партнер бачив флірт
```

---

## 2. ФАЙЛИ

### Діалоги: `dialogues/{char}/{char}_{тема}.rpy`

Тема — коротка назва англійською, що відразу зрозуміла:

| Тип | Патерн | Приклад |
|-----|--------|---------|
| Інтро | `{char}_intro` | `arthur_intro.rpy` |
| Якірний | `{char}_{тема}` | `arthur_cooking.rpy` |
| Глибокий | `{char}_{тема}` | `arthur_icr_trauma.rpy` |
| Milestone довіри | `{char}_trust_milestone` | `arthur_trust_milestone.rpy` |
| Milestone друзів | `{char}_friends_milestone` | `arthur_friends_milestone.rpy` |
| Ланцюжок | `{char}_{тема}` з `_done` флагом попереднього | `arthur_skana_story.rpy` |

### Івенти: `events/{тип}/{опис}.rpy`

| Тип | Патерн | Приклад |
|-----|--------|---------|
| Групова сцена | `events/group/{назва}` | `bar_night.rpy` |
| Парний banter | `events/pairs/{char1}_{char2}_{місце}` | `amir_aoi_arcade.rpy` |
| Місійний діалог | `events/missions/{char}_mission_{N}` | `arthur_mission_3.rpy` |
| Реакція подарунок | `events/gifts/{char}_gift_reactions` | `arthur_gift_reactions.rpy` |
| Awareness | `events/awareness/{патерн}_{char}` | `spending_time_arthur.rpy` |

### Сцени: `scenes/{назва}.rpy`

Лінійні, одноразові: `intro.rpy`, `finale_win.rpy`, `finale_lose.rpy`, `loop_restart.rpy`

### Заглушки: `stubs/{char}_stubs.rpy`

Один файл на персонажа: `arthur_stubs.rpy`

### Правила для файлів

1. **Тільки англійська, lowercase, underscore** — `arthur_cooking.rpy`, не `Артур_готування.rpy`
2. **Без номерів окрім місій** — `arthur_cooking.rpy`, не `arthur_dialogue_03.rpy`
3. **Тема = суть діалогу** — прочитав назву = зрозумів про що
4. **Парні — обидва персонажі в алфавітному порядку** — `amir_aoi_arcade`, не `aoi_amir_arcade`
5. **Не дублювати папку в імені** — `dialogues/arthur/arthur_cooking.rpy`, не `dialogues/arthur/arthur_dialogue_cooking.rpy`

---

## 3. LABEL

Формат: збігається з ID файлу і флагу.

```
Файл:  dialogues/arthur/arthur_cooking.rpy
Label: arthur_cooking
Флаг:  arthur_cooking_done
ID:    arthur_cooking
```

Все одне ім'я в різних контекстах + суфікс стану для флагу.

### Винятки

| Тип | Label | Чому |
|-----|-------|------|
| Stub | `stub_Артур_cooking` | Кирилиця в імені (так працює диспетчер) |
| Romance confession | `romance_confession_артур` | Кирилиця (генерується циклом) |

---

## 4. ІНСАЙТИ (ID)

Формат: `{хто/що}_{факт}` — без суфіксу `_done`, бо інсайт не подія а знання.

```
hex_exists          → Гекс існує
arthur_leader       → Артур — лідер
aoi_logistics       → Аоі — логістика
quincy_marksman     → Квінсі — стрілець
lettie_medic        → Летті — медик
nickname_marty      → Прізвисько Марті
```

---

## 5. ЗМІННІ ЩО СТАВЛЯТЬСЯ ДИСПЕТЧЕРОМ

| Змінна | Де | Тип |
|--------|-----|-----|
| `seen_dialogues` | set | ID діалогів що пройдені (збігається з label) |
| `talked_today` | set | Кирилиця, імена NPC з якими говорив сьогодні |
| `flags` | dict | Всі флаги (ключ = ім'я флагу, значення = True) |
| `flags[X + "_day"]` | dict | День коли флаг поставлено |
