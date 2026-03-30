# game/events/group/bar_night.rpy
# Групова сцена: вечір у барі

init python:
    DIALOGUE_ENTRIES.append({
        "id": "bar_night",
        "who": "Артур",
        "conditions": {
            "flag_false": ["group_bar_night_done"],
            "location": "bar_skana",
            "chars_at_location": ["Артур", "Летті"],
            "rank_min": 1,
            "chemistry_min": ("Артур", 20),
            "time_from": 1140,  # після 19:00
        },
        "priority": 70,
        "chance": 50,
        "label": "bar_night",
    })

label bar_night:
    $ store.talked_today.add("Артур")
    $ store.talked_today.add("Летті")

    show arthur at left
    show lettie at right

    ar "Сідай. Летті розповідає історію про свого першого пацієнта."
    $ advance_time(5)

    le "Я НЕ розповідаю. Ти попросив, я відмовила."
    $ advance_time(5)

    ar "Це і є початок кожної хорошої історії."
    $ advance_time(5)

    mc "Тепер я точно хочу почути."
    $ advance_time(5)

    le "...Добре. Але тільки тому, що бар порожній і мені байдуже."
    $ advance_time(5)

    le "Перший пацієнт. Солдат з пораненням ноги. Прийшов і сказав — 'Не хвилюйтесь, це просто подряпина.'"
    $ advance_time(5)

    le "Там стирчала кістка."
    $ advance_time(5)

    ar "..."
    $ advance_time(5)

    mc "І що ти зробила?"
    $ advance_time(5)

    le "Зшила. Сказала йому що так, подряпина. Він заснув щасливим."
    $ advance_time(5)

    le "Наступного дня прийшов з тортом. ТОРТОМ. На війні."
    $ advance_time(5)

    ar "Ось тому вона найкращий медик."
    $ advance_time(5)

    le "Ось тому я п'ю каву. Замість торта."
    $ advance_time(5)

    $ add_chemistry("Артур", 2)
    $ add_chemistry("Летті", 2)

    $ store.seen_dialogues.add("bar_night")
    $ set_flag("group_bar_night_done")
    $ add_insight("lettie_first_patient", "Першим пацієнтом Летті був солдат, який називав зламану ногу подряпиною.")

    hide arthur
    hide lettie
    return
