// ═══════════════════════════════════════════════════
// ДІАЛОГ ПІДТВЕРДЖЕННЯ
// ═══════════════════════════════════════════════════
//
// confirmDialog("Ви впевнені?", function() { ... })
// Модальне вікно з кнопками ТАК / НІ

var _confirmOverlay = null;

function confirmDialog(message, onConfirm, onCancel) {
  if (_confirmOverlay) _confirmOverlay.remove();

  _confirmOverlay = document.createElement("div");
  _confirmOverlay.id = "confirm-dialog";
  _confirmOverlay.innerHTML =
    '<div class="confirm-box">' +
      '<div class="confirm-message">' + message + '</div>' +
      '<div class="confirm-buttons">' +
        '<button class="btn confirm-yes">ТАК</button>' +
        '<button class="btn confirm-no">НІ</button>' +
      '</div>' +
    '</div>';

  _confirmOverlay.querySelector(".confirm-yes").addEventListener("click", function(e) {
    e.stopPropagation();
    _confirmOverlay.remove();
    _confirmOverlay = null;
    if (onConfirm) onConfirm();
  });

  _confirmOverlay.querySelector(".confirm-no").addEventListener("click", function(e) {
    e.stopPropagation();
    _confirmOverlay.remove();
    _confirmOverlay = null;
    if (onCancel) onCancel();
  });

  // Закрити при Escape
  _confirmOverlay.addEventListener("keydown", function(e) {
    if (e.key === "Escape") {
      _confirmOverlay.remove();
      _confirmOverlay = null;
      if (onCancel) onCancel();
    }
  });

  document.getElementById("viewport").appendChild(_confirmOverlay);
}
