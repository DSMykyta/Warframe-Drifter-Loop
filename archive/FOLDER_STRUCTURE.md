# СТРУКТУРА ПРОЄКТУ — Drifter Loop

Як читати: кожна папка має своє призначення. Коли додаєш новий файл — визнач його тип і поклади у відповідне місце.

---

## game/ — ЯДРО

Системні файли. Не чіпати при додаванні контенту.

```
script.rpy              # Головний потік: start, location_loop, execute_mission
vars.rpy                # Всі default змінні
dispatcher.rpy          # Condition-based система: get_dialogue(), build_daily_deck()
day_logic.rpy           # Цикл дня: next_day(), advance_time()
triggers.rpy            # Локації (граф, назви, travel) + тригерний рух NPC
missions.rpy            # Генерація та виконання місій
injuries.rpy            # Стаки травм
promises.rpy            # Обіцянки: create, check, fulfill
gifts.rpy               # Подарункова логіка
inventory.rpy           # Каталог магазину, покупки
romance.rpy             # Романс: зізнання, розрив, наслідки флірту
help_requests.rpy        # Запити допомоги через пейджер
images.rpy              # Layered images, transforms
```

**Принцип:** один файл = одна система. Якщо система нова (наприклад, крафт) — новий файл в корені.

---

## game/screens/ — ЕКРАНИ

Все що гравець бачить як UI. Кожен screen — окремий файл.

```
gui.rpy                 # GUI параметри (розміри, кольори)
options.rpy             # Config гри (назва, версія)
screens.rpy             # HUD, location_ui, navigation, стилі
screen_mainmenu.rpy     # Головне меню
screen_say.rpy          # Діалогове вікно
screen_save.rpy         # Збереження / завантаження
screen_preferences.rpy  # Налаштування
screen_map.rpy          # Інтерактивна мапа молу
screen_missions.rpy     # Меню місій
screen_shop.rpy         # Магазин
screen_journal.rpy      # Щоденник
screen_thought_cabinet.rpy  # Шафа думок
screen_pager.rpy        # Пейджер
screen_about.rpy        # Про гру
```

**Принцип:** новий UI-екран = новий `screen_*.rpy` тут.

---

## game/scenes/ — СЦЕНИ

Лінійні, одноразові послідовності. Не condition-based — викликаються напряму.

```
finale_win.rpy          # Перемога, day30_warning, check_day31
finale_lose.rpy         # Поразка (часова петля)
loop_restart.rpy        # NG+ функції, дежавю діалоги
intro.rpy               # (майбутнє) Вступна сцена
```

**Принцип:** сцена відбувається один раз за проходження. Якщо це повторюваний діалог — він в `dialogues/`.

---

## game/dialogues/ — ДІАЛОГИ

Condition-based діалоги, згруповані по персонажах. Кожен реєструється в `DIALOGUE_ENTRIES`.

```
dialogues/
  {char}/
    {char}_intro.rpy            # Перше знайомство
    {char}_{topic}.rpy          # Якорні та глибокі діалоги
    {char}_trust_milestone.rpy  # Milestone хімії 60
    {char}_friends_milestone.rpy # Milestone хімії 120
    ...
```

**Принцип:** один діалог = один файл. Ім'я = `{персонаж}_{тема}.rpy`. Файл містить `init python` з реєстрацією + label з діалогом.

---

## game/events/ — ІВЕНТИ

Cross-character контент: групові сцени, парні бантери, місійні діалоги, реакції.

```
events/
  group/                # Групові сцени (3+ персонажів)
    bar_night.rpy
    ...
  pairs/                # Парний banter (2 NPC в локації)
    amir_aoi_arcade.rpy
    ...
  missions/             # Міні-діалоги під час місій → MISSION_DIALOGUE_ENTRIES
    {char}_mission_{N}.rpy
    ...
  gifts/                # Реакції на подарунки (по персонажах)
    {char}_gift_reactions.rpy
    ...
  awareness/            # NPC помічають патерни гравця
    spending_time_{char}.rpy
    gossip_reactions.rpy
    ...
```

**Принцип:** якщо контент стосується 2+ персонажів або ситуації (не конкретної розмови) — він тут.

---

## game/stubs/ — ЗАГЛУШКИ

Короткі фрази коли немає eligible діалогів. Автоматично обираються диспетчером.

```
stubs/
  {char}_stubs.rpy      # 10-20 тем на персонажа, label = stub_{Ім'я}_{тема}
```

---

## game/ — РЕСУРСИ

```
backgrounds/            # Фони локацій (.webp, .png)
character_sprites/      # Спрайти персонажів (.png)
fonts/                  # Шрифти
gui/                    # GUI елементи
images/                 # Ігрові зображення
```