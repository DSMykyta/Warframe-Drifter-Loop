# game/script.rpy
# ═══════════════════════════════════════════════════
# ГОЛОВНИЙ ПОТІК ГРИ
# ═══════════════════════════════════════════════════

label start:
    # Відновити інсайти з минулої петлі
    if persistent.insights_log:
        $ store.insights_log = list(persistent.insights_log)
    # Інтро — допит на футкорті
    if not store.flags.get("intro_done"):
        call intro
    # Сцена 2 — дослідження молу, знахідка карти
    if not store.flags.get("has_map"):
        call explore_mall
    # Побудувати першу колоду діалогів
    $ build_daily_deck()
    jump generic_day


# ═══════════════════════════════════════════════════
# УНІВЕРСАЛЬНИЙ ДЕНЬ
# ═══════════════════════════════════════════════════

label generic_day:
    # Титр на чорному тлі
    scene black
    $ _time_str = get_time_display()
    show text "{size=48}[day] грудня / [_time_str]{/size}" at truecenter
    pause 2
    hide text

    # Робочий фон
    scene bg mall
    jump location_loop


# ═══════════════════════════════════════════════════
# LOCATION LOOP — центральний ігровий цикл
# ═══════════════════════════════════════════════════

label location_loop:
    # Показати фон поточної локації
    $ show_location_bg()

    # Показати спрайти NPC в локації
    $ show_location_chars()

    # Показати HUD
    show screen hud

    # Перевірити banter при вході
    $ _banter = get_banter(current_location)
    if _banter is not None:
        $ _banter_who = _banter.get("who", "")
        $ _banter_text = _banter.get("text", "")
        if _banter_text:
            "[_banter_who]: [_banter_text]"

    # Показати екран взаємодії з локацією
    call screen location_ui

    # Обробити вибір
    $ _choice = _return

    if _choice == "map":
        call screen mall_map
        jump location_loop

    if _choice == "missions":
        call missions_ui
        jump location_loop

    if _choice == "sleep":
        $ next_day()
        # Автозбереження
        $ renpy.save("auto-1", "День [store.day]")
        # Перевірка фіналу (день 31)
        if store.day >= 31:
            call check_day31
        jump generic_day

    if _choice == "wait":
        jump do_wait

    if _choice == "shop":
        call screen shop
        jump location_loop

    if _choice == "journal":
        call screen journal
        jump location_loop

    if _choice == "gallery":
        call screen gallery
        jump location_loop

    if _choice == "insights":
        call screen thought_cabinet
        jump location_loop

    if isinstance(_choice, tuple):
        # Клік на персонажа → показати меню взаємодії
        if _choice[0] == "interact":
            $ _interact_target = _choice[1]
            jump interact_with_npc

        # Fallback для старого формату
        if _choice[0] == "talk":
            $ _interact_target = _choice[1]
            jump interact_with_npc

        if _choice[0] == "gift":
            $ _gift_target = _choice[1]
            call gift_submenu(_gift_target)
            jump location_loop

    jump location_loop


# ═══════════════════════════════════════════════════
# ВЗАЄМОДІЯ З NPC — ПІДМЕНЮ
# ═══════════════════════════════════════════════════

label interact_with_npc:
    # Обрати ОДИН eligible діалог (за пріоритетом)
    $ _active_dlg = get_active_dialogue(_interact_target)
    # Зібрати бонусні опції
    $ _bonus = get_bonus_options(_interact_target)
    # Чи є що подарувати
    $ _can_gift = bool(store.inventory) and _interact_target not in store.gifted_today

    # Якщо нема діалогу з titles — fallback на старий get_dialogue
    if _active_dlg is None:
        $ _dlg_label = get_dialogue(_interact_target)
        if _dlg_label:
            $ store.talked_today.add(_interact_target)
            $ reset_interaction(_interact_target)
            $ store.interaction_counts[_interact_target] = store.interaction_counts.get(_interact_target, 0) + 1
            call expression _dlg_label
        jump location_loop

    # Є діалог з titles → показати меню
    $ _titles = _active_dlg["titles"]
    $ _dlg_id = _active_dlg["id"]
    call screen npc_interact_menu(_interact_target, _titles, _bonus, _can_gift)
    $ _interact_choice = _return

    if _interact_choice == "dismiss":
        jump location_loop

    if _interact_choice == "gift":
        call gift_submenu(_interact_target)
        jump location_loop

    # Вибрали гілку діалогу
    if isinstance(_interact_choice, tuple):
        if _interact_choice[0] == "topic":
            $ _topic_label = _interact_choice[1]
            $ store.talked_today.add(_interact_target)
            $ reset_interaction(_interact_target)
            $ store.interaction_counts[_interact_target] = store.interaction_counts.get(_interact_target, 0) + 1
            $ dialogue_begin()
            call expression _topic_label
            $ dialogue_end()
            $ store.seen_dialogues.add(_dlg_id)
            $ set_flag(_dlg_id + "_done")
            jump location_loop

        if _interact_choice[0] == "bonus":
            $ _bonus_label = _interact_choice[1]
            $ store.talked_today.add(_interact_target)
            $ reset_interaction(_interact_target)
            $ _char_img = CHAR_IMAGE_TAG.get(_interact_target, "arthur")
            show expression _char_img at char_center
            $ dialogue_begin()
            call expression _bonus_label
            $ dialogue_end()
            hide expression _char_img
            jump location_loop

    jump location_loop


# ═══════════════════════════════════════════════════
# МЕХАНІКА "ЗАЧЕКАТИ"
# ═══════════════════════════════════════════════════

label do_wait:
    if is_night():
        "Занадто пізно. Краще піти спати."
        jump location_loop

    # Обчислити час до наступної години
    $ _cur_hour_end = ((store.minutes // 60) + 1) * 60
    $ _wait_mins = _cur_hour_end - store.minutes
    if _wait_mins <= 0:
        $ _wait_mins = 60

    # Шанс на переривання (30%)
    $ _interrupted = renpy.random.randint(1, 100) <= 30
    if _interrupted:
        # Перемотати половину часу, потім переривання
        $ advance_time(_wait_mins // 2)
        $ _help = check_help_requests()
        if _help is not None:
            $ _help_who = _help["who"]
            $ _help_msg = _help["message"]
            "Пейджер: [_help_who] — [_help_msg]"
            menu:
                "Допомогти":
                    $ execute_help_request(_help)
                    $ show_location_bg()
                    "Допоміг [_help_who]. Отримано 100 крон."
                "Ігнорувати":
                    "Пропускаєш запит."
            jump location_loop
        # Якщо немає help request — простий banter
        "Поки чекаєш, хтось підходить..."
        jump location_loop

    # Повне очікування
    $ advance_time(_wait_mins)
    $ _time_str = get_time_display()
    "Зачекав до [_time_str]."
    jump location_loop


# ═══════════════════════════════════════════════════
# МІСІЇ
# ═══════════════════════════════════════════════════

label missions_ui:
    call screen missions_menu
    if isinstance(_return, int):
        $ selected_mission = _return
        jump execute_mission
    return

label execute_mission:
    $ m = missions[selected_mission]
    $ dur_mins = max(1, m['level']) * 45  # Баланс v2: було ×60

    # Встановити напарника для condition-based місійних діалогів
    $ store.current_mission_partner = m['partner']

    scene black
    show text "Виконується місія [m['name']]" at truecenter
    pause 1.5
    hide text

    # Місійний міні-діалог (якщо є напарник)
    if m['partner'] is not None:
        $ _mission_dlg = get_mission_dialogue(m['partner'])
        if _mission_dlg:
            call expression _mission_dlg

    $ store.minutes += dur_mins
    $ store.hour = store.minutes // 60

    # Травми (тільки якщо є напарник)
    $ _mission_aborted = False
    if m['partner'] is not None:
        # Лічильник повторних місій з напарником
        $ store.missions_today_with[m['partner']] = store.missions_today_with.get(m['partner'], 0) + 1

        # Перевірка травм
        $ _injury_result = roll_mission_injury(m['level'], m['partner'])
        if _injury_result is not None:
            $ _inj_messages, _mission_aborted = apply_mission_injuries(_injury_result, m['partner'])
            python:
                for _msg in _inj_messages:
                    renpy.say(None, _msg)

    if _mission_aborted:
        # Евакуація: час коротший (50%), нагород нема, +хімія за допомогу
        $ store.minutes -= dur_mins // 2
        $ store.hour = store.minutes // 60
        $ add_chemistry(m['partner'], 5)
        $ on_mission_complete()
        if m['partner'] is not None:
            $ reset_interaction(m['partner'])
        $ generate_missions()
        $ store.current_mission_partner = None
        "Місію перервано. Евакуація напарника."
        return

    # Нагороди
    $ money += m['reward']
    $ hex_rep += m['rep']
    $ try_rank_up()

    # Хімія напарника (раз на день на персонажа, +6, gate: розмова за 3 дні)
    if m['partner'] is not None and m['partner'] not in mission_chem_today:
        if can_get_mission_chem(m['partner']):
            $ add_chemistry(m['partner'], 6)
        $ mission_chem_today.add(m['partner'])

    # Скинути лічильник neglect
    $ on_mission_complete()

    # Скинути decay для напарника
    if m['partner'] is not None:
        $ reset_interaction(m['partner'])

    # Перегенерувати місії
    $ generate_missions()

    # Скинути напарника
    $ store.current_mission_partner = None

    "Місія виконана. Отримано [m['reward']] крон. Репутація +[m['rep']]."
    return
