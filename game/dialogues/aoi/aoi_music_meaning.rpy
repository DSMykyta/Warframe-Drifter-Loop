# game/dialogues/aoi/aoi_music_meaning.rpy
# Чому On-Lyne важливі для Аоі

init python:
    DIALOGUE_ENTRIES.append({
        "id": "aoi_music_meaning",
        "who": "Аоі",
        "conditions": {
            "flag_true": ["aoi_onlyne_music_done"],
            "flag_false": ["aoi_music_meaning_done"],
            "rank_min": 2,
            "chemistry_min": ("Аоі", 35),
        },
        "priority": 45,
        "chance": 100,
        "label": "aoi_music_meaning",
    })

label aoi_music_meaning:
    show aoi at char_center
    $ store.talked_today.add("Аоі")

    "Аоі сидить з навушниками на шиї. Тиха мелодія ледь чутна."
    $ advance_time(5)

    ao "♪ ...we were on-lyne, before the static came... ♪"
    $ advance_time(5)

    mc "Знову On-Lyne?"
    $ advance_time(5)

    ao "Завжди. Ця пісня — 'Before the Static'. Їхній перший сингл."
    $ advance_time(5)

    ao "Я почула її, коли мені було шістнадцять. До... до всього. До того, як я дізналася, що люди можуть бути настільки жорстокими за зачиненими дверима."
    $ advance_time(5)

    mc "До чого — 'до всього'?"
    $ advance_time(5)

    ao "До того, як я навчилася читати людей. Не обличчя — а те, що за ними."
    $ advance_time(5)

    ao "Коли ти знаєш, що людина думає одне, а каже інше — музика стає єдиним чесним голосом. On-Lyne ніколи не брехали."
    $ advance_time(5)

    ao "Кожна їхня пісня — це момент, коли я ще вірила, що світ простий. Що люди кажуть те, що думають."
    $ advance_time(5)

    mc "А зараз?"
    $ advance_time(5)

    ao "Зараз я знаю краще. Але коли граю їхню музику — на три хвилини все повертається. Ті три хвилини того варті."
    $ advance_time(5)

    $ store.seen_dialogues.add("aoi_music_meaning")
    $ set_flag("aoi_music_meaning_done")
    $ add_insight("aoi_music_deeper", "On-Lyne для Аоі — не просто музика. Це зв'язок з часом коли вона ще не вміла читати людей")

    hide aoi
    return
