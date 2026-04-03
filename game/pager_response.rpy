# game/pager_response.rpy
# ═══════════════════════════════════════════════════
# ПЕЙДЖЕР — ОБРОБКА ВІДПОВІДЕЙ + ПАТЧ dialogue_begin
# ═══════════════════════════════════════════════════

default pager_response = None
default _pager_pending_label = None
default _pager_pending_who = None

init -3 python:

    def _pager_accept():
        """Кнопка ТАК."""
        pager_click()
        store.pager_response = "accept"
        store._pager_pending_label = store.pager_request_accept
        store._pager_pending_who = store.pager_request_who
        store.pager_mode = "status"
        store.pager_unread = False

    def _pager_decline():
        """Кнопка НІ."""
        pager_click()
        store.pager_response = "decline"
        store._pager_pending_label = store.pager_request_decline
        store._pager_pending_who = store.pager_request_who
        store.pager_mode = "status"
        store.pager_unread = False

    def has_pending_pager():
        return store.pager_response is not None

    def consume_pager_response():
        resp = store.pager_response
        label = store._pager_pending_label
        who = store._pager_pending_who
        store.pager_response = None
        store._pager_pending_label = None
        store._pager_pending_who = None
        return resp, label, who

    # ═══ Допоміжні: ховати/показувати пейджер для fullscreen ═══

    def hide_pager():
        renpy.hide_screen("pager_hud")

    def show_pager():
        if store.flags.get("has_pager"):
            renpy.show_screen("pager_hud")
