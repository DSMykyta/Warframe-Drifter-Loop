# game/dialogues/aoi/aoi_rank1_convo4.rpy
# Аоі — Ранг 1, Розмова 4: Обійми

init python:
    DIALOGUE_ENTRIES.append({
        "id": "aoi_rank1_convo4",
        "who": "Аоі",
        "conditions": {
            "flag_true": ["aoi_intro_done", "aoi_rank1_convo3_done"],
            "flag_false": ["aoi_rank1_convo4_done"],
            "rank_min": 1,
        },
        "priority": 45,
        "chance": 100,
        "label": "aoi_rank1_convo4",
    })

label aoi_rank1_convo4:
    show aoi at char_center
    $ store.talked_today.add("Аоі")

    ao "Дрифтер! Я тут складала орігамі і подумала — тобі ніхто сьогодні не казав нічого приємного, правда?"
    $ advance_time(3)

    mc "Мені рідко хто каже щось приємне."
    $ advance_time(3)

    ao "Це неприпустимо. Тримай."
    $ advance_time(3)

    "Аоі простягає маленьку паперову фігурку. Щось середнє між котом і ведмедем."
    $ advance_time(3)

    ao "Це віртуальне обійми. Ну, паперове. Але з тим самим ефектом."
    $ advance_time(3)

    menu:
        "Дякую. Це мило.":
            jump aoi_r1c4_sweet

        "Що це за звірятко?":
            jump aoi_r1c4_animal

        "А справжні обійми не пропонуєш?":
            jump aoi_r1c4_real_hug

label aoi_r1c4_sweet:
    mc "Дякую, Аоі. Справді мило."
    $ advance_time(3)

    ao "Бачиш! Маленькі речі мають силу. Одне орігамі може змінити настрій на весь день."
    $ advance_time(3)

    $ add_chemistry("Аоі", 2)

    jump aoi_r1c4_animals

label aoi_r1c4_animal:
    mc "Це... кіт? Чи ведмідь? Чи щось інше?"
    $ advance_time(3)

    ao "Це котоведмідь. Мій власний вид. Я його винайшла."
    $ advance_time(3)

    mc "Котоведмідь."
    $ advance_time(3)

    ao "Так! Має м'якість кота і обіймальність ведмедя. Ідеальна істота."
    $ advance_time(3)

    $ add_chemistry("Аоі", 2)
    $ add_insight("aoi_origami_creatures", "Аоі вигадує власні види тварин через орігамі. Її фірмовий — котоведмідь.")

    jump aoi_r1c4_animals

label aoi_r1c4_real_hug:
    mc "А якщо я хочу справжні обійми, а не паперові?"
    $ advance_time(3)

    ao "О! Сміливо. Але ні. Справжні обійми — це ранг дружби вище. Ти ще не заслужив."
    $ advance_time(3)

    mc "Є система рангів для обіймів?"
    $ advance_time(3)

    ao "Звичайно! Паперове обійми — базовий рівень. Далі — помах рукою з ентузіазмом. Потім — поплескування по плечу. І тільки потім — повні обійми."
    $ advance_time(3)

    mc "А яка вершина?"
    $ advance_time(3)

    ao "Обійми з розгону. Але це тільки для найближчих людей."
    $ advance_time(3)

    $ add_chemistry("Аоі", 4)

    jump aoi_r1c4_animals

label aoi_r1c4_animals:

    ao "До речі, котоведмідь — не просто фантазія. Я подумала: в твоєму часі ж є дивні тварини, правда?"
    $ advance_time(3)

    mc "Дивні — це м'яко сказано."
    $ advance_time(3)

    ao "Розкажи! Які найдивніші?"
    $ advance_time(3)

    menu:
        "Розповісти про предасайтів з Деймосу":
            jump aoi_r1c4_predasites

        "Розповісти про кубрау":
            jump aoi_r1c4_kubrows

label aoi_r1c4_predasites:
    mc "На Деймосі, супутнику Марса, є створіння — предасайти. Уяви собі дикого звіра з інфікованою плоттю, кістяними наростами і трьома рядами зубів."
    $ advance_time(3)

    ao "Це жахливо."
    $ advance_time(3)

    mc "А тепер уяви, що деякі люди їх приручають. І тримають як домашніх улюбленців."
    $ advance_time(3)

    ao "Що?!"
    $ advance_time(3)

    mc "Я сам допомагаю їх зберігати. Є ціла система консервації — ловиш, лікуєш, знаходиш їм дім."
    $ advance_time(3)

    ao "Ти рятуєш монстрів?"
    $ advance_time(3)

    mc "Вони не монстри. Просто... інші. Вони не просили бути такими."
    $ advance_time(3)

    ao "Це... знаєш, це найкрасивіше, що я сьогодні чула."
    $ advance_time(3)

    $ add_chemistry("Аоі", 4)
    $ add_insight("aoi_conservation", "Аоі вражена тим, що Дрифтер рятує створінь з Деймосу. Їй близька ідея турботи про тих, кого інші вважають потворними.")

    jump aoi_r1c4_end

label aoi_r1c4_kubrows:
    mc "Є кубрау — щось на зразок величезних вовків. Дуже вірні, дуже небезпечні. Дехто вирощує їх з яєць."
    $ advance_time(3)

    ao "Космічні вовки! Я хочу одного."
    $ advance_time(3)

    mc "Вони потребують постійного догляду. Без уваги — хворіють."
    $ advance_time(3)

    ao "Як і всі. Навіть люди."
    $ advance_time(3)

    mc "Є навіть програма розведення. Генетичне різноманіття, рідкісні забарвлення..."
    $ advance_time(3)

    ao "Ти серйозно цим займаєшся? У вільний час від порятунку всесвіту?"
    $ advance_time(3)

    mc "Хтось має."
    $ advance_time(3)

    $ add_chemistry("Аоі", 2)
    $ add_insight("aoi_kubrow_interest", "Аоі зацікавилась кубрау — космічними вовками. Їй подобається ідея догляду за небезпечними, але вірними істотами.")

    jump aoi_r1c4_end

label aoi_r1c4_end:

    ao "Знаєш, Дрифтер, я думаю, ти добра людина."
    $ advance_time(3)

    mc "Чому?"
    $ advance_time(3)

    ao "Бо ти рятуєш тварин, приймаєш паперових котоведмедів і відповідаєш на дивні питання о третій годині дня."
    $ advance_time(3)

    ao "А тепер тримай свого котоведмедя і йди. Мені треба зробити ще п'ять штук. Летті хоче жирафу."
    $ advance_time(3)

    $ add_chemistry("Аоі", 2)

    $ store.seen_dialogues.add("aoi_rank1_convo4")
    $ set_flag("aoi_rank1_convo4_done")

    hide aoi
    return
