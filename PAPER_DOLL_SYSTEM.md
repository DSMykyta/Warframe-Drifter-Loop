# PAPER DOLL SPRITE SYSTEM — Warframe: Drifter Loop

## КОНЦЕПЦІЯ

Персонаж збирається на льоту з шарів. Не один спрайт на комбінацію одягу — а набір файлів які накладаються. 3 штанів × 5 верхів × 4 верхніх шари = 60 комбінацій з ~15 файлів. Місяць без повторів.

---

## СТЕК ШАРІВ (знизу вверх)

| # | Шар | Опис | Приклад |
|---|------|------|---------|
| 1 | Тіло | Базовий template без рук. Від шиї до коліна. Одне на персонажа. | `arthur-body-base.png` |
| 2 | Морда | Емоції. Окремий шар обличчя. Накладається на голову. | `arthur-face-smile.png` |
| 3 | Колготки | Тільки для персонажів з колготками (Елеонор, Летті в барі, Міраж). Інші — пропуск. | `eleanor-tights-black.png` |
| 4 | Штани | Від талії до коліна. Міксуються з будь-яким верхом. | `arthur-pants-501_dark.png` |
| 5 | Кофта | Одяг на торсі. БЕЗ рукавів — руки вирізані, дірки заінпейнчені (AI заповнює одяг під руками). | `arthur-top-white_tshirt.png` |
| 6 | Пояс | Або окремий шар, або частина штанів/кофти. Перекриває стик талії. | `arthur-belt-brown_leather.png` |
| 7 | Куртка | ТІЛЬКИ торс без рукавів. Поли куртки. Інпейнт під руками. | `arthur-jacket-perfecto_torso.png` |
| 8 | Руки | Голі передпліччя + кисті в позі. Один спрайт на позу. | `arthur-arms-crossed_bare.png` |
| 9 | Рукава | Прив'язані до конкретної куртки. Накладаються поверх голих рук. | `arthur-sleeves-perfecto.png` |
| 10 | Чокер | Шия: чокер, шарф, ланцюжок. | `arthur-neck-scarf_charcoal.png` |
| 11 | Окуляри | Верхній шар. Окуляри, берет, серьги. | `amir-glasses-yellow_round.png` |

---

## КЛЮЧОВЕ РІШЕННЯ: ПОРЯДОК ШАРІВ ЗМІНЮЄТЬСЯ

Куртка розстебнута vs застебнута — два різних стеки:

### Куртка розстебнута (поли обрамляють тіло):
```
1. Тіло
2. Морда
3. Штани
4. Кофта (футболка)
5. Руки (голі, схрещені)
6. Куртка (поли лягають ПОВЕРХ рук, обрамляють)
7. Аксесуари
```

### Куртка застебнута (руки поверх куртки):
```
1. Тіло
2. Морда
3. Штани
4. Кофта (футболка, ледь видно)
5. Куртка (торс без рукавів)
6. Руки (голі, схрещені, поверх куртки)
7. Рукава (прив'язані до куртки, поверх рук)
8. Аксесуари
```

### В коді — прапорець:
```renpy
# jacket_mode: "open" | "closed" | None
if jacket_mode == "open":
    # руки → куртка поверх
elif jacket_mode == "closed":
    # куртка → руки → рукава поверх
else:
    # без куртки: кофта → руки
```

---

## ПОЗИ

Базова поза — одна на персонажа. Весь одяг генерується під неї.

| Персонаж | Базова поза | Причина |
|----------|------------|---------|
| Артур | Руки схрещені | Лідерська закрита поза, 90% сцен |
| Аоі | Руки на стегнах / одна рука вгору | Енергійна, відкрита |
| Амір | Руки в русі / жестикуляція | Гіперактивний |
| Квінсі | Одна рука в кишені | Розслаблений снайпер |
| Летті | Руки схрещені або тримає кухоль | Закрита або з кавою |
| Елеонор | Руки вниз / одна на лікті | Контрольована |
| Kullervo | Руки вниз, сутулий | Апатія |
| Mirage | Рука на стегні | Впевнена поза |
| Rhino | Руки опущені, незграбно | Підліток в тілі гіганта |

### Рідкісні пози (суцільні спрайти):
- Рука за головою (ніяковіє)
- Тримає кухоль / склянку
- Спирається на стіну
- Бойова стійка

**Рідкісні пози = суцільний спрайт з зафіксованим одягом.** Рандомізатор вимкнено. Код знає: ця поза = цей конкретний outfit, без варіацій.

---

## ГЕНЕРАЦІЯ СПРАЙТІВ

### Інструмент
Nano Banana 2 Pro (Google Gemini API). Підтримує:
- Character consistency
- Text rendering (для напису на футболці)
- Natural language editing
- Multi-image context

### Процес генерації одного шару одягу:
1. Взяти базовий template персонажа (тіло в позі)
2. Промпт: "Put [опис одягу] on this character. Keep exact same pose, lighting, style."
3. Отримати повний спрайт в одязі
4. Вирізати потрібний шар (торс без рук, або тільки штани)
5. Інпейнт дірки від вирізаних рук (щоб одяг продовжувався під ними)
6. Зберегти як прозорий PNG

### Для рукавів:
1. Згенерувати спрайт в застебнутій куртці
2. Вирізати ТІЛЬКИ рукава (від плечей до кистей)
3. Зберегти окремо — це шар рукавів для цієї куртки

---

## ФАЙЛОВА СТРУКТУРА

```
character_sprites/
  Arthur/
    # Базові шари
    body-base.png                          # Тіло без рук
    face-smile.png                         # Емоції (6-8 штук)
    face-laugh.png
    face-angry.png
    face-tired.png
    face-surprised.png
    face-aggressive.png
    
    # Штани (від талії до коліна)
    pants-501_dark.png
    pants-carhartt_double_knee.png
    pants-rothco_bdu_olive.png
    pants-bar_clean_501.png
    
    # Кофти (торс без рук, інпейнт)
    top-white_tshirt.png                   # Біла футболка (парна, 彼女の彼氏)
    top-grey_marl_tshirt.png               # M&S сіра
    top-navy_jumper.png                    # Woolovers в'язаний
    top-champion_hoodie.png                # Champion толстовка
    top-oxford_shirt.png                   # Барний варіант
    
    # Куртки (торс без рукавів, інпейнт)
    jacket-perfecto_torso.png              # Schott шкірянка
    jacket-barbour_torso.png               # Barbour Bedale
    jacket-trucker_torso.png               # Levi's джинсовка
    jacket-bar_blazer_torso.png            # Барний піджак
    
    # Руки (в позі, прозорий фон)
    arms-crossed_bare.png                  # Базова поза, голі руки
    arms-down_bare.png                     # Руки вниз (template)
    arms-behind_head_bare.png              # Рідкісна — рука за голову
    
    # Рукава (прив'язані до куртки)
    sleeves-perfecto.png                   # Рукава шкірянки
    sleeves-barbour.png                    # Рукава Barbour
    sleeves-trucker.png                    # Рукава джинсовки
    
    # Аксесуари (прозорі шари)
    acc-scarf_charcoal.png                 # Шарф
    acc-towel_shoulder.png                 # Рушник на плечі
    acc-nothing.png                        # Порожній (для рандомізатора)
    
    # Суцільні (рідкісні пози, одяг зафіксований)
    special-kitchen_tshirt_towel.png       # Кухонна сцена
    special-holding_mug.png                # З кухлем
    special-leaning_wall_perfecto.png      # Спирається на стіну в шкірянці
```

---

## РАНДОМІЗАТОР ОДЯГУ

### Логіка (щоденна ротація):
```python
def get_daily_outfit(char_name):
    """Визначає outfit на день. Викликається в next_day()."""
    
    # Перевірити спеціальні флаги (фіксований одяг)
    if flags.get("arthur_bar_tonight"):
        return FIXED_OUTFITS["arthur_bar"]
    
    # Звичайний рандом з пулу
    tops = OUTFIT_POOLS[char_name]["tops"]
    pants = OUTFIT_POOLS[char_name]["pants"]
    jackets = OUTFIT_POOLS[char_name]["jackets"]  # включає None (без куртки)
    accessories = OUTFIT_POOLS[char_name]["accessories"]  # включає None
    
    # Вагові шанси
    top = weighted_random(tops)
    pant = weighted_random(pants)
    jacket = weighted_random(jackets)
    acc = weighted_random(accessories)
    
    return {
        "top": top,
        "pants": pant,
        "jacket": jacket,
        "jacket_mode": "open" if jacket and random() > 0.5 else "closed" if jacket else None,
        "accessory": acc,
    }
```

### Вагові шанси (приклад Аоі):
```python
OUTFIT_POOLS["Аоі"]["tops"] = [
    ("top-baby_tee_fila", 25),           # 25% — повсякденна
    ("top-playstation_longsleeve", 20),   # 20% — для прохолодних днів
    ("top-hanes_crop", 20),              # 20% — база
    ("top-paired_tshirt", 7),            # 7% — парна футболка (рідкісна!)
    ("top-dickies_coverall", 15),        # 15% — робоча
    ("top-evangelion_tee", 13),          # 13% — домашня (тільки якщо backroom)
]
```

### Тригерні футболки:
```python
# Парна футболка Аоі — 7% шанс
# Якщо рандомізатор її надів І гравець має флаг arthur_tshirt_noticed:
if current_outfit["Аоі"]["top"] == "top-paired_tshirt":
    set_flag("aoi_wearing_paired_tshirt")
    # Диспетчер побачить eligible запис з цим флагом
```

---

## ОДЯГ ЯК ЛУТ (МІСІЙНІ ЗНАХІДКИ)

Нові речі додаються в пул рандомізатора через флаги:

```python
# Місійний діалог: знайшли шкіряну куртку
# В mission_event.rpy:
menu:
    "Забрати собі":
        $ set_flag("drifter_got_leather_jacket")
    "Залишити Артуру":
        $ set_flag("arthur_got_new_leather_jacket")
        # Додає в пул Артура новий спрайт
        $ OUTFIT_POOLS["Артур"]["jackets"].append(("jacket-found_leather_torso", 15))

# В сцені з Летті:
# Летті: "Де взяла?" / "В он з того" [показує на труп]
$ set_flag("lettie_got_lumberjack_shirt")
$ OUTFIT_POOLS["Летті"]["tops"].append(("top-lumberjack_shirt", 20))
```

---

## REN'PY РЕАЛІЗАЦІЯ

### Layered Image:
```renpy
layeredimage arthur:
    # 1. Тіло
    always:
        "character_sprites/Arthur/body-base.png"
    
    # 2. Морда
    group face auto:
        attribute smile default
        attribute laugh
        attribute angry
        attribute tired
        attribute surprised
        attribute aggressive
    
    # 3. Штани (з daily outfit)
    if store.daily_outfits.get("Артур", {}).get("pants"):
        add "character_sprites/Arthur/[store.daily_outfits['Артур']['pants']].png"
    
    # 4. Кофта
    if store.daily_outfits.get("Артур", {}).get("top"):
        add "character_sprites/Arthur/[store.daily_outfits['Артур']['top']].png"
    
    # 5-7. Куртка + руки (порядок залежить від jacket_mode)
    if store.daily_outfits.get("Артур", {}).get("jacket_mode") == "open":
        # Руки під курткою
        add "character_sprites/Arthur/arms-crossed_bare.png"
        add "character_sprites/Arthur/[store.daily_outfits['Артур']['jacket']].png"
    elif store.daily_outfits.get("Артур", {}).get("jacket_mode") == "closed":
        # Куртка під руками + рукава
        add "character_sprites/Arthur/[store.daily_outfits['Артур']['jacket']].png"
        add "character_sprites/Arthur/arms-crossed_bare.png"
        # Рукава поверх
        $ _sleeve = store.daily_outfits['Артур']['jacket'].replace('jacket-', 'sleeves-').replace('_torso', '')
        add "character_sprites/Arthur/[_sleeve].png"
    else:
        # Без куртки — просто руки
        add "character_sprites/Arthur/arms-crossed_bare.png"
    
    # 8-9. Аксесуари
    if store.daily_outfits.get("Артур", {}).get("accessory"):
        add "character_sprites/Arthur/[store.daily_outfits['Артур']['accessory']].png"
```

---

## КІЛЬКІСТЬ ФАЙЛІВ НА ПЕРСОНАЖА

### Артур (приклад повного набору):

| Тип | Кількість | Файли |
|-----|-----------|-------|
| Тіло | 1 | body-base |
| Морди | 6-8 | smile, laugh, angry, tired, surprised, aggressive, angry_teeth, very_surprised |
| Штани | 3-4 | 501, carhartt, rothco, bar_clean |
| Кофти | 5-6 | white_tshirt, grey_marl, navy_jumper, champion_hoodie, oxford_shirt, paired_tshirt |
| Куртки (торс) | 3-4 | perfecto, barbour, trucker, bar_blazer |
| Руки (пози) | 2-3 | crossed_bare, down_bare, behind_head |
| Рукава | 3-4 | perfecto, barbour, trucker (по одному на куртку) |
| Аксесуари | 2-3 | scarf, towel, nothing |
| Суцільні | 2-3 | kitchen, holding_mug, leaning_wall |
| **РАЗОМ** | **~30** | |

### Комбінації з 30 файлів:
- 4 штанів × 6 кофт × 5 верхніх варіантів (без куртки + 4 куртки) = **120 комбінацій**
- × 3 аксесуари = **360 візуальних варіантів**
- × 7 емоцій = **2520 унікальних станів**

### На всіх 9 персонажів:
- ~30 файлів × 9 = **~270 файлів**
- Генерація: ~270 промптів в Nano Banana + нарізка + інпейнт
- Реально: 2-3 тижні роботи

---

## ПРІОРИТЕТИ ГЕНЕРАЦІЇ

### Фаза 1 — Мінімум для запуску (на персонажа):
- 1 тіло
- 3-4 морди (smile, angry, tired, neutral)
- 1 штани
- 2 кофти
- 1 куртка + рукава
- 1 руки (базова поза)
= **~10 файлів на персонажа, ~90 всього**

### Фаза 2 — Повний гардероб:
- Решта штанів, кофт, курток
- Додаткові пози рук
- Аксесуари
= **~20 файлів додатково на персонажа**

### Фаза 3 — Лут і спеціальні:
- Місійні знахідки
- Суцільні спрайти для рідкісних сцен
- CG для галереї
= **по мірі написання контенту**

---

## КОНТЕКСТ

Hex живуть у Höllvania Central Mall. Навколо — магазини одягу. Обмеження не дефіцит а характер вибору. 12-18 речей одягу на персонажа реалістично. Кожна річ — або привезена з собою (ICR, до Хьольванії), або знайдена в молу, або здобута на місії. Кожна має історію. Навіть якщо гравець її ніколи не почує.
