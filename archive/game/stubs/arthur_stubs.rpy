# game/stubs/arthur_stubs.rpy
# Стаби для Артура — короткі фонові діалоги без прогресу.

label stub_Артур_square_food:
    show arthur at char_center
    ar "Їжа з пайків. Квадратна. Сумна."
    $ advance_time(5)
    ar "Але їстівна. І на тому дякую."
    $ advance_time(5)
    hide arthur
    return

label stub_Артур_keys:
    show arthur at char_center
    ar "Ключі від складу... десь тут були."
    $ advance_time(5)
    ar "А, ні. В іншій кишені."
    $ advance_time(5)
    ar "Коли маєш шість кишень — це і благо, і прокляття."
    $ advance_time(5)
    hide arthur
    return

label stub_Артур_danko:
    show arthur at char_center
    ar "Данко знову щось гуркоче в ангарі."
    $ advance_time(5)
    mc "Він завжди так?"
    $ advance_time(5)
    ar "Ні. Іноді він гуркоче голосніше."
    $ advance_time(5)
    hide arthur
    return

label stub_Артур_sword_cleaning:
    show arthur at char_center
    ar "Клинок треба чистити щодня. Навіть якщо не використовував."
    $ advance_time(5)
    ar "Іржа не питає дозволу."
    $ advance_time(5)
    hide arthur
    return

label stub_Артур_weather:
    show arthur at char_center
    ar "Погода в молі завжди однакова — ніякої."
    $ advance_time(5)
    mc "Це погано?"
    $ advance_time(5)
    ar "Ні. Менше сюрпризів — менше проблем."
    $ advance_time(5)
    hide arthur
    return

label stub_Артур_cooking:
    show arthur at char_center
    ar "Сьогодні готую з того, що є. Як завжди."
    $ advance_time(5)
    ar "Хоча б сіль ще залишилась."
    $ advance_time(5)
    ar "Без солі навіть пайок не врятувати."
    $ advance_time(5)
    hide arthur
    return

label stub_Артур_drinks:
    show arthur at char_center
    ar "Вода. Фільтрована. Тепла."
    $ advance_time(5)
    mc "Чаю немає?"
    $ advance_time(5)
    ar "Чай закінчився два тижні тому. Не нагадуй."
    $ advance_time(5)
    hide arthur
    return

label stub_Артур_sleep:
    show arthur at char_center
    ar "Спав годин зо три. Може, чотири."
    $ advance_time(5)
    ar "Для лідера — це розкіш."
    $ advance_time(5)
    hide arthur
    return

label stub_Артур_silence:
    show arthur at char_center
    ar "Тихо сьогодні."
    $ advance_time(5)
    ar "..."
    $ advance_time(5)
    ar "Добре. Нехай буде тихо."
    $ advance_time(5)
    hide arthur
    return

label stub_Артур_quincy_annoying:
    show arthur at char_center
    ar "Квінсі знову щось розібрав і не зібрав назад."
    $ advance_time(5)
    mc "Ти злишся?"
    $ advance_time(5)
    ar "Ні. Я звик. Це гірше."
    $ advance_time(5)
    hide arthur
    return
