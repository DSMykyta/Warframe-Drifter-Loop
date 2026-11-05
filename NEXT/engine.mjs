// Drifter Loop NEXT: чисте ядро умовно-подієвого рушія, без браузерних залежностей.
export const SAVE_VERSION = 1;
export const SAVE_KEY = "drifter-next-save-v1";

const clone = x => JSON.parse(JSON.stringify(x));
const own = (object, key) => Object.prototype.hasOwnProperty.call(object, key);

export function newGame() {
  return {
    version: SAVE_VERSION,
    day: 1,
    location: "garage",
    flags: {},
    relationships: { lettie: 0, arthur: 0 },
    seen: [],
    log: []
  };
}

function parts(path) {
  if (typeof path !== "string" || !path ||
      path.split(".").some(k => !k || ["__proto__", "prototype", "constructor"].includes(k))) {
    throw new Error("Некоректний шлях: " + path);
  }
  return path.split(".");
}

export function getValue(state, path) {
  let current = state;
  for (const part of parts(path)) {
    if (current === null || typeof current !== "object" || !own(current, part)) return undefined;
    current = current[part];
  }
  return current;
}

function setValue(state, path, value) {
  const segments = parts(path);
  const key = segments.pop();
  let object = state;
  for (const part of segments) {
    if (!object || typeof object !== "object" || !own(object, part)) {
      throw new Error("Невідомий шлях стану: " + path);
    }
    object = object[part];
  }
  if (!object || !own(object, key)) throw new Error("Невідомий ключ стану: " + path);
  object[key] = value;
}

export function unmet(state, when) {
  if (!when) return [];
  if (own(when, "all")) {
    if (!Array.isArray(when.all)) throw new Error("all має бути масивом");
    return when.all.flatMap(rule => unmet(state, rule));
  }
  if (own(when, "any")) {
    if (!Array.isArray(when.any)) throw new Error("any має бути масивом");
    if (when.any.some(rule => unmet(state, rule).length === 0)) return [];
    return ["Не виконана жодна з альтернатив (any)"];
  }
  if (own(when, "not")) {
    return unmet(state, when.not).length ? [] : ["Заперечення (not) не виконано"];
  }
  let actual;
  let passed = false;
  switch (when.op) {
    case "flag":
      if (typeof when.key !== "string" || !when.key ||
          ["__proto__", "prototype", "constructor"].includes(when.key)) {
        throw new Error("Некоректний прапорець");
      }
      actual = own(state.flags, when.key) ? state.flags[when.key] : false;
      passed = actual === when.value;
      break;
    case "eq":
      actual = getValue(state, when.path);
      passed = actual === when.value;
      break;
    case "ne":
      actual = getValue(state, when.path);
      passed = actual !== when.value;
      break;
    case "gte":
      actual = getValue(state, when.path);
      passed = typeof actual === "number" && actual >= when.value;
      break;
    case "lt":
      actual = getValue(state, when.path);
      passed = typeof actual === "number" && actual < when.value;
      break;
    default:
      throw new Error("Невідома умова: " + JSON.stringify(when));
  }
  if (passed) return [];
  const subject = when.op === "flag" ? "flags." + when.key : when.path;
  return [subject + " [" + when.op + "] очікується " +
    JSON.stringify(when.value) + ", зараз " + JSON.stringify(actual)];
}

export function inspectEvent(state, event) {
  const reasons = [];
  if (event.once && state.seen.includes(event.id)) reasons.push("Одноразову подію вже пройдено");
  reasons.push(...unmet(state, event.when));
  return { available: reasons.length === 0, reasons };
}

export function orderedEvents(state, events) {
  return events.map(event => ({ event, ...inspectEvent(state, event) }))
    .sort((a, b) => (b.event.priority || 0) - (a.event.priority || 0) ||
      a.event.id.localeCompare(b.event.id));
}

function applyEffect(state, effect) {
  switch (effect.op) {
    case "set_flag":
      if (typeof effect.key !== "string" || !effect.key ||
        ["__proto__", "prototype", "constructor"].includes(effect.key) ||
        typeof effect.value !== "boolean") throw new Error("Некоректна зміна прапорця");
      state.flags[effect.key] = effect.value;
      break;
    case "inc": {
      const before = getValue(state, effect.path);
      if (typeof before !== "number" || typeof effect.by !== "number" ||
          !Number.isFinite(before + effect.by)) throw new Error("Некоректна зміна числа");
      setValue(state, effect.path, before + effect.by);
      break;
    }
    case "set_location":
      if (typeof effect.value !== "string" || !effect.value) throw new Error("Некоректна локація");
      state.location = effect.value;
      break;
    default:
      throw new Error("Невідомий ефект: " + effect.op);
  }
}

export function choose(state, events, eventId, choiceId) {
  const event = events.find(e => e.id === eventId);
  if (!event) throw new Error("Невідома подія: " + eventId);
  const verdict = inspectEvent(state, event);
  if (!verdict.available) throw new Error("Подія недоступна: " + verdict.reasons.join("; "));
  const choice = (event.choices || []).find(c => c.id === choiceId);
  if (!choice) throw new Error("Невідомий вибір: " + choiceId);
  const reasons = unmet(state, choice.when);
  if (reasons.length) throw new Error("Вибір недоступний: " + reasons.join("; "));
  // Транзакція: якщо хоча б один ефект помилковий, оригінальний стан не змінюється.
  const next = clone(state);
  for (const effect of choice.effects || []) applyEffect(next, effect);
  next.seen.push(event.id);
  next.log.unshift("День " + next.day + ": " + event.title + " — " + choice.label);
  next.log = next.log.slice(0, 100);
  return next;
}

export function moveTo(state, location) {
  if (!["garage", "medbay", "cafe"].includes(location)) throw new Error("Невідома локація");
  return { ...clone(state), location };
}

export function nextDay(state) {
  const next = clone(state);
  next.day += 1;
  return next;
}

export function serialize(state) {
  validateState(state);
  return JSON.stringify({ schema: "drifter-next", version: SAVE_VERSION, state });
}

export function validateState(state) {
  if (!state || typeof state !== "object" || Array.isArray(state) ||
      state.version !== SAVE_VERSION ||
      !Number.isInteger(state.day) || state.day < 1 ||
      typeof state.location !== "string" ||
      !state.flags || typeof state.flags !== "object" || Array.isArray(state.flags) ||
      !state.relationships || typeof state.relationships !== "object" ||
      typeof state.relationships.lettie !== "number" ||
      typeof state.relationships.arthur !== "number" ||
      !Array.isArray(state.seen) || !state.seen.every(x => typeof x === "string") ||
      !Array.isArray(state.log) || !state.log.every(x => typeof x === "string")) {
    throw new Error("Стан гри не відповідає версії " + SAVE_VERSION);
  }
  return true;
}

export function deserialize(raw) {
  const data = JSON.parse(raw);
  if (!data || data.schema !== "drifter-next" || data.version !== SAVE_VERSION) {
    throw new Error("Невідома версія збереження");
  }
  validateState(data.state);
  return clone(data.state);
}
