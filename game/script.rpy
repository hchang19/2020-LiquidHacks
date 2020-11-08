# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#defining scenes
image welcome = "./scenes/Welcome.PNG"
image cook = "./scenes/Cook.PNG"
image eat_out = "./scenes/Eat Out.PNG"
image gym = "./scenes/Gym.PNG"
image practice = "./scenes/Practice.PNG"
image run = "./scenes/Run.PNG"
image map = "Map.PNG"

# defining characters
define n = Character("Blue", who_color="#0f447a") # n for narrator
define i = Character("Impact", who_color="#e5ff32")
define b = Character("Broxah", who_color="32dcff")
define j = Character("Jensen", who_color="7d32ff")
define t = Character("Tactical", who_color="ff3255")
define c = Character("CoreJJ", who_color="ff32b4")

# User stats
define name = ""
define status = ""
define nationality = ""
define birthday = ""
define game = ""
define friendship = [0, 0, 0, 0, 0]
define gameplay_level = 0
define health = 0
define stamina = 0

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



# The game starts here.

label start:

    scene welcome
    show n

    n "Congratulations! You're accepted to the Team Liquid Bootcamp!
        Please fill out this form to finalize your information."
    # application screen

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
    jump teamIntroduction

    label teamIntroduction:
        show i smile2:
            xpos 0
        show b smile:
            xpos .2
        show j smile:
            xpos .4
        show t smile2:
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
