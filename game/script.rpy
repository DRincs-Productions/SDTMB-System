﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init -1:
    define mc = Character("Player")
    define a = Character("Alice", icon = "icon alice")
    define an = Character("Ann", icon = "icon ann")


# The game starts here.

label start:

    call screen room_navigation

screen room_navigation():
    modal True
    # Tools
    frame:
        yalign 0.0 xalign 0.0
        hbox:
            textbutton "SmartPhone" action Show("smartphone")
            textbutton "TV" action Show("tv", 
                home_screen="/stmb_interface/tv_screen_home.webp",
                background="/stmb_interface/tv.webp",
                my_align=(0.45, 0.07),
                my_size=(900, 490)
            )
            textbutton "Exit" action Quit(confirm=False)
