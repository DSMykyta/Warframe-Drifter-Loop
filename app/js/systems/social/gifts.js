// ═══════════════════════════════════════════════════
// СИСТЕМА ПОДАРУНКІВ
// ═══════════════════════════════════════════════════
//
// Порт з gifts.rpy + inventory.rpy (таблиці реакцій)
//
// 1 подарунок на персонажа на день, витрачає 10 хв.
// Улюблений = +12 хімії, liked = +7, small = +3, нейтральний = +1.
// Образливий = штраф хімії + плітки.

// Хто що любить: {item_id: {character: chemistry_bonus}}
// Баланс v2: loved=+12, liked=+7, small=+3
var GIFT_REACTIONS = {
  // Артур — кухня
  "toaster":        {"\u0410\u0440\u0442\u0443\u0440": 12},
  "toaster_oven":   {"\u0410\u0440\u0442\u0443\u0440": 12},
  "microwave":      {"\u0410\u0440\u0442\u0443\u0440": 12},
  "announce":       {"\u0410\u0440\u0442\u0443\u0440": 12},
  "propane_tank":   {"\u0410\u0440\u0442\u0443\u0440": 7},

  // Аоі — музика, транспорт
  "onlyne_album":        {"\u0410\u043e\u0456": 12},
  "wireless_headphones": {"\u0410\u043e\u0456": 12, "\u0410\u043c\u0456\u0440": 12},
  "speaker_system":      {"\u0410\u043e\u0456": 12},
  "scooticle":           {"\u0410\u043e\u0456": 12},
  "gas_can":             {"\u0410\u043e\u0456": 3},
  "roadsigns":           {"\u0410\u043e\u0456": 3},

  // Амір — техніка, ігри
  "hockey_table":  {"\u0410\u043c\u0456\u0440": 12},
  "gpu_256":       {"\u0410\u043c\u0456\u0440": 7},
  "game_system":   {"\u0410\u043c\u0456\u0440": 7},
  "game_monitor":  {"\u0410\u043c\u0456\u0440": 7},
  "tv_840hd":      {"\u0410\u043c\u0456\u0440": 7, "\u041a\u0432\u0456\u043d\u0441\u0456": 3},

  // Квінсі — електроніка, медіа
  "video_camera":  {"\u041a\u0432\u0456\u043d\u0441\u0456": 12},
  "av_receiver":   {"\u041a\u0432\u0456\u043d\u0441\u0456": 7},
  "speaker":       {"\u041a\u0432\u0456\u043d\u0441\u0456": 7},
  "cellphone":     {"\u041a\u0432\u0456\u043d\u0441\u0456": 3},
  "poster":        {"\u041a\u0432\u0456\u043d\u0441\u0456": 3},
  "vhs_series":    {"\u041a\u0432\u0456\u043d\u0441\u0456": 3},

  // Летті — кава, побут
  "coffee_machine": {"\u041b\u0435\u0442\u0442\u0456": 12},
  "medical_kit":    {"\u041b\u0435\u0442\u0442\u0456": 7},
  "coffee_cups":    {"\u041b\u0435\u0442\u0442\u0456": 3},
  "coffee_mug":     {"\u041b\u0435\u0442\u0442\u0456": 3},
  "pillows":        {"\u0415\u043b\u0435\u043e\u043d\u043e\u0440": 3},
  "cardboard_box":  {"\u041b\u0435\u0442\u0442\u0456": 3},

  // Елеонор — природа, канцелярія
  "hanging_planter": {"\u0415\u043b\u0435\u043e\u043d\u043e\u0440": 12},
  "notepad":         {"\u0415\u043b\u0435\u043e\u043d\u043e\u0440": 7},
  "binder":          {"\u0415\u043b\u0435\u043e\u043d\u043e\u0440": 3},
  "pens":            {"\u0415\u043b\u0435\u043e\u043d\u043e\u0440": 3},
  "pencils":         {"\u0415\u043b\u0435\u043e\u043d\u043e\u0440": 3}
};


// Образливі подарунки: {item_id: {character: [penalty, reaction_text]}}
var OFFENSIVE_GIFTS = {
  // Аоі ненавидить кухонне — стереотипи
  "toaster":      {"\u0410\u043e\u0456": [-5, "\u0426\u0435 \u043d\u0430\u0442\u044f\u043a? \u0429\u043e \u044f \u0436\u0456\u043d\u043a\u0430 \u0456 \u043c\u0430\u044e \u043c\u0456\u0441\u0446\u0435 \u043d\u0430 \u043a\u0443\u0445\u043d\u0456?"]},
  // Це натяк? Що я жінка і маю місце на кухні?
  "toaster_oven": {"\u0410\u043e\u0456": [-5, "\u041a\u0443\u0445\u043e\u043d\u043d\u0430 \u0442\u0435\u0445\u043d\u0456\u043a\u0430. \u0414\u043b\u044f \u043c\u0435\u043d\u0435. \u0421\u0435\u0440\u0439\u043e\u0437\u043d\u043e?"]},
  // Кухонна техніка. Для мене. Серйозно?
  "microwave":    {"\u0410\u043e\u0456": [-5, "\u041c\u0456\u043a\u0440\u043e\u0445\u0432\u0438\u043b\u044c\u043e\u0432\u043a\u0430. \u042f\u043a\u0430... \u043e\u0440\u0438\u0433\u0456\u043d\u0430\u043b\u044c\u043d\u0430 \u0456\u0434\u0435\u044f."]},
  // Мікрохвильовка. Яка... оригінальна ідея.

  // Квінсі не терпить натяків на слабкість
  "medical_kit":  {"\u041a\u0432\u0456\u043d\u0441\u0456": [-3, "\u0414\u0443\u043c\u0430\u0454\u0448 \u044f \u043d\u0435 \u0432\u043f\u043e\u0440\u0430\u044e\u0441\u044c \u0441\u0430\u043c? \u0419\u0434\u0438 \u0437\u0432\u0456\u0434\u0441\u0438."]},
  // Думаєш я не впораюсь сам? Йди звідси.

  // Артур — дешеві сувеніри
  "keychains":    {"\u0410\u0440\u0442\u0443\u0440": [-3, "...\u0422\u0438 \u0441\u0435\u0440\u0439\u043e\u0437\u043d\u043e? \u041a\u0440\u0430\u0449\u0435 \u0431 \u043d\u0456\u0447\u043e\u0433\u043e \u043d\u0435 \u043f\u0440\u0438\u043d\u043e\u0441\u0438\u0432."]},
  // ...Ти серйозно? Краще б нічого не приносив.
  "roadsigns":    {"\u0410\u0440\u0442\u0443\u0440": [-3, "\u0414\u043e\u0440\u043e\u0436\u043d\u0456 \u0437\u043d\u0430\u043a\u0438. \u0414\u044f\u043a\u0443\u044e. \u0414\u0443\u0436\u0435... \u043a\u043e\u0440\u0438\u0441\u043d\u043e."]},
  // Дорожні знаки. Дякую. Дуже... корисно.

  // Амір — книги/нудне
  "binder":       {"\u0410\u043c\u0456\u0440": [-2, "\u041e... \u0434\u044f\u043a\u0443\u044e... \u044f... \u043f\u043e\u0441\u0442\u0430\u0432\u043b\u044e \u043d\u0430 \u043f\u043e\u043b\u0438\u0446\u044e. \u0414\u0435\u0441\u044c."]},
  // О... дякую... я... поставлю на полицю. Десь.
  "notepad":      {"\u0410\u043c\u0456\u0440": [-2, "\u0411\u043b\u043e\u043a\u043d\u043e\u0442. \u0422\u0430\u043a. \u0417\u0430\u043f\u0438\u0448\u0443 \u0442\u0443\u0434\u0438... \u0449\u043e\u0441\u044c."]},
  // Блокнот. Так. Запишу туди... щось.

  // Елеонор — техніка/гучне
  "speaker_system": {"\u0415\u043b\u0435\u043e\u043d\u043e\u0440": [-5, "\u0422\u0438 \u0437\u043d\u0430\u0454\u0448 \u0449\u043e \u0432 \u043c\u0435\u043d\u0435 \u0432 \u0433\u043e\u043b\u043e\u0432\u0456? \u0406 \u0442\u0438 \u043d\u0435\u0441\u0435\u0448 \u0426\u0415?"]},
  // Ти знаєш що в мене в голові? І ти несеш ЦЕ?
  "speaker":        {"\u0415\u043b\u0435\u043e\u043d\u043e\u0440": [-3, "\u0413\u0443\u0447\u043d\u0435. \u0421\u0430\u043c\u0435 \u0442\u0435, \u0447\u043e\u0433\u043e \u043c\u0435\u043d\u0456 \u043d\u0435 \u0432\u0438\u0441\u0442\u0430\u0447\u0430\u043b\u043e. \u041d\u0456."]},
  // Гучне. Саме те, чого мені не вистачало. Ні.
  "hockey_table":   {"\u0415\u043b\u0435\u043e\u043d\u043e\u0440": [-5, "\u0425\u043e\u043a\u0435\u0439\u043d\u0438\u0439 \u0441\u0442\u0456\u043b. \u0414\u043b\u044f \u043c\u0435\u043d\u0435. \u0422\u0438 \u0432\u0437\u0430\u0433\u0430\u043b\u0456 \u043c\u0435\u043d\u0435 \u0437\u043d\u0430\u0454\u0448?"]},
  // Хокейний стіл. Для мене. Ти взагалі мене знаєш?

  // Летті — стереотипи
  "hanging_planter": {"\u041b\u0435\u0442\u0442\u0456": [-3, "\u041a\u0432\u0456\u0442\u043a\u0430. \u0414\u043b\u044f \u043b\u0456\u043a\u0430\u0440\u044f. \u042f\u043a\u0438\u0439 \u043d\u0435 \u043c\u0430\u0454 \u0447\u0430\u0441\u0443 \u043d\u0430\u0432\u0456\u0442\u044c \u043a\u0430\u0432\u0443 \u0434\u043e\u043f\u0438\u0442\u0438."]},
  // Квітка. Для лікаря. Який не має часу навіть каву допити.
  "pillows":         {"\u041b\u0435\u0442\u0442\u0456": [-2, "\u041f\u043e\u0434\u0443\u0448\u043a\u0438. \u0414\u0443\u043c\u0430\u0454\u0448 \u044f \u0442\u0443\u0442 \u0441\u043f\u043b\u044e? ...\u041d\u0443, \u0456\u043d\u043e\u0434\u0456. \u0410\u043b\u0435 \u0446\u0435 \u043d\u0435 \u043f\u0440\u0438\u0432\u0456\u0434."]}
  // Подушки. Думаєш я тут сплю? ...Ну, іноді. Але це не привід.
};


registerState("gifts", {
  gifted_today: []   // ["Артур", "Аоі"] — кому дарували сьогодні
});


// Дарує предмет персонажу. Повертає {bonus, reaction, is_offensive}
function giveGift(character, itemId) {
  // Перевірити чи вже дарував сьогодні
  if (gameState.gifts.gifted_today.indexOf(character) >= 0) {
    return {bonus: 0, reaction: "\u0422\u0438 \u0432\u0436\u0435 \u0434\u0430\u0440\u0443\u0432\u0430\u0432 \u043c\u0435\u043d\u0456 \u0441\u044c\u043e\u0433\u043e\u0434\u043d\u0456.", is_offensive: false};
    // Ти вже дарував мені сьогодні.
  }

  // Перевірити чи є предмет
  if (!gameState.inventory.items[itemId] || gameState.inventory.items[itemId] <= 0) {
    return {bonus: 0, reaction: "\u0423 \u0442\u0435\u0431\u0435 \u043d\u0435\u043c\u0430\u0454 \u0446\u044c\u043e\u0433\u043e \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0443.", is_offensive: false};
    // У тебе немає цього предмету.
  }

  // Забрати з інвентарю
  gameState.inventory.items[itemId]--;
  if (gameState.inventory.items[itemId] <= 0) {
    delete gameState.inventory.items[itemId];
  }

  // Позначити що дарував сьогодні
  gameState.gifts.gifted_today.push(character);

  // Час на подарунок
  advanceTime(10);

  // Перевірка на образливий подарунок
  if (OFFENSIVE_GIFTS[itemId] && OFFENSIVE_GIFTS[itemId][character]) {
    var offData = OFFENSIVE_GIFTS[itemId][character];
    var penalty = offData[0];
    var reaction = offData[1];
    addChemistry(character, penalty);  // penalty < 0, daily cap не обмежує
    var badFlag = "bad_gift_" + charFlag(character) + "_" + itemId;
    setFlag(badFlag);
    addGossip("bad_gift_" + itemId, [character], 1);
    return {bonus: penalty, reaction: reaction, is_offensive: true};
  }

  // Перевірка на улюблений подарунок
  if (GIFT_REACTIONS[itemId] && GIFT_REACTIONS[itemId][character]) {
    var bonus = GIFT_REACTIONS[itemId][character];
    var actual = addChemistry(character, bonus);
    resetInteraction(character);
    var goodFlag = "gifted_" + charFlag(character) + "_" + itemId;
    setFlag(goodFlag);
    if (bonus >= 12) {
      return {bonus: actual, reaction: "...\u0426\u0435 \u0441\u0430\u043c\u0435 \u0442\u0435, \u0449\u043e \u043c\u0435\u043d\u0456 \u043f\u043e\u0442\u0440\u0456\u0431\u043d\u043e. \u0414\u044f\u043a\u0443\u044e.", is_offensive: false};
      // ...Це саме те, що мені потрібно. Дякую.
    } else if (bonus >= 7) {
      return {bonus: actual, reaction: "\u041e, \u043d\u0435\u043f\u043e\u0433\u0430\u043d\u043e. \u0414\u044f\u043a\u0443\u044e.", is_offensive: false};
      // О, непогано. Дякую.
    } else {
      return {bonus: actual, reaction: "\u0414\u044f\u043a\u0443\u044e, \u043f\u0440\u0438\u0454\u043c\u043d\u043e.", is_offensive: false};
      // Дякую, приємно.
    }
  }

  // Нейтральний подарунок — +1 (баланс v2)
  var neutralActual = addChemistry(character, 1);
  return {bonus: neutralActual, reaction: "\u0414\u044f\u043a\u0443\u044e... \u043c\u0430\u0431\u0443\u0442\u044c.", is_offensive: false};
  // Дякую... мабуть.
}
