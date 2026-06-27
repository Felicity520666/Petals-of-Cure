# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define d = Character("Dandelion Spirit", color="#ffe926")
define pov = Character("[povname]", color="#ffa647")
define l = Character("Lotus Spirit", color="#cd92d5")
define w = Character("Witch", color="#e30646")

transform smallright:
    zoom 0.8
    xalign 0.7
    yalign 1.0

transform smallleft:
    zoom 0.8
    xalign -0.4
    yalign 1.0

image nerd_time = Movie(play="images/nerd.ogg", image="images/moment.png")
image real = Movie(play="images/dd.ogg")
image sr = Movie(play="images/pg.ogg")
image rose = Movie(play="images/rose.ogg")
image sunflower = Movie(play="images/sunflower.ogg")
image lavender = Movie(play="images/lavender.ogg")
image forget = Movie(play="images/forget.ogg")
image daffodil = Movie(play="images/daffodil.ogg")
image orchid = Movie(play="images/orchid.ogg")
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
    pov "I can feel the warm sunshine gently shining through the window and..."
    scene wired with vpunch
    play sound "freesound_community-medium-explosion-40472.mp3" volume 4.0
    play music "uniquecreativeaudio-surveying-a-disaster-instrumental-169701.mp3"
    pov "Oh my! What just happened?!"
    pov "Better go check it out..."
    scene black with fade
    play sound "opening-door-411632.mp3" volume 3.0
    pause 2.0
    scene disaster with fade
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
    d "She has been brewing a {b}terrible{/b} potion. It can slowly drain the life from anything full of vitality, especially us flower spirits!"
    d "Many flowers have already been affected... Every plant has a spirit, and now many are withering away because of this poison..."
    d "If this continues, the consequences will be DISASTROUS! And..."
    scene disaster with hpunch
    stop sound
    pov "Wait, okay, but how can I help? I'm just a normal high school student and have no magical powers if that's what you're thinking."
    d "Please, just travel across the land, awaken and purify each flower spirit, and collect one petal from each of them."
    d "Once you have gathered enough, you can face the witch."
    d "The power of the petals will help you destroy and defeat her."
    pov "Uh.. so my mission is just going around and picking petals?"
    d "No, you can't just take them by force. Some flowers may have already been corrupted by the darkness."
    d "You have to awaken them first. Only then, if they choose to trust you, they may willingly give you one of their petals."
    d "That petal will not just be a normal petal. It carries the spirit and life force of that flower. That is why it must be given freely."
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
    pause 1.5
    show daniel smile at smallright with moveinleft
    pov "Wow. This place is so beautiful and calm."
    l "Um... excuse me, who are you?"
    pov "Oh hi! My name is [povname]. I just got a mission to collect petals from flower spirits in order to defeat an evil witch."
    l "Flower spirits? Oh! Sounds interesting! I thought they only exist in fairy tales."
    pov "Wait, what do you mean by that?"
    pov "YOU are a flower spirit!"
    l "What...? Sorry, but I don't understand."
    pov "Shoot! You must be one of the spirits that have been affected by the poison."
    l "Poison? What are you talking about? I don't remember anything..."
    pov "I see... do you know who you are?"
    l "I... I don't think so..."
    pov "Hmm... you look like a lotus flower, and you can talk, so you must be a lotus spirit."
    l "A lotus... This name sounds familiar... Could you tell me more about myself, I might be able to remember more!"
    pov "Hmmm... well, I did learn a little bit about lotus in school."
    stop music fadeout 1.5
    play sound "musheran-win-176035.mp3" volume 4.5
    scene moment with vpunch
    pause 1.0
    scene nerd_time with dissolve
    play music "shtakalberry-lotus-inspiring-asian-chillout-443674.mp3" fadein 1.5
    pov "So, from what I remember, lotus, also known as Nelumbo nucifera, or colloquially as water lily, is adapted to grow in the floodplains of slow-moving rivers and delta areas."
    scene flower with fade
    pov "Stands of lotus drop hundreds of thousands of seeds every year to the bottom of the pond."
    scene rl with blinds
    pov "Some sprout immediately, though most are eaten by wildlife. The remaining seeds can remain dormant for an extensive period of time as the pond silts in and dries out!"
    scene lotus with vpunch
    show daniel smile at smallright
    play music "the_mountain-win-483309.mp3"
    l "Whoa! Hold your horses! I think I remember something now!"
    l "In my family, we have been talking about our relative in China. She had been sleeping underground in a dry lakebed for nearly 1,300 years. Scientists later discovered her, planted her, and amazingly, she still sprouted and grew into a living lotus plant!"
    pov "Wow, see? Darkness may have covered you, but it didn't erase you! You are the lotus that can bloom again!"
    scene pp with irisin
    pov "The lotus serves as a sacred symbol of purity, rebirth, and strength. Because lotuses rise from the mud without stains, they are viewed as a symbol of purity."
    pov "And since they return to the murky water each evening and open their blooms at the break of day, lotus flowers are also symbols of strength, resilience, and rebirth!"
    scene lotus with fade
    show daniel smile at smallright
    l "I... I am starting to remember more! We lotus also represent the transcending of man's spirit over worldly matter since we bloom from the underworld into the light."
    pov "Yes! And you know what? I'm on a mission to awaken and purify flower spirits, and collect petals to... um, defeat an evil witch apparently. So..."
    l "How brave of you! Here, this is my petal! Take it and may it help you on your journey!"
    scene black with fade
    play music "good_b_music-called-to-win-30sec-195403.mp3" fadein 2.5
    "And so, our cute protagonist continued his journey to collect the petals. After a long time, he collected many petals and gained a lot of knowledge. At last, he finally met the witch."
    scene f1 with hpunch
    play music "paulyudin-tension-tension-music-491416.mp3"
    show daniel smile at smallright with moveinleft
    pov "Haha! I finally found you, you evil witch!"
    w "Even if you find me, it changes nothing."
    play sound "freesound_community-witch-103635.mp3"
    w "My power is far too strong! You will never stop my darkness! You will never stop my ambition!"
    pov "Ha! You are so wrong!"
    pov "On this journey, I awakened many flower fairies and collected their petals."
    pov "But more than that, I learned from them."
    scene real with fade
    pov "First, I met the Dandelion Spirit, who taught me hope, wishes, freedom, and the courage to keep going."
    scene sr with fade
    pov "Then, I met the Lotus Spirit, who showed me purity, awakening, rebirth, and strength!"
    scene rose with fade
    pov "I also got to meet the beautiful Rose Spirit, who taught me passion and love that does not give up."
    scene sunflower with fade
    pov "And then, the Sunflower Spirit showed me joy, light, loyalty, and the power to face the sun."
    scene lavender with fade
    pov "Then, I met the Lavender Spirit, who taught me peace, healing, and calmness after pain."
    scene forget with fade
    pov "I also met the Forget-Me-Not Spirit. She taught me memories, longing, and the promise to never forget what matters."
    scene daffodil with fade
    pov "Next, I saw the Daffodil Spirit. I learned new beginnings, self-discovery, and the return of spring."
    scene orchid with fade
    pov "Last but not least, the Orchid Spirit taught me elegance, mystery, and quiet strength."
    scene f1 with hpunch
    play music "nastelbom-epic-fight-436865.mp3"
    pov "And now, I have all the power I need to defeat you and your darkness!"
    pov "Even in the darkest place, something can still bloom!!!"
    scene f2 with dissolve
    pause 1.0
    scene f3 with dissolve
    play sound "alesiadavina-dark-witch-annoyed-growl-sinister-female-voice-sfx-553605.mp3"
    pause 3.5
    scene black with fade
    "And so, our brave protagonist began the final fight against the witch."
    "At first, he might not know where the journey would lead."
    "But along the way, he collected, little by little, from the world around us."
    "So, when your own journey feels uncertain, take a moment to slow down and notice the small things you used to ignore."
    "Maybe they aren't just flowers."
    "Maybe they are quiet guidance."
    "The end."

    return
