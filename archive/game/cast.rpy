# game/cast.rpy
# ═══════════════════════════════════════════════════
# КАСТ — ЄДИНЕ ДЖЕРЕЛО ПРАВДИ ДЛЯ ПЕРСОНАЖІВ
# ═══════════════════════════════════════════════════
# Всі системи тягнуть дані звідси. Щоб додати персонажа —
# додай запис в CAST_DATA, решта підхопить автоматично.

init -10 python:

    # ═══ ГОЛОВНА ТАБЛИЦЯ ПЕРСОНАЖІВ ═══

    CAST_DATA = {
        "Артур": {
            "id": "arthur",
            "image_tag": "arthur",
            "home": "security_desk",
            "color": "#a0c4ff",
            "namebox_bg": "#1a2a5acc",
            "sprite_folder": "character_sprites/Character-Arthur-Hex",
            "face": "character_sprites/Character-Arthur-Hex/face-calm.png",
            "default_outfit": "casual",
            "default_pose": "arms_crossed",
        },
        "Елеонор": {
            "id": "eleanor",
            "image_tag": "eleanor",
            "home": "furniture",
            "color": "#d8b4fe",
            "namebox_bg": "#3a1a5acc",
            "sprite_folder": "character_sprites/Character-Eleanor-Hex",
            "face": "character_sprites/Character-Eleanor-Hex/face-template.png",
            "default_outfit": "casual",
            "default_pose": "arms_crossed",
        },
        "Летті": {
            "id": "lettie",
            "image_tag": "lettie",
            "home": "medbay",
            "color": "#a5f3fc",
            "namebox_bg": "#0a3a4acc",
            "sprite_folder": "character_sprites/Character-Lettie-Hex",
            "face": "character_sprites/Character-Lettie-Hex/face-template.png",
            "default_outfit": "casual",
            "default_pose": "arms_crossed",
        },
        "Амір": {
            "id": "amir",
            "image_tag": "amir",
            "home": "arcade",
            "color": "#fef08a",
            "namebox_bg": "#4a3f0acc",
            "sprite_folder": "character_sprites/Character-Amir-Hex",
            "face": "character_sprites/Character-Amir-Hex/face-template-hm.png",
            "default_outfit": "casual",
            "default_pose": "arms_crossed",
        },
        "Аоі": {
            "id": "aoi",
            "image_tag": "aoi",
            "home": "music_shop",
            "color": "#f0abfc",
            "namebox_bg": "#4a1260cc",
            "sprite_folder": "character_sprites/Character-Aoi-Hex",
            "face": "character_sprites/Character-Aoi-Hex/face-template.png",
            "default_outfit": "casual",
            "default_pose": "arms_crossed",
        },
        "Квінсі": {
            "id": "quincy",
            "image_tag": "quince",
            "home": "range",
            "color": "#fca5a5",
            "namebox_bg": "#5a1a1acc",
            "sprite_folder": "character_sprites/Character-Quincy-Hex",
            "face": "character_sprites/Character-Quincy-Hex/face-template.png",
            "default_outfit": "casual",
            "default_pose": "arms_crossed",
        },
    }

    # ═══ АВТОГЕНЕРОВАНІ СПИСКИ (з CAST_DATA) ═══

    CAST = list(CAST_DATA.keys())

    HOME_LOCATIONS = {name: data["home"] for name, data in CAST_DATA.items()}

    CHAR_FLAG_ID = {name: data["id"] for name, data in CAST_DATA.items()}

    CHAR_FACE_AVATARS = {name: data["face"] for name, data in CAST_DATA.items()}

    # Маппінг кирилиця → image tag (для show/hide спрайтів)
    CHAR_IMAGE_TAG = {name: data["image_tag"] for name, data in CAST_DATA.items()}

    # Множина всіх image tags (для speaker dimming)
    _CHAR_TAGS = set(data["image_tag"] for data in CAST_DATA.values())

    def char_flag(name):
        """Повертає латинський ID для флагів."""
        return CHAR_FLAG_ID.get(name, name.lower())

    # ═══ ІНІЦІАЛІЗАЦІЯ СЛОВНИКІВ ПО КАСТУ ═══

    def _init_cast_dict(default_value=0):
        """Створює dict {ім'я: default_value} для всіх в касті."""
        return {name: default_value for name in CAST}
