# game/dialogues/aoi/aoi_trust_milestone.rpy
# MILESTONE: Аоі знімає навушники — найвищий знак довіри

init python:
    DIALOGUE_ENTRIES.append({
        "id": "aoi_trust_milestone",
        "who": "Аоі",
        "conditions": {
            "flag_false": ["aoi_trust_milestone_done"],
            "chemistry_min": ("Аоі", 60),
        },
        "priority": 80,
        "chance": 100,
        "label": "aoi_trust_milestone",
    })

label aoi_trust_milestone:
    show aoi at char_center
    $ store.talked_today.add("Аоі")

    "Аоі стоїть біля вікна. Навушники на голові, як завжди. Але щось інакше."
    $ advance_time(5)

    ao "Ходи сюди."
    $ advance_time(5)

    mc "Щось трапилось?"
    $ advance_time(5)

    ao "Ні. Навпаки."
    $ advance_time(5)

    "Аоі повільно знімає навушники. Кладе їх на підвіконня."
    $ advance_time(5)

    ao "Я завжди ношу їх. Ти знаєш чому?"
    $ advance_time(5)

    mc "Музика?"
    $ advance_time(5)

    ao "Частково. Але більше — бар'єр. Між мною і... всім. Людьми. Шумом. Очікуваннями."
    $ advance_time(5)

    ao "Коли вони на мені — я в безпеці. Я контролюю, що чую. Що впускаю."
    $ advance_time(5)

    mc "А зараз?"
    $ advance_time(5)

    ao "Зараз... я хочу почути світ без фільтра. Поруч з тобою."
    $ advance_time(5)

    "Тиша. Справжня тиша. Не та, що за навушниками — а спільна."
    $ advance_time(5)

    ao "Дякую. Що не намагаєшся заповнити кожну секунду словами. Це... рідкість."
    $ advance_time(5)

    $ add_chemistry("Аоі", 5)

    $ store.seen_dialogues.add("aoi_trust_milestone")
    $ set_flag("aoi_trust_milestone_done")
    $ add_insight("aoi_trust", "Аоі зняла навушники при мені. Для неї це — найвищий знак довіри")

    hide aoi
    return
