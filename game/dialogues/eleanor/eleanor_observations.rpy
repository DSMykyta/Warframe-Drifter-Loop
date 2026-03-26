# game/dialogues/eleanor/eleanor_observations.rpy

init python:
    DIALOGUE_ENTRIES.append({
        "id": "eleanor_observations",
        "who": "Елеонор",
        "conditions": {
            "flag_true": ["eleanor_intro_done"],
            "flag_false": ["eleanor_observations_done"],
            "rank_min": 1,
        },
        "priority": 45,
        "chance": 100,
        "label": "eleanor_observations",
    })

label eleanor_observations:
    show eleanor at char_center
    $ store.talked_today.add("Елеонор")

    el "Ти помічав, як Квінсі завжди тримає праву руку ближче до кишені? Навіть коли розслаблений."
    $ advance_time(5)

    mc "Ні, не звертав уваги. А ти давно спостерігаєш?"
    $ advance_time(5)

    el "Завжди. Це... професійна звичка. Журналіст бачить деталі, які інші пропускають."
    $ advance_time(5)

    el "Летті, наприклад, п'є каву лівою рукою, але перев'язує рани — правою. Амір ніколи не повертається спиною до дверей."
    $ advance_time(5)

    mc "Це вражає. Або трохи лякає."
    $ advance_time(5)

    el "Люди кажуть те саме, коли розуміють, що я... бачу більше, ніж показую."
    $ advance_time(5)

    el "Іноді я просто... знаю, що хтось збирається щось сказати. Ще до того, як відкриє рот."
    $ advance_time(5)

    $ store.seen_dialogues.add("eleanor_observations")
    $ set_flag("eleanor_observations_done")
    $ add_insight("eleanor_watches", "Елеонор постійно спостерігає за людьми. Каже — звичка журналіста")

    hide eleanor
    return
