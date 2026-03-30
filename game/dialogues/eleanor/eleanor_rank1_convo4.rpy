# game/dialogues/eleanor/eleanor_rank1_convo4.rpy
# Елеонор — Ранг 1, Розмова 4: Імунітет

init python:
    DIALOGUE_ENTRIES.append({
        "id": "eleanor_rank1_convo4",
        "who": "Елеонор",
        "conditions": {
            "flag_true": ["eleanor_intro_done", "eleanor_rank1_convo3_done"],
            "flag_false": ["eleanor_rank1_convo4_done"],
            "rank_min": 1,
        },
        "priority": 45,
        "chance": 100,
        "label": "eleanor_rank1_convo4",
    })

label eleanor_rank1_convo4:
    show eleanor at char_center
    $ store.talked_today.add("Елеонор")

    el "Можу я поставити тобі нечемне запитання?"
    $ advance_time(3)

    mc "Від тебе я інших і не чекаю."
    $ advance_time(3)

    el "Як це — бути імунним?"
    $ advance_time(3)

    mc "Імунним?"
    $ advance_time(3)

    el "До Техроту. Ми всі тут повільно гниємо зсередини. Летті перевіряє нас щотижня. Артур робить вигляд, що йому байдуже. Амір молиться."
    $ advance_time(3)

    el "А ти просто... ходиш. Чистий. Незайманий. Ніби це все тебе не стосується."
    $ advance_time(3)

    mc "Елеонор..."
    $ advance_time(3)

    el "Я не звинувачую. Справді. Але іноді, коли я дивлюсь на тебе — і знаю, що Техрот ніколи не торкнеться твоєї шкіри — я відчуваю щось дуже негарне."
    $ advance_time(3)

    el "Заздрість. Брудну, дитячу, ірраціональну заздрість."
    $ advance_time(3)

    menu:
        "Ти маєш повне право на це. Не вибачайся.":
            jump eleanor_r1c4_validate

        "Я розумію. Але я тут не для того, щоб бути проблемою.":
            jump eleanor_r1c4_empathize

        "Що я можу зробити? Серйозно.":
            jump eleanor_r1c4_help

label eleanor_r1c4_validate:
    mc "Елеонор, ти маєш повне право злитися. Я б на твоєму місці злився теж."
    $ advance_time(3)

    el "Не кажи так. Ти не маєш права бути ще й розуміючим. Це робить мою злість безпідставною."
    $ advance_time(3)

    mc "Вона не безпідставна. Ситуація несправедлива. Просто я — не причина."
    $ advance_time(3)

    el "Ні. Ти — дзеркало. А дзеркала показують те, на що не хочеш дивитись."
    $ advance_time(3)

    el "Я дивлюсь на тебе — і бачу себе без Техроту. Ким я могла б бути. І це... болить."
    $ advance_time(3)

    $ add_chemistry("Елеонор", 2)

    jump eleanor_r1c4_fear

label eleanor_r1c4_empathize:
    mc "Я розумію. І я не ображаюсь. Але я тут не для того, щоб тобі нагадувати про те, що ти втрачаєш."
    $ advance_time(3)

    el "А для чого ти тут?"
    $ advance_time(3)

    mc "Щоб допомогти. Це банально, але правда."
    $ advance_time(3)

    el "Банальні речі іноді — найважчі для прийняття."
    $ advance_time(3)

    $ add_chemistry("Елеонор", 2)

    jump eleanor_r1c4_fear

label eleanor_r1c4_help:
    mc "Що я можу зробити? Конкретно. Не слова — дії."
    $ advance_time(3)

    el "Конкретно? Знайти ліки від Техроту. Мала дрібниця."
    $ advance_time(3)

    mc "Я серйозно."
    $ advance_time(3)

    el "І я серйозно. Але якщо чесно..."
    $ advance_time(3)

    el "Те, що ти тут — вже допомога. Войд у тобі дає Летті дані, яких у неї раніше не було. Ти — ходячий експеримент."
    $ advance_time(3)

    mc "Радий бути корисним. Навіть як лабораторна мишка."
    $ advance_time(3)

    el "Не мишка. Ключ. Можливо."
    $ advance_time(3)

    $ add_chemistry("Елеонор", 4)
    $ set_flag("eleanor_galvanized")

    jump eleanor_r1c4_fear

label eleanor_r1c4_fear:

    el "Знаєш, чого я боюсь найбільше?"
    $ advance_time(3)

    mc "Скажи."
    $ advance_time(3)

    el "Не смерті. Смерть — це фінал. Кінцеві титри. Я з цим змирилась."
    $ advance_time(3)

    el "Я боюсь проміжного стану. Коли Техрот забере мій розум — але залишить тіло. Ходячий м'ясний мішок із залишками Елеонор всередині."
    $ advance_time(3)

    el "Коли я не зможу скласти речення. Коли мої нотатки стануть безглуздям. Коли я забуду, що таке абзац."
    $ advance_time(3)

    el "Для журналістки — це не смерть. Це гірше."
    $ advance_time(3)

    menu:
        "Ми не дозволимо цьому статись.":
            mc "Ми не дозволимо цьому статись. Летті працює над цим. Я працюю. Ти сама працюєш."
            $ advance_time(3)

            el "«Ми.» Ти часто вживаєш це слово. Я починаю звикати."
            $ advance_time(3)

            el "...Дякую, Дрифтер. За те, що не відвів погляд."
            $ advance_time(3)

            $ add_chemistry("Елеонор", 2)

        "Якщо це станеться — я буду поруч. До кінця.":
            mc "Якщо найгірше станеться — я нікуди не піду. Буду поруч."
            $ advance_time(3)

            el "Не давай обіцянок, які не зможеш стримати."
            $ advance_time(3)

            mc "Я їх не даю."
            $ advance_time(3)

            el "..."
            $ advance_time(3)

            el "Вибач. За заздрість. За різкість. За все."
            $ advance_time(3)

            el "Ти не заслуговуєш на мою гіркоту. Ніхто не заслуговує."
            $ advance_time(3)

            $ add_chemistry("Елеонор", 4)

    $ store.seen_dialogues.add("eleanor_rank1_convo4")
    $ set_flag("eleanor_rank1_convo4_done")
    $ add_insight("eleanor_techrot_fear", "Елеонор боїться не смерті від Техроту — а втрати розуму. Для неї нездатність формулювати думки гірша за смерть.")

    hide eleanor
    return
