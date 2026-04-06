// ═══════════════════════════════════════════════════
// КАВОВИЙ АВТОМАТ — КАВ'ЯРНЯ
// ═══════════════════════════════════════════════════
//
// Порт з coffee.rpy
//
// Два меню: базове (завжди доступне) і молочне (відкривається квестом).
// Кожен NPC має улюблений напій — +4 хімії замість +2.

// Базове меню (завжди доступне)
var COFFEE_MENU_BASE = [
  {id: "coffee_black",    name: "\u0427\u043e\u0440\u043d\u0430 \u043a\u0430\u0432\u0430",       price: 5,  desc: "\u0413\u0430\u0440\u044f\u0447\u0430. \u0413\u0456\u0440\u043a\u0430. \u0427\u0435\u0441\u043d\u0430."},
  // Чорна кава / Гаряча. Гірка. Чесна.
  {id: "coffee_espresso",  name: "\u041f\u043e\u0434\u0432\u0456\u0439\u043d\u0438\u0439 \u0435\u0441\u043f\u0440\u0435\u0441\u043e",  price: 25, desc: "\u0423\u0434\u0430\u0440. \u0414\u043b\u044f \u0442\u0438\u0445 \u0445\u0442\u043e \u043d\u0435 \u0441\u043f\u0430\u0432."}
  // Подвійний еспресо / Удар. Для тих хто не спав.
];

// Молочне меню (потрібен квест)
var COFFEE_MENU_MILK = [
  {id: "coffee_latte",      name: "\u041b\u0430\u0442\u0435",       price: 15, desc: "\u041c\u2019\u044f\u043a\u0430, \u0437 \u043c\u043e\u043b\u043e\u043a\u043e\u043c.", requires_milk: true},
  // Лате / М'яка, з молоком.
  {id: "coffee_cocoa",      name: "\u041a\u0430\u043a\u0430\u043e",      price: 15, desc: "\u0421\u043e\u043b\u043e\u0434\u043a\u0435, \u0433\u0443\u0441\u0442\u0435, \u0442\u0435\u043f\u043b\u0435.", requires_milk: true},
  // Какао / Солодке, густе, тепле.
  {id: "coffee_cappuccino", name: "\u041a\u0430\u043f\u0443\u0447\u0456\u043d\u043e", price: 20, desc: "\u041f\u0456\u043d\u0430, \u043c\u043e\u043b\u043e\u043a\u043e, \u043a\u0430\u0432\u0430. \u041a\u043b\u0430\u0441\u0438\u043a\u0430.", requires_fresh: true}
  // Капучіно / Піна, молоко, кава. Класика.
];


// Хто що любить
var COFFEE_PREFERENCES = {
  "\u0410\u0440\u0442\u0443\u0440":   "coffee_espresso",   // Артур
  "\u041b\u0435\u0442\u0442\u0456":   "coffee_latte",      // Летті
  "\u0410\u043e\u0456":     "coffee_cocoa",      // Аоі
  "\u0410\u043c\u0456\u0440":    "coffee_espresso",   // Амір
  "\u041a\u0432\u0456\u043d\u0441\u0456":  "coffee_black",      // Квінсі
  "\u0415\u043b\u0435\u043e\u043d\u043e\u0440": "coffee_latte"       // Елеонор
};


// Стан кави зберігається в inventory.items (кава = предмет інвентарю)
// Окремий стейт не потрібен, але реєструємо для сумісності
registerState("coffee", {});


// Повертає список доступних напоїв з урахуванням молока
function getAvailableCoffees() {
  var result = COFFEE_MENU_BASE.slice();
  if (getFlag("milk_drinks_unlocked")) {
    for (var i = 0; i < COFFEE_MENU_MILK.length; i++) {
      var c = COFFEE_MENU_MILK[i];
      if (c.requires_fresh && !getFlag("milk_cappuccino_unlocked")) continue;
      result.push(c);
    }
  }
  return result;
}


// Чи є хоча б одна кава в інвентарі
function hasAnyCoffee() {
  var coffees = getAvailableCoffees();
  for (var i = 0; i < coffees.length; i++) {
    if ((gameState.inventory.items[coffees[i].id] || 0) > 0) return true;
  }
  return false;
}


// Список кав в інвентарі
function getCoffeeList() {
  var result = [];
  var coffees = getAvailableCoffees();
  for (var i = 0; i < coffees.length; i++) {
    var qty = gameState.inventory.items[coffees[i].id] || 0;
    if (qty > 0) {
      result.push({id: coffees[i].id, name: coffees[i].name, qty: qty});
    }
  }
  return result;
}


// Купити каву. Повертає true якщо успішно.
function buyCoffee(coffeeId) {
  var coffees = getAvailableCoffees();
  for (var i = 0; i < coffees.length; i++) {
    if (coffees[i].id === coffeeId) {
      if (gameState.money.amount >= coffees[i].price) {
        gameState.money.amount -= coffees[i].price;
        gameState.inventory.items[coffeeId] = (gameState.inventory.items[coffeeId] || 0) + 1;
        return true;
      }
      return false;
    }
  }
  return false;
}


// Випити каву. Повертає id або null.
function drinkCoffee(coffeeId) {
  if ((gameState.inventory.items[coffeeId] || 0) <= 0) return null;
  gameState.inventory.items[coffeeId]--;
  if (gameState.inventory.items[coffeeId] <= 0) {
    delete gameState.inventory.items[coffeeId];
  }
  return coffeeId;
}


// Дати каву NPC. Повертає бонус хімії (4 якщо улюблений, 2 інакше).
function giveCoffeeTo(name, coffeeId) {
  if ((gameState.inventory.items[coffeeId] || 0) <= 0) return 0;

  // Забрати з інвентарю
  gameState.inventory.items[coffeeId]--;
  if (gameState.inventory.items[coffeeId] <= 0) {
    delete gameState.inventory.items[coffeeId];
  }

  // Позначити що давав каву сьогодні
  setFlag("coffee_given_" + charFlag(name) + "_today");

  // Улюблений = +4, інакше +2
  var preferred = COFFEE_PREFERENCES[name];
  if (coffeeId === preferred) return 4;
  return 2;
}


// Чи можна дати каву NPC (є кава + ще не давав сьогодні)
function canGiveCoffeeTo(name) {
  if (!hasAnyCoffee()) return false;
  var flag = "coffee_given_" + charFlag(name) + "_today";
  return !getFlag(flag);
}
