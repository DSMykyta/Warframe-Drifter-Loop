# game/events/gifts/aoi_gift_reactions.rpy
# Реакції Аоі на погані подарунки (кухонна техніка — стереотипи)

# ═══════════════════════════════════════════════
# ТОСТЕР
# ═══════════════════════════════════════════════

init python:
    DIALOGUE_ENTRIES.append({
        "id": "aoi_bad_gift_toaster",
        "who": "Аоі",
        "conditions": {
            "flag_true": ["bad_gift_aoi_toaster"],
            "flag_false": ["gift_aoi_toaster_done"],
            "rank_min": 1,
        },
        "priority": 75,
        "chance": 100,
        "label": "aoi_bad_gift_toaster",
    })

label aoi_bad_gift_toaster:
    show aoi at char_center
    $ store.talked_today.add("Аоі")

    ao "Є розмова."
    $ advance_time(5)

    ao "Той тостер, що ти приніс."
    $ advance_time(5)

    mc "Щось не так?"
    $ advance_time(5)

    ao "Ти подарував мені кухонну техніку."
    $ advance_time(5)

    ao "Мені. Кухонну. Техніку."
    $ advance_time(5)

    ao "Ти хоч розумієш, як це виглядає?"
    $ advance_time(5)

    mc "Я не мав на увазі нічого такого..."
    $ advance_time(5)

    ao "Може й не мав. Але я все життя чую ці натяки."
    $ advance_time(5)

    ao "'Приготуй щось', 'Ти ж вмієш', 'Це жіноче'..."
    $ advance_time(5)

    ao "Мені боляче, що навіть тут це повторюється."
    $ advance_time(5)

    mc "Вибач. Я справді не думав про це."
    $ advance_time(5)

    ao "...Добре. Вірю. Просто... не роби так більше."
    $ advance_time(5)

    $ set_flag("gift_aoi_toaster_done")
    $ store.seen_dialogues.add("aoi_bad_gift_toaster")
    $ add_insight("aoi_stereotypes", "Аоі ненавидить коли її зводять до стереотипів. Кухонна техніка — табу.")

    hide aoi
    return


# ═══════════════════════════════════════════════
# ТОСТЕР-ДУХОВКА
# ═══════════════════════════════════════════════

init python:
    DIALOGUE_ENTRIES.append({
        "id": "aoi_bad_gift_toaster_oven",
        "who": "Аоі",
        "conditions": {
            "flag_true": ["bad_gift_aoi_toaster_oven"],
            "flag_false": ["gift_aoi_toaster_oven_done"],
            "rank_min": 1,
        },
        "priority": 75,
        "chance": 100,
        "label": "aoi_bad_gift_toaster_oven",
    })

label aoi_bad_gift_toaster_oven:
    show aoi at char_center
    $ store.talked_today.add("Аоі")

    ao "Нам треба поговорити."
    $ advance_time(5)

    ao "Та духовка. Серйозно?"
    $ advance_time(5)

    mc "Я думав, корисна річ..."
    $ advance_time(5)

    ao "Корисна. Для когось на кухні. А я не на кухні."
    $ advance_time(5)

    ao "Я механік. Я вожу скутер. Я слухаю On-lyne на повній гучності."
    $ advance_time(5)

    ao "І мені набридло, що люди бачать лише те, що хочуть бачити."
    $ advance_time(5)

    mc "Ти маєш рацію. Це було безтактно."
    $ advance_time(5)

    ao "Ладно. Забули. Але запам'ятай."
    $ advance_time(5)

    $ set_flag("gift_aoi_toaster_oven_done")
    $ store.seen_dialogues.add("aoi_bad_gift_toaster_oven")
    $ add_insight("aoi_identity", "Аоі визначає себе через свої інтереси, не стереотипи. Поважай це.")

    hide aoi
    return


# ═══════════════════════════════════════════════
# МІКРОХВИЛЬОВКА
# ═══════════════════════════════════════════════

init python:
    DIALOGUE_ENTRIES.append({
        "id": "aoi_bad_gift_microwave",
        "who": "Аоі",
        "conditions": {
            "flag_true": ["bad_gift_aoi_microwave"],
            "flag_false": ["gift_aoi_microwave_done"],
            "rank_min": 1,
        },
        "priority": 75,
        "chance": 100,
        "label": "aoi_bad_gift_microwave",
    })

label aoi_bad_gift_microwave:
    show aoi at char_center
    $ store.talked_today.add("Аоі")

    ao "Мікрохвильовка."
    $ advance_time(5)

    ao "Ти подарував мені мікрохвильовку."
    $ advance_time(5)

    ao "Знаєш, що я з нею зробила? Розібрала на деталі."
    $ advance_time(5)

    mc "...Що?"
    $ advance_time(5)

    ao "Магнетрон пішов на запчастини. Хоч якась користь."
    $ advance_time(5)

    ao "Але це не знімає того, що ти вирішив: 'О, дівчина — дам їй кухонне'."
    $ advance_time(5)

    mc "Я не думав так, чесно."
    $ advance_time(5)

    ao "Тоді думай наступного разу. Взагалі. Будь ласка."
    $ advance_time(5)

    $ set_flag("gift_aoi_microwave_done")
    $ store.seen_dialogues.add("aoi_bad_gift_microwave")
    $ add_insight("aoi_resourceful", "Аоі розібрала мікрохвильовку на деталі. Практична, але ображена.")

    hide aoi
    return
