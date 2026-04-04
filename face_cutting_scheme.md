# Sprite cutting scheme + combination table — 3 layers

---

## Схема нарізки

Кожне з 12 фото ріжеться на **3 частини** по горизонталі.

```
┌─────────────────────┐
│                     │
│   BROWS layer       │  ← від верху до нижнього краю брови
│                     │
├─────────────────────┤  ← розріз 1: одразу під бровою
│                     │
│   EYES layer        │  ← повіки + зіниця + ніс (статичний)
│                     │
├─────────────────────┤  ← розріз 2: між носом і верхньою губою
│                     │
│   MOUTH layer       │  ← фільтрум + губи + підборіддя
│                     │
└─────────────────────┘
```

**Правило canvas:** всі 3 шари кожного файлу мають **однаковий розмір** з оригіналом.
Активна зона — пікселі, решта — прозора.
Ніс іде в EYES layer — він ніколи не змінюється, прихований у середньому шарі.

---

## Неймінг файлів

```
{char}_brows_{state}.png
{char}_eyes_{state}.png
{char}_mouth_{state}.png
```

### Brows (9 унікальних файлів):

| Файл | Джерело | Опис |
|---|---|---|
| `char_brows_neutral.png` | 01 — neutral.png | рівні, без напруги |
| `char_brows_furrowed_soft.png` | 02 — focused.png | злегка зведені, без складок |
| `char_brows_drooped.png` | 03 — tired.png | опущені зовні, розслаблені |
| `char_brows_asymmetric.png` | 04 — smug.png | обидві різної висоти (smug) |
| `char_brows_raised_inward.png` | 05 — concerned.png | підняті і зведені до центру |
| `char_brows_raised_high.png` | 06 — surprised.png | підняті вгору — шок |
| `char_brows_furrowed_hard.png` | 07 — angry.png | різко зведені вниз |
| `char_brows_raised_inner.png` | 08 — pained.png | inner corners вгору, outer вниз (inverted V) |
| `char_brows_one_raised.png` | 12 — one_raised.png | одна підняті, одна на місці — скептицизм |

### Eyes (9 унікальних файлів):

| Файл | Джерело | Опис |
|---|---|---|
| `char_eyes_neutral.png` | 01 — neutral.png | відкриті, прямо |
| `char_eyes_direct.png` | 02 — focused.png | відкриті, інтенсивний погляд прямо |
| `char_eyes_halflit.png` | 03 — tired.png | напівприкриті, прямо |
| `char_eyes_wide.png` | 06 — surprised.png | широко відкриті, прямо |
| `char_eyes_squint.png` | 07 — angry.png | звужені, повіки опущені |
| `char_eyes_closed.png` | 08 — pained.png | закриті |
| `char_eyes_warm.png` | 09 — joy.png | звужені теплом, зморшки в куточках |
| `char_eyes_side.png` | 10 — sideeye.png | зіниці вбік |
| `char_eyes_rolled.png` | 11 — eyeroll.png | зіниці вгору, більше білка знизу |

> фото 04, 05, 12 — очі дублюють існуючі. Окремі файли не потрібні.

### Mouth (9 унікальних файлів):

| Файл | Джерело | Опис |
|---|---|---|
| `char_mouth_neutral.png` | 01 — neutral.png | закритий, рівний |
| `char_mouth_tense_light.png` | 02 — focused.png | злегка стиснений |
| `char_mouth_slack.png` | 03 — tired.png | розслаблений, трохи вниз |
| `char_mouth_smirk.png` | 04 — smug.png | асиметрична, один куточок вгору |
| `char_mouth_frown.png` | 05 — concerned.png | куточки вниз |
| `char_mouth_open.png` | 06 — surprised.png | відкритий овал |
| `char_mouth_tense.png` | 07 — angry.png | стиснений прямий |
| `char_mouth_pained.png` | 08 — pained.png | куточки вниз, стиснений |
| `char_mouth_grin.png` | 09 — joy.png | щира, широка |

> фото 10, 11, 12 — рот нейтральний, дублює існуючий файл.

---

## Таблиця комбінацій

| Емоція | Brows | Eyes | Mouth |
|---|---|---|---|
| Нейтральна | `neutral` | `neutral` | `neutral` |
| Спокійна | `neutral` | `halflit` | `neutral` |
| Зосереджена | `furrowed_soft` | `direct` | `tense_light` |
| Втомлена | `drooped` | `halflit` | `slack` |
| Smug | `asymmetric` | `halflit` | `smirk` |
| Самовпевнена | `asymmetric` | `halflit` | `grin` |
| Задоволена | `neutral` | `neutral` | `smirk` |
| Радість | `neutral` | `warm` | `grin` |
| Стурбована | `raised_inward` | `neutral` | `frown` |
| Сумна | `raised_inward` | `neutral` | `frown` |
| Знесилена | `drooped` | `halflit` | `frown` |
| Здивована | `raised_high` | `wide` | `open` |
| Шокована | `raised_high` | `wide` | `open` |
| Зла | `furrowed_soft` | `direct` | `frown` |
| Лютa | `furrowed_hard` | `squint` | `tense` |
| Роздратована | `furrowed_soft` | `neutral` | `neutral` |
| Біль | `raised_inner` | `closed` | `pained` |
| Сміється | `neutral` | `warm` | `grin` |
| Підозра | `raised_inward` | `side` | `neutral` |
| Зневага | `asymmetric` | `side` | `neutral` |
| Байдужість | `neutral` | `side` | `neutral` |
| Роздратована (в бік) | `furrowed_soft` | `side` | `neutral` |
| "Ой бля" | `raised_high` | `rolled` | `neutral` |
| "Ой бля" + відкритий рот | `raised_high` | `rolled` | `slack` |
| "Ти це серйозно?" | `one_raised` | `neutral` | `neutral` |
| "Ти це серйозно?" + смірк | `one_raised` | `neutral` | `smirk` |
| "Ти це серйозно?" (в бік) | `one_raised` | `side` | `neutral` |
| Говорить нейтрально | `neutral` | `neutral` | `open` |
| Говорить зі злістю | `furrowed_hard` | `squint` | `open` |
| Говорить стурбовано | `raised_inward` | `neutral` | `open` |
| Focused (говорить) | `furrowed_soft` | `direct` | `open` |

---

## Ren'Py LayeredImage

```renpy
layeredimage char_face:
    group brows:
        attribute neutral default:      "char_brows_neutral.png"
        attribute furrowed_soft:        "char_brows_furrowed_soft.png"
        attribute drooped:              "char_brows_drooped.png"
        attribute asymmetric:           "char_brows_asymmetric.png"
        attribute raised_inward:        "char_brows_raised_inward.png"
        attribute raised_high:          "char_brows_raised_high.png"
        attribute furrowed_hard:        "char_brows_furrowed_hard.png"
        attribute raised_inner:         "char_brows_raised_inner.png"
        attribute one_raised:           "char_brows_one_raised.png"
    group eyes:
        attribute neutral default:      "char_eyes_neutral.png"
        attribute direct:               "char_eyes_direct.png"
        attribute halflit:              "char_eyes_halflit.png"
        attribute wide:                 "char_eyes_wide.png"
        attribute squint:               "char_eyes_squint.png"
        attribute closed:               "char_eyes_closed.png"
        attribute warm:                 "char_eyes_warm.png"
        attribute side:                 "char_eyes_side.png"
        attribute rolled:               "char_eyes_rolled.png"
    group mouth:
        attribute neutral default:      "char_mouth_neutral.png"
        attribute tense_light:          "char_mouth_tense_light.png"
        attribute slack:                "char_mouth_slack.png"
        attribute smirk:                "char_mouth_smirk.png"
        attribute frown:                "char_mouth_frown.png"
        attribute open:                 "char_mouth_open.png"
        attribute tense:                "char_mouth_tense.png"
        attribute pained:               "char_mouth_pained.png"
        attribute grin:                 "char_mouth_grin.png"
```

Виклик:
```renpy
show char_face brows_raised_high eyes_rolled mouth_neutral    # ой бля
show char_face brows_one_raised eyes_neutral mouth_neutral    # ти це серйозно
show char_face brows_one_raised eyes_side mouth_smirk         # скептичний смірк
show char_face brows_furrowed_hard eyes_squint mouth_tense    # лютa
show char_face brows_neutral eyes_warm mouth_grin             # радість
```
