# game/clothing.rpy
# ═══════════════════════════════════════════════════════════════
# СИСТЕМА ОДЯГУ — АВТОСКАН + РАНДОМІЗАЦІЯ
# ═══════════════════════════════════════════════════════════════
#
# Конвенція назв файлів (дефіс між секціями):
#
#   clothing/:  {character}-{garment}-{color}-{pose}-z{index}.png
#   face/:      face-{emotion}.png
#
# Приклади:
#   arthur-jacket_biker-black-crossed-z40.png
#   arthur-jeans-blue-neutral-z20.png
#   arthur-tshirt_jp-white-crossed-z30.png
#   arthur-scarf-neutral-neutral-z60.png
#   face-calm.png
#
# Z-Index:
#   z10 = base (тіло)
#   z20 = bottom (штани)
#   z30 = top under (футболка)
#   z40 = top over (куртка)
#   z60 = extra (шарф, рушник)
#   z70 = face (обличчя — окрема папка)
#   z80 = injury (бинти)
#
# Кинув файл по конвенції в clothing/ — система підхопить.
# Нічого прописувати вручну не треба.
#
# ═══════════════════════════════════════════════════════════════


init -5 python:
    import os
    import re

    # ═══ ПАРСЕР ФАЙЛІВ ОДЯГУ ═══

    def _scan_clothing(sprite_folder):
        """Сканує папку clothing/ і парсить назви файлів.
        Повертає dict:
        {
            "garment_id": {              # "jacket_biker-black"
                "garment": "jacket_biker",
                "color": "black",
                "zindex": 40,
                "poses": ["crossed", "down"],
                "files": {
                    "crossed": "clothing/arthur-jacket_biker-black-crossed-z40.png",
                    "down":    "clothing/arthur-jacket_biker-black-down-z40.png",
                }
            }
        }
        """
        clothing_dir = os.path.join(config.gamedir, sprite_folder, "clothing")
        if not os.path.isdir(clothing_dir):
            return {}

        result = {}
        pattern = re.compile(r'^(.+)-(.+)-(.+)-(.+)-z(\d+)\.png$')

        for fname in os.listdir(clothing_dir):
            if not fname.endswith(".png"):
                continue
            m = pattern.match(fname)
            if not m:
                continue
            char, garment, color, pose, zindex = m.groups()
            zindex = int(zindex)

            garment_id = "{}-{}".format(garment, color)
            if garment_id not in result:
                result[garment_id] = {
                    "garment": garment,
                    "color": color,
                    "zindex": zindex,
                    "poses": [],
                    "files": {},
                }
            if pose not in result[garment_id]["poses"]:
                result[garment_id]["poses"].append(pose)
            result[garment_id]["files"][pose] = "clothing/" + fname

        return result

    def _scan_faces(sprite_folder):
        """Сканує папку face/ і повертає dict {emotion: path}."""
        face_dir = os.path.join(config.gamedir, sprite_folder, "face")
        if not os.path.isdir(face_dir):
            return {}

        result = {}
        pattern = re.compile(r'^face-(.+)\.png$')

        for fname in os.listdir(face_dir):
            m = pattern.match(fname)
            if m:
                emotion = m.group(1)
                result[emotion] = "face/" + fname

        return result


    # ═══ ПОБУДОВА ГАРДЕРОБУ З ФАЙЛІВ ═══

    def _build_wardrobe():
        """Сканує clothing/ для кожного персонажа з CAST_DATA.
        Будує WARDROBE автоматично."""
        wardrobe = {}

        for name, data in CAST_DATA.items():
            folder = data.get("sprite_folder")
            if not folder:
                continue

            items = _scan_clothing(folder)
            faces = _scan_faces(folder)

            if not items and not faces:
                continue

            # Знайти всі унікальні пози
            all_poses = set()
            for item in items.values():
                all_poses.update(item["poses"])

            # Згрупувати по z-index (шар)
            by_zindex = {}
            for gid, item in items.items():
                z = item["zindex"]
                if z not in by_zindex:
                    by_zindex[z] = []
                by_zindex[z].append(gid)

            wardrobe[name] = {
                "poses": list(all_poses) or ["crossed"],
                "items": items,
                "faces": faces,
                "by_zindex": by_zindex,
            }

        return wardrobe

    # Сканувати один раз при запуску
    WARDROBE = _build_wardrobe()


    # ═══ КОНТЕКСТ ЧАСУ ДОБИ ═══

    def get_time_context():
        """Визначає контекст часу доби для вибору одягу."""
        h = store.minutes // 60
        if h < 9:
            return "morning"
        elif h < 18:
            return "day"
        elif h < 22:
            return "evening"
        else:
            return "night"

    def get_outfit_context(name):
        """Визначає контекст для вибору одягу NPC.
        Пріоритет: місія > локація > час доби."""
        if store.current_mission_partner == name:
            return "mission"
        loc = get_char_location(name) if name in CAST else None
        if loc == "bar":
            return "bar"
        return get_time_context()


    # ═══ РАНДОМНИЙ ВИБІР ОДЯГУ ═══

    def pick_outfit(name):
        """Вибирає рандомний набір шарів для NPC.
        Повертає dict {zindex: garment_id} — по одному предмету на шар."""
        w = WARDROBE.get(name)
        if not w:
            return {}

        outfit = {}
        for z, garment_ids in w["by_zindex"].items():
            outfit[z] = renpy.random.choice(garment_ids)
        return outfit

    def pick_pose(name):
        """Вибирає рандомну позу для NPC."""
        w = WARDROBE.get(name)
        if not w:
            return "crossed"
        return renpy.random.choice(w["poses"])

    def get_outfit_layers(name, pose=None):
        """Повертає список шляхів до файлів (знизу вгору) для поточного аутфіту.
        Кожен шлях — відносний від sprite_folder."""
        w = WARDROBE.get(name)
        if not w:
            return []

        if pose is None:
            pose = store.current_poses.get(name, "crossed")

        outfit = store.current_outfits.get(name, {})
        if not isinstance(outfit, dict):
            outfit = pick_outfit(name)
            store.current_outfits[name] = outfit

        layers = []
        for z in sorted(outfit.keys()):
            gid = outfit[z]
            item = w["items"].get(gid)
            if not item:
                continue
            # Шукаємо файл для потрібної пози, fallback на neutral
            fpath = item["files"].get(pose) or item["files"].get("neutral")
            if fpath:
                layers.append((z, fpath))

        return layers

    def get_face_path(name, emotion="calm"):
        """Повертає шлях до файлу емоції."""
        w = WARDROBE.get(name)
        if not w:
            return None
        return w["faces"].get(emotion)

    def refresh_all_outfits():
        """Перевибирає одяг для всіх NPC. Викликати в next_day()."""
        for name in CAST:
            store.current_outfits[name] = pick_outfit(name)
            store.current_poses[name] = pick_pose(name)

    def set_outfit(name, outfit_dict):
        """Примусово встановлює аутфіт (для скриптових сцен).
        outfit_dict = {20: "jeans-blue", 30: "tshirt_jp-white", 40: "jacket_biker-black"}"""
        store.current_outfits[name] = outfit_dict

    def set_pose(name, pose_name):
        """Примусово встановлює позу."""
        store.current_poses[name] = pose_name

    def get_sprite_full_path(name, layer_path):
        """Повертає повний шлях від game/ для спрайта."""
        folder = CAST_DATA.get(name, {}).get("sprite_folder", "")
        return folder + "/" + layer_path


# ═══════════════════════════════════════════════════════════════
# RUNTIME ЗМІННІ
# ═══════════════════════════════════════════════════════════════

default current_outfits = {name: {} for name in CAST}

default current_poses = {name: "crossed" for name in CAST}
