# SPRITE NAMING CONVENTION

## Структура папок

```
character_sprites/
  Character-{Name}-{Faction}/
    knee-test.png                    <- тестовий спрайт (тимчасовий)
    face/
      face-{emotion}.png             <- обличчя (без пози!)
    clothing/
      {char}-{garment}-{color}-{pose}-z{index}.png
```

## Шари одягу (clothing/)

### Формат назви

```
{character}-{garment}-{color}-{pose}-z{zindex}.png
```

Дефіс `-` між секціями. Підкреслення `_` тільки всередині секцій.

Парсер розбирає автоматично по дефісах — прописувати в коді нічого не треба. Кинув файл — система підхопить.

| Поле | Опис | Приклади |
|------|------|----------|
| `character` | Ім'я латиницею, lowercase | `arthur`, `eleanor`, `aoi` |
| `garment` | Назва предмету (`_` для складених) | `jacket_biker`, `tshirt_jp`, `jeans`, `pants_bdu` |
| `color` | Колір/варіант (`_` для складених) | `black`, `white`, `dark_blue`, `white_blue` |
| `pose` | Поза тіла | `crossed`, `down`, `neutral`, `left_up` |
| `zindex` | Число — порядок шару (більше = вище) | `z20`, `z30`, `z40`, `z60` |

### Z-Index таблиця

| Z-Index | Шар | Що тут |
|---------|-----|--------|
| z10 | Base | Тіло (голе, без одягу) |
| z20 | Bottom | Штани, спідниці, спортивки |
| z30 | Top (під) | Футболки, сорочки |
| z40 | Top (над) | Куртки, пальта |
| z60 | Extra | Шарфи, рушники, аксесуари |
| z70 | Face | Обличчя (окрема папка face/) |
| z80 | Injury | Бинти, пов'язки |

### Пози

| Код | Опис | Для яких шарів |
|-----|------|----------------|
| `crossed` | Руки схрещені на грудях | z30, z40 (верхній одяг) |
| `down` | Руки опущені | z30, z40 |
| `neutral` | Нейтральна (штани, аксесуари) | z20, z60 (не залежать від рук) |
| `left_up` | Ліва рука піднята | z30, z40 |

**Правило:** Штани (z20) і аксесуари (z60) завжди `neutral` бо не залежать від положення рук.

### Приклади

```
arthur-jacket_biker-black-crossed-z40.png      <- чорна байкерська куртка, руки схрещені
arthur-jacket_biker-black-down-z40.png         <- та сама куртка, руки опущені
arthur-jeans-blue-neutral-z20.png              <- сині джинси
arthur-jeans_501-indigo-neutral-z20.png        <- джинси 501 індиго
arthur-tshirt_jp-white-crossed-z30.png         <- біла JP футболка, руки схрещені
arthur-scarf-neutral-neutral-z60.png           <- шарф
arthur-towel-white_blue-neutral-z60.png        <- рушник біло-синій
```

## Обличчя (face/)

### Формат назви

```
face-{emotion}.png
```

Обличчя **не залежить від пози** тіла. Один файл на емоцію.

| Емоція | Файл |
|--------|------|
| Спокійний | `face-calm.png` |
| Усмішка | `face-smile.png` |
| Сміх | `face-laugh.png` |
| Злий | `face-angry.png` |
| Злий (зуби) | `face-angry_teeth.png` |
| Агресивний | `face-aggressive.png` |
| Здивований | `face-surprised.png` |
| Дуже здивований | `face-very_surprised.png` |
| Втомлений | `face-tired.png` |

## Як додати нового персонажа

1. Створити папку `Character-{Name}-{Faction}/`
2. Покласти `knee-test.png` (тимчасовий повний спрайт)
3. Створити `face/` з мінімум `face-calm.png`
4. Створити `clothing/` з шарами по конвенції вище
5. Додати запис в `CAST_DATA` в `cast.rpy`

Все. Парсер автоматично підхопить файли при запуску гри.

## Як парсер читає

```
arthur-jacket_biker-black-crossed-z40.png
  |        |          |      |      |
  |        |          |      |      └─ z-index (порядок шару)
  |        |          |      └─ поза (crossed/down/neutral)
  |        |          └─ колір
  |        └─ предмет одягу
  └─ персонаж
```

`split("-")` → 5 частин → готово.
