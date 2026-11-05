# game/dialogues/quincy/quincy_camera.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "quincy_camera",
        "who": "Квінсі",
        "conditions": {
            "flag_false": ["quincy_camera_done"],
            "rank_min": 1,
        },
        "priority": 50,
        "chance": 100,
        "label": "quincy_camera",
    })

label quincy_camera:
    show quince at char_center
    $ store.talked_today.add("Квінсі")

    qu "Не рухайся. Знімаю."
    $ advance_time(5)

    mc "Квінсі, ти знову з камерою?"
    $ advance_time(5)

    qu "Always, mate. Камера — мій третій глаз. Все треба фіксувати."
    $ advance_time(5)

    mc "Навіщо?"
    $ advance_time(5)

    qu "Для доказів, innit. Якщо ми колись вибремось з цієї петлі — хтось має показати, що тут було."
    $ advance_time(5)

    menu:
        "А може це щось особисте?":
            $ advance_time(5)
            mc "А може це щось особисте?"

            qu "...Fk off. Я сказав — для доказів."
            $ advance_time(5)

            qu "...Просто... деякі речі зникають. Люди забувають. А плівка — ні."
            $ advance_time(5)
            $ set_flag("quincy_camera_personal")

        "Розумію. Хтось має бути літописцем.":
            $ advance_time(5)
            mc "Розумію. Хтось має бути літописцем."

            qu "Cheers. Хоч хтось це розуміє. Артур каже — не витрачай плівку. А я кажу — плівка важливіша за набої."
            $ advance_time(5)

    qu "Anyway. У мене ще пів касети. Треба знімати вибірково."
    $ advance_time(5)

    $ store.seen_dialogues.add("quincy_camera")
    $ set_flag("quincy_camera_done")
    $ add_insight("quincy_camera", "Квінсі знімає все на камеру. Каже — для доказів")

    hide quince
    return
