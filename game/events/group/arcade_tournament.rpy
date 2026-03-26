# game/events/group/arcade_tournament.rpy
# Групова сцена: турнір в аркаді (комп'ютерний клуб)

init python:
    DIALOGUE_ENTRIES.append({
        "id": "arcade_tournament",
        "who": "Амір",
        "conditions": {
            "flag_true": ["amir_intro_done", "aoi_intro_done", "quincy_intro_done"],
            "flag_false": ["group_arcade_tournament_done"],
            "location": "comp_club",
            "chars_at_location": ["Амір", "Аоі"],
            "rank_min": 1,
            "chemistry_min": ("Амір", 20),
        },
        "priority": 70,
        "chance": 60,
        "label": "arcade_tournament",
    })

label arcade_tournament:
    $ store.talked_today.add("Амір")
    $ store.talked_today.add("Аоі")

    show amir at left
    show aoi at right

    am "Гей! Ідеальний момент. У мене тут працює старий файтинг. Хочеш турнір?"
    $ advance_time(5)

    ao "Я вже граю. Тренуюсь."
    $ advance_time(5)

    mc "Турнір на трьох?"
    $ advance_time(5)

    am "На скільки завгодно! Система підтримує до чотирьох."
    $ advance_time(5)

    menu:
        "Прийняти виклик":
            $ advance_time(5)
            mc "Давай. Покажу вам, як грають справжні бійці."

            am "О-о-о! Велика заява! Аоі, ти чула?"
            $ advance_time(5)

            ao "Чула. Запам'ятала. Використаю."
            $ advance_time(5)

            "Починається запекла битва на екрані..."
            $ advance_time(10)

            am "НІ! Як?! Вона знову виграла!"
            $ advance_time(5)

            ao "Терпіння і спостережливість."
            $ advance_time(5)

            mc "Реванш?"
            $ advance_time(5)

            am "ОБОВ'ЯЗКОВО."
            $ advance_time(5)

            $ chemistry["Амір"] += 3
            $ chemistry["Аоі"] += 3

        "Просто подивитись":
            $ advance_time(5)
            mc "Я краще подивлюсь. Цікаво, хто виграє."

            am "Слабак! Ну добре, будеш коментатором."
            $ advance_time(5)

            ao "Менше відволікань. Добре."
            $ advance_time(5)

            "Амір програє три раунди поспіль."
            $ advance_time(10)

            am "Вона жахлива. В хорошому сенсі."
            $ advance_time(5)

            $ chemistry["Амір"] += 1
            $ chemistry["Аоі"] += 1

    $ store.seen_dialogues.add("arcade_tournament")
    $ set_flag("group_arcade_tournament_done")
    $ add_insight("group_arcade", "Амір та Аоі грають у файтинги разом. Аоі завжди виграє.")

    hide amir
    hide aoi
    return
