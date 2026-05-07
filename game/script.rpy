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
    scene fleur with irisin
    $ povname = renpy.input("Name the male lead:", length = 32)
    $ povname = povname.strip()
    if not povname:
        $ povname = "Daniel"
    scene wake with fade
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
