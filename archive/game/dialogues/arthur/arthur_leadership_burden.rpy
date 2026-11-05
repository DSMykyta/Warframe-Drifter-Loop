# game/dialogues/arthur/arthur_leadership_burden.rpy
# Артур про тягар лідерства

init python:
    DIALOGUE_ENTRIES.append({
        "id": "arthur_leadership_burden",
        "who": "Артур",
        "conditions": {
            "flag_true": ["arthur_skana_story_told"],
            "flag_false": ["arthur_leadership_burden_done"],
            "chemistry_min": ("Артур", 60),
            "rank_min": 3,
        },
        "priority": 50,
        "chance": 100,
        "label": "arthur_leadership_burden",
    })

label arthur_leadership_burden:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    ar "Можу я бути з тобою відвертим?"
    $ advance_time(5)

    mc "Звісно."
    $ advance_time(5)

    ar "Я втомився."
    $ advance_time(5)

    ar "Не фізично. Фізично я витримаю ще довго. А от тут..."
    $ advance_time(5)

    ar "Кожного ранку я прокидаюсь і першим ділом рахую. Хто живий. Хто поранений. Хто може вийти на завдання."
    $ advance_time(5)

    ar "Потім я складаю план. І в кожному плані є рядок, який я не кажу вголос — «якщо хтось не повернеться»."
    $ advance_time(5)

    mc "Ти завжди думаєш про найгірше?"
    $ advance_time(5)

    ar "Лідер мусить. Інакше найгірше стає несподіванкою. А несподіванки вбивають."
    $ advance_time(5)

    ar "Але іноді... іноді я хочу просто прокинутися і не думати, хто сьогодні може загинути через моє рішення."
    $ advance_time(5)

    menu:
        "Ти не зобов'язаний нести це сам":
            $ advance_time(5)
            mc "Артуре, ти не зобов'язаний нести це наодинці. Ми — команда."

            ar "Команда виконує рішення. Але приймає їх хтось один. Так працює відповідальність."
            $ advance_time(5)

            mc "Тоді дозволь мені хоча б бути поруч, коли тобі важко."
            $ advance_time(5)

            ar "...Це вже більше, ніж я звик отримувати."
            $ advance_time(5)
            $ add_chemistry("Артур", 2)

        "Може, варто передати лідерство комусь іншому?":
            $ advance_time(5)
            mc "А ти не думав передати лідерство? Хоча б тимчасово?"

            ar "Кому? Амір занадто м'який. Квінсі занадто імпульсивний. Летті скаже, що їй все одно, а потім візьме на себе більше, ніж треба."
            $ advance_time(5)

            ar "Елеонор могла б. Але вона не хоче. І я не маю права її змушувати."
            $ advance_time(5)
            $ add_chemistry("Артур", 2)

        "Ти робиш це добре. Повір мені":
            $ advance_time(5)
            mc "Я бачу, як ти керуєш. Ти робиш це добре, Артуре."

            ar "«Добре» — це коли всі живі. Поки що — так. Але кожен день це лотерея."
            $ advance_time(5)

            ar "Дякую. Мені... рідко таке кажуть."
            $ advance_time(5)
            $ add_chemistry("Артур", 4)

    ar "Вибач. Не хотів вивалювати це все на тебе."
    $ advance_time(5)

    mc "Не вибачайся. Для цього і є друзі."
    $ advance_time(5)

    $ store.seen_dialogues.add("arthur_leadership_burden")
    $ set_flag("arthur_leadership_burden_done")
    $ add_insight("arthur_burden", "Артур щодня живе з вагою рішень, від яких залежать життя. Він втомлений, але не зупиняється.")

    hide arthur
    return
