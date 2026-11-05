# game/stubs/lettie_stubs.rpy
# Stub dialogues for Летті — short fallback lines when no other dialogue is available.

label stub_Летті_rats:
    show lettie at char_center
    le "Сьогодні Пацюк-3 вкрав шматок сиру зі складу."
    $ advance_time(5)
    le "Горда за нього."
    $ advance_time(5)
    hide lettie
    return

label stub_Летті_coffee:
    show lettie at char_center
    le "Це вже четверта чашка. Або п'ята. Рахунок втрачено десь після другої."
    $ advance_time(5)
    mc "Тобі це точно не шкодить?"
    $ advance_time(5)
    le "Шкодить мені все. Кава хоча б приємна."
    $ advance_time(5)
    hide lettie
    return

label stub_Летті_health:
    show lettie at char_center
    le "Ти виглядаєш жахливо."
    $ advance_time(5)
    mc "Дякую, Летті."
    $ advance_time(5)
    le "Це не комплімент. Це діагноз. Іди поспи."
    $ advance_time(5)
    hide lettie
    return

label stub_Летті_sarcasm:
    show lettie at char_center
    le "Знаєш, що мене тримає на плаву?"
    $ advance_time(5)
    mc "Кава?"
    $ advance_time(5)
    le "Ні. Усвідомлення, що без мене ви всі помрете протягом тижня."
    $ advance_time(5)
    hide lettie
    return

label stub_Летті_sleep:
    show lettie at char_center
    le "Три години сну — це вже розкіш."
    $ advance_time(5)
    le "Минулого тижня було дві. Прогрес."
    $ advance_time(5)
    hide lettie
    return

label stub_Летті_weather:
    show lettie at char_center
    le "Надворі знову якась дрянь з неба сиплеться."
    $ advance_time(5)
    mc "Це називається дощ."
    $ advance_time(5)
    le "Я знаю, як це називається. Мені все одно не подобається."
    $ advance_time(5)
    hide lettie
    return

label stub_Летті_patients:
    show lettie at char_center
    le "Сьогодні приходив один з порізом. Каже — «само загоїться»."
    $ advance_time(5)
    le "Я йому пояснила, що сепсис теж сам приходить."
    $ advance_time(5)
    le "Більше не сперечався."
    $ advance_time(5)
    hide lettie
    return

label stub_Летті_silence:
    show lettie at char_center
    le "Тихо сьогодні."
    $ advance_time(5)
    le "Мені це не подобається. Тиша зазвичай означає, що хтось робить щось дурне непомітно."
    $ advance_time(5)
    hide lettie
    return

label stub_Летті_research:
    show lettie at char_center
    le "Я перечитала старі медичні журнали. Половина порад — відверта маячня."
    $ advance_time(5)
    mc "Наприклад?"
    $ advance_time(5)
    le "«Прикладіть п'явку». До всього. Перелом — п'явка. Кашель — п'явка."
    $ advance_time(5)
    le "Хоча, чесно, я розумію спокусу простих рішень."
    $ advance_time(5)
    hide lettie
    return

label stub_Летті_cynicism:
    show lettie at char_center
    le "Кожен день ми робимо вигляд, що все під контролем."
    $ advance_time(5)
    le "І кожен день це працює. Дивовижно."
    $ advance_time(5)
    hide lettie
    return
