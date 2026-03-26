# game/scenes/arthur_kitchen_demo.rpy
# Демо-сцена: arthur_cooking рівень. Chemistry ~15, rank 1.
# Потребує: arthur_about_team_done
# 5 гілок в головному виборі, переплітаються з попередніми відповідями.
# Гілка матері та гілка обладнання → CG.
# Гілка команди, гілка допомоги → хімія без CG.
# Гілка "піду" → негатив.

image cg_arthur_kitchen = "images/cg/arthur_kitchen_cg.png"

layeredimage arthur_kitchen:
    always:
        xalign 0.5
        ypos 0
        "character_sprites/Arthur/waist-arms_crossed-white_tshirt-black_sweats-towel.png"
    group face:
        xalign 0.5
        ypos 0
        attribute smile:
            "character_sprites/Arthur/face-smile.png"
        attribute laugh:
            "character_sprites/Arthur/face-laugh.png"
        attribute angry:
            "character_sprites/Arthur/face-angry.png"
        attribute angry_teeth:
            "character_sprites/Arthur/face-angry_teeth.png"
        attribute aggressive:
            "character_sprites/Arthur/face-aggressive.png"
        attribute surprised:
            "character_sprites/Arthur/face-surprised.png"
        attribute very_surprised:
            "character_sprites/Arthur/face-very_surprised.png"
        attribute tired:
            "character_sprites/Arthur/face-tired.png"

label arthur_kitchen_demo:

    scene bg_foodcourt with dissolve
    play music "audio/boiling.mp3" fadein 1.0 loop
    play audio "<to 30.0>audio/kitchen_ambient.mp3" fadein 1.0
    pause 1.5

    show arthur_kitchen at char_center with dissolve
    $ store.talked_today.add("Артур")

    # Внутрішній трекер — впливає на тон пізніших відповідей
    $ _arthur_warmth = 0

    ar "Каша з сушеними грибами. Нічого особливого."
    $ advance_time(5)

    # ═══ ПЕРШИЙ ВИБІР — перше враження ═══
    menu:
        "Пахло на весь коридор.":
            $ advance_time(5)
            mc "Пахло на весь коридор."

            show arthur_kitchen aggressive
            ar "...Перебільшуєш."
            $ advance_time(5)
            $ _arthur_warmth += 1

        "Можна?":
            $ advance_time(5)
            show arthur_kitchen
            pause 0.3
            $ _arthur_warmth += 1

        "Ти що, для всіх готуєш?":
            $ advance_time(5)
            mc "Ти що, для всіх готуєш?"

            show arthur_kitchen aggressive
            ar "Що, отак просто? Вперся і питаєш?"
            $ advance_time(5)

            ar "Хто хоче — їсть. Хто не хоче — сухпайок в шафі."
            $ advance_time(5)

        "[[Просто сісти.]":
            $ advance_time(5)
            pause 0.3
            $ _arthur_warmth += 1

    show arthur_kitchen
    ar "Я просто не люблю, коли люди йдуть на завдання голодними. Це впливає на концентрацію."
    $ advance_time(5)

    # ═══ ДРУГИЙ ВИБІР — тон розмови ═══
    menu:
        "Тобто це тактичне рішення, а не турбота?":
            $ advance_time(5)
            mc "Тобто це тактичне рішення, а не турбота?"

            ar "Можеш називати як хочеш."
            $ advance_time(5)

        "Дякую.":
            $ advance_time(5)
            mc "Дякую."

            show arthur_kitchen aggressive
            ar "Не дякуй. Їж."
            $ advance_time(5)
            $ _arthur_warmth += 1

        "Летті казала, що ти для всіх готуєш.":
            $ advance_time(5)
            mc "Летті казала, що ти для всіх готуєш."

            show arthur_kitchen aggressive
            ar "...Хто розповів? Летті, мабуть."
            $ advance_time(5)

            show arthur_kitchen
            ar "Так, готую. Коли є час і продукти."
            $ advance_time(5)

            ar "Це... заспокоює."
            $ advance_time(5)
            $ _arthur_warmth += 2

    # ═══ ГОЛОВНИЙ ВИБІР — 5 гілок ═══
    menu:

        # ── ГІЛКА 1: Матір (глибока, CG) ──
        "Звідки ти взагалі навчився готувати?":
            $ advance_time(5)
            mc "Звідки ти взагалі навчився готувати?"

            show arthur_kitchen aggressive
            ar "Лізти в мою особисту історію — не найліпший спосіб це зробити."
            $ advance_time(5)

            menu:
                "Просто хочу пізнати тебе більше.":
                    $ advance_time(5)
                    mc "Просто хочу пізнати тебе більше."

                    show arthur_kitchen
                    ar "..."
                    $ advance_time(5)

                    # Якщо був теплий до цього — відкривається легше
                    if _arthur_warmth >= 2:
                        show arthur_kitchen tired
                        ar "Мати вчила. Давно. Ще до того, як все змінилося."
                        $ advance_time(5)
                    else:
                        show arthur_kitchen tired
                        ar "...Мати вчила."
                        $ advance_time(5)
                        pause 0.5
                        ar "Давно."
                        $ advance_time(5)

                    ar "Вона казала — хто вміє готувати, той ніколи не буде самотнім."
                    $ advance_time(5)
                    $ set_flag("arthur_mentioned_mother")
                    $ chemistry["Артур"] += 3

                    show arthur_kitchen
                    $ add_insight("arthur_mother_taught", "Мати Артура вчила його готувати. «Хто вміє готувати — ніколи не буде самотнім.»")

                    scene cg_arthur_kitchen with dissolve
                    pause 3.0
                    $ persistent.cg_unlocked.add("arthur_kitchen_cg")

                    scene bg_foodcourt with dissolve
                    show arthur_kitchen at char_center

                "Вибач. Не зважай.":
                    $ advance_time(5)
                    mc "Вибач. Не зважай."

                    show arthur_kitchen
                    ar "Та ні, усе норм."
                    $ advance_time(5)

                    ar "Спершу треба придбати кілька келихів міцного. Потім особисті питання."
                    $ advance_time(5)
                    $ chemistry["Артур"] += 1
                    $ set_flag("arthur_drinks_first")

                "[[Не тиснути.]":
                    $ advance_time(5)
                    show arthur_kitchen
                    $ chemistry["Артур"] += 1

        # ── ГІЛКА 2: Обладнання (легша, CG) ──
        "А що з кухонним обладнанням тут?":
            $ advance_time(5)
            mc "А що з кухонним обладнанням тут?"

            ar "Жахливе."
            $ advance_time(5)

            show arthur_kitchen smile
            ar "Але я знайшов робочий тостер на минулому рейді. Це було... приємно."
            $ advance_time(5)

            show arthur_kitchen
            ar "Дрібниці тримають на плаву. Тостер, гострий ніж, чиста сковорідка."
            $ advance_time(5)
            $ chemistry["Артур"] += 2

            if _arthur_warmth >= 2:
                ar "Якщо побачиш щось на рейді — тягни. Я знайду застосування."
                $ advance_time(5)
                $ set_flag("arthur_wants_kitchen_gear")

            scene cg_arthur_kitchen with dissolve
            pause 3.0
            $ persistent.cg_unlocked.add("arthur_kitchen_cg")

            scene bg_foodcourt with dissolve
            show arthur_kitchen at char_center

        # ── ГІЛКА 3: Команда (середня, без CG) ──
        "Хто ще тут їсть?":
            $ advance_time(5)
            mc "Хто ще тут їсть?"

            ar "Амір приходить перший. Завжди."
            $ advance_time(5)

            show arthur_kitchen smile
            ar "Потім дивується що каша не піца."
            $ advance_time(5)

            show arthur_kitchen
            ar "Аоі бере з собою. Летті каже що отруюю. Квінсі не приходить."
            $ advance_time(5)

            menu:
                "А Елеонор?":
                    $ advance_time(5)
                    mc "А Елеонор?"

                    show arthur_kitchen tired
                    ar "..."
                    $ advance_time(5)

                    ar "Елеонор їсть окремо."
                    $ advance_time(5)
                    $ set_flag("arthur_eleanor_eats_alone")
                    $ chemistry["Артур"] += 2

                "Квінсі — його проблеми.":
                    $ advance_time(5)
                    mc "Квінсі — його проблеми."

                    show arthur_kitchen aggressive
                    ar "Мої проблеми. Я відповідаю за кожного."
                    $ advance_time(5)
                    $ chemistry["Артур"] += 1

                "[[Не коментувати.]":
                    $ advance_time(5)
                    $ chemistry["Артур"] += 1

        # ── ГІЛКА 4: Допомогти (взаємодія, без CG) ──
        "Можу допомогти? Помити, порізати, що треба.":
            $ advance_time(5)
            mc "Можу допомогти? Помити, порізати, що треба."

            show arthur_kitchen very_surprised
            ar "..."
            $ advance_time(5)

            if _arthur_warmth >= 2:
                show arthur_kitchen
                ar "Ніж на стійці. Гриби дрібно."
                $ advance_time(5)
                $ chemistry["Артур"] += 3
                $ set_flag("arthur_let_help_cook")
                $ add_insight("arthur_shared_kitchen", "Артур пустив на свою кухню. Це більше ніж здається.")
            else:
                show arthur_kitchen aggressive
                ar "Моя кухня. Моя відповідальність."
                $ advance_time(5)

                ar "Сядь. Їж."
                $ advance_time(5)
                $ chemistry["Артур"] += 1

        # ── ГІЛКА 5: Піти (негатив) ──
        "Нічого, я піду.":
            $ advance_time(5)
            mc "Нічого, я піду."

            show arthur_kitchen aggressive
            ar "Яка втрата."
            $ advance_time(5)
            $ chemistry["Артур"] -= 1

            # Коротка кінцівка — без чайника, без фіналу
            $ store.seen_dialogues.add("arthur_cooking")
            $ set_flag("arthur_cooking_done")
            $ set_flag("arthur_cooking_rejected")
            $ add_journal_entry("Артур готував. Я пішов.", "conversation")

            hide arthur_kitchen with dissolve
            stop music fadeout 1.0
            stop audio fadeout 1.0
            return

    # ═══ ЧАЙНИК — спільний для гілок 1-4 ═══
    play sound "audio/kettle_whistle.mp3"
    show arthur_kitchen surprised
    pause 0.3
    show arthur_kitchen angry
    ar "Заради Сола—"
    $ advance_time(5)

    hide arthur_kitchen with dissolve
    pause 1.0
    stop sound fadeout 0.3

    show arthur_kitchen at char_center with dissolve

    show arthur_kitchen
    ar "Це все що тебе цікавило?"
    $ advance_time(5)

    menu:
        "Поки що так.":
            $ advance_time(5)
            ar "Зрозумів."
            $ advance_time(5)

        "[[Кивнути.]":
            $ advance_time(5)

    # ═══ ЗАКРИТТЯ ═══
    $ store.seen_dialogues.add("arthur_cooking")
    $ set_flag("arthur_cooking_done")
    $ add_insight("arthur_cooks_for_team", "Артур готує для загону. Каже — тактика, не турбота.")
    $ add_journal_entry("Артур готував кашу з грибами. Каже — для концентрації.", "conversation")

    hide arthur_kitchen with dissolve
    stop music fadeout 1.0
    stop audio fadeout 1.0

    return
