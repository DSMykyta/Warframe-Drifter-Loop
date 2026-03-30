# game/dialogues/aoi/aoi_rank1_convo1.rpy
# Аоі — Ранг 1, Розмова 1: Кава чи чай?

init python:
    DIALOGUE_ENTRIES.append({
        "id": "aoi_rank1_convo1",
        "who": "Аоі",
        "conditions": {
            "flag_true": ["aoi_intro_done"],
            "flag_false": ["aoi_rank1_convo1_done"],
            "rank_min": 1,
        },
        "priority": 50,
        "chance": 100,
        "label": "aoi_rank1_convo1",
    })

label aoi_rank1_convo1:
    show aoi at char_center
    $ store.talked_today.add("Аоі")

    ao "Дрифтер! Стій-стій-стій. У мене дуже важливе питання."
    $ advance_time(3)

    mc "Що сталось?"
    $ advance_time(3)

    ao "Кава чи чай?"
    $ advance_time(3)

    mc "...Це було «дуже важливе питання»?"
    $ advance_time(3)

    ao "Найважливіше! За цим стоїть ціла філософія. Кавові люди — це одне. Чайні — зовсім інше."
    $ advance_time(3)

    menu:
        "Кава. Чорна, без цукру.":
            jump aoi_r1c1_coffee

        "Чай. Зелений, якщо є.":
            jump aoi_r1c1_tea

        "А де варіант «бабл-ті»?":
            jump aoi_r1c1_bubbletea

label aoi_r1c1_coffee:
    mc "Кава. Міцна, чорна, без компромісів."
    $ advance_time(3)

    ao "О-о-о. Серйозна людина. Така, знаєш, вставай-о-шостій-ранку енергія."
    $ advance_time(3)

    mc "А ти?"
    $ advance_time(3)

    ao "Я — чай з молоком і трьома ложками цукру. Ми буквально протилежності."
    $ advance_time(3)

    $ add_chemistry("Аоі", 2)

    jump aoi_r1c1_boredom

label aoi_r1c1_tea:
    mc "Чай. Зелений, якщо є. Або будь-який, чесно кажучи."
    $ advance_time(3)

    ao "Чайна людина! Ми вже друзі. Це вирішено. Офіційно."
    $ advance_time(3)

    mc "Так швидко?"
    $ advance_time(3)

    ao "Чай об'єднує. Це давня мудрість. Я щойно її вигадала, але це не робить її менш правдивою."
    $ advance_time(3)

    $ add_chemistry("Аоі", 4)

    jump aoi_r1c1_boredom

label aoi_r1c1_bubbletea:
    mc "Зачекай, а де варіант «бабл-ті»? Я ж знаю, що ти його обожнюєш."
    $ advance_time(3)

    ao "Ти... ти запам'ятав?"
    $ advance_time(3)

    ao "Бабл-ті — це окрема категорія. Це не чай і не кава. Це мистецтво."
    $ advance_time(3)

    mc "Мистецтво з кульками тапіоки."
    $ advance_time(3)

    ao "Саме так! Ідеальний баланс текстури й смаку. Як гарна мелодія — кожен елемент на своєму місці."
    $ advance_time(3)

    $ add_chemistry("Аоі", 4)
    $ add_insight("aoi_bubbletea_art", "Аоі вважає бабл-ті окремою формою мистецтва. Порівнює з музикою.")

    jump aoi_r1c1_boredom

label aoi_r1c1_boredom:

    ao "Знаєш, чому я питаю? Бо мені нестерпно нудно."
    $ advance_time(3)

    mc "Нудно? Посеред усього цього?"
    $ advance_time(3)

    ao "Саме! Навколо хаос, місії, небезпека. А я сиджу тут і рахую тріщини на стелі. Їх сімнадцять, до речі."
    $ advance_time(3)

    menu:
        "Може, прогуляємось? Покажу тобі околиці.":
            mc "Тоді вставай. Покажу тобі щось цікавіше за тріщини."
            $ advance_time(3)

            ao "Серйозно? Просто так?"
            $ advance_time(3)

            mc "Просто так. Іноді найкращі пригоди починаються без плану."
            $ advance_time(3)

            ao "Мені це подобається. Людина без плану, але з напрямком."
            $ advance_time(3)

            $ add_chemistry("Аоі", 4)

        "Я теж рахую дивні речі, коли нудно.":
            mc "Я рахую патрони. Коли нудно — перераховую двічі."
            $ advance_time(3)

            ao "Ха! У нас обох є свої дивні звички."
            $ advance_time(3)

            ao "Але тріщини цікавіші. В них є характер. Патрони — ні."
            $ advance_time(3)

            $ add_chemistry("Аоі", 2)

    ao "Дякую за розмову, Дрифтер. Тепер я знаю найважливіше про тебе."
    $ advance_time(3)

    mc "Що я п'ю?"
    $ advance_time(3)

    ao "Що ти готовий відповідати на дурні питання. Це рідкісна якість!"
    $ advance_time(3)

    $ store.seen_dialogues.add("aoi_rank1_convo1")
    $ set_flag("aoi_rank1_convo1_done")

    hide aoi
    return
