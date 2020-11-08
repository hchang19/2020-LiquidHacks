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

#Randomly generated userstats
define gameplay_level = 0
define health = 0
define stamina = 0

# Create stats for the player
define pov = Character("[name]", who_color="f77f00")

# The game starts here.

label start:

    scene welcome
    show n
    n "Congratulations! You're accepted to the Team Liquid Bootcamp!
        Before you meet the team members, we will like to know you a little better. Please answer the following questions truthfully and honestly"

    # REMOVE THIS
    jump load_team_info

    # application screen
    label ask_name:
        python:
            name = renpy.input("What is your name?")
            name = name.strip()

        if not name:
            n "Hmm. Sorry, I didn't quite catch that. Can you repeat yourself one more time?"
            jump ask_name
    
    n "Nice to meet you [name]. Just a few more questions to go!"

    label ask_status:
        python:
            status = renpy.input("What is your current career status? (unemployed/active/retired)")
            status = status.strip()

        if not status or status not in ['unemployed', 'active' , 'retired']:
            n "Sorry, that is not a valid answer for status. Please read carefully and fill it out again"
            jump ask_status
        else:
            n "so you are currently [status]. Sounds good!"
    
    label ask_nationality:
        python:
            nationality = renpy.input("Which country do you hail from?")
            nationality = nationality.strip()

        if not nationality:
            n "You can't leave this spot blank! Please just fill it out."
            jump ask_nationality
        else:
            n "Oh, so you are from [nationality]"

    label ask_birthday:
        python:
            import datetime
            birthday = renpy.input("What is your birthday? (YYYY-MM-DD)")

            try:
                birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d')
                birthday = birthday.strftime("%b %d, %Y")
            except ValueError:
                birthday = None
        if not birthday:
            n "Your formatting is a little weird... Try again"
            jump ask_birthday
        else:
            n "I see! Your birthday is on [birthday]! Hang in there we are almost done!"
                
    label ask_game:
        python:
            game = "League of Legends"
        n "Hmm. The file says you are here applying for the {b}[game]{/b} team! Cool beans! Lets go and do a quick
        checkup before we meet the team members"

    label generate_stat:
        n "Beep Boop Beep. Checking your skill, health, and stamina..."
        python:
            import random

            gameplay_level = random.randrange(10,50,1)
            health = random.randrange(10,50,5)
            stamina = random.randrange(10,50,5)
            total = gameplay_level +  health + stamina
        n "Your stats are back! Let's take a look at them."
        n " Gameplay: [gameplay_level] \n
           Health: [health] \n
           Stamina: [stamina]"

        if total < 75:
            n "A bit low, but I am sure you can do better in a couple of days!"
        else:
            n "Some pretty decent scores if I do say so myself!"
    label ask_covid:
        n "One last step before we meet the team members! How did your 2 week quarantine go?"
        
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
