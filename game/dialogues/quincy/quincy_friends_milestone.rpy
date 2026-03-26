# game/dialogues/quincy/quincy_friends_milestone.rpy
# MILESTONE: Квінсі дарує VHS-касету зі записом команди

init python:
    DIALOGUE_ENTRIES.append({
        "id": "quincy_friends_milestone",
        "who": "Квінсі",
        "conditions": {
            "flag_false": ["quincy_friends_milestone_done"],
            "chemistry_min": ("Квінсі", 120),
        },
        "priority": 85,
        "chance": 100,
        "label": "quincy_friends_milestone",
    })

label quincy_friends_milestone:
    show quince at char_center
    $ store.talked_today.add("Квінсі")

    "Квінсі тримає касету. Не зі своєї колекції — нову. На ній маркером написано: 'US.'"
    $ advance_time(5)

    qu "Right. Це буде weird, але just... take it."
    $ advance_time(5)

    mc "Що це?"
    $ advance_time(5)

    qu "Я знайшов камеру. Стару, аналогову. Записує на VHS."
    $ advance_time(5)

    qu "І я... знімав. Потроху. Коли ніхто не дивився."
    $ advance_time(5)

    mc "Що на ній?"
    $ advance_time(5)

    qu "Ми. Всі. Артур, як він вранці варить каву і думає, що ніхто не бачить, як він усміхається. Летті, яка співає в медвідсіку. Амір, який розмовляє з генератором."
    $ advance_time(5)

    qu "Аоі, яка складає журавликів і закриває очі після кожного. Елеонор, яка пише щось у блокнот і потім перечитує п'ять разів."
    $ advance_time(5)

    qu "І ти. Як ти ходиш між нами і... тримаєш все це разом."
    $ advance_time(5)

    mc "Квінсі..."
    $ advance_time(5)

    qu "Не треба. Не роби це emotional. Я даю тобі касету, not proposing."
    $ advance_time(5)

    "Він усміхається. Але очі — серйозні."
    $ advance_time(5)

    qu "Петля стирає дні. Але плівку — ні. Якщо колись все забудеться... подивись цю касету. So we remember."
    $ advance_time(5)

    menu:
        "Дякую. Це найкращий подарунок.":
            $ advance_time(5)
            mc "Дякую. Це найкращий подарунок, який мені давали."

            qu "Yeah, well. Don't tell anyone. I have a reputation."
            $ advance_time(5)

        "Ми не забудемо.":
            $ advance_time(5)
            mc "Ми не забудемо. Навіть без касети."

            qu "Maybe. Але з касетою — напевно."
            $ advance_time(5)

    $ chemistry["Квінсі"] += 10

    $ store.seen_dialogues.add("quincy_friends_milestone")
    $ set_flag("quincy_friends_milestone_done")
    $ add_insight("quincy_filmmaker", "Квінсі потайки знімав нас усіх на VHS. Зберіг моменти які петля б стерла. Щоб ми пам'ятали")

    hide quince
    return
