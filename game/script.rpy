# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Blue", who_color="#0f447a") # n for narrator
define i = Character("Impact", who_color="#e5ff32")
define b = Character("Broxah", who_color="32dcff")
define j = Character("Jensen", who_color="7d32ff")
define t = Character("Tactical", who_color="ff3255")
define c = Character("CoreJJ", who_color="ff32b4")

#Define and generate player stats through liquidDb API

# Linking images
init:
    image b smile:
        "./Broxah/Broxah_smile.PNG"
        zoom 1.2
        xanchor .12
    image b smile2:
        "./Broxah/Broxah_smile2.PNG"
        xanchor .12
        zoom 1.2
    image b talk:
        "./Broxah/Broxah_talk.PNG"
        zoom 1.2
        xanchor .12
    image b upset:
        "./Broxah/Broxah_upset.PNG"
        zoom 1.2
        xanchor .12
    image b wave:
        "./Broxah/Broxah_wave.PNG"
        zoom 1.2
        xanchor .12
    image i smile:
        "./Impact/Impact_smile.PNG"
        zoom 1.2
        xanchor .12
    image i smile2:
        "./Impact/Impact_smile2.PNG"
        xanchor .12
        zoom 1.2
    image i talk:
        "./Impact/Impact_talk.PNG"
        xanchor .12
        zoom 1.2
    image i upset:
        "./Impact/Impact_upset.PNG"
        xanchor .12
        zoom 1.2
    image i wave:
        "./Impact/Impact_wave.PNG"
        zoom 1.2
        xanchor .12
    image j smile:
        "./Jensen/Jensen_smile.PNG"
        zoom 1.2
        xanchor .12
    image j smile2:
        "./Jensen/Jensen_smile2.PNG"
        zoom 1.2
        xanchor .12
    image j talk:
        "./Jensen/Jensen_talk.PNG"
        zoom 1.2
        xanchor .12
    image j upset:
        "./Jensen/Jensen_upset.PNG"
        zoom 1.2
        xanchor .12
    image j wave:
        "./Jensen/Jensen_wave.PNG"
        zoom 1.2
        xanchor .12
    image t smile:
        "./Tactical/Tactical_smile.PNG"
        zoom 1.2
        xanchor .12
    image t smile2:
        "./Tactical/Tactical_smile2.PNG"
        zoom 1.2
        xanchor .12
    image t talk:
        "./Tactical/Tactical_talk.PNG"
        zoom 1.2
        xanchor .12
    image t upset:
        "./Tactical/Tactical_upset.PNG"
        zoom 1.2
    image t wave:
        "./Tactical/Tactical_wave.PNG"
        zoom 1.2
        xanchor .12
    image c smile:
        "./CoreJJ/CoreJJ_smile.PNG"
        zoom 1.2
        xanchor .12
    image c smile2:
        "./CoreJJ/CoreJJ_smile2.PNG"
        zoom 1.2
        xanchor .12
    image c talk:
        "./CoreJJ/CoreJJ_talk.PNG"
        zoom 1.2
        xanchor .12
    image c upset:
        "./CoreJJ/CoreJJ_upset.PNG"
        zoom 1.2
        xanchor .12
    image c wave:
        "./CoreJJ/CoreJJ_wave.PNG"
        zoom 1.2
        xanchor .12

# Create stats for the player
define pov = Character("[povname]", who_color="f77f00")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show n
    # These display lines of dialogue.
    n "Congratulations! You're accepted to the Team Liquid Bootcamp!
        Before you meet the team members, we will like to know you a little better. Please answer the following questions truthfully and honestly"

    # application screen
    python: 
        povname = renpy.input("Do you mind telling me your name?")
        povname = povname.strip()

        name_flag = True
        if not povname:
            povname = "Beanbag"
            name_flag = False

    if provided_name:
        n "Oh I see! Welcome to Team Liquid, [povname]! You will have a great time here"
    else:
        n "Okay Mr. Mysterious man. Since you didn't give us a name, I am just going to call you [povname]. Got it?"
        pov "Uhh... okay."
    
    

    n "Thank you. Now that we have you information, we can set you up in your room.
        But before that, I must ask how do you feel after quarantining for 2 weeks?"
    menu:
        "I’m fine, I just have a bit of trouble breathing.":
            "You have COVID-19." # (Your health goes down/ you have COVID)
        "My head is clear and the air has never smelled better.":
            "You're healthy."
        "You know just coughing up blood, the usual.":
            "You're dying." #(Death)
        "Eh, same as always.":
            "You're fine." # (Fine)
        "I’m not telling. Why do you wanna know?!":
            "You're mean." # (RNG health?)

    show i smile2:
        xpos 0
    show b smile2:
        xpos .2
    show j upset:
        xpos .4
    show t talk:
        xpos .6
    show c wave:
        xpos .8
    n "Here's the team! Introduce your self by clicking on them!"
    hide i
    hide b
    hide j
    hide t
    hide c
    n "Meeting people can be exhausting, why don’t you rest up and I’ll get you tomorrow."
    menu:
        "Stay up a bit longer.":
            "You choose to stay up longer." # health goes down
        "Go to bed now.":
            "Blue is right. I'm pooped."



return # This ends the game.
