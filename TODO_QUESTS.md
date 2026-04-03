# TODO: Квести та тимчасові заглушки

## Тимчасові флаги (script.rpy → label start)

Прибрати коли буде готовий відповідний квест:

- `set_flag("coffee_machine_found")` — автомат працює без квесту. Замінити на квест Аміра.

## Приховані локації (triggers.rpy → HIDDEN_LOCATIONS)

Потрібні квести/тригери для відкриття:

- `comp_club` — флаг `comp_club_unlocked`
- `balcony` — флаг `balcony_unlocked`
- `bar` — вже прив'язаний до `syndicate_rank_3`
- `rooftop` — флаг `rooftop_unlocked`
- `security_room` — флаг `security_room_unlocked`
- `warehouse` — флаг `warehouse_unlocked`
- `utility` — флаг `utility_unlocked`
- `cinema` — флаг `cinema_unlocked`
- `gym` — флаг `gym_unlocked`
- `billiard` — флаг `billiard_unlocked`
- `barbershop` — флаг `barbershop_unlocked`
- `photo_studio` — флаг `photo_studio_unlocked`
- `laundry` — флаг `laundry_unlocked`
- `parking` — флаг `parking_unlocked`
- `wc` — флаг `wc_unlocked`
- `room_1` — флаг `room_1_unlocked`
- `room_2` — флаг `room_2_unlocked`
- `shop_1` — флаг `shop_1_unlocked`
- `shop_2` — флаг `shop_2_unlocked`
- `shop_3` — флаг `shop_3_unlocked`
- `bookshop` — флаг `bookshop_unlocked`

## Квест: Кавовий автомат

Ідея: знайти на місії → Амір починає ремонтувати → потрібні деталі → кав'ярня відкривається → Летті починає там бувати → ланцюжок діалогів.

Файл: окремий .rpy (наприклад game/quests/quest_coffee.rpy).

## Місійні івенти (game/events/missions/)

Система готова: `get_mission_dialogue()` в dispatcher.rpy.
Перевіряє conditions + chance. Якщо chance провалений або нема eligible — просто анімація і результат.

Як писати місійний івент:

```python
init python:
    MISSION_DIALOGUE_ENTRIES.append({
        "id": "arthur_ambush_event",
        "who": "Артур",
        "conditions": {
            "chemistry_min": ("Артур", 35),
            "rank_min": 2,
        },
        "priority": 50,
        "chance": 20,          # 20% шанс спрацювати
        "label": "arthur_ambush_event",
    })
```

- `chance: 20` — 20% що з'явиться на місії з цим напарником
- `conditions` — ранг, хімія, флаги, день, локація
- `priority` — вищий = перевіряється першим
- Без `chance` або `chance: 100` = гарантований (не рекомендується для звичайних)
- Label — повноцінна сцена з фоном, спрайтами, меню

Файли класти в `game/events/missions/`.
