# game/dialogues/amir/amir_nightmares.rpy
# Амір розповідає про свої кошмари — схеми, що горять, люди, що кричать

init python:
    DIALOGUE_ENTRIES.append({
        "id": "amir_nightmares",
        "who": "Амір",
        "conditions": {
            "flag_true": ["amir_nightmares_hint_done"],
            "flag_false": ["amir_nightmares_done"],
            "rank_min": 2,
            "chemistry_min": ("Амір", 50),
        },
        "priority": 50,
        "cooldown_tag": "heavy_lore",
        "chance": 100,
        "label": "amir_nightmares",
    })

label amir_nightmares:
    show amir at char_center
    $ store.talked_today.add("Амір")

    am "Знаєш, чому я граю до третьої ночі?"
    $ advance_time(5)

    mc "Тому що ти геймер?"
    $ advance_time(5)

    am "Тому що коли засинаю раніше — вони приходять."
    $ advance_time(5)

    am "Схеми. Мікросхеми. Плати. Вони горять, плавляться, але не тихо. Вони кричать. Як люди."
    $ advance_time(5)

    mc "Схеми не кричать, Амір."
    $ advance_time(5)

    am "Я знаю. Але в снах — кричать. Кожен дріт, кожен контакт — голос. І я чую, як вони просять мене полагодити, але мої руки проходять крізь них."
    $ advance_time(5)

    am "А потім схеми стають обличчями. Людьми, яких я... не знаю. Чи знаю? Не пам'ятаю."
    $ advance_time(5)

    menu:
        "Може, це спогади?":
            $ advance_time(5)
            mc "Може, це спогади? Те, що було до петлі?"
            am "Може. Або те, що буде після. Знаєш, що найстрашніше? Я не знаю, чи це минуле чи майбутнє. Може, я вже бачив, як все закінчується."
            $ advance_time(5)
            am "І моя голова захищає мене, показуючи це як сон. Щоб я не зійшов з розуму вдень."
            $ advance_time(5)

        "Ти розповідав комусь?":
            $ advance_time(5)
            mc "Ти розповідав комусь із команди?"
            am "Летті знає, що я погано сплю. Вона дає мені таблетки іноді. Але деталі... ні. Як ти скажеш людям, що бачиш, як горить все, що вони побудували?"
            $ advance_time(5)
            am "Я — техник. Я маю будувати, лагодити, створювати. А в снах — тільки руйную."
            $ advance_time(5)

    am "Тому ігри. Тому музика. Тому жарти. Все, що завгодно, аби не сидіти в тиші. Бо в тиші я чую, як горять дроти."
    $ advance_time(5)

    am "...Вибач. Зазвичай я веселіший. Давай поговоримо про щось інше. Будь ласка."
    $ advance_time(5)

    $ store.seen_dialogues.add("amir_nightmares")
    $ set_flag("amir_nightmares_done")
    $ add_insight("amir_nightmare_detail", "Аміру сняться палаючі схеми з людськими голосами — він не знає чи це спогади чи пророцтва")

    hide amir
    return
