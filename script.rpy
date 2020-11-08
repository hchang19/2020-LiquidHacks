# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Blue") # n for narrator
define i = Character("Impact")
define b = Character("Broxah")
define j = Character("Jensen")
define t = Character("Tactical")
define c = Character("CoreJJ")

# Linking images
image b smile = "Broxah_smile.PNG"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show n happy
    show b smile at left:
        zoom 1.2


    # These display lines of dialogue.

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

    n "Here's the team! Introduce your self by clicking on them!"

    n "Meeting people can be exhausting, why don’t you rest up and I’ll get you tomorrow."
menu:
    "Stay up a bit longer.":
        "You choose to stay up longer." # health goes down
    "Go to bed now.":
        "Blue is right. I'm pooped."
    # This ends the game.

return
