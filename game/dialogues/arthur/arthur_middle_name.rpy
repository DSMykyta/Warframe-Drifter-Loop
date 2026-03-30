# game/dialogues/arthur/arthur_middle_name.rpy
# Артур — розмова з вибором звертання та теми

init python:
    DIALOGUE_ENTRIES.append({
        "id": "arthur_middle_name",
        "who": "Артур",
        "conditions": {
            "flag_true": ["arthur_atomicycle_done"],
            "flag_false": ["arthur_middle_name_done"],
            "chemistry_min": ("Артур", 15),
            "rank_min": 2,
        },
        "priority": 50,
        "chance": 100,
        "label": "arthur_middle_name",
    })

label arthur_middle_name:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    mc "Артуре, я тут подумав... як до тебе краще звертатися?"
    $ advance_time(5)

    ar "А що не так з «Артур»?"
    $ advance_time(5)

    menu:
        "Привіт, Артуре — класика":
            $ advance_time(5)
            mc "Та ні, все нормально. Привіт, Артуре."

            ar "Привіт. Бачиш, працює."
            $ advance_time(5)

        "А Джеймс? Звучить солідно":
            $ advance_time(5)
            mc "Може, Джеймс? Як Бонд."

            ar "...Мене не звати Джеймс. І я не агент."
            $ advance_time(5)

            ar "Хоча... технічно колись був. Але не Джеймс."
            $ advance_time(5)

        "Петершем — є ж у тебе прізвище?":
            $ advance_time(5)
            mc "А як щодо Петершем? Чув, так тебе кликали в ICR."

            ar "Звідки ти... Добре. Так, Петершем — моє прізвище. Але тут його ніхто не вживає."
            $ advance_time(5)

            ar "Тут я просто Артур. Мені так легше."
            $ advance_time(5)
            $ set_flag("arthur_surname_known")

        "Бро!":
            $ advance_time(5)
            mc "Бро!"

            ar "...Ні."
            $ advance_time(5)

            ar "Якщо ти скажеш це при Квінсі, він ніколи не дасть мені забути."
            $ advance_time(5)

    ar "А чому раптом питаєш?"
    $ advance_time(5)

    mc "Та просто цікаво. Давай краще поговоримо про щось."
    $ advance_time(5)

    menu:
        "Який твій улюблений колір?":
            $ advance_time(5)
            mc "Який у тебе улюблений колір?"

            ar "Сірий. Непомітний, практичний."
            $ advance_time(5)

            mc "Як і ти сам."
            $ advance_time(5)

            ar "Саме тому."
            $ advance_time(5)

        "Розкажи ще про меч":
            $ advance_time(5)
            mc "Я бачив у тебе на стіні клинок. Що це за зброя?"

            ar "Скана. Не зараз. Може, якось розповім."
            $ advance_time(5)

            ar "Це не та тема, яку починають між справами."
            $ advance_time(5)
            $ set_flag("arthur_skana_teased")

        "Тварину не хочеш завести?":
            $ advance_time(5)
            mc "Слухай, а ти б не хотів завести якусь тваринку? Кота, наприклад."

            ar "На базі? Де кожного дня може прилетіти снаряд?"
            $ advance_time(5)

            ar "...Хоча визнаю, кіт на базі підняв би мораль."
            $ advance_time(5)
            $ set_flag("arthur_wants_pet")

        "Подарувати" if len(inventory) > 0:
            call gift_submenu("Артур")

    $ store.seen_dialogues.add("arthur_middle_name")
    $ set_flag("arthur_middle_name_done")
    $ add_insight("arthur_personality", "Артур цінує простоту. Прізвище Петершем, але тут — просто Артур.")

    hide arthur
    return
