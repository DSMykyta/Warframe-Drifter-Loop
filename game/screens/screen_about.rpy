screen about():
    tag menu
    modal True

    frame:
        xfill True yfill True

        vbox:
            spacing 15
            xalign 0.5 yalign 0.5

            text "WARFRAME: DRIFTER LOOP" size 28 xalign 0.5
            text "Візуальна новела по всесвіту Warframe 1999." size 16 xalign 0.5
            text "Версія 1.0" size 14 color "#888" xalign 0.5

            null height 20

            textbutton "Назад" action Return() xalign 0.5
