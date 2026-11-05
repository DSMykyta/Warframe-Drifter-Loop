# game/dialogues/eleanor/eleanor_journalism_past.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "eleanor_journalism_past",
        "who": "Елеонор",
        "conditions": {
            "flag_true": ["eleanor_journalism_done"],
            "flag_false": ["eleanor_journalism_past_done"],
            "chemistry_min": ("Елеонор", 50),
            "rank_min": 2,
        },
        "priority": 50,
        "chance": 100,
        "label": "eleanor_journalism_past",
    })

label eleanor_journalism_past:
    show eleanor at char_center
    $ store.talked_today.add("Елеонор")

    el "Пам'ятаєш, я казала, що копала там, де не хотіли? Я не договорила."
    $ advance_time(5)

    mc "Що ти розслідувала?"
    $ advance_time(5)

    el "ІКР. Інститут Координованих Ресурсів. Офіційно — гуманітарна організація. Допомога після катастроф, відновлення інфраструктури."
    $ advance_time(5)

    el "Неофіційно... Я знайшла патерни. Кожне місто, куди вони заходили з «допомогою» — через рік починало хворіти."
    $ advance_time(5)

    mc "Хворіти? Як?"
    $ advance_time(5)

    el "Технологічний занепад. Системи виходили з ладу. Не одразу — повільно, як іржа. Спочатку дрібниці. Потім — все."
    $ advance_time(5)

    el "Я написала три статті. Першу — надрукували. Другу — редактор відхилив без пояснень. Третю..."
    $ advance_time(5)

    el "Третю мені повернули з запискою: «Не для публікації. Ніколи.»"
    $ advance_time(5)

    mc "І ти зупинилась?"
    $ advance_time(5)

    el "Ні. Я почала копати глибше. І ось тоді стало по-справжньому страшно."
    $ advance_time(5)

    el "Бо я зрозуміла — те, що вбивало міста, не було випадковістю. Воно мало назву. І хтось це контролював."
    $ advance_time(5)

    el "Але довести... У мене не було доказів, які б витримали перевірку. Тільки патерни. Мої патерни."
    $ advance_time(5)

    $ store.seen_dialogues.add("eleanor_journalism_past")
    $ set_flag("eleanor_journalism_past_done")
    $ add_insight("eleanor_icr_investigation", "Елеонор розслідувала ІКР до колапсу. Знайшла зв'язок між їхньою «допомогою» і технологічним занепадом міст.")

    hide eleanor
    return
