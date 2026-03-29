# game/dialogues/amir/amir_friends_milestone.rpy
# MILESTONE: Амір називає гравця своїм "Player 2" — емоційний момент для геймера

init python:
    DIALOGUE_ENTRIES.append({
        "id": "amir_friends_milestone",
        "who": "Амір",
        "conditions": {
            "flag_true": ["amir_trust_milestone_done"],
            "flag_false": ["amir_friends_milestone_done"],
            "rank_min": 2,
            "chemistry_min": ("Амір", 120),
        },
        "priority": 85,
        "chance": 100,
        "label": "amir_friends_milestone",
    })

label amir_friends_milestone:
    show amir at char_center
    $ store.talked_today.add("Амір")

    am "Можеш сісти? Мені треба щось... офіційно оголосити."
    $ advance_time(5)

    mc "Офіційно?"
    $ advance_time(5)

    am "Так. Я думав над цим довго. Ну, кілька петель точно. Може, більше."
    $ advance_time(5)

    am "В кожній грі є Player 1. Це я. Завжди був. Player 1 — одинак, який проходить все сам, бо нікому не довіряє контролер."
    $ advance_time(5)

    am "Але найкращі ігри — кооперативні. І найкращий кооп — коли Player 2 не просто поруч, а розуміє, коли стріляти, а коли прикривати."
    $ advance_time(5)

    mc "Амір, ти..."
    $ advance_time(5)

    am "Ти — мій Player 2. Офіційно. Безстроково. Без права відмови."
    $ advance_time(5)

    menu:
        "Прийнято, Player 1.":
            $ advance_time(5)
            mc "Прийнято, Player 1."
            am "...Окей, я зараз точно не плачу. Це алергія. На пил. Який у вентиляції. Яку я сам лагодив, тож це моя провина."
            $ advance_time(5)

        "Це найбільше, що ти міг мені сказати, так?":
            $ advance_time(5)
            mc "Це найбільше, що ти міг мені сказати, так?"
            am "Ти навіть не уявляєш. Я ніколи нікого так не називав. Player 2 — це не просто номер. Це людина, заради якої ти не ставиш на паузу."
            $ advance_time(5)

    am "Знаєш, у старих іграх Player 2 завжди був другорядним. Луїджі, Тейлс, другий контролер, який ніхто не бере."
    $ advance_time(5)

    am "Але не тут. Тут Player 2 — рівний. Тому що я так вирішив. І тому що ти це заслужив."
    $ advance_time(5)

    am "А тепер — давай поб'ємо мій рекорд. Разом. Бо удвох — ми нестримні."
    $ advance_time(5)

    $ add_chemistry("Амір", 8)

    $ store.seen_dialogues.add("amir_friends_milestone")
    $ set_flag("amir_friends_milestone_done")
    $ add_insight("amir_player2", "Амір назвав гравця своїм Player 2 — для нього це найвища форма дружби і визнання")

    hide amir
    return
