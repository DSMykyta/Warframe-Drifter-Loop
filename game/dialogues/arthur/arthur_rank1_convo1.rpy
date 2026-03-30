# game/dialogues/arthur/arthur_rank1_convo1.rpy
# Артур — Ранг 1, Розмова 1: Спроба познайомитись ближче

init python:
    DIALOGUE_ENTRIES.append({
        "id": "arthur_rank1_convo1",
        "who": "Артур",
        "conditions": {
            "flag_true": ["arthur_intro_done"],
            "flag_false": ["arthur_rank1_convo1_done"],
            "rank_min": 1,
        },
        "priority": 50,
        "chance": 100,
        "label": "arthur_rank1_convo1",
    })

label arthur_rank1_convo1:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    mc "Артуре, маю хвилинку. Хотів би поговорити."
    $ advance_time(3)

    ar "Поговорити. Про що саме?"
    $ advance_time(3)

    mc "Ну... ми ж працюємо разом. Хочу краще розуміти, з ким маю справу."
    $ advance_time(3)

    ar "Ти маєш справу з командиром оперативної групи. Що ще треба знати?"
    $ advance_time(3)

    menu:
        "Розкажи про свій бойовий досвід":
            jump arthur_r1c1_soldiering

        "Ви з Елеонор давно знайомі?":
            jump arthur_r1c1_eleanor

        "Просто розкажи про себе. Як людину.":
            jump arthur_r1c1_personal

label arthur_r1c1_soldiering:
    mc "Як давно ти в цій справі? Ну, бойові операції, командування..."
    $ advance_time(3)

    ar "Достатньо давно, щоб не рахувати роки."
    $ advance_time(3)

    ar "Це не та тема, яку обговорюють між місіями. Досвід або є, або його немає."
    $ advance_time(3)

    mc "Я не сумніваюсь у твоєму досвіді. Просто цікаво."
    $ advance_time(3)

    ar "Цікавість — розкіш для тих, хто не на передовій."
    $ advance_time(3)

    menu:
        "Ми зараз не на передовій. Можна й розслабитись.":
            mc "Ми зараз не на передовій. Сидимо в безпечному місці. Можна й поговорити нормально."
            $ advance_time(3)

            ar "..."
            $ advance_time(3)

            ar "Може, ти й маєш рацію. Але звичка тримати дистанцію — вона не просто так."
            $ advance_time(3)

            $ add_chemistry("Артур", 2)

        "Вибач, не хотів тиснути.":
            mc "Зрозумів. Не буду наполягати."
            $ advance_time(3)

            ar "Не вибачайся. Краще запитай щось конкретне, ніж чекай відвертості від незнайомця."
            $ advance_time(3)

    jump arthur_r1c1_quick_questions

label arthur_r1c1_eleanor:
    mc "Ви з Елеонор... здається, знаєте одне одного давно."
    $ advance_time(3)

    ar "Елеонор — мій найстаріший товариш по зброї. Ми пройшли багато разом."
    $ advance_time(3)

    mc "Яка вона була в дитинстві?"
    $ advance_time(3)

    ar "А яке тобі до цього діло?"
    $ advance_time(3)

    menu:
        "Хочу зрозуміти динаміку команди. Це важливо для роботи.":
            mc "Чим краще я розумію зв'язки в групі, тим ефективніше можу працювати."
            $ advance_time(3)

            ar "Хм. Логічно, хоч і звучить як виправдання."
            $ advance_time(3)

            ar "Елеонор завжди була... рішучою. Навіть коли ми були дітьми. Вона ніколи не чекала дозволу діяти."
            $ advance_time(3)

            $ add_chemistry("Артур", 2)
            $ add_insight("arthur_eleanor_childhood", "Артур та Елеонор знайомі з дитинства. Елеонор завжди була рішучою.")

        "Просто цікаво. Можеш не відповідати.":
            mc "Та просто цікаво. Якщо не хочеш — не треба."
            $ advance_time(3)

            ar "Правильна відповідь — не хочу. Поки що."
            $ advance_time(3)

    jump arthur_r1c1_quick_questions

label arthur_r1c1_personal:
    mc "Забудь про ранги й місії. Хто ти як людина, Артуре?"
    $ advance_time(3)

    ar "Людина, яка задає такі питання, або наївна, або хоче щось отримати."
    $ advance_time(3)

    mc "Або просто хоче з кимось нормально поговорити."
    $ advance_time(3)

    ar "Нормально поговорити..."
    $ advance_time(3)

    ar "Це вимагає довіри. А довіра вимагає часу. І, можливо, алкоголю."
    $ advance_time(3)

    menu:
        "Тоді якось вип'ємо разом. Серйозно.":
            mc "Домовились. Якось посидимо, вип'ємо, й ти розкажеш мені все."
            $ advance_time(3)

            ar "Все — навряд чи. Але... побачимо."
            $ advance_time(3)

            $ add_chemistry("Артур", 4)
            $ set_flag("arthur_drinks_hinted")

        "Я нікуди не поспішаю. Почекаю.":
            mc "Я терплячий. Зачекаю, поки будеш готовий."
            $ advance_time(3)

            ar "Терпіння — це рідкість. Добре."
            $ advance_time(3)

            $ add_chemistry("Артур", 2)

    jump arthur_r1c1_quick_questions

label arthur_r1c1_quick_questions:

    ar "Ти все ще тут. Отже, є ще питання?"
    $ advance_time(3)

    menu:
        "Який твій улюблений колір?":
            mc "Ладно, щось легке. Який твій улюблений колір?"
            $ advance_time(3)

            ar "Серйозно? Колір?"
            $ advance_time(3)

            mc "Серйозно."
            $ advance_time(3)

            ar "Червоний."
            $ advance_time(3)

            mc "Чому?"
            $ advance_time(3)

            ar "Тому що він чесний. Не прикидається чимось іншим."
            $ advance_time(3)

            $ add_insight("arthur_fav_color", "Улюблений колір Артура — червоний. Каже, що червоний — чесний колір.")

            mc "А Елеонор?"
            $ advance_time(3)

            ar "Чорний. Або фіолетовий. Залежить від настрою."
            $ advance_time(3)

            $ add_chemistry("Артур", 2)
            $ add_insight("eleanor_fav_color", "Улюблений колір Елеонор — чорний або фіолетовий, за словами Артура.")

        "Яке твоє друге ім'я?":
            mc "У тебе є друге ім'я?"
            $ advance_time(3)

            ar "Навіщо тобі?"
            $ advance_time(3)

            mc "Щоб знати. Просто так."
            $ advance_time(3)

            ar "...Джеймс."
            $ advance_time(3)

            mc "Артур Джеймс. Звучить солідно."
            $ advance_time(3)

            ar "Ще одне слово про це — і розмова закінчена."
            $ advance_time(3)

            $ add_chemistry("Артур", 2)
            $ add_insight("arthur_middle_name", "Друге ім'я Артура — Джеймс. Не любить про це говорити.")

        "Ні, все. Дякую за розмову.":
            mc "Та ні, на сьогодні досить. Дякую, що поговорив."
            $ advance_time(3)

            ar "Не дякуй за те, чого ще не було."
            $ advance_time(3)

            jump arthur_r1c1_end

    ar "Ще щось?"
    $ advance_time(3)

    menu:
        "У тебе в дитинстві були домашні тварини?":
            mc "Останнє питання. Чесно. Домашні тварини — були?"
            $ advance_time(3)

            ar "Ти збираєш на мене досьє?"
            $ advance_time(3)

            mc "Може."
            $ advance_time(3)

            ar "...Була рибка. Мурчик."
            $ advance_time(3)

            mc "Мурчик? Рибка?!"
            $ advance_time(3)

            ar "Я був дитиною. Діти називають тварин дурними іменами."
            $ advance_time(3)

            mc "І скільки прожив Мурчик?"
            $ advance_time(3)

            ar "Тринадцять років."
            $ advance_time(3)

            mc "Тринадцять?! Для рибки це ціла вічність."
            $ advance_time(3)

            ar "Мурчик був стійкий. Як і його господар."
            $ advance_time(3)

            $ add_chemistry("Артур", 4)
            $ add_insight("arthur_pet_fish", "У Артура в дитинстві була рибка Мурчик. Прожила 13 років. Артур пишається цим.")

        "Ні, достатньо на сьогодні.":
            mc "Все, не буду більше мучити. На сьогодні достатньо."
            $ advance_time(3)

            ar "Розумний вибір."
            $ advance_time(3)

label arthur_r1c1_end:

    ar "Дрифтер."
    $ advance_time(3)

    mc "Так?"
    $ advance_time(3)

    ar "Наступного разу принеси випити. Тоді, може, й розкажу більше."
    $ advance_time(3)

    $ store.seen_dialogues.add("arthur_rank1_convo1")
    $ set_flag("arthur_rank1_convo1_done")

    hide arthur
    return
