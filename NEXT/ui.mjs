import { newGame, orderedEvents, unmet, choose, moveTo, nextDay, serialize, deserialize, SAVE_KEY } from "./engine.mjs";
import { events } from "./events.mjs";

const el = id => document.getElementById(id);
let state = newGame();

function status(message) { el("status").textContent = message; }
function saveState() {
  try {
    localStorage.setItem(SAVE_KEY, serialize(state));
    return true;
  } catch (error) {
    status("Збереження не вдалося: " + error.message);
    return false;
  }
}
function loadState() {
  try {
    const raw = localStorage.getItem(SAVE_KEY);
    if (!raw) { status("Збереження ще немає"); return false; }
    state = deserialize(raw);
    render();
    status("Збереження відновлено");
    return true;
  } catch (error) {
    status("Завантаження не вдалося: " + error.message);
    return false;
  }
}
function make(tag, text, className) {
  const node = document.createElement(tag);
  node.textContent = text;
  if (className) node.className = className;
  return node;
}
function renderEvent(entry, locked) {
  const card = make("article", "", "event" + (locked ? " locked" : ""));
  card.append(make("div", "Пріоритет " + (entry.event.priority || 0), "flag"));
  card.append(make("h3", entry.event.title));
  card.append(make("p", entry.event.description || "", "small"));
  if (locked) {
    for (const reason of entry.reasons) card.append(make("div", reason, "reason"));
  } else {
    const choices = make("div", "", "choices");
    for (const option of entry.event.choices || []) {
      const reasons = unmet(state, option.when);
      const button = make("button", option.label, reasons.length ? "" : "primary");
      button.disabled = Boolean(reasons.length);
      button.title = reasons.join("; ");
      button.addEventListener("click", () => {
        try {
          state = choose(state, events, entry.event.id, option.id);
          const saved = saveState();
          render();
          if (saved) status("Дію виконано, стан автоматично збережено");
        } catch (error) { status(error.message); }
      });
      choices.append(button);
    }
    card.append(choices);
  }
  return card;
}
function render() {
  el("location").value = state.location;
  const entries = orderedEvents(state, events);
  el("available").replaceChildren();
  el("blocked").replaceChildren();
  const available = entries.filter(entry => entry.available);
  const blocked = entries.filter(entry => !entry.available);
  if (!available.length) el("available").append(make("div", "Поки немає доступних подій", "muted"));
  for (const entry of available) el("available").append(renderEvent(entry, false));
  for (const entry of blocked) el("blocked").append(renderEvent(entry, true));
  el("state").textContent = JSON.stringify({
    day: state.day, location: state.location, flags: state.flags,
    relationships: state.relationships, seen: state.seen
  }, null, 2);
  el("log").replaceChildren();
  if (!state.log.length) el("log").append(make("p", "Поки нічого не відбулося"));
  for (const line of state.log) el("log").append(make("p", line));
}
el("location").addEventListener("change", event => {
  state = moveTo(state, event.target.value); saveState(); render(); status("Локацію змінено");
});
el("day").addEventListener("click", () => {
  state = nextDay(state); saveState(); render(); status("Новий день");
});
el("save").addEventListener("click", () => { if (saveState()) status("Збережено"); });
el("load").addEventListener("click", loadState);
el("reset").addEventListener("click", () => {
  if (!window.confirm("Почати нову петлю? Поточний стан буде втрачено.")) return;
  state = newGame(); saveState(); render(); status("Нова петля");
});
if (localStorage.getItem(SAVE_KEY)) loadState();
else { render(); status("Нова гра — зроби перший вибір"); }
