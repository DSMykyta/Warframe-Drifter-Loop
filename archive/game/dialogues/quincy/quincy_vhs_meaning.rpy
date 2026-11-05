# game/dialogues/quincy/quincy_vhs_meaning.rpy
# Чому Квінсі колекціонує VHS

init python:
    DIALOGUE_ENTRIES.append({
        "id": "quincy_vhs_meaning",
        "who": "Квінсі",
        "conditions": {
            "flag_true": ["quincy_vhs_done"],
            "flag_false": ["quincy_vhs_meaning_done"],
            "rank_min": 2,
            "chemistry_min": ("Квінсі", 30),
        },
        "priority": 50,
        "chance": 100,
        "label": "quincy_vhs_meaning",
    })

label quincy_vhs_meaning:
    show quince at char_center
    $ store.talked_today.add("Квінсі")

    "Квінсі перебирає касети. Акуратно, як хірург. Кожну бере двома руками."
    $ advance_time(5)

    mc "Ти з ними поводишся як з... артефактами."
    $ advance_time(5)

    qu "Because they are, mate. Кожна касета — це хтось, хто натиснув 'record' і вирішив: ось цей момент варто зберегти."
    $ advance_time(5)

    mc "Але ж є цифра. Вічна, без втрат якості."
    $ advance_time(5)

    qu "Вічна? Bollocks. Цифра — це ілюзія вічності. Один збій — і все зникає. Poof. Ніби й не було."
    $ advance_time(5)

    qu "VHS деградує. З кожним переглядом картинка трішки гірша. Кольори тьмяніші. Звук тихіший."
    $ advance_time(5)

    qu "Як пам'ять, розумієш? Ти не пам'ятаєш обличчя матері ідеально. Ти пам'ятаєш... відчуття. Розмитий контур."
    $ advance_time(5)

    mc "І це краще?"
    $ advance_time(5)

    qu "Imperfect memories are better than none. Стерта касета — це все одно касета. Стертий файл — це nothing."
    $ advance_time(5)

    qu "У петлі все обнуляється. Але касети залишаються. Дряпані, розмиті, imperfect. Але — залишаються."
    $ advance_time(5)

    $ store.seen_dialogues.add("quincy_vhs_meaning")
    $ set_flag("quincy_vhs_meaning_done")
    $ add_insight("quincy_vhs_philosophy", "Квінсі збирає VHS бо недосконалі спогади кращі за жодних. Касети — як пам'ять що деградує але існує")

    hide quince
    return
