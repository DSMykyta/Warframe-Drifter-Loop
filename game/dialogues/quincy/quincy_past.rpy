# game/dialogues/quincy/quincy_past.rpy
# Глибоке минуле Квінсі — від кіношколи до снайпера

init python:
    DIALOGUE_ENTRIES.append({
        "id": "quincy_past",
        "who": "Квінсі",
        "conditions": {
            "flag_true": ["quincy_loneliness_done"],
            "flag_false": ["quincy_past_done"],
            "rank_min": 4,
            "chemistry_min": ("Квінсі", 85),
        },
        "priority": 50,
        "chance": 100,
        "label": "quincy_past",
    })

label quincy_past:
    show quince at char_center
    $ store.talked_today.add("Квінсі")

    "Квінсі крутить в руках стару лінзу від камери. Протирає її, дивиться крізь неї."
    $ advance_time(5)

    qu "Знаєш, ким я хотів бути?"
    $ advance_time(5)

    mc "Снайпером?"
    $ advance_time(5)

    qu "Filmmaker. Режисером. Я вступив до кіношколи в Брістолі. Двадцять один рік. Повний ідіот з камерою і мріями."
    $ advance_time(5)

    qu "Знімав короткометражки. Документалки. Одна навіть виграла приз на студентському фестивалі. 'Best Eye for Detail.'"
    $ advance_time(5)

    mc "Що сталося?"
    $ advance_time(5)

    qu "Війна. Не та, що в новинах з красивою графікою. Справжня. Потрібні були люди, які вміють тримати руки стабільно і бачити деталі на відстані."
    $ advance_time(5)

    qu "Рекрутер сказав: 'Ти дивишся в об'єктив краще за будь-кого.' Я думав, він говорить про камеру."
    $ advance_time(5)

    qu "Камеру замінили на приціл. Монтажний стіл — на снайперську позицію. 'Best Eye for Detail' — на 'Best Kill Ratio.'"
    $ advance_time(5)

    mc "Ти не хотів цього."
    $ advance_time(5)

    qu "Ніхто не хоче. Але коли ти вмієш — тебе не питають. Тебе використовують."
    $ advance_time(5)

    qu "Знаєш що найгірше? Приціл і камера — одне й те саме. Ти кадруєш. Наводиш фокус. Чекаєш ідеальний момент. Тільки результат різний."
    $ advance_time(5)

    qu "Камера зберігає момент. Приціл — знищує."
    $ advance_time(5)

    "Він ставить лінзу на стіл. Акуратно. Як реліквію."
    $ advance_time(5)

    qu "VHS, камера, касети — це я намагаюсь повернутися. До того хлопця з Брістоля, який вірив, що камера може змінити світ."
    $ advance_time(5)

    qu "Maybe it still can. Якщо записати правильний момент."
    $ advance_time(5)

    $ store.seen_dialogues.add("quincy_past")
    $ set_flag("quincy_past_done")
    $ add_insight("quincy_filmmaker_past", "Квінсі був студентом кіношколи в Брістолі. Війна перетворила камеру на приціл. VHS — спроба повернутися до себе справжнього")

    hide quince
    return
