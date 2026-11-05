# game/screens/screen_gallery.rpy

init python:
    CG_LIST = [
        {
            "id": "arthur_kitchen_cg",
            "path": "images/cg/arthur_kitchen_cg.png",
            "title": "Кафе «Скана»",
        },
    ]

screen gallery():
    modal True
    add Solid("#09090bf0")

    vbox:
        align (0.5, 0.05)
        text "ГАЛЕРЕЯ" size 28 color "#a855f7" xalign 0.5 bold True

    vpgrid:
        align (0.5, 0.5)
        cols 3
        spacing 20
        xmaximum 1200
        ymaximum 700
        mousewheel True

        for _cg in CG_LIST:
            if _cg["id"] in persistent.cg_unlocked:
                button:
                    xsize 350
                    ysize 200
                    action Show("cg_viewer", cg_path=_cg["path"], cg_title=_cg["title"])
                    add _cg["path"] xsize 350 ysize 200 fit "contain"
            else:
                frame:
                    xsize 350
                    ysize 200
                    background "#ffffff10"
                    text "?" size 48 color "#ffffff20" align (0.5, 0.5)

    button:
        xpos 0.96 ypos 0.03 xanchor 1.0
        action Return()
        text "Закрити" size 16 color "#fca5a5"

screen cg_viewer(cg_path, cg_title):
    modal True
    add cg_path align (0.5, 0.5) fit "contain"
    text "[cg_title]" size 18 color "#ffffffcc" xalign 0.5 ypos 0.95
    button:
        xpos 0.96 ypos 0.03 xanchor 1.0
        action Hide("cg_viewer")
        text "X" size 20 color "#fca5a5"
