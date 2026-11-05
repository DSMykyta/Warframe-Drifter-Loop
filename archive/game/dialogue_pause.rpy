# game/dialogue_pause.rpy
# ═══════════════════════════════════════════════════
# МЕХАНІКА ПАУЗ — зупиняє діалог до дії гравця
# ═══════════════════════════════════════════════════
#
# Використання:
#
#   # Зачекати натиск кнопки пейджера:
#   $ start_action_wait()
#   call screen wait_for_action
#   $ _result = store._wait_result   # "left"/"center"/"right"
#   $ end_action_wait()
#
#   # Зачекати будь-яку зовнішню дію (через set_wait_result):
#   $ start_action_wait()
#   call screen wait_for_action
#   $ _result = store._wait_result   # що завгодно
#   $ end_action_wait()
#
# Підтримувані джерела:
#   - Пейджер (кнопки left/center/right)
#   - Будь-що через set_wait_result("значення")

default _action_waiting = False
default _wait_result = None


init -2 python:

    # ═══ КЕРУВАННЯ ═══

    def start_action_wait():
        """Починає очікування дії."""
        store._action_waiting = True
        store._wait_result = None

    def end_action_wait():
        """Завершує очікування."""
        store._action_waiting = False
        store._wait_result = None

    def set_wait_result(value):
        """Встановлює результат з будь-якого джерела."""
        if store._action_waiting:
            store._wait_result = value

    def is_waiting_for_action():
        """Чи зараз чекаємо на дію."""
        return store._action_waiting

    # ═══ ПАТЧ ПЕЙДЖЕРА ═══
    # Якщо діалог чекає — кнопки пейджера записують результат
    # замість нормальної роботи.

    _base_pager_prev = pager_prev_msg
    _base_pager_next = pager_next_msg
    _base_pager_dismiss = pager_dismiss
    _base_pager_accept = _pager_accept
    _base_pager_decline = _pager_decline

    def pager_prev_msg():
        if store._action_waiting:
            pager_click()
            store._wait_result = "left"
            return
        _base_pager_prev()

    def pager_next_msg():
        if store._action_waiting:
            pager_click()
            store._wait_result = "right"
            return
        _base_pager_next()

    def pager_dismiss():
        if store._action_waiting:
            pager_click()
            store._wait_result = "center"
            return
        _base_pager_dismiss()

    def _pager_accept():
        if store._action_waiting:
            pager_click()
            store._wait_result = "left"
            return
        _base_pager_accept()

    def _pager_decline():
        if store._action_waiting:
            pager_click()
            store._wait_result = "right"
            return
        _base_pager_decline()


# ═══ ЕКРАН ОЧІКУВАННЯ ═══
# Прозорий. Блокує діалог. Тільки пейджер (zorder 90) працює.
# Timer перевіряє результат кожні 0.1 сек.

screen wait_for_action():
    timer 0.1 repeat True action If(
        store._wait_result is not None,
        true=Return(store._wait_result),
        false=NullAction()
    )
