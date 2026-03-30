# game/events/pairs/amir_aoi_arcade.rpy
# Парний діалог: Амір та Аоі в комп'ютерному клубі

init python:
    BANTER_ENTRIES.append({
        "id": "amir_aoi_arcade",
        "location": "comp_club",
        "chars": ["Аоі", "Амір"],
        "conditions": {
            "flag_false": ["pair_amir_aoi_arcade_seen"],
        },
        "label": "amir_aoi_arcade",
    })

label amir_aoi_arcade:
    show aoi at left
    show amir at right

    am "Аоі! Один раунд. Я знайшов нову комбо."
    $ advance_time(5)

    ao "Твоя остання 'нова комбо' тривала дві секунди."
    $ advance_time(5)

    am "Ця — три! Прогрес!"
    $ advance_time(5)

    ao "...Добре. Один раунд."
    $ advance_time(5)

    "Через хвилину Амір програє."
    $ advance_time(5)

    am "Як. ЯК."
    $ advance_time(5)

    ao "Ти завжди атакуєш першим. Це передбачувано."
    $ advance_time(5)

    $ set_flag("pair_amir_aoi_arcade_seen")
    $ store.seen_dialogues.add("amir_aoi_arcade")

    hide aoi
    hide amir
    return
