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

# what day it is
define day_num = 1
define day_start = True
define sleep_late = 0
# User stats
define name = ""
define status = ""
define nationality = ""
define birthday = ""
define game = ""
define friendship = {
        "impact": 0,
        "broxah": 0,
        "jensen": 0,
        "tactical": 0,
        "corejj": 0
    }

#Randomly generated userstats
define gameplay_level = 0
define health = 0
define curr_stamina = 0
define max_stamina = 0

# Create stats for the player
define pov = Character("[name]", who_color="f77f00")

# The game starts here.

label start:
    scene welcome
    show n
    n "Congratulations! You're accepted to the Team Liquid Bootcamp!
        Before you meet the team members, we will like to know you a little better. Please answer the following questions truthfully and honestly."
    # application screen
    label ask_name:
        python:
            name = renpy.input("What is your name?")
            name = name.strip()

        if not name:
            n "Hmm. Sorry, I didn't quite catch that. Can you repeat yourself one more time?"
            jump ask_name

    n "Nice to meet you [name]. We are glad to have you here!"

    label ask_status:
        python:
            status = renpy.input("What is your current career status? (unemployed/active/retired)")
            status = status.strip()

        if not status or status not in ['unemployed', 'active' , 'retired']:
            n "Sorry, that is not a valid answer for status. Please read carefully and fill it out again."
            jump ask_status
        else:
            n "So you are currently [status]. Sounds good!"

    label ask_nationality:
        python:
            nationality = renpy.input("Which country do you hail from?")
            nationality = nationality.strip()

        if not nationality:
            n "You can't leave this spot blank! Please just fill it out."
            jump ask_nationality
        else:
            n "Oh, so you are from [nationality]. That's pretty cool!"

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
            n "Your formatting is a little weird... Try again."
            jump ask_birthday
        else:
            n "I see! Your birthday is on [birthday]! Hang in there we are almost done!"

    label ask_game:
        python:
            game = "League of Legends"
        n "Hmm. The file says you are here applying for the {b}[game]{/b} team! Cool beans! Lets go and do a quick
        checkup before we meet the team members."

    label generate_stat:
        n "Beep Boop Beep. Checking your skill, health, and stamina..."
        python:
            import random

            gameplay_level = random.randrange(10,50,1)
            health = random.randrange(10,50,5)
            max_stamina = random.randrange(20,50,5)
            total = gameplay_level +  health + max_stamina
        n "Your stats are back! Let's take a look at them."
        n " Gameplay: [gameplay_level] \n
           Health: [health] \n
           Stamina: [max_stamina]"

        if total < 75:
            n "A bit low, but I am sure you can do better in a couple of days!"
        else:
            n "Some pretty decent scores if I do say so myself!"

    label ask_covid:
        n "One last step before we meet the team members! How did your 2 week quarantine go?"

        menu:
            "I’m fine, I just have a bit of trouble breathing.":
                n "You have might have COVID-19. It will surely take a toll on your health." # (Your health goes down/ you have COVID)
                $ health -= 5
            "My head is clear and the air has never smelled better.":
                n "It must have been stuffy where you were, huh? Glad to hear you're healthy though!"
            "You know just coughing up blood, the usual.":
                n "Sir, please leave the house right now." #(Death)
                $ health = -1
                jump end_scene
            "Eh, same as always.":
                n "Glad to hear you're doing alright." # (Fine)

    n "Thank you for the information! Now, it's time to meet the team!"
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
    hide b
    hide j
    hide t
    hide c
    show n at left
    show i wave at right
    i "Hey, I'm Impact, the Team Liquid's top laner. Good to meet you and good luck! I hope to see you around."
    hide i
    show b wave at right
    b "I'm Broxah, the jungler for Team Liquid. Welcome to the bootcamp, I'm sure you're going to love it here!"
    hide b
    show j wave at right
    j "Hello. I'm Jensen. I'm the mid laner for Team Liquid. Congratulations on making it to the bootcamp!"
    hide j
    show t wave at right
    t "I'm Tactical. I am the adc for bot lane on Team Liquid. Great to finally meet you. I've heard great things about you."
    hide t
    show c wave at right
    c "Hello, I'm CoreJJ. I'm the support laner on Team Liquid. It's very nice to meet you! I can't wait to play together!"
    hide c
    hide n
    show n
    n "Meeting people can be exhausting, why don’t you rest up and I’ll get you tomorrow."
    menu:
        "Stay up a bit longer.":
            pov "yes! People building mud huts from scratch! I love youtube!"

            $ health -= 5
            $ sleep_late += 1
        "Go to bed now.":
            pov "Blue is right. I'm pooped."

    $ day_num += 1
    jump day_start
