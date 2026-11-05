# game/stubs/amir_stubs.rpy
# Stub dialogues for Амір — short fallback lines when no other dialogue is available.

label stub_Амір_games:
    show amir at char_center
    am "Я знайшов стару консоль у підсобці. Екран тріснутий, але працює."
    $ advance_time(5)
    mc "І що на ній?"
    $ advance_time(5)
    am "Якийсь платформер. Вже пройшов два рівні. Третій — біль."
    $ advance_time(5)
    hide amir
    return

label stub_Амір_electronics:
    show amir at char_center
    am "Цей генератор тримається на скотчі та моїй вірі в нього."
    $ advance_time(5)
    am "Скотч закінчується."
    $ advance_time(5)
    hide amir
    return

label stub_Амір_future:
    show amir at char_center
    am "Іноді думаю — що буде через рік."
    $ advance_time(5)
    mc "І що думаєш?"
    $ advance_time(5)
    am "Що краще думати про те, що буде через годину. Менше розчарувань."
    $ advance_time(5)
    hide amir
    return

label stub_Амір_food:
    show amir at char_center
    am "Як думаєш, скільки разів можна їсти консерви, перш ніж сам станеш консервою?"
    $ advance_time(5)
    mc "Це... філософське питання?"
    $ advance_time(5)
    am "Це крик душі. Хочу нормальну їжу."
    $ advance_time(5)
    hide amir
    return

label stub_Амір_sleep:
    show amir at char_center
    am "Вчора заснув прямо за столом. Прокинувся — обличчя на клавіатурі."
    $ advance_time(5)
    am "На екрані було сто сторінок літери «ж». Поетично."
    $ advance_time(5)
    hide amir
    return

label stub_Амір_weather:
    show amir at char_center
    am "Електроніка не любить вологість. Я теж."
    $ advance_time(5)
    am "Ми з нею маємо багато спільного."
    $ advance_time(5)
    hide amir
    return

label stub_Амір_high_score:
    show amir at char_center
    am "Я побив свій рекорд у тетрісі."
    $ advance_time(5)
    mc "Вітаю. Скільки?"
    $ advance_time(5)
    am "Не скажу. Ти спробуєш побити, і я цього не переживу."
    $ advance_time(5)
    hide amir
    return

label stub_Амір_mall_people:
    show amir at char_center
    am "Бачив сьогодні, як двоє сперечалися через стілець."
    $ advance_time(5)
    am "Стільців навколо було шість порожніх. Людям просто потрібен привід."
    $ advance_time(5)
    hide amir
    return

label stub_Амір_energy:
    show amir at char_center
    am "Батарейки сідають. І в ліхтарику теж."
    $ advance_time(5)
    mc "А ти?"
    $ advance_time(5)
    am "Я на останніх відсотках. Потрібна зарядка. Бажано кавою."
    $ advance_time(5)
    hide amir
    return

label stub_Амір_jokes:
    show amir at char_center
    am "Чому програміст пішов з роботи?"
    $ advance_time(5)
    mc "Чому?"
    $ advance_time(5)
    am "Бо не отримав масив. ...Масив. Розумієш?"
    $ advance_time(5)
    am "Ладно, я сам вийду."
    $ advance_time(5)
    hide amir
    return
