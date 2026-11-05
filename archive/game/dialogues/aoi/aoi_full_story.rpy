# game/dialogues/aoi/aoi_full_story.rpy
# Повна розповідь Аоі про ICR

init python:
    DIALOGUE_ENTRIES.append({
        "id": "aoi_full_story",
        "who": "Аоі",
        "conditions": {
            "flag_true": ["aoi_icr_past_done", "has_dossier_aoi"],
            "flag_false": ["aoi_full_story_done"],
            "rank_min": 3,
            "chemistry_min": ("Аоі", 80),
        },
        "priority": 55,
        "cooldown_tag": "heavy_lore",
        "chance": 100,
        "label": "aoi_full_story",
    })

label aoi_full_story:
    show aoi at char_center
    $ store.talked_today.add("Аоі")

    ao "Ти знайшов досьє."
    $ advance_time(5)

    mc "Так. Але я хочу почути від тебе."
    $ advance_time(5)

    ao "Справедливо."
    $ advance_time(5)

    "Аоі сідає. Вперше — без навушників, без журавлика в руках. Просто сидить."
    $ advance_time(5)

    ao "ICR. Інтелектуальна Контр-Розвідка. Звучить офіційно, так? Офіційно — ми збирали інформацію. Неофіційно..."
    $ advance_time(5)

    ao "Неофіційно — ми знали все про кожного. Кожну слабкість. Кожну таємницю. Кожну точку тиску."
    $ advance_time(5)

    ao "Мене взяли коли мені було вісімнадцять. Я була... здібна. Спостережлива. Ідеальний кандидат."
    $ advance_time(5)

    mc "Що ти робила?"
    $ advance_time(5)

    ao "Аналіз. Профілювання. Я могла подивитися на людину десять хвилин — і знати, що вона зробить через тиждень."
    $ advance_time(5)

    ao "Спочатку це було... захоплюючим. Потім я зрозуміла, для чого ці профілі використовують."
    $ advance_time(5)

    ao "Людей ламали. Не фізично — психологічно. Мої звіти ставали інструкціями з руйнування. Кожен журавлик, якого я складаю — це людина, чий профіль я написала."
    $ advance_time(5)

    mc "Тому ти хочеш забути?"
    $ advance_time(5)

    ao "Хотіла. Раніше. Зараз... я не впевнена. Може, забувати — це теж форма зради."
    $ advance_time(5)

    ao "Я пішла з ICR коли зрозуміла, що наступний профіль — мій. Вони не відпускають тих, хто знає забагато."
    $ advance_time(5)

    ao "Петля врятувала мене. Іронічно, так? Пастка, яка стала сховком."
    $ advance_time(5)

    mc "Ти в безпеці. Тут."
    $ advance_time(5)

    ao "Я знаю. Вперше за довгий час — я знаю."
    $ advance_time(5)

    $ store.seen_dialogues.add("aoi_full_story")
    $ set_flag("aoi_full_story_done")
    $ add_insight("aoi_icr_full", "Аоі була аналітиком ICR з 18 років. Її профілі використовували щоб ламати людей. Пішла коли зрозуміла що наступна ціль — вона сама")

    hide aoi
    return
