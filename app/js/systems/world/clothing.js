// ═══════════════════════════════════════════════════
// СИСТЕМА ОДЯГУ — Z-LAYERING + OUTFIT PICKER
// ═══════════════════════════════════════════════════
//
// Порт з game/clothing.rpy
//
// В браузері немає автоскану файлів, тому гардероб задається вручну.
// Конвенція файлів та ж сама:
//   clothing/{char}-{garment}-{color}-{pose}-z{index}.png
//   face/face-{emotion}.png
//
// Z-Index шари:
//   z10 = base (тіло)
//   z20 = bottom (штани)
//   z30 = top_under (футболка)
//   z40 = top_over (куртка)
//   z60 = extra (шарф)
//   z70 = face (обличчя)
//   z80 = injury (бинти)

registerState("clothing", {
  current_outfits: {},   // {name: {z20: "garment_id", z30: "garment_id"}}
  current_poses: {}      // {name: "crossed"}
});


// ═══ ГАРДЕРОБ: реєстр одягу ═══
// Заповнювати вручну або через JSON-маніфест

var WARDROBE = {};

// Зареєструвати одяг для персонажа
// Приклад: registerClothing("Артур", "jacket_biker-black", 40, ["crossed", "down"])
function registerClothing(name, garmentId, zindex, poses) {
  if (!WARDROBE[name]) {
    WARDROBE[name] = {poses: [], items: {}, faces: {}, by_zindex: {}};
  }
  var w = WARDROBE[name];
  var parts = garmentId.split("-");
  var garment = parts[0] || garmentId;
  var color = parts[1] || "default";

  w.items[garmentId] = {
    garment: garment,
    color: color,
    zindex: zindex,
    poses: poses || ["crossed"],
    files: {}
  };

  // Побудувати файлові шляхи
  var charShort = _getCharShort(name);
  for (var i = 0; i < (poses || ["crossed"]).length; i++) {
    var pose = (poses || ["crossed"])[i];
    w.items[garmentId].files[pose] = "clothing/" + charShort + "-" + garmentId + "-" + pose + "-z" + zindex + ".png";
    if (w.poses.indexOf(pose) < 0) w.poses.push(pose);
  }

  // Додати в by_zindex
  if (!w.by_zindex[zindex]) w.by_zindex[zindex] = [];
  w.by_zindex[zindex].push(garmentId);
}

// Зареєструвати обличчя
function registerFace(name, emotion, path) {
  if (!WARDROBE[name]) {
    WARDROBE[name] = {poses: [], items: {}, faces: {}, by_zindex: {}};
  }
  WARDROBE[name].faces[emotion] = path;
}


// ═══ ВИБІР ОДЯГУ ═══

function pickOutfit(name) {
  var w = WARDROBE[name];
  if (!w) return {};
  var outfit = {};
  for (var z in w.by_zindex) {
    var options = w.by_zindex[z];
    outfit[z] = options[Math.floor(Math.random() * options.length)];
  }
  return outfit;
}

function pickPose(name) {
  var w = WARDROBE[name];
  if (!w || w.poses.length === 0) return "crossed";
  return w.poses[Math.floor(Math.random() * w.poses.length)];
}

function getOutfitLayers(name, pose) {
  var w = WARDROBE[name];
  if (!w) return [];
  if (!pose) pose = (gameState.clothing.current_poses[name]) || "crossed";
  var outfit = gameState.clothing.current_outfits[name] || {};
  if (!outfit || Object.keys(outfit).length === 0) {
    outfit = pickOutfit(name);
    gameState.clothing.current_outfits[name] = outfit;
  }

  var layers = [];
  var zKeys = Object.keys(outfit).sort(function(a, b) { return a - b; });
  for (var i = 0; i < zKeys.length; i++) {
    var z = zKeys[i];
    var gid = outfit[z];
    var item = w.items[gid];
    if (!item) continue;
    var fpath = item.files[pose] || item.files["neutral"] || item.files["crossed"];
    if (fpath) layers.push({z: parseInt(z), path: fpath});
  }
  return layers;
}

function getFacePath(name, emotion) {
  var w = WARDROBE[name];
  if (!w) return null;
  return w.faces[emotion || "calm"] || null;
}

function setOutfit(name, outfitDict) {
  gameState.clothing.current_outfits[name] = outfitDict;
}

function setPose(name, poseName) {
  gameState.clothing.current_poses[name] = poseName;
}

function refreshAllOutfits() {
  for (var short in CAST) {
    var name = CAST[short].name;
    gameState.clothing.current_outfits[name] = pickOutfit(name);
    gameState.clothing.current_poses[name] = pickPose(name);
  }
}


// ═══ ДОПОМІЖНЕ ═══

function _getCharShort(name) {
  for (var short in CAST) {
    if (CAST[short].name === name) return short;
  }
  return name.toLowerCase();
}


// Контекст часу доби
function getTimeContext() {
  var h = Math.floor(gameState.time.minutes / 60);
  if (h < 9) return "morning";
  if (h < 18) return "day";
  if (h < 22) return "evening";
  return "night";
}

function getOutfitContext(name) {
  if (gameState.missions && gameState.missions.current_partner === name) return "mission";
  return getTimeContext();
}
