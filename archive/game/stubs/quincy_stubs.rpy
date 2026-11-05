# game/stubs/quincy_stubs.rpy
# Стаби для Квінсі — короткі фонові діалоги без прогресу.

label stub_Квінсі_weapons:
    show quince at char_center
    qu "Розбираю, чищу, збираю. Медитація для людей з корисними хобі."
    $ advance_time(5)
    mc "А звичайна медитація?"
    $ advance_time(5)
    qu "Нудна. І не вбиває грінір."
    $ advance_time(5)
    hide quince
    return

label stub_Квінсі_silence:
    show quince at char_center
    qu "Тсс."
    $ advance_time(5)
    qu "Чуєш? Ось це — ідеальні умови для пострілу."
    $ advance_time(5)
    qu "А тепер ти заговорив і все зіпсував."
    $ advance_time(5)
    hide quince
    return

label stub_Квінсі_trolling:
    show quince at char_center
    qu "Переклав речі Аміра на іншу полицю. Чекаю реакцію."
    $ advance_time(5)
    mc "Навіщо?"
    $ advance_time(5)
    qu "Мистецтво не потребує виправдань."
    $ advance_time(5)
    hide quince
    return

label stub_Квінсі_training:
    show quince at char_center
    qu "Двісті повторень на спуск. Щодня."
    $ advance_time(5)
    qu "М'язова пам'ять — єдина пам'ять, яка не бреше."
    $ advance_time(5)
    hide quince
    return

label stub_Квінсі_sleep:
    show quince at char_center
    qu "Снайпери вміють спати де завгодно. Професійна навичка."
    $ advance_time(5)
    mc "І як якість сну?"
    $ advance_time(5)
    qu "Жахлива. Зате стабільно жахлива."
    $ advance_time(5)
    hide quince
    return

label stub_Квінсі_weather:
    show quince at char_center
    qu "Вітру немає. Вологість стабільна. Ідеальна балістика."
    $ advance_time(5)
    qu "Шкода, що стріляти нема в кого. Поки що."
    $ advance_time(5)
    hide quince
    return

label stub_Квінсі_amir_loud:
    show quince at char_center
    qu "Амір розмовляє так, ніби весь мол має його чути."
    $ advance_time(5)
    qu "Новина: весь мол його чує. І страждає."
    $ advance_time(5)
    hide quince
    return

label stub_Квінсі_film:
    show quince at char_center
    qu "Знайшов касету. VHS. Бойовик вісімдесятих."
    $ advance_time(5)
    mc "Добрий?"
    $ advance_time(5)
    qu "Жахливий. Подивлюсь двічі."
    $ advance_time(5)
    hide quince
    return

label stub_Квінсі_accuracy:
    show quince at char_center
    qu "Влучність — це не талант. Це тисячі годин, коли всі інші спали."
    $ advance_time(5)
    qu "Або дивились жахливі бойовики. Це теж я, якщо чесно."
    $ advance_time(5)
    hide quince
    return

label stub_Квінсі_boredom:
    show quince at char_center
    qu "Нудно."
    $ advance_time(5)
    mc "Можеш щось зробити корисне."
    $ advance_time(5)
    qu "Можу. Але не буду. З принципу."
    $ advance_time(5)
    hide quince
    return
