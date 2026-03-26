# game/romance.rpy
# Система романсу — ексклюзивний, з одним персонажем

init -5 python:

    def start_dating(name):
        """Починає романс з персонажем. Ексклюзивний."""
        if store.dating is not None:
            return False
        if store.chemistry.get(name, 0) < 160:
            return False
        store.dating = name
        set_flag("dating_" + name.lower())
        add_journal_entry("Ми з {} тепер разом. Це... несподівано. Але правильно.".format(name), "romance")
        return True

    def break_up(name):
        """Розрив стосунків."""
        if store.dating != name:
            return False
        store.dating = None
        set_flag("breakup_" + name.lower())
        store.chemistry[name] = max(0, store.chemistry[name] - 30)
        add_journal_entry("Розрив з {}. Я не думав що буде так боляче.".format(name), "romance")
        return True

    def check_flirt_consequences(target_name):
        """Перевіряє наслідки флірту з кимось при наявності партнера."""
        if store.dating is None:
            return None
        if store.dating == target_name:
            return None  # Фліртуєш з партнером — ок
        # Фліртуєш з іншим при наявності партнера
        partner = store.dating
        # Публічний флірт — одразу наслідки
        if get_chars_at(store.current_location):
            for char in get_chars_at(store.current_location):
                if char == partner:
                    # Партнер бачить — одразу конфлікт
                    store.chemistry[partner] -= 5
                    set_flag("flirt_caught_by_" + partner.lower())
                    return "caught"
        # Приватний — шанс через плітки
        add_gossip(target_name, "flirt", target_name)
        store.gossip_heat += 1
        return "private"


# ═══════════════════════════════════════════════
# РОМАНС-ДІАЛОГИ — ЗІЗНАННЯ
# ═══════════════════════════════════════════════

# Зізнання доступне коли chemistry >= 160 і friends_milestone вже пройдений

init python:
    for _char in ["Артур", "Елеонор", "Летті", "Амір", "Аоі", "Квінсі"]:
        _char_lower = _char.lower()
        DIALOGUE_ENTRIES.append({
            "id": "romance_confession_" + _char_lower,
            "who": _char,
            "conditions": {
                "chemistry_min": (_char, 160),
                "flag_true": [_char_lower + "_friends_milestone_done"],
                "flag_false": ["romance_confession_" + _char_lower + "_done", "dating_" + _char_lower],
                "dating": None,  # Не зустрічається з ніким
            },
            "priority": 90,
            "chance": 100,
            "label": "romance_confession_" + _char_lower,
        })


# ═══ Зізнання labels ═══

label romance_confession_артур:
    show arthur at char_center
    $ store.talked_today.add("Артур")

    ar "Треба поговорити. Серйозно."
    $ advance_time(5)

    ar "Я... не вмію це казати. Ніколи не вмів."
    $ advance_time(5)

    ar "Але ти — єдина людина, з якою я почуваюсь... справжнім. Без обладунків."
    $ advance_time(5)

    ar "Якщо ти відчуваєш те ж саме — скажи. Якщо ні — я зрозумію."
    $ advance_time(5)

    menu:
        "Я теж, Артуре. Давно хотів сказати.":
            $ advance_time(5)
            ar "...Добре. Тоді ми разом. Без зайвих слів."
            $ advance_time(5)
            $ start_dating("Артур")

        "Ти мій найкращий друг. Але не більше.":
            $ advance_time(5)
            ar "Зрозумів. Дякую за чесність."
            $ advance_time(5)
            $ chemistry["Артур"] -= 5

    $ store.seen_dialogues.add("romance_confession_артур")
    $ set_flag("romance_confession_артур_done")

    hide arthur
    return


label romance_confession_елеонор:
    show eleanor at char_center
    $ store.talked_today.add("Елеонор")

    el "Я ніколи нікому цього не кажу. Я навіть не впевнена що вмію."
    $ advance_time(5)

    el "Але я перестала читати твої думки. Спеціально. Бо хочу щоб ти сам сказав."
    $ advance_time(5)

    el "Те що я відчуваю... це не дослідження. Не закономірність. Це просто ти."
    $ advance_time(5)

    menu:
        "Елеоноре. Я теж.":
            $ advance_time(5)
            el "...Мені не потрібно читати думки. Я бачу. В очах."
            $ advance_time(5)
            $ start_dating("Елеонор")

        "Ти дуже важлива для мене. Але як подруга.":
            $ advance_time(5)
            el "Зрозуміло. Я запишу це. Десь."
            $ advance_time(5)
            $ chemistry["Елеонор"] -= 5

    $ store.seen_dialogues.add("romance_confession_елеонор")
    $ set_flag("romance_confession_елеонор_done")

    hide eleanor
    return


label romance_confession_летті:
    show lettie at char_center
    $ store.talked_today.add("Летті")

    le "Я поганий лікар."
    $ advance_time(5)

    mc "Чому?"
    $ advance_time(5)

    le "Бо лікарі не повинні закохуватись у пацієнтів."
    $ advance_time(5)

    le "А я закохалась. І навіть не можу звинувачувати кофеїн."
    $ advance_time(5)

    menu:
        "Летті. Це взаємно.":
            $ advance_time(5)
            le "...Чорт. Я сподівалась що ні. Тоді мені було б легше."
            $ advance_time(5)
            le "Але... добре. Ти і я. Поглянемо."
            $ advance_time(5)
            $ start_dating("Летті")

        "Ти мій друг. Я не хочу зіпсувати це.":
            $ advance_time(5)
            le "Правильна відповідь. Медично обґрунтована. Дякую."
            $ advance_time(5)
            $ chemistry["Летті"] -= 5

    $ store.seen_dialogues.add("romance_confession_летті")
    $ set_flag("romance_confession_летті_done")

    hide lettie
    return


label romance_confession_амір:
    show amir at char_center
    $ store.talked_today.add("Амір")

    am "Знаєш, в іграх є момент коли ти зустрічаєш NPC і розумієш — це не просто NPC."
    $ advance_time(5)

    am "Це... щось більше. Те що змінює всю гру."
    $ advance_time(5)

    am "Ти — моє 'щось більше'. Без жартів. Серйозно."
    $ advance_time(5)

    menu:
        "Аміре. Ти теж змінив мою гру.":
            $ advance_time(5)
            am "Achievement Unlocked: Two-Player Mode."
            $ advance_time(5)
            $ start_dating("Амір")

        "Ти мій найкращий друг, Аміре.":
            $ advance_time(5)
            am "...Game Over. Але дякую за гру."
            $ advance_time(5)
            $ chemistry["Амір"] -= 5

    $ store.seen_dialogues.add("romance_confession_амір")
    $ set_flag("romance_confession_амір_done")

    hide amir
    return


label romance_confession_аоі:
    show aoi at char_center
    $ store.talked_today.add("Аоі")

    ao "Тисяча журавликів."
    $ advance_time(5)

    mc "Що?"
    $ advance_time(5)

    ao "Я склала тисячу журавликів. І загадала бажання."
    $ advance_time(5)

    ao "Бажання — ти."
    $ advance_time(5)

    menu:
        "Аоі. Моє бажання теж — ти.":
            $ advance_time(5)
            ao "...Тоді воно здійснилось. Для нас обох."
            $ advance_time(5)
            $ start_dating("Аоі")

        "Аоі... Я не можу бути більше ніж друг.":
            $ advance_time(5)
            ao "Зрозуміло. Журавлик номер тисяча один — інше бажання."
            $ advance_time(5)
            $ chemistry["Аоі"] -= 5

    $ store.seen_dialogues.add("romance_confession_аоі")
    $ set_flag("romance_confession_аоі_done")

    hide aoi
    return


label romance_confession_квінсі:
    show quince at char_center
    $ store.talked_today.add("Квінсі")

    qu "Ненавиджу це. Ненавиджу що мушу це казати."
    $ advance_time(5)

    qu "Я знімав людей на камеру. Шукав ідеальний кадр. Завжди."
    $ advance_time(5)

    qu "З тобою я забуваю про камеру. Просто... дивлюсь."
    $ advance_time(5)

    qu "І це лякає. Чорт забирай."
    $ advance_time(5)

    menu:
        "Квінсі. Поклади камеру. Я тут.":
            $ advance_time(5)
            qu "...Поклав. Чорт. Перший раз за три роки."
            $ advance_time(5)
            $ start_dating("Квінсі")

        "Ти мій друг, Квінсі. Найкращий.":
            $ advance_time(5)
            qu "Ага. Друг. Класика жанру. Ладно."
            $ advance_time(5)
            $ chemistry["Квінсі"] -= 5

    $ store.seen_dialogues.add("romance_confession_квінсі")
    $ set_flag("romance_confession_квінсі_done")

    hide quince
    return
