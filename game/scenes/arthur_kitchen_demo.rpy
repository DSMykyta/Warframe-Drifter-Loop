# game/scenes/arthur_kitchen_demo.rpy
# Chemistry ~15, rank 1. Потребує: arthur_about_team_done.
# Про що: Артур дозволив тобі бути в його просторі. Не зіпсуй.
# 5 кінцівок визначаються накопиченим warmth, не прямим вибором.
# Деякі "ввічливі" відповіді дратують. Деякі "грубі" — працюють.
# Обличчя Артура — єдина підказка для гравця.

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

    show arthur_kitchen at char_center with dissolve
    $ store.talked_today.add("Артур")
    $ _w = 0

    ar "Каша з сушеними грибами. Нічого особливого."
    $ advance_time(5)

    # ═══ BEAT 1: Перша реакція ═══
    menu:
        "О, дякую! Виглядає чудово.":
            $ advance_time(5)
            mc "О, дякую! Виглядає чудово."
            show arthur_kitchen aggressive
            ar "Не дякуй. Не для тебе старався."
            $ advance_time(5)
            # Подяка робить це особистим. Він цього не хоче.
            $ _w -= 1

        "Виглядає... сумнівно.":
            $ advance_time(5)
            mc "Виглядає... сумнівно."
            show arthur_kitchen aggressive
            pause 0.3
            show arthur_kitchen smile
            ar "Чесно. Ціную."
            $ advance_time(5)
            ar "Їж. Потім скаржся."
            $ advance_time(5)
            # Чесність. Він це поважає.
            $ _w += 1

        "[[Сісти. Взяти ложку.]":
            $ advance_time(5)
            pause 0.5
            # Мовчки сів — не тиснеш, не лащишся. Правильно.
            $ _w += 2

    show arthur_kitchen
    pause 0.3

    ar "Я не люблю, коли люди йдуть на завдання голодними."
    $ advance_time(5)

    ar "Впливає на концентрацію."
    $ advance_time(5)

    # ═══ BEAT 2: Тон розмови ═══
    menu:
        "Ти турбуєшся за нас.":
            $ advance_time(5)
            mc "Ти турбуєшся за нас."
            show arthur_kitchen aggressive
            ar "Я турбуюся за результат місій."
            $ advance_time(5)
            # Назвав це турботою вголос — він заперечує.
            $ _w -= 1

        "Тактика.":
            $ advance_time(5)
            mc "Тактика."
            show arthur_kitchen
            ar "Можеш називати як хочеш."
            $ advance_time(5)
            $ _w += 1

        "[[Їсти мовчки.]":
            $ advance_time(5)
            pause 0.8
            show arthur_kitchen tired
            pause 0.3
            show arthur_kitchen
            $ _w += 2

    # ═══ BEAT 3: Артур на мить знімає маску ═══
    show arthur_kitchen tired
    pause 0.5
    ar "..."
    $ advance_time(5)

    # Він дивиться на свої руки. Мить тиші. Що ти робиш?
    menu:
        "Все нормально?":
            $ advance_time(5)
            mc "Все нормально?"
            show arthur_kitchen aggressive
            ar "Нормально."
            $ advance_time(5)
            # Прямий виклик. Він закривається.
            $ _w -= 1

        "Хто тебе навчив?":
            $ advance_time(5)
            mc "Хто тебе навчив?"
            show arthur_kitchen aggressive
            ar "Ти думаєш, що я достатньо тебе знаю, щоб ділитися таким?"
            $ advance_time(5)
            # Занадто рано. Занадто прямо.
            $ _w -= 2

        "Каша непогана.":
            $ advance_time(5)
            mc "Каша непогана."
            show arthur_kitchen
            ar "...Перебільшуєш."
            $ advance_time(5)
            # Повернув до їжі — безпечна тема. Не тиснув.
            $ _w += 1

        "[[Чекати.]":
            $ advance_time(5)
            pause 1.0
            show arthur_kitchen
            $ _w += 2

    # ═══ РОЗВ'ЯЗКА: залежить від _w ═══

    if _w >= 5:
        # ── КІНЦІВКА 1: Мати (найглибша, CG) ──
        show arthur_kitchen tired
        ar "Мати вчила."
        $ advance_time(5)

        pause 0.3

        ar "Давно. Ще до того, як все змінилося."
        $ advance_time(5)

        ar "Казала — хто вміє готувати, той ніколи не буде самотнім."
        $ advance_time(5)

        show arthur_kitchen
        pause 0.5

        $ set_flag("arthur_mentioned_mother")
        $ chemistry["Артур"] += 5
        $ add_insight("arthur_mother_taught", "Мати Артура вчила його готувати. «Хто вміє готувати — ніколи не буде самотнім.»")

        scene cg_arthur_kitchen with dissolve
        pause 4.0
        $ persistent.cg_unlocked.add("arthur_kitchen_cg")

    elif _w >= 3:
        # ── КІНЦІВКА 2: Тостер (тепла, CG) ──
        show arthur_kitchen smile
        ar "Знайшов робочий тостер на минулому рейді."
        $ advance_time(5)

        show arthur_kitchen
        ar "Це було... приємно."
        $ advance_time(5)

        ar "Дрібниці тримають на плаву. Тостер, гострий ніж, чиста сковорідка."
        $ advance_time(5)

        $ chemistry["Артур"] += 3
        $ set_flag("arthur_wants_kitchen_gear")

        scene cg_arthur_kitchen with dissolve
        pause 4.0
        $ persistent.cg_unlocked.add("arthur_kitchen_cg")

    elif _w >= 1:
        # ── КІНЦІВКА 3: Нейтральна ──
        show arthur_kitchen
        ar "Допомій тарілку, якщо не важко."
        $ advance_time(5)

        $ chemistry["Артур"] += 1

    elif _w >= -1:
        # ── КІНЦІВКА 4: Холодна ──
        show arthur_kitchen aggressive
        ar "Це все що тебе цікавило?"
        $ advance_time(5)

        ar "Зрозумів."
        $ advance_time(5)

    else:
        # ── КІНЦІВКА 5: Стіна ──
        show arthur_kitchen aggressive
        ar "Гадаю, тут є над чим попрацювати."
        $ advance_time(5)

        ar "Не тобі. Мені."
        $ advance_time(5)
        $ chemistry["Артур"] -= 2

    # ═══ ЗАКРИТТЯ ═══
    $ store.seen_dialogues.add("arthur_cooking")
    $ set_flag("arthur_cooking_done")
    $ add_insight("arthur_cooks_for_team", "Артур готує для загону. Каже — тактика, не турбота.")
    $ add_journal_entry("Артур готував кашу з грибами.", "conversation")

    if _w < 3:
        hide arthur_kitchen with dissolve

    stop music fadeout 1.0
    stop audio fadeout 1.0

    return
