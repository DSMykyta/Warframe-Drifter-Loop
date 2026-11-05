# game/scenes/intro.rpy
# ═══════════════════════════════════════════════════
# ІНТРО: Допит на футкорті + знайомство з Гексом
# ═══════════════════════════════════════════════════

label intro:

    scene black
    pause 1.0

    scene bg_foodcourt with dissolve

    show amir at far_left
    show aoi at center_left
    show arthur at center
    show eleanor at center_right
    show lettie at right_of_center
    show quince at far_right

    pause 0.5

    am "Ого. Тобто ти типу... Марті МакФлай?"

    qu "Знущаєшся, мабуть?"

    ar "Якщо це туфта — я Марті особисто згодую Техроту."

    ar "Але часу нема."

    am "Бомба... знаєш, воно сходиться."

    menu:
        "З Новим Роком.":
            qu "Ха."
            $ set_flag("intro_dark_humor")
            $ add_chemistry("Квінсі", 2)

        "Я не прошу вірити. Перевірте.":
            ar "Перевіримо."
            $ set_flag("intro_asked_to_verify")
            $ add_chemistry("Артур", 2)

        "[[Нічого не сказати.]":
            am "Він... не буде відповідати?"
            ar "Амір."
            am "Все, мовчу."
            $ set_flag("intro_stayed_silent")
            $ add_chemistry("Артур", 1)
            $ add_chemistry("Квінсі", 1)

    ar "Добре, Марті. Ти нам, може, і потрібний."

    ar "Але спробуєш ще раз залізти мені в голову—"

    ar "—і Летті нічого буде зшивати."

    le "Si."

    ar "Ми зрозуміли один одного?"

    menu:
        "Так точно.":
            ar "Хоч щось."
            $ set_flag("intro_military_response")
            $ add_chemistry("Артур", 2)

        "Поки мене не прив'язують до стільців — так.":
            qu "Ха."
            am "Він мені подобається."
            ar "Тобі всі подобаються, Амір."
            $ set_flag("intro_sarcastic_response")
            $ add_chemistry("Квінсі", 2)
            $ add_chemistry("Амір", 1)

        "Обіцяю.":
            pause 0.5
            $ set_flag("intro_promised")
            $ add_chemistry("Елеонор", 2)

    # Розв'язали

    le "Руку покажи."

    le "Чисто. Між кістками. Жити будеш."

    le "На жаль."

    $ set_flag("lettie_bandaged_hand")
    $ add_chemistry("Летті", 1)

    ao "Я Аоі."

    menu:
        "Дріфтер. Відносно приємно.":
            ao "Відносно. В наших умовах — майже комплімент."
            $ add_chemistry("Аоі", 2)

        "[[Потиснути руку.]":
            ao "Небалакучий тип."
            $ add_chemistry("Аоі", 1)
            $ add_chemistry("Артур", 1)

        "Вибач за голову. Не було іншого способу.":
            ao "Не мені вибачати. Але дякую що сказав."
            $ add_chemistry("Аоі", 1)

    am "Амір! Технічна частина. І аркади."

    am "Якщо потрібно щось полагодити або... ну..."

    ar "Амір."

    am "Тихо. Так."

    $ add_chemistry("Амір", 1)

    qu "Квінсі. Тир. Без стуку не заходь."

    hide quince with dissolve

    ar "Бекрум. Коридор, другі двері. Завтра о восьмій."

    hide arthur with dissolve

    ao "Музичний. Другий поверх. Якщо що."

    hide aoi with dissolve

    am "Ну, бувай, Марті."

    hide amir with dissolve

    le "Рану промий вранці. Водою. Не спирт."

    hide lettie with dissolve

    hide eleanor with dissolve

    # ═══ ПІСЛЯ ДОПИТУ ═══

    scene black with dissolve
    pause 0.5

    if not is_loop_restart():
        "Бекрум. Коридор, другі двері — як Артур сказав."

        "Кинув речі. Рука ниє, але пов'язка тримається."

        "Треба оглянути це місце."

    # ═══ ІНІЦІАЛІЗАЦІЯ ═══
    $ set_flag("intro_done")
    $ set_flag("met_arthur")
    $ set_flag("met_aoi")
    $ set_flag("met_amir")
    $ set_flag("met_quincy")
    $ set_flag("met_lettie")
    $ set_flag("met_eleanor")

    if not is_loop_restart():
        $ set_flag("nickname_marty")

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
