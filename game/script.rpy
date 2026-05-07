# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pov = Character("[povname]", color="#ffa647")

transform smallright:
    zoom 0.3
    xalign 0.7
    yalign 1.0

transform smallleft:
    zoom 0.3
    xalign -0.4
    yalign 1.0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "hitslab-flower-garden-flower-music-281288.mp3"
    scene fleur with fade
    pause 1.5
    $ povname = renpy.input("Name the male lead:", length = 32)
    $ povname = povname.strip()
    if not povname:
        $ povname = "Daniel"
    
    scene wake with irisin
    play music "wumeiwansui-miraculous-flower-161931.mp3" fadein 2.0
    play sound "yawning-6096.mp3"
  
    return
