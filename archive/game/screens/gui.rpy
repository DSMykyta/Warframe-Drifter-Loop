################################################################################
## Ініціалізація
################################################################################

## Оператор init offset змушує оператори ініціалізації в цьому файлі
## виконуватися перед операторами init в будь-якому іншому файлі.
init offset = -2

## Виклик gui.init скидає стилі до розумних значень за замовчуванням і
## встановлює ширину та висоту гри.
init python:
    gui.init(1920, 1080)

## Увімкнути перевірку недійсних або нестабільних властивостей в екранах або
## перетвореннях
define config.check_conflicting_properties = True


################################################################################
## Змінні конфігурації GUI
################################################################################


## Кольори #####################################################################
##
## Кольори тексту в інтерфейсі.

## ═══ HEX CYBERPUNK PALETTE (з hex-vn.jsx) ═══
## Акцентований колір — неоновий фіолетовий
define gui.accent_color = '#a855f7'

## Кнопка в стані спокою — приглушений сірий
define gui.idle_color = '#8888aa'

## Дрібний текст
define gui.idle_small_color = '#6a6a8a'

## Ховер — яскравий рожево-фіолетовий
define gui.hover_color = '#d946ef'

## Вибрана кнопка — жовтий акцент
define gui.selected_color = '#facc15'

## Неактивна кнопка
define gui.insensitive_color = '#ffffff25'

## Смуги — темні з фіолетовим
define gui.muted_color = '#1a1a2e'
define gui.hover_muted_color = '#a855f766'

## Текст діалогу та інтерфейсу — світлий на темному
define gui.text_color = '#d4cfc6'
define gui.interface_text_color = '#d4cfc6'


## Шрифти та розміри шрифтів ###################################################

## Шрифт — Courier New
define gui.text_font = "fonts/CourierNew-Regular.ttf"

## Шрифт для імен персонажів
define gui.name_text_font = "fonts/CourierNew-Bold.ttf"

## Шрифт для інтерфейсу
define gui.interface_text_font = "fonts/CourierNew-Regular.ttf"

## Розмір звичайного тексту діалогу.
define gui.text_size = 33

## Розмір імен персонажів.
define gui.name_text_size = 45

## Розмір тексту в інтерфейсі гри.
define gui.interface_text_size = 33

## Розмір міток в інтерфейсі гри.
define gui.label_text_size = 36

## Розмір тексту на екрані сповіщень.
define gui.notify_text_size = 24

## Розмір назви гри.
define gui.title_text_size = 75


## Головне та ігрове меню ######################################################

## Зображення, які використовуються для головного та ігрового меню.
## Фон головного меню тепер в screen_mainmenu.rpy
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/main_menu.png"


## Діалог ######################################################################
##
## Ці змінні керують тим, як діалог відображатиметься на екрані один рядок за
## раз.

## Висота текстового поля, що містить діалог.
define gui.textbox_height = 278

## Розташування текстового поля вертикально на екрані. 0,0 – верх, 0,5 – центр,
## 1,0 – низ.
define gui.textbox_yalign = 1.0


## Розташування імені персонажа, відносно текстового поля. Це може бути ціла
## кількість пікселів зліва чи зверху або 0,5 до центру.
define gui.name_xpos = 360
define gui.name_ypos = 0

## Горизонтальне вирівнювання імені персонажа. Це може бути 0,0 для вирівнювання
## по лівому краю, 0,5 для вирівнювання по центру та 1,0 для вирівнювання по
## правому краю.
define gui.name_xalign = 0.0

## Ширина, висота та межі поля, що містять ім’я персонажа, або None, щоб
## автоматично змінити його розмір.
define gui.namebox_width = None
define gui.namebox_height = None

## Межі поля, що містять імʼя персонажа, у порядку зліва, зверху, справа, знизу.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## Якщо встановлено «True», тло поля імен буде мозаїкою, якщо «False», тло поля
## імен буде масштабовано.
define gui.namebox_tile = False


## Розташування діалогу відносно текстового поля. Це може бути ціла кількість
## пікселів відносно лівого чи верхнього краю текстового поля або 0,5 до центру.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## Максимальна ширина тексту діалогу в пікселях.
define gui.dialogue_width = 1116

## Горизонтальне вирівнювання тексту діалогу. Це може бути 0,0 для вирівнювання
## по лівому краю, 0,5 для вирівнювання по центру та 1,0 для вирівнювання по
## правому краю.
define gui.dialogue_text_xalign = 0.0


## Кнопки ######################################################################
##
## Ці змінні разом із файлами зображень у gui/button контролюють аспекти показу
## кнопок.

## Ширина та висота кнопки в пікселях. Якщо встановлено «None», Ren'Py обчислить
## розмір.
define gui.button_width = None
define gui.button_height = None

## Межі з кожного боку кнопки в порядку зліва, зверху, справа та знизу.
define gui.button_borders = Borders(6, 6, 6, 6)

## Якщо встановлено «True», зображення тла буде мозаїчно. Якщо «False»,
## зображення тла буде лінійно масштабовано.
define gui.button_tile = False

## Шрифт, який використовується кнопкою.
define gui.button_text_font = gui.interface_text_font

## Розмір тексту, який використовується кнопкою.
define gui.button_text_size = gui.interface_text_size

## Колір тексту кнопки в різних станах.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## Горизонтальне вирівнювання тексту кнопки. (0,0 — ліворуч, 0,5 — центр, 1,0 —
## праворуч).
define gui.button_text_xalign = 0.0


## Ці змінні перевизначають налаштування для різних типів кнопок. Перегляньте
## документацію про GUI, щоб дізнатися про типи доступних кнопок і для чого
## кожна з них використовується.
##
## Ці налаштування використовуються стандартним інтерфейсом:

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Ви також можете додати власні налаштування, додавши змінні з правильними
## назвами. Наприклад, ви можете розкоментувати наступний рядок, щоб встановити
## ширину кнопки навігації.

# define gui.navigation_button_width = 250


## Кнопки вибору ###############################################################
##
## Кнопки вибору використовуються в ігрових меню.

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#d8b4fe'
define gui.choice_button_text_hover_color = "#facc15"
define gui.choice_button_text_insensitive_color = '#ffffff25'


## Кнопки комірок збережень ####################################################
##
## Кнопка комірки збереження — це особливий вид кнопки. Він містить мале
## зображення та текст, що описує вміст комірки збереження. Комірка збереження
## використовує файли зображень у gui/button, як і інші типи кнопок.

## Кнопка комірки збереження.
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## Ширина та висота малих зображень, що використовуються комірками збереження.
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## Кількість стовпців і рядків у сітці комірок збереження.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Позиціонування та інтервали #################################################
##
## Ці змінні керують розташуванням і відстанню між різними елементами
## інтерфейсу.

## Розташування лівої сторони навігаційних кнопок відносно лівої сторони екрана.
define gui.navigation_xpos = 60

## Вертикальна позиція індикатора пропуску.
define gui.skip_ypos = 15

## Вертикальна позиція екрана сповіщень.
define gui.notify_ypos = 68

## Інтервал між елементами у меню вибору.
define gui.choice_spacing = 33

## Кнопки в розділі навігації головного та ігрового меню.
define gui.navigation_spacing = 6

## Контролює розмір інтервалу між параметрами.
define gui.pref_spacing = 15

## Контролює відстань між кнопками налаштувань.
define gui.pref_button_spacing = 0

## Відстань між кнопками сторінки файлу.
define gui.page_spacing = 0

## Відстань між комірками збережень.
define gui.slot_spacing = 15

## Позиція тексту головного меню.
define gui.main_menu_text_xalign = 1.0


## Рамки #######################################################################
##
## Ці змінні керують виглядом рамок, що можуть містити компоненти інтерфейсу,
## коли накладання або вікно відсутні.

## Загальні рамки.
define gui.frame_borders = Borders(6, 6, 6, 6)

## Рамка, яка використовується як частина екрана підтвердження.
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## Рамка, яка використовується як частина екрана пропуску.
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## Рамка, яка використовується як частина екрана сповіщень.
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## Чи слід фонові рамки розміщувати мозаїчно?
define gui.frame_tile = False


## Панелі, смуги прокрутки та повзунки #########################################
##
## Ці керують виглядом і розміром панель, смуг прокрутки та повзунків.
##
## Стандартний інтерфейс використовує лише повзунки та вертикальні смуги
## прокрутки. Усі інші смуги використовуються лише на екранах, написаних
## автором.

## Висота горизонтальних смуг, смуг прокрутки та повзунків. Ширина вертикальних
## смуг, смуг прокручування та повзунків.
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## True якщо зображення панелей мають бути мозаїчно. False, якщо вони повинні
## бути лінійно масштабовані.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Горизонтальні межі.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## Вертикальні межі.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## What to do with unscrollable scrollbars in the game menu. "hide" hides them,
## while None shows them.
define gui.unscrollable = "hide"


## Історія #####################################################################
##
## На екрані історії відображається діалог, який гравець уже закрив.

## Кількість блоків історії діалогів, яких Ren'Py збереже.
define config.history_length = 250

## Висота запису на екрані історії або «None», щоб зробити висоту змінною шляхом
## швидкодії.
define gui.history_height = 210

## Додатковий простір для додавання між записами на екрані «Історія».
define gui.history_spacing = 0

## Положення, ширина та вирівнювання мітки, що вказує ім’я персонажа, що
## говорить.
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## Позиція, ширина та вирівнювання тексту діалогу.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## Режим NVL ###################################################################
##
## На екрані режиму NVL відображається діалог, який вимовляють персонажі режиму
## NVL.

## Межі тла вікна заднього плану режиму NVL.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## Ren'Py відобразить максимальну кількість записів у режимі NVL. Якщо потрібно
## показати більше записів, найстаріший запис буде видалено.
define gui.nvl_list_length = 6

## Висота запису в режимі NVL. Встановіть значення None, щоб записи динамічно
## регулювали висоту.
define gui.nvl_height = 173

## Інтервал між записами режиму NVL, коли gui.nvl_height має значення None, і
## між записами режиму NVL і меню режиму NVL.
define gui.nvl_spacing = 15

## Положення, ширина та вирівнювання мітки, що вказує ім’я персонажа, що
## говорить.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## Позиція, ширина та вирівнювання тексту діалогу.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## Положення, ширина та вирівнювання тексту nvl_thought (тексту, який вимовляє
## персонаж nvl_narrator.)
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## Позиціонування nvl menu_buttons.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


## Локалізація #################################################################

## Це визначає, де дозволений розрив рядка. Стандартне значення підходить
## для більшості мов. Список доступних значень можна знайти на https://
## www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Мобільні пристрої
################################################################################

init python:

    ## Це збільшує розмір кнопок швидкої панелі доступу, щоб їх було легше
    ## торкатися на планшетах і телефонах.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## Це змінює розмір і відстань між різними елементами інтерфейсу, щоб вони
    ## були видимими на телефонах.
    @gui.variant
    def small():

        ## Розміри шрифтів
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## Налаштунки розташування текстового поля.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## Зміна розміру і відстані між різними речами.
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## Макет кнопки збереження.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-режим.
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30
