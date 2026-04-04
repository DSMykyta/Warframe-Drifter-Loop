# Face expression prompts — 3-layer system

Кожне фото дає 3 шари: **brows / eyes / mouth**.
Після нарізки шари комбінуються незалежно.
Первинна цінність кожного фото позначена ★.

---

## 01 — neutral
Not an exaggerated emotion, relaxed facial muscles, eyebrows in flat resting position with no tension ★, eyes open naturally looking straight forward, mouth closed and level with no curve up or down

## 02 — focused
Not an exaggerated emotion, eyebrows very slightly lowered and minimally drawn together with absolutely no forehead creases and no wrinkles between brows ★, eyes open and looking straight forward with calm intensity, mouth closed with lips lightly pressed together

## 03 — tired
Not an exaggerated emotion, eyebrows relaxed and slightly drooped at outer ends ★, eyelids heavy and half-lowered with eyes looking straight forward ★, mouth slightly slack with corners of lips neutral or faintly down

## 04 — smug
Not an exaggerated emotion, one eyebrow very marginally higher than the other creating a subtle asymmetry ★, eyes slightly narrowed with a calm half-lidded gaze looking straight forward, mouth with one corner subtly raised in an asymmetric expression ★

## 05 — concerned
Not an exaggerated emotion, eyebrows raised and pulled very slightly inward toward center with a faint crease between them ★, eyes open normally looking straight forward, mouth closed with corners of lips very slightly downward ★

## 06 — surprised
Not an exaggerated emotion, eyebrows raised upward higher than resting position ★, eyes opened wider than usual looking straight forward ★, mouth open in a small relaxed oval ★

## 07 — angry
Not an exaggerated emotion, eyebrows sharply lowered and firmly drawn together creating a strong furrow ★, upper eyelids descended with eyes narrowed looking straight forward ★, lips pressed firmly together in a straight tense line ★

## 08 — pained
Not an exaggerated emotion, eyebrows raised upward at inner corners only while outer corners stay low creating an inverted V shape ★, eyes closed or nearly closed ★, mouth closed with lips pressed together and corners pulled slightly down ★

## 09 — joy
Not an exaggerated emotion, eyebrows in relaxed natural position, eyes slightly narrowed with genuine warmth and small crinkles at outer corners looking straight forward ★, both corners of mouth raised evenly in a real smile with lips slightly parted showing upper teeth and cheeks gently lifted ★

## 10 — sideeye
Not an exaggerated emotion, eyebrows in flat neutral resting position with no tension, eyes open normally but irises shifted to one side looking away from camera ★, mouth closed and neutral with no expression

## 11 — eyeroll
Not an exaggerated emotion, eyebrows raised slightly in mild exasperation, eyes with irises rolled upward showing more white at the bottom than usual ★, mouth closed and neutral or very slightly slack, overall expression of mild "oh come on" not theatrical shock

## 12 — one_raised
Not an exaggerated emotion, one eyebrow raised noticeably higher while the other stays at resting position or drops very slightly ★, eyes open and looking straight forward with a calm skeptical gaze, mouth closed and level with no expression, asymmetry only in the brows not the rest of the face

---

## Що дає кожне фото

| Фото | brows | eyes | mouth |
|---|---|---|---|
| 01 neutral | brows_neutral | eyes_neutral | mouth_neutral |
| 02 focused | brows_furrowed_soft | eyes_direct | mouth_tense_light |
| 03 tired | brows_drooped | eyes_halflit | mouth_slack |
| 04 smug | brows_asymmetric | eyes_halflit *(дубль)* | mouth_smirk |
| 05 concerned | brows_raised_inward | eyes_neutral *(дубль)* | mouth_frown |
| 06 surprised | brows_raised_high | eyes_wide | mouth_open |
| 07 angry | brows_furrowed_hard | eyes_squint | mouth_tense |
| 08 pained | brows_raised_inner | eyes_closed | mouth_pained |
| 09 joy | brows_neutral *(дубль)* | eyes_warm | mouth_grin |
| 10 sideeye | brows_neutral *(дубль)* | eyes_side | mouth_neutral *(дубль)* |
| 11 eyeroll | brows_raised_high *(дубль)* | eyes_rolled | mouth_neutral *(дубль)* |
| 12 one_raised | brows_one_raised | eyes_neutral *(дубль)* | mouth_neutral *(дубль)* |

Унікальних brows: 9 / eyes: 9 / mouth: 9
