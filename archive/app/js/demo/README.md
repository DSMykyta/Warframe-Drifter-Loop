# ДЕМО РЕЖИМ

## Як повернути гру з демо назад на звичайний режим

В `app/index.html` знайди блок `<!-- Сцени -->` і `<!-- ДЕМО -->`.

### Зараз (демо):
```html
<!-- Сцени (діалоги вимкнені, фінал потрібен для демо тесту) -->
<!--
<script src="js/scenes/intro.js"></script>
<script src="js/scenes/explore_mall.js"></script>
<script src="js/scenes/stubs.js"></script>
<script src="js/scenes/coffee_quest.js"></script>
<script src="js/scenes/pair_events.js"></script>
<script src="js/scenes/metro_jacket.js"></script>
-->
<script src="js/scenes/finale.js"></script>
<script src="js/scenes/finale_lose.js"></script>

<!-- ДЕМО -->
<script src="js/demo/demo_dialogues.js"></script>
<script src="js/demo/demo_systems.js"></script>
<script src="js/demo/demo_missions.js"></script>
<script src="js/demo/demo_init.js"></script>

<!-- Автозавантажувач діалогів (вимкнений під час демо) -->
<!--<script src="js/engine/autoloader.js"></script>-->
```

### Повернути гру:
```html
<!-- Сцени -->
<script src="js/scenes/intro.js"></script>
<script src="js/scenes/explore_mall.js"></script>
<script src="js/scenes/stubs.js"></script>
<script src="js/scenes/coffee_quest.js"></script>
<script src="js/scenes/pair_events.js"></script>
<script src="js/scenes/metro_jacket.js"></script>
<script src="js/scenes/finale.js"></script>
<script src="js/scenes/finale_lose.js"></script>

<!-- ДЕМО (вимкнено) -->
<!--
<script src="js/demo/demo_dialogues.js"></script>
<script src="js/demo/demo_systems.js"></script>
<script src="js/demo/demo_missions.js"></script>
<script src="js/demo/demo_init.js"></script>
-->

<!-- Автозавантажувач діалогів -->
<script src="js/engine/autoloader.js"></script>
```

Тобто: розкоментуй сцени, закоментуй демо, розкоментуй autoloader.
