# game/events/pairs/aoi_lettie_medbay.rpy
# Парний діалог: Аоі та Летті в медпункті

init python:
    BANTER_ENTRIES.append({
        "id": "aoi_lettie_medbay",
        "location": "medbay",
        "chars": ["Аоі", "Летті"],
        "conditions": {
            "flag_false": ["pair_aoi_lettie_medbay_seen"],
        },
        "label": "aoi_lettie_medbay",
    })

label aoi_lettie_medbay:
    show aoi at left
    show lettie at right

    ao "Летті. Я принесла чай."
    $ advance_time(5)

    le "Чай? Ти знаєш, що я п'ю тільки каву."
    $ advance_time(5)

    ao "Знаю. Тому принесла чай. Тобі потрібен сон, а не черговий кофеїн."
    $ advance_time(5)

    le "..."
    $ advance_time(5)

    le "Нахабна. Але... дякую."
    $ advance_time(5)

    ao "Будь ласка."
    $ advance_time(5)

    le "Тільки нікому не кажи, що я це випила."
    $ advance_time(5)

    $ set_flag("pair_aoi_lettie_medbay_seen")
    $ store.seen_dialogues.add("aoi_lettie_medbay")

    hide aoi
    hide lettie
    return
