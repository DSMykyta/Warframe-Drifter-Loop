import test from "node:test";
import assert from "node:assert/strict";
import { newGame, orderedEvents, inspectEvent, choose, moveTo, serialize, deserialize, nextDay } from "./engine.mjs";
import { events } from "./events.mjs";

const byId = (state, id) => inspectEvent(state, events.find(e => e.id === id)).available;

test("початково доступна лише місія", () => {
  const state = newGame();
  assert.deepEqual(orderedEvents(state, events).filter(x => x.available).map(x => x.event.id),
    ["mission_return"]);
});

test("умовний ланцюжок: поранення → пейджер/лікування → кав'ярня", () => {
  let state = newGame();
  state = choose(state, events, "mission_return", "injured");
  assert.equal(byId(state, "mission_return"), false);
  assert.equal(byId(state, "pager_request"), true);
  assert.equal(byId(state, "treat_arthur"), false);
  state = moveTo(state, "medbay");
  assert.equal(byId(state, "treat_arthur"), true);
  state = choose(state, events, "treat_arthur", "help");
  assert.equal(state.relationships.lettie, 5);
  assert.equal(state.flags.arthur_injured, false);
  assert.equal(state.flags.arthur_treated, true);
  state = choose(state, events, "pager_request", "read");
  state = moveTo(state, "cafe");
  assert.equal(byId(state, "cafe_followup"), true);
  state = choose(state, events, "cafe_followup", "talk");
  assert.equal(byId(state, "lettie_new_topic"), true);
  assert.equal(state.relationships.lettie, 7);
});

test("безпечна місія не запускає лікування", () => {
  let state = choose(newGame(), events, "mission_return", "safe");
  state = moveTo(state, "medbay");
  assert.equal(byId(state, "treat_arthur"), false);
});

test("недоступну одноразову подію не можна повторити", () => {
  const state = choose(newGame(), events, "mission_return", "safe");
  assert.throws(() => choose(state, events, "mission_return", "injured"), /недоступна/i);
  assert.equal(state.flags.arthur_injured, false);
});

test("збереження і завантаження повертають повний стан", () => {
  let state = choose(newGame(), events, "mission_return", "injured");
  state = nextDay(moveTo(state, "medbay"));
  state = choose(state, events, "treat_arthur", "help");
  const restored = deserialize(serialize(state));
  assert.deepEqual(restored, state);
  assert.equal(byId(restored, "treat_arthur"), false);
  assert.equal(byId(restored, "pager_request"), true);
  assert.equal(restored.day, 2);
});

test("неправильне або чуже збереження відхиляється", () => {
  assert.throws(() => deserialize("не JSON"));
  assert.throws(() => deserialize(JSON.stringify({ schema: "other", version: 1, state: newGame() })), /версія/i);
});

test("невідомий ефект не змінює оригінальний стан", () => {
  const state = newGame();
  const broken = [{ id: "test", once: true, choices: [{ id: "x", effects: [
    { op: "set_flag", key: "partial", value: true },
    { op: "unknown" }
  ] }] }];
  assert.throws(() => choose(state, broken, "test", "x"), /Невідомий ефект/);
  assert.deepEqual(state, newGame());
});

test("застосовується пріоритет подій", () => {
  const catalogue = [
    { id: "low", priority: 5 },
    { id: "high", priority: 50 }
  ];
  assert.deepEqual(orderedEvents(newGame(), catalogue).map(x => x.event.id), ["high", "low"]);
});
