# game/stubs/eleanor_stubs.rpy
# Стаби для Елеонор — короткі фонові діалоги без прогресу.

label stub_Елеонор_philosophy:
    show eleanor at char_center
    el "Якщо ми повторюємо один і той самий день... чи має значення, що ми робимо?"
    $ advance_time(5)
    mc "Сподіваюсь, що так."
    $ advance_time(5)
    el "Я теж. Інакше навіщо записувати."
    $ advance_time(5)
    hide eleanor
    return

label stub_Елеонор_observations:
    show eleanor at char_center
    el "Тріщина на стіні біля сходів стала довшою."
    $ advance_time(5)
    el "Або мені здається. Треба перевірити записи."
    $ advance_time(5)
    hide eleanor
    return

label stub_Елеонор_writing:
    show eleanor at char_center
    el "Записую все. Навіть те, що здається нудним."
    $ advance_time(5)
    mc "Навіщо?"
    $ advance_time(5)
    el "Бо нудне сьогодні може стати важливим завтра."
    $ advance_time(5)
    hide eleanor
    return

label stub_Елеонор_plants:
    show eleanor at char_center
    el "Цей фікус не повинен рости без сонця. Але росте."
    $ advance_time(5)
    el "Вперта рослина. Поважаю."
    $ advance_time(5)
    hide eleanor
    return

label stub_Елеонор_sleep:
    show eleanor at char_center
    el "Не спала. Читала старі нотатки."
    $ advance_time(5)
    el "Половину не впізнаю. Ніби хтось інший писав."
    $ advance_time(5)
    el "Хоча почерк мій."
    $ advance_time(5)
    hide eleanor
    return

label stub_Елеонор_weather:
    show eleanor at char_center
    el "Освітлення сьогодні тьмяніше. Чи помічаєш?"
    $ advance_time(5)
    mc "Ні, не особливо."
    $ advance_time(5)
    el "Я помічаю. На три відсотки тьмяніше. Записала."
    $ advance_time(5)
    hide eleanor
    return

label stub_Елеонор_patterns:
    show eleanor at char_center
    el "Є закономірність. Кожен третій цикл щось змінюється."
    $ advance_time(5)
    mc "Що саме?"
    $ advance_time(5)
    el "Поки не знаю. Але знайду."
    $ advance_time(5)
    hide eleanor
    return

label stub_Елеонор_books:
    show eleanor at char_center
    el "Знайшла книгу без обкладинки. Читаю вже вдруге."
    $ advance_time(5)
    el "Або втретє. Тут важко рахувати."
    $ advance_time(5)
    hide eleanor
    return

label stub_Елеонор_quiet:
    show eleanor at char_center
    el "Тиша — це не відсутність звуку. Це присутність уваги."
    $ advance_time(5)
    el "...Вибач. Іноді я надто багато думаю вголос."
    $ advance_time(5)
    hide eleanor
    return

label stub_Елеонор_riddles:
    show eleanor at char_center
    el "Що має корені, але не росте? Має сторінки, але не книга?"
    $ advance_time(5)
    mc "Не знаю. Що?"
    $ advance_time(5)
    el "Мертве дерево. Хоча... книга теж підходить."
    $ advance_time(5)
    el "Погана загадка. Треба придумати кращу."
    $ advance_time(5)
    hide eleanor
    return
