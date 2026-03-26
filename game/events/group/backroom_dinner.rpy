# game/events/group/backroom_dinner.rpy
# Групова сцена: спільна вечеря в бекрумі

init python:
    DIALOGUE_ENTRIES.append({
        "id": "backroom_dinner",
        "who": "Артур",
        "conditions": {
            "flag_true": ["arthur_intro_done", "arthur_cooking_done"],
            "flag_false": ["group_backroom_dinner_done"],
            "location": "backroom",
            "rank_min": 2,
            "time_from": 1080,  # після 18:00
            "time_to": 1320,   # до 22:00
        },
        "priority": 75,
        "chance": 40,
        "label": "backroom_dinner",
    })

label backroom_dinner:
    $ store.talked_today.add("Артур")

    show arthur at char_center

    ar "Готую на всіх. Сідай, поки гаряче."
    $ advance_time(5)

    mc "Що сьогодні?"
    $ advance_time(5)

    ar "Рагу. З того, що знайшов на складі. Не питай з чого."
    $ advance_time(5)

    "Поступово підтягуються інші."
    $ advance_time(5)

    mc "Непогано. Навіть дуже."
    $ advance_time(5)

    ar "Дякую. Це... приємно чути."
    $ advance_time(5)

    ar "Рідко хтось каже 'дякую' за їжу. Зазвичай просто їдять і йдуть."
    $ advance_time(5)

    menu:
        "Завтра допоможу готувати":
            $ advance_time(5)
            mc "Хочеш, завтра допоможу? Вдвох швидше."

            ar "...Добре. Приходь о сьомій. І не спізнюйся."
            $ advance_time(5)

            $ chemistry["Артур"] += 5
            $ set_flag("group_cooking_together_offered")

        "Просто подякувати":
            $ advance_time(5)
            mc "Серйозно, Артуре. Це важливо для команди."

            ar "Знаю. Тому і роблю."
            $ advance_time(5)

            $ chemistry["Артур"] += 3

    $ store.seen_dialogues.add("backroom_dinner")
    $ set_flag("group_backroom_dinner_done")
    $ add_insight("arthur_cooks_for_team", "Артур регулярно готує на весь загін. Рідко чує подяку.")

    hide arthur
    return
