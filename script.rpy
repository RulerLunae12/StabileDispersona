define p1 = Character('[viname]', color="#ffff", what_callback=translate_filter)
define p2 = Character('Краули', color="#ffff", what_callback=translate_filter)
define p3 = Character('Сильваир', color="#ffff", what_callback=translate_filter)
define p4 = Character('Чопт', color="#ffff", what_callback=translate_filter)
define p5 = Character('Скарлателла', color="#ffff", what_callback=translate_filter)
define p6 = Character('Касси', color="#ffff", what_callback=translate_filter)
define e = Character('ÃêÐ¯Û¥√╬µ', color="#ffff", what_callback=translate_filter)

label start:

    $ clean_unused_words()
    $ normalize_human_dict()
    $ migrate_human_dict()

    window hide
    scene black

    show text"""
    Эта игра является художественным произведением в жанре Alternate Reality Game (ARG).

    В процессе игры вам могут быть предложены действия вне игрового окна:
    — запуск файлов,
    — взаимодействие с файлами на вашем компьютере,
    — закрытие игры в неожиданный момент.

    Никакие действия не производятся без вашего разрешения.

    Продолжая, вы соглашаетесь участвовать в экспериментальном интерактивном опыте.

    Если вы не готовы — закройте игру сейчас.

    Вы готовы продолжить?
    """ at truecenter with fade

    with dissolve
    pause
    hide text

    menu:
            "Да": 
                jump name
            "Нет":
                $ renpy.quit()

label name:

    scene black

    "Как тебя зовут?"

    $ viname = renpy.input("Введите своё имя!", default="Адами", length=20, allow = "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯяAaBbCcDdEeFfGgHhIiJjKklMmNnOoPpQqRrSsTtUuVvWwXxYyZz" )

    $ viname = viname.strip()
    $ viname_lower = viname.lower()

    if viname == "Адами":
        "Ты уверен, что хочешь выбрать именно это имя?"

        menu name1:

            "Да, на все сто!":

                jump hardmode

            "Нет, я передумал!":

                jump intro_text

    elif viname == "":
        "Ты не можешь оставить это поле пустым!"

        jump start
    
    else:
        jump intro_text


label hardmode:
    scene black

    ##экран темный, шорох, Адами просыпается и поднимается с колен. видим стартовую сцену из оригинальной игры

    p1 "Снова здесь..."

    p1 "Сколько бы ты, красный уебок, не пытался меня здесь заперет, я всё равно выберусь отсюда!"

    ##Поворот, видим рядом лыбу скарлета

    p5 "Тебе разве не нравится играть со мной, человечка?"

    p1"Оставь меня в покое!"

    ##Начинаем бежать от него по коридору, темнеет экран, слышим помехи

    ##Пока бежим, видим в одном из дверных проемов Скарлета, и поворачиваемм другое место

    ## Мы в той комнате, где должен быть Чопт, но его нет, спускаемся в подвал

    ##Мы ныкаемся в комнате Сильваира, забегаем в его операционную, прячемся под стол

    ##Слышим шаги, закрываем глаза

    p1 ". . ."

    ##Нас резко хватают за ногу и вытягивают из под стола
    ##Крик гг
    ##видим сильваира вверх ногами, он давит лыбу

    e "ÃЖ√∩≡╝-†Ф ¥ þΘΣм"

    ##Сильваир давит лыбу, экран темнеет, мы слышим стук.

    ##Экран светлеет и мы видим сильваира с топором

    ##Стук, весь экран в красном, слышим крик

    p5 "Какая жалость..."

    ##За спиной сильваира, в дверном проеме, видим Скарлета, он выглядит немного грустным

    ##Сильв поворачивается к нему, недовольный, весь в крови

    e "þШ╩∑ øт$џ∂ΘVª"

    ## Экран темнеет

    window hide
    centered """
    Адами, это твой конец.

    Игра окончена.
    
    но...
    
    Я найду ещё одну, такую, как ты"""

    $ renpy.pause(2)

    $ renpy.quit()
