label intro_text:

    $ dictionary_button = True

    image bg scary_room = "images/bg_scary_room.png"
    scene bg scary_room

    p1 "Ты видишь: {translate=вода}вода{/translate} и {translate=камень}камень{/translate}."

    "{font=Homifont.ttf}Ты не понимаешь, что это значит...{font}"

    "Ты слышишь слово: {a=translate:Привет}{font=Homifont.ttf}Привет{/font}{/a}."

    "{a=translate:пиписька}{font=Homifont.ttf}пиписька{/font}{/a}. {a=translate:Колбаса}{font=Homifont.ttf}Колбаса{/font}{/a} "

    "Ты не слышишь слово: {a=translate:пиписька}{font=Homifont.ttf}пиписька{/font}{/a}."

    "{a=translate:Бутерброд}{font=Homifont.ttf}Бутерброд{/font}{/a} — звучит очень глупо, но пока плевать, мы тестируем игру."

    "{a=translate:Колбаса}{font=Homifont.ttf}Колбаса{/font}{/a} — еще одна глупость, придуманная для тестирования."
    "Также сейчас я буду демонстрировать возможности игры."

    "Вот твое время [current_time]."

    "А вот день, когда ты в игре [current_date]"

    "А сейчас фокус!"

    play movie "video/video.webm"
    
    "Видео должно было появиться, но я не знаю, как это сделать."

    return
