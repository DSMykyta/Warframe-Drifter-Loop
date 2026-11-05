# game/stubs/aoi_stubs.rpy
# Стаби для Аоі — короткі фонові діалоги без прогресу.

label stub_Аоі_origami:
    show aoi at char_center
    ao "Складаю журавлика. Тисяча — і бажання здійсниться."
    $ advance_time(5)
    ao "Це номер сімдесят три."
    $ advance_time(5)
    hide aoi
    return

label stub_Аоі_music:
    show aoi at char_center
    ao "..."
    $ advance_time(5)
    mc "Що слухаєш?"
    $ advance_time(5)
    ao "Тишу між треками. Найкращий момент."
    $ advance_time(5)
    hide aoi
    return

label stub_Аоі_bubbletea:
    show aoi at char_center
    ao "Таро з подвійними перлинами. Холодний."
    $ advance_time(5)
    mc "Де ти взагалі знаходиш інгредієнти?"
    $ advance_time(5)
    ao "Не питай. Просто радій, що є."
    $ advance_time(5)
    hide aoi
    return

label stub_Аоі_bikes:
    show aoi at char_center
    ao "Бачила каталог мотоциклів у книгарні. Старий, ще до Петлі."
    $ advance_time(5)
    ao "Kawasaki Ninja ZX-6R. Ідеальна геометрія."
    $ advance_time(5)
    ao "Шкода, що нікуди їхати."
    $ advance_time(5)
    hide aoi
    return

label stub_Аоі_sleep:
    show aoi at char_center
    ao "Спала нормально."
    $ advance_time(5)
    mc "Серйозно?"
    $ advance_time(5)
    ao "Ні. Але навіщо обговорювати."
    $ advance_time(5)
    hide aoi
    return

label stub_Аоі_weather:
    show aoi at char_center
    ao "Вентиляція сьогодні тихіша. Відчуваєш?"
    $ advance_time(5)
    mc "Ні."
    $ advance_time(5)
    ao "Значить, тільки я."
    $ advance_time(5)
    hide aoi
    return

label stub_Аоі_quincy_noise:
    show aoi at char_center
    ao "Квінсі розбирає щось металеве. Знову."
    $ advance_time(5)
    ao "Треба навушники."
    $ advance_time(5)
    hide aoi
    return

label stub_Аоі_mall_stores:
    show aoi at char_center
    ao "На другому поверсі є магазин з канцелярією. Там хороший папір."
    $ advance_time(5)
    mc "Для орігамі?"
    $ advance_time(5)
    ao "Для всього. Але так, в основному для орігамі."
    $ advance_time(5)
    hide aoi
    return

label stub_Аоі_dreams:
    show aoi at char_center
    ao "Снилось море. Справжнє, не з фільму."
    $ advance_time(5)
    ao "Запах солі. Вітер."
    $ advance_time(5)
    ao "Прокинулась — кондиціонер."
    $ advance_time(5)
    hide aoi
    return

label stub_Аоі_stars:
    show aoi at char_center
    ao "Дах молу — єдине місце, звідки видно зірки."
    $ advance_time(5)
    mc "Ти ходиш на дах?"
    $ advance_time(5)
    ao "Іноді. Коли треба подумати без стін навколо."
    $ advance_time(5)
    hide aoi
    return
