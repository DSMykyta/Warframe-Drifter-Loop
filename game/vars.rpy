# game/vars.rpy
# ═══════════════════════════════════════════════════
# ГЛОБАЛЬНІ ЗМІННІ — Warframe: Drifter Loop
# ═══════════════════════════════════════════════════

# -------------- час і день --------------
default day = 1              # 1 грудня
default minutes = 480        # 08:00 (в хвилинах від 00:00)
default hour = 8             # derived, для HUD сумісності

# -------------- ресурси --------------
default money = 0            # крони
default hex_rep = 0          # репутація Гексу

# -------------- прогресія --------------
default syndicate_rank = 1   # ранг Гексу (1-6)

# -------------- щоденні скиди --------------
default talked_today = set()
default gifted_today = set()
default mission_chem_today = set()      # замість mission_rel_done
default tags_used_today = {}            # {"Артур": {"heavy_lore"}, ...}

# -------------- хімія (дружба) --------------
default chemistry = {
    "Артур":   0,
    "Елеонор": 0,
    "Летті":   0,
    "Амір":    0,
    "Аоі":     0,
    "Квінсі":  0,
}

# -------------- стосунки & романс --------------
default dating = None        # None або ім'я (ексклюзивний романс)

# -------------- локація --------------
default current_location = "mall"
default current_mission_partner = None

# -------------- діалогова система --------------
default seen_dialogues = set()          # {"arthur_middle_name", ...}
default stub_pools = {}                 # {"Артур": ["topic1", ...]}
default daily_deck = {}                 # {"Артур": [entry1, ...]}

# -------------- флаги --------------
default flags = {}                      # динамічно заповнюється через set_flag()

# -------------- інвентар --------------
default inventory = {}                  # {"item_id": кількість}

# -------------- обіцянки --------------
default promises = []                   # [{who, where, from_min, to_min, day, label}, ...]

# -------------- місії --------------
default days_without_mission = 0

# -------------- розпад стосунків --------------
default days_since_interaction = {
    "Артур":   0,
    "Елеонор": 0,
    "Летті":   0,
    "Амір":    0,
    "Аоі":     0,
    "Квінсі":  0,
}
default decay_paused_until = 0          # день до якого decay на паузі

# -------------- плітки --------------
default gossip_heat = 0                 # при >= 10 тригерить awareness
default active_gossip = []              # [{fact, knowers, day_created, spread_delay}, ...]

# -------------- протухлі івенти --------------
default expired_events = set()          # {"arthur_eleanor_rooftop_fight", ...}

# -------------- шафа думок --------------
default insights_log = []               # [{id, text, day, type}, ...]
default raw_thoughts = []               # [{id, text, requires}, ...]

# -------------- пейджер --------------
default pager_messages = []            # ["Квінсі шукав тебе", ...]
default pager_mode = "status"          # "status", "message", "request"
default pager_msg_index = 0
default pager_unread = False
default pager_request_text = ""
default pager_request_accept = None    # label або None
default pager_request_decline = None

# -------------- щоденник --------------
default journal_entries = []            # [{day, text, type}, ...]

# -------------- патерни взаємодії --------------
default interaction_counts = {
    "Артур":   0,
    "Елеонор": 0,
    "Летті":   0,
    "Амір":    0,
    "Аоі":     0,
    "Квінсі":  0,
}

# -------------- persistent (між петлями) --------------
default persistent.cg_unlocked = set()
default persistent.loop_count = 0
default persistent.completed = False
default persistent.all_friends = False
default persistent.insights_log = []
default persistent.previous_journal = []

# -------------- місійний трекер --------------
default missions_today_with = {}     # {"Артур": 2, ...} — місій з ким сьогодні

# -------------- діалоговий лічильник реплік --------------
default dialogue_line_count = 0        # скільки реплік сказано в поточному діалозі

# -------------- daily chemistry cap трекер --------------
default chemistry_gained_today = {
    "Артур":   0,
    "Елеонор": 0,
    "Летті":   0,
    "Амір":    0,
    "Аоі":     0,
    "Квінсі":  0,
}


# ═══════════════════════════════════════════════════
# СЛУЖБОВІ ФУНКЦІЇ — ЧАС
# ═══════════════════════════════════════════════════

init -3 python:

    def advance_time(mins):
        """Просуває час на mins хвилин. Оновлює hour."""
        store.minutes += mins
        store.hour = store.minutes // 60

    # ═══ ДІАЛОГОВА ОБГОРТКА ═══

    DIALOGUE_TIME_PER_LINE = 3  # хвилин за репліку

    def dialogue_begin():
        """Викликати на початку кожного діалогу.
        Ховає HUD/пейджер, скидає лічильник реплік."""
        store.dialogue_line_count = 0
        renpy.hide_screen("hud")
        renpy.hide_screen("pager_hud")
        renpy.hide_screen("pager")

    def dialogue_end():
        """Викликати в кінці кожного діалогу.
        Списує час (count × 3 хв), повертає HUD."""
        mins = store.dialogue_line_count * DIALOGUE_TIME_PER_LINE
        if mins > 0:
            advance_time(mins)
        store.dialogue_line_count = 0
        renpy.show_screen("hud")
        renpy.show_screen("pager_hud")

    def _count_dialogue_line(event, interact=True, **kwargs):
        """Глобальний callback: рахує кожну репліку."""
        if interact and event == "begin":
            store.dialogue_line_count += 1

    config.all_character_callbacks.append(_count_dialogue_line)

    def is_night():
        """Після 24:00 (1440 хв) — ніч, персонажі зникли."""
        return store.minutes >= 1440

    def get_time_display():
        """Форматує хвилини в 'ГГ:ХХ' для HUD."""
        h = store.minutes // 60
        m = store.minutes % 60
        return "{:02d}:{:02d}".format(h, m)

    def get_chem_rank(name):
        """Повертає текстовий рівень хімії з персонажем."""
        pts = store.chemistry.get(name, 0)
        if pts >= 160: return "Кохання"
        if pts >= 120: return "Друзі"
        if pts >= 90:  return "Близько"
        if pts >= 60:  return "Довіра"
        if pts >= 35:  return "Подобається"
        if pts >= 15:  return "Привітно"
        return "Нейтрально"

    # ═══ БАЛАНС: КОНСТАНТИ ═══
    RANK_THRESHOLDS = {2: 30, 3: 80, 4: 150, 5: 230, 6: 300}

    # Daily cap хімії per NPC
    DAILY_CHEMISTRY_CAP = 15

    # Mission chem gate: потрібна розмова за останні N днів
    MISSION_CHEM_TALK_GATE = 3

    # Канонічний маппінг: кирилиця → латинський ID для флагів
    # ВСІ автогенеровані флаги МАЮТЬ використовувати цей маппінг
    CHAR_FLAG_ID = {
        "Артур":   "arthur",
        "Елеонор": "eleanor",
        "Летті":   "lettie",
        "Амір":    "amir",
        "Аоі":     "aoi",
        "Квінсі":  "quincy",
    }

    def char_flag(name):
        """Повертає латинський ID для флагів. ЗАВЖДИ використовувати замість name.lower()."""
        return CHAR_FLAG_ID.get(name, name.lower())

    def can_rank_up():
        """Перевіряє чи можна підвищити ранг Гексу."""
        nxt = store.syndicate_rank + 1
        return nxt <= 6 and store.hex_rep >= RANK_THRESHOLDS.get(nxt, 99999)

    def add_chemistry(name, amount):
        """Додає хімію з daily cap. Єдина функція для зміни хімії.
        Репутація НЕ залежить від хімії — тільки від місій."""
        if amount <= 0:
            store.chemistry[name] = max(0, store.chemistry.get(name, 0) + amount)
            return amount

        old = store.chemistry.get(name, 0)
        gained_today = store.chemistry_gained_today.get(name, 0)
        remaining_cap = max(0, DAILY_CHEMISTRY_CAP - gained_today)
        actual = min(amount, remaining_cap)
        if actual <= 0:
            return 0

        store.chemistry[name] = old + actual
        store.chemistry_gained_today[name] = gained_today + actual

        return actual

    def can_get_mission_chem(name):
        """Перевіряє чи NPC може отримати mission chemistry (gate: розмова за 3 дні)."""
        return store.days_since_interaction.get(name, 0) <= MISSION_CHEM_TALK_GATE

    def try_rank_up():
        """Підвищує ранг якщо можливо. Повертає True якщо підвищив."""
        if can_rank_up():
            store.syndicate_rank += 1
            set_flag("rank_" + str(store.syndicate_rank))
            add_journal_entry("Ранг Гексу підвищено до {}.".format(store.syndicate_rank), "event")
            build_daily_deck()  # Нові діалоги можуть стати доступними
            return True
        return False


# ═══════════════════════════════════════════════════
# ПЕРСОНАЖІ — hex-vn кольори
# ═══════════════════════════════════════════════════

define ar = Character("Артур",   namebox_style="namebox_arthur",   what_style="say_window", who_color="#a0c4ff", image="arthur",  callback=speaker_callback("arthur"))
define el = Character("Елеонор", namebox_style="namebox_eleanor",  what_style="say_window", who_color="#d8b4fe", image="eleanor", callback=speaker_callback("eleanor"))
define le = Character("Летті",   namebox_style="namebox_lettie",   what_style="say_window", who_color="#a5f3fc", image="lettie",  callback=speaker_callback("lettie"))
define am = Character("Амір",    namebox_style="namebox_amir",     what_style="say_window", who_color="#fef08a", image="amir",    callback=speaker_callback("amir"))
define ao = Character("Аоі",     namebox_style="namebox_aoi",      what_style="say_window", who_color="#f0abfc", image="aoi",     callback=speaker_callback("aoi"))
define qu = Character("Квінсі",  namebox_style="namebox_quincy",   what_style="say_window", who_color="#fca5a5", image="quince",  callback=speaker_callback("quince"))
define mc = Character("Дрифтер", namebox_style="namebox_mc",       what_style="say_window", who_color="#facc15")


# ═══════════════════════════════════════════════════
# СТИЛІ NAMEBOX
# ═══════════════════════════════════════════════════

style namebox_npc:
    background "#0d0d1a99"
    padding (16, 8, 16, 8)

style namebox_arthur is namebox_npc:
    background "#1a2a5acc"

style namebox_eleanor is namebox_npc:
    background "#3a1a5acc"

style namebox_lettie is namebox_npc:
    background "#0a3a4acc"

style namebox_amir is namebox_npc:
    background "#4a3f0acc"

style namebox_aoi is namebox_npc:
    background "#4a1260cc"

style namebox_quincy is namebox_npc:
    background "#5a1a1acc"

style namebox_mc is namebox_npc:
    background "#a855f733"

style say_window:
    background "#09090fdd"
    xmaximum 600
    padding (18, 10, 18, 10)
