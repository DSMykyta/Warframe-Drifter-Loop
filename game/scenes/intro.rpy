# game/scenes/intro.rpy
# Допит. Дріфтер прив'язаний до стільця на футкорті.
# Вже розповів про час, петлю, реактор. Гекс вирішує.

label intro:

    scene black
    pause 1.0

    scene bg_mall_foodcourt with dissolve

    show amir at far_left
    show aoi at center_left
    show arthur at center
    show eleanor at center_right
    show lettie at right_of_center
    show quince at far_right

    pause 0.5

    am "Ого. Тобто ти типу... Марті МакФлай?"
    $ advance_time(5)

    qu "Знущаєшся, мабуть?"
    $ advance_time(5)

    ar "Якщо це туфта — я Марті особисто згодую Техроту."
    $ advance_time(5)

    ar "Але часу нема."
    $ advance_time(5)

    am "Бомба... знаєш, воно сходиться."
    $ advance_time(5)

    menu:
        "З Новим Роком.":
            qu "Ха."
            $ advance_time(5)
            $ set_flag("intro_dark_humor")
            $ chemistry["Квінсі"] += 2

        "Я не прошу вірити. Перевірте.":
            ar "Перевіримо."
            $ advance_time(5)
            $ set_flag("intro_asked_to_verify")
            $ chemistry["Артур"] += 2

        "[[Нічого не сказати.]":
            am "Він... не буде відповідати?"
            $ advance_time(5)
            ar "Амір."
            $ advance_time(5)
            am "Все, мовчу."
            $ advance_time(5)
            $ set_flag("intro_stayed_silent")
            $ chemistry["Артур"] += 1
            $ chemistry["Квінсі"] += 1

    ar "Добре, Марті. Ти нам, може, і потрібний."
    $ advance_time(5)

    ar "Але спробуєш ще раз залізти мені в голову—"
    $ advance_time(5)

    ar "—і Летті нічого буде зшивати."
    $ advance_time(5)

    le "Si."
    $ advance_time(5)

    ar "Ми зрозуміли один одного?"
    $ advance_time(5)

    menu:
        "Так точно.":
            ar "Хоч щось."
            $ advance_time(5)
            $ set_flag("intro_military_response")
            $ chemistry["Артур"] += 2

        "Поки мене не прив'язують до стільців — так.":
            qu "Ха."
            $ advance_time(5)
            am "Він мені подобається."
            $ advance_time(5)
            ar "Тобі всі подобаються, Амір."
            $ advance_time(5)
            $ set_flag("intro_sarcastic_response")
            $ chemistry["Квінсі"] += 2
            $ chemistry["Амір"] += 1

        "Обіцяю.":
            pause 0.5
            $ set_flag("intro_promised")
            $ chemistry["Елеонор"] += 2

    # Розв'язали

    le "Руку покажи."
    $ advance_time(5)

    le "Чисто. Між кістками. Жити будеш."
    $ advance_time(5)

    le "На жаль."
    $ advance_time(5)

    $ set_flag("lettie_bandaged_hand")
    $ chemistry["Летті"] += 1

    ao "Я Аоі."
    $ advance_time(5)

    menu:
        "Дріфтер. Відносно приємно.":
            ao "Відносно. В наших умовах — майже комплімент."
            $ advance_time(5)
            $ chemistry["Аоі"] += 2

        "[[Потиснути руку.]":
            ao "Небалакучий тип."
            $ advance_time(5)
            $ chemistry["Аоі"] += 1
            $ chemistry["Артур"] += 1

        "Вибач за голову. Не було іншого способу.":
            ao "Не мені вибачати. Але дякую що сказав."
            $ advance_time(5)
            $ chemistry["Аоі"] += 1

    am "Амір! Технічна частина. І аркади."
    $ advance_time(5)

    am "Якщо потрібно щось полагодити або... ну..."
    $ advance_time(5)

    ar "Амір."
    $ advance_time(5)

    am "Тихо. Так."
    $ advance_time(5)

    $ chemistry["Амір"] += 1

    qu "Квінсі. Тир. Без стуку не заходь."
    $ advance_time(5)

    hide quince with dissolve

    ar "Бекрум. Коридор, другі двері. Завтра о восьмій."
    $ advance_time(5)

    hide arthur with dissolve

    ao "Музичний. Другий поверх. Якщо що."
    $ advance_time(5)

    hide aoi with dissolve

    am "Ну, бувай, Марті."
    $ advance_time(5)

    hide amir with dissolve

    le "Рану промий вранці. Водою. Не спирт."
    $ advance_time(5)

    hide lettie with dissolve

    hide eleanor with dissolve

    # ═══ БЕКРУМ ═══

    scene bg_backroom with dissolve

    if not is_loop_restart():
        "Ентраті десь у місті. Гекс його шукає."

        "Тепер і я."

        "Треба дізнатися хто такий цей Марті, і чому вони мене так називають."

    # ═══ ІНІЦІАЛІЗАЦІЯ ═══
    # Завжди (кожна петля)
    $ set_flag("intro_done")
    $ set_flag("met_arthur")
    $ set_flag("met_aoi")
    $ set_flag("met_amir")
    $ set_flag("met_quincy")
    $ set_flag("met_lettie")
    $ set_flag("met_eleanor")

    # Тільки перша петля — внутрішні думки і флаги що відкривають гілки
    if not is_loop_restart():
        $ set_flag("nickname_marty")

    # Завжди — інсайти і щоденник
    $ add_journal_entry("Допит. Розв'язали. Марті. Завтра о восьмій.", "event")

    $ add_insight("hex_exists", "Шестеро в молі. Гекс.")
    $ add_insight("arthur_leads", "Артур — лідер. Меч наскрізь через долоню — між кістками.")
    $ add_insight("nickname_marty", "Амір назвав Марті. Прижилось.")
    $ add_insight("aoi_logistics", "Аоі — логістика. Перша простягнула руку.")
    $ add_insight("quincy_marksman", "Квінсі. Тир. Без стуку.")
    $ add_insight("amir_tech", "Амір — технік. Аркади.")

    if store.flags.get("lettie_bandaged_hand"):
        $ add_insight("lettie_medic", "Летті — медик. Перевʼязала без питань.")

    return
