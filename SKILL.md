# SKILL.md — Ren'Py Screen Language для Drifter Loop

Цей скіл вирішує конкретну проблему: Claude погано пише Ren'Py screens.
Діалоги, логіка, Python — добре. Screens — погано. Причина: нішевий DSL
з неочевидними правилами. Цей документ закриває прогалини.

---

## КРИТИЧНІ ПРАВИЛА (порушення = зламаний UI)

### 1. НІКОЛИ не змішуй pos і align по одній осі

```renpy
# ЗЛАМАЄ — ypos + yalign конфлікт:
hbox:
    xpos 80 ypos 40
    yalign 0.0           # ← КОНФЛІКТ з ypos

# ПРАВИЛЬНО — або pos, або align:
hbox:
    xpos 80 ypos 40      # позиція по обох осях через pos
    
hbox:
    xalign 0.5 yalign 0.5  # або через align
```

Правило: `xpos` несумісний з `xalign`, `ypos` несумісний з `yalign`.
Якщо задав `ypos` — не чіпай `yalign` (і навпаки).

### 2. Return() ЗАБОРОНЕНО в overlay screens під час діалогу

```renpy
# ЗЛАМАЄ — Return() під час say interaction:
screen my_overlay():
    button:
        action Return("clicked")  # ← вбиває say, діалог стрибає

# ПРАВИЛЬНО — Function() для overlay:
screen my_overlay():
    button:
        action Function(my_handler)  # ← безпечно під час say
```

Return() дозволено ТІЛЬКИ в screens які викликані через `call screen`.
Для `show screen` під час діалогу — тільки Function(), SetVariable(), NullAction().

### 3. Solid() і кольори — ЗАВЖДИ в лапках

```renpy
# ПРАВИЛЬНО:
background Solid("#0d0d1acc")
add Solid("#ffffff10", xsize=100, ysize=1)

# ЗЛАМАЄ:
background #0d0d1acc        # ← не displayable
```

### 4. vpgrid вимагає cols АБО rows

```renpy
# ПРАВИЛЬНО:
vpgrid:
    cols 1
    spacing 8
    mousewheel True
    # ...елементи

# ЗЛАМАЄ — vpgrid без cols/rows:
vpgrid:
    spacing 8
    # ...елементи → помилка
```

### 5. screen з use — дочірній screen не може мати modal/tag/zorder

```renpy
# ПРАВИЛЬНО — зовнішній screen задає modal:
screen parent():
    modal True
    use child_content()

screen child_content():
    # Просто контент, без modal/tag
    vbox:
        text "Контент"

# ЗЛАМАЄ:
screen child_content():
    modal True  # ← ігнорується або помилка
```

---

## ПАТЕРНИ ДЛЯ SCREENS

### Патерн 1: Повноекранне меню (save, load, journal, gallery)

```renpy
screen my_menu():
    tag menu     # закриває інші menu screens

    # 1. Фон — ЗАВЖДИ першим
    add Solid("#09090f")

    # 2. Заголовок
    text "НАЗВА" xpos 80 ypos 40 size 48 color "#d8b4fe" bold True

    # 3. Кнопка назад
    textbutton "◄ НАЗАД":
        xpos 80 ypos 980
        action Return()
        text_size 20
        text_color "#ffffff40"
        text_hover_color "#d8b4fe"

    # 4. Скролюваний контент
    vpgrid:
        xpos 80 ypos 120
        xsize 1100 ysize 840
        cols 1
        spacing 8
        mousewheel True
        scrollbars "vertical"

        # ...елементи
```

### Патерн 2: Overlay поверх діалогу (пейджер, HUD, сповіщення)

```renpy
screen my_overlay():
    zorder 90     # вище за say (default), hud (50)
    # НЕ modal — кліки проходять до say window
    # НЕ tag menu — не закриває інші screens

    fixed:
        xpos 1900 ypos 1060
        xanchor 1.0 yanchor 1.0
        xsize 400 ysize 220

        # Контент...

        # Кнопки — ТІЛЬКИ Function/SetVariable:
        button:
            action Function(my_handler)
```

### Патерн 3: Modal popup (interact menu, confirmation)

```renpy
screen my_popup():
    modal True    # блокує кліки на фон
    tag interact  # закриває інші interact screens

    # Напівпрозорий фон
    add Solid("#00000066")

    vbox:
        align (0.5, 0.5)
        spacing 8
        xmaximum 700

        # Контент...

        button:
            action Return("result")  # Return() ОК тут — це call screen
```

### Патерн 4: Кнопка-слот (для save/load, missions, inventory)

```renpy
screen _slot_btn(slot_id, slot_action):
    button:
        xfill True
        ysize 82
        action slot_action
        padding (16, 10, 16, 10)
        background Solid("#a855f710")
        hover_background Solid("#a855f720")

        hbox:
            spacing 16
            yalign 0.5
            # ...контент
```

---

## СТИЛІ ПРОЄКТУ

### Кольорова палітра

```
Фон:          #09090f (чорний з синім відтінком)
Панелі:       #0d0d1acc, #0d0d1ae0 (напівпрозорі)
Текст:        #d4cfc6 (основний), #d8b4fe (акцент/фіолетовий)
Приглушений:  #ffffff40, #ffffff30, #ffffff20 (рівні прозорості)
Жовтий:       #facc15 (виділення, гроші, автослот)
Блакитний:    #a5f3fc (час, інформація)
Червоний:     #fca5a5, #ef4444 (небезпека, HP, Квінсі)
Рожевий:      #d946ef, #f0abfc (Аоі)
```

### Кольори персонажів

```
Артур:    #a0c4ff / #4a7cff (синій)
Елеонор:  #d8b4fe / #a855f7 (фіолетовий)
Летті:    #a5f3fc / #22d3ee (блакитний)
Амір:     #fef08a / #facc15 (жовтий)
Аоі:      #f0abfc / #d946ef (рожевий)
Квінсі:   #fca5a5 / #ef4444 (червоний)
Дріфтер:  #facc15 / #a855f7
```

### Шрифти

```
Моноширинний (пейджер, дані): fonts/JetBrainsMono-Bold.ttf, fonts/JetBrainsMono-Regular.ttf
Fallback (якщо немає шрифту): не вказуй font — Ren'Py візьме default
```

### Стилі кнопок (вже визначені в screens.rpy)

```
hex_btn          — стандартна (фіолетова підсвітка)
hex_btn_disabled — неактивна (темна)
hex_btn_accent   — акцент (жовта підсвітка)
interact_btn     — для interact menu (повна ширина)
interact_btn_bonus — для bonus options (жовта)
interact_btn_dismiss — для "піти" (приглушена)
```

---

## АРХІТЕКТУРА SCREENS В ПРОЄКТІ

### Файлова структура

```
game/screens/
├── screens.rpy          — navigation, hud, pager_hud, location_ui, стилі
├── screen_say.rpy       — діалогове вікно (KIM style)
├── screen_choice.rpy    — menu вибору
├── screen_interact.rpy  — підменю NPC (topics + bonus + gift)
├── screen_save.rpy      — збереження/завантаження
├── screen_map.rpy       — карта молу
├── screen_missions.rpy  — список місій
├── screen_journal.rpy   — щоденник
├── screen_thought_cabinet.rpy — шафа думок
├── screen_gallery.rpy   — галерея CG
├── screen_shop.rpy      — магазин
├── screen_squad.rpy     — інфо по персонажах
├── screen_pager.rpy     — promise overlay (старий)
├── screen_mainmenu.rpy  — головне меню
├── screen_preferences.rpy — налаштування
├── screen_about.rpy     — про гру
├── screen_telepathy.rpy — ?
```

### zorder ієрархія

```
100  scanlines (overlay ефект)
 90  pager_hud (пейджер — ЗАВЖДИ видно)
 80  promise overlay (screen pager)
 50  hud (верхня панель)
 —   say window (default)
 —   location_ui, modals
```

### Коли screen показується

| Screen | Як показується | Як ховається |
|--------|---------------|-------------|
| hud | `show screen hud` в location_loop | `renpy.hide_screen("hud")` в dialogue_begin |
| pager_hud | `show screen pager_hud` після отримання | НІКОЛИ не ховається |
| location_ui | `call screen location_ui` | Автоматично при Return |
| npc_interact_menu | `call screen` | Return |
| save/load | `ShowMenu("save")` | Return |
| mall_map | `call screen mall_map` | Return |

---

## ПЕЙДЖЕР — КЛЮЧОВИЙ КОМПОНЕНТ

### Проблема

Пейджер має працювати ПОВЕРХ діалогу. Кнопки prev/next/accept/decline
мають реагувати на кліки БЕЗ переривання say interaction.

### Рішення

1. `zorder 90` — вище за say
2. Кнопки використовують `Function()`, НЕ `Return()`
3. Accept/decline записують результат в `store.pager_response`
4. `location_loop` перевіряє `has_pending_pager()` і виконує label
5. `dialogue_begin()` НЕ ховає пейджер

### Змінні пейджера (vars.rpy)

```python
pager_messages = []        # [{"who": "Аоі", "text": "..."}, ...]
pager_mode = "status"      # "status" | "message" | "request"
pager_msg_index = 0
pager_unread = False
pager_request_who = ""
pager_request_text = ""
pager_request_accept = None   # label
pager_request_decline = None  # label
pager_response = None         # None | "accept" | "decline"
```

### Функції (dispatcher.rpy)

```python
add_pager_message(who, text)         # додати повідомлення
pager_send_request(who, text, accept_label, decline_label)
pager_click()                        # звук кнопки
pager_prev_msg() / pager_next_msg()  # навігація
pager_dismiss()                      # toggle status/messages
clear_pager()                        # очистити (next_day)
_pager_accept() / _pager_decline()   # обробка accept/decline
has_pending_pager()                  # перевірка
consume_pager_response()             # забрати результат
```

---

## dialogue_begin / dialogue_end

```python
def dialogue_begin():
    """Ховає HUD. НЕ ховає пейджер. Скидає лічильник реплік."""
    store.dialogue_line_count = 0
    renpy.hide_screen("hud")
    # НЕ ховати pager_hud!

def dialogue_end():
    """Списує час (count × 3 хв). Повертає HUD."""
    mins = store.dialogue_line_count * DIALOGUE_TIME_PER_LINE
    if mins > 0:
        advance_time(mins)
    store.dialogue_line_count = 0
    renpy.show_screen("hud")
```

---

## НЕ ЗАЛЕЖАТИ ВІД ЗОВНІШНІХ PNG ДЛЯ UI

Якщо PNG не існує або пошкоджений — screen рендерить порожньо без помилки.
ЗАВЖДИ використовуй Solid() для фонів кнопок і панелей.

```renpy
# ПРАВИЛЬНО — працює завжди:
background Solid("#0d0d1acc")
add Solid("#ffffff10", xsize=580, ysize=1)  # роздільник

# РИЗИКОВАНО — якщо файлу нема, нічого не видно:
background "gui/save/save_slot.png"
```

Виняток: декоративні елементи (пейджер каркас, ефекти) де відсутність
PNG = просто нема декору, а не зламаний UI.

---

## ТЕСТУВАННЯ SCREEN

Після написання/зміни screen — перевірити:

1. Ren'Py стартує без помилок (синтаксис)
2. Screen відображається (щось видно на екрані)
3. Кнопки клікабельні (hover працює)
4. Return/Function правильно обраний (див. правило #2)
5. Скрол працює (для vpgrid — перевірити mousewheel)
6. Текст не вилазить за межі (xmaximum, xsize)

Для дебагу: `Shift+D` в грі → console → `renpy.show_screen("screen_name")`

---

## SAVE/LOAD МЕТАДАНІ

vars.rpy зберігає метадані в кожному save через `config.save_json_callbacks`:

```python
def _save_metadata(d):
    d["_game_day"] = store.day
    d["_game_time"] = store.minutes
    d["_game_location"] = store.current_location
    d["_game_chemistry"] = dict(store.chemistry)
    d["_game_hex_rep"] = store.hex_rep
```

Читати: `renpy.slot_json(slot)` → dict з цими полями.

---

## ЧЕКЛИСТ ПЕРЕД ВІДПРАВКОЮ SCREEN

- [ ] Немає змішування pos + align по одній осі
- [ ] Return() тільки в call screen, Function() для show screen
- [ ] Фони через Solid(), не PNG (крім декору)
- [ ] vpgrid має cols або rows
- [ ] zorder відповідає ієрархії (90 пейджер, 50 hud)
- [ ] Кольори з палітри проєкту
- [ ] Текст з правильним розміром (48 заголовки, 20 кнопки, 14-16 інфо)
- [ ] Тестовий запуск пройшов
