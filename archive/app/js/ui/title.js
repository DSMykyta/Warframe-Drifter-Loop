// ═══════════════════════════════════════════════════
// ЛОГІКА ЗАГОЛОВКІВ
// ═══════════════════════════════════════════════════
//
// Заголовок на кожному екрані: <DRIFTER_LOOP/>
// При переході на інший екран — слово друкується між / і >
//   Наприклад: <DRIFTER_LOOP/ЗАВАНТАЖИТИ>
// При виході — стирається по буквах назад до <DRIFTER_LOOP/>
//
// Використання в HTML:
//   <h1 data-word="ЗАВАНТАЖИТИ"><DRIFTER_LOOP/></h1>
//
// Якщо data-word нема — заголовок не змінюється.

var _titleTimer = null;
var TITLE_BASE = "<DRIFTER_LOOP/>";

// Друкувати слово між / і >
function titleTypeIn(element, callback) {
  var word = element.getAttribute("data-word");
  if (!word) {
    if (callback) callback();
    return;
  }

  element.textContent = TITLE_BASE;
  var i = 0;

  clearInterval(_titleTimer);
  _titleTimer = setInterval(function() {
    i++;
    if (i >= word.length) {
      element.textContent = "<DRIFTER_LOOP/" + word + ">";
      clearInterval(_titleTimer);
      if (callback) callback();
    } else {
      element.textContent = "<DRIFTER_LOOP/" + word.slice(0, i) + ">";
    }
  }, 40);
}

// Стерти слово по буквах
function titleTypeOut(element, callback) {
  var word = element.getAttribute("data-word");
  if (!word) {
    if (callback) callback();
    return;
  }

  var current = word.length;

  clearInterval(_titleTimer);
  _titleTimer = setInterval(function() {
    current--;
    if (current <= 0) {
      element.textContent = TITLE_BASE;
      clearInterval(_titleTimer);
      if (callback) callback();
    } else {
      element.textContent = "<DRIFTER_LOOP/" + word.slice(0, current) + ">";
    }
  }, 30);
}
