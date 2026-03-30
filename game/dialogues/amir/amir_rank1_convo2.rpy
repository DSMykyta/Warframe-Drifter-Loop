# game/dialogues/amir/amir_rank1_convo2.rpy
# Амір — Ранг 1, Розмова 2: Ігри та роботи

init python:
    DIALOGUE_ENTRIES.append({
        "id": "amir_rank1_convo2",
        "who": "Амір",
        "conditions": {
            "flag_true": ["amir_intro_done", "amir_rank1_convo1_done"],
            "flag_false": ["amir_rank1_convo2_done"],
            "rank_min": 1,
        },
        "priority": 45,
        "chance": 100,
        "label": "amir_rank1_convo2",
    })

label amir_rank1_convo2:
    show amir at char_center
    $ store.talked_today.add("Амір")
    $ dialogue_begin()

    am "Дрифтер! Важливе питання! Критичне!"

    mc "Слухаю?"

    am "У майбутньому є ігри?!"

    menu:
        "Ні. Усі ігри заборонили під час Великої Марсіанської Війни.":
            jump amir_r1c2_prank

        "Є, звісно. Ми ж не всі роботи.":
            jump amir_r1c2_robots

        "Є. А що?":
            jump amir_r1c2_favorites

label amir_r1c2_prank:
    am "Що?! Серйоз—"

    am "Стоп."

    am "Мій внутрішній детектор нісенітниць щойно спрацював."

    mc "Ахаха, не втримався. Вибач."

    am "Ну-ну, дуже смішно."

    mc "Та ладно, є ігри. Заспокойся."

    jump amir_r1c2_favorites

label amir_r1c2_robots:
    am "Які мої улюблені— Стоп."

    am "ЩО?!"

    am "РОБОТИ?!"

    am "ТИ ЩОЙНО СКАЗАВ РОБОТИ?!"

    mc "Ну... так. Цефалони, дрони Корпусу, Сентієнти..."

    am "уменестількипитаньщоянеможунавітьзібратисьздумками"

    am "тинерозумієшщоцедляменеозначає"

    mc "Тільки не перегорай."

    am "МОЖУ ПЕРЕГОРІТИ!"

    am "ладно... ладно... я в нормі..."

    mc "То що, про ігри?"

    am "Ігри... так... Вибач, мені треба піти прилягти."

    am "Або пробігти кілька кіл навколо бази."

    am "Не знаю що, але щось треба зробити з цією енергією."

    $ add_chemistry("Амір", 2)
    $ set_flag("amir_robots_hyped")
    $ add_insight("amir_robots_obsession", "Амір божеволіє від теми роботів. Ледь не перегорів від радощів.")

    jump amir_r1c2_end

label amir_r1c2_favorites:
    am "Ну, і яке в тебе улюблене? Настілки? Карти? Аркади? Відеоігри?"

    menu:
        "У мене була тільки одна настільна гра. Одна.":
            am "Настілки! Я їх обожнюю! Ну, я все обожнюю, але настілки — це особливе."

            am "Тільки зі мною ніхто більше не грає після того інциденту з додатковими правилами до «Оцелотів у Космосі 4»."

            am "О! Ідея! Ти вчиш мене свою гру, а я тебе — свою!"

            menu:
                "Домовились!":
                    am "ЙЄСС! Ти не пошкодуєш, обіцяю!"

                    $ add_chemistry("Амір", 4)
                    $ set_flag("amir_boardgame_deal")
                    $ add_insight("amir_boardgames", "Амір обожнює настільні ігри, але ніхто не хоче з ним грати. Ми домовились обмінятись іграми.")

                "А в нас хіба немає роботи?":
                    am "Роботу ЗАВЖДИ можна відкласти заради настілок!"

                    am "Ну добре, не завжди. Але зараз — точно!"

                    $ add_chemistry("Амір", 2)

        "Я не дуже вмію грати, чесно.":
            am "Не біда! Хочеш, навчу?"

            menu:
                "Було б круто.":
                    am "ЧУДОВО! Зі мною вже ніхто не хоче грати, тож це буде прекрасно!"

                    am "Клянусь, не пошкодуєш!"

                    mc "Ой-ой."

                    am "ЗАПІЗНО! НАЗАД ДОРОГИ НЕМАЄ!"

                    $ add_chemistry("Амір", 4)
                    $ set_flag("amir_gaming_lessons")

                "Може, якось іншим разом.":
                    am "Ну ладно... Але пропозиція безстрокова!"

                    $ add_chemistry("Амір", 2)

    jump amir_r1c2_end

label amir_r1c2_end:

    $ dialogue_end()
    $ store.seen_dialogues.add("amir_rank1_convo2")
    $ set_flag("amir_rank1_convo2_done")

    hide amir
    return
