# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define d = Character("Dandelion Spirit", color="#ffe926")
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
    play sound "yawning-6096.mp3" volume 8.5
    pause 3.5
    pov "Ah! What a beautiful dream! I'm so looking forward to this beautiful spring day!"
    pov "I can feel the warm sunshine gently shining throught the window and..."
    scene disaster with vpunch
    play sound "freesound_community-medium-explosion-40472.mp3" volume 4.0
    play music "uniquecreativeaudio-surveying-a-disaster-instrumental-169701.mp3"
    pause 5.5
    pov "What the..."
    pov "What is happening?!"
    pov "Where is this place and where did my beautiful spring day go?!"
    pov "Why is the whole world suddenly... in chaos?"
    play sound "freesound_community-ough-47202.mp3"
    pov "IS THIS SOME KIND OF JOKE?!"
    play sound "dl.mp3" volume 49.5
    d "Um... hi. Please don't panic."
    pov "AND WHAT THE HELL ARE YOU?!"
    d "A dandelion obviously."
    pov "A TALKING DANDELION?! Okay, I am now officially 100%% sure I'm losing my mind."
    d "I'm a dandelion spirit, actually."
    d "And please don't freak out. I'm trying to help! Just quiet down and listen to me young man."
    pov "Okay, okay, first of all, what is happening?"
    d "You may not know this, but far away in the dark countryside, there lives an evil and powerful witch."
    scene poison with fade
    play sound "freesound_community-bubbles-003-6397.mp3"
    d "She has been brewing a {b}terrible{/b} potion, it can slowly drain the life from anything full of vitality, especially us flower sprits!"
    d "Many flowers have already been affected... Every plant has a sprit, and now many are withering away because of this poison..."
    d "If this continues, the consequences will be DISASTROUS! And..."
    scene disaster with hpunch
    stop sound
    pov "Wait, okay, but how can I help? I'm just a normal high school student and have no magical powers if that's what you're thinking."
    d "Please, just travel across the land, awaken and purify each flower sprit, and collect one petal from each of them."
    d "Once you have gathered enough, you can face the witch."
    d "The power of the petals will help you destroy and defeat her."
    pov "Uh.. so my mission is just going around and picking petals?"
    d "No, you can't just take them by force. Some flowers may have already been corrupted by the darkness."
    d "You have to awaken then first, only then, if they choose to trust you, they may willingly give you one fo their petals."
    d "That petal will not just be a normal petal, it carries that spirit and life force of that flower. That is why is must be given freely."
    d "And, I'll give you one of mine, now you carry the power of the dandelions."
    pov "Okay then, thank you... I guess I'll have to do this."
    d "Good luck!"
    stop music fadeout 1.0
    scene min with blinds
    play sound "later.mp3" volume 2.5
    play music "footsteps-dirt-gravel-6823.mp3" volume 5.5
    pause 4.5


    scene lotus 
    play music "adiiswanto-inner-lotus-garden-343243.mp3"
  
    return
