# game/events/pairs/eleanor_lettie_info.rpy
# Парний діалог: Елеонор та Летті в інфо-кімнаті

init python:
    BANTER_ENTRIES.append({
        "id": "eleanor_lettie_info",
        "location": "security_desk",
        "chars": ["Елеонор", "Летті"],
        "conditions": {
            "flag_false": ["pair_eleanor_lettie_info_seen"],
        },
        "label": "eleanor_lettie_info",
    })

label eleanor_lettie_info:
    show eleanor at left
    show lettie at right

    el "Летті, у мене питання. Суто професійне."
    $ advance_time(5)

    le "Якщо про здоров'я — прийди в медпункт. Якщо про щось інше — я не зацікавлена."
    $ advance_time(5)

    el "Про записи. Ти ведеш медичний журнал?"
    $ advance_time(5)

    le "Так. Чому?"
    $ advance_time(5)

    el "Мені цікаво порівняти наші нотатки. Я бачу закономірності у поведінці людей, ти — у їхньому здоров'ї."
    $ advance_time(5)

    le "Хочеш сказати, що поведінка і здоров'я пов'язані? Яке відкриття."
    $ advance_time(5)

    el "Хочу сказати, що разом ми побачимо більше."
    $ advance_time(5)

    le "...Може. Поговоримо пізніше."
    $ advance_time(5)

    $ set_flag("pair_eleanor_lettie_info_seen")
    $ store.seen_dialogues.add("eleanor_lettie_info")

    hide eleanor
    hide lettie
    return
