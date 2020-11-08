label boot_camp:
    scene Welcome with fade
    show n
    n "Welcome to your second day of bootcamp! Here are some things you can choose to do:"

    menu:
        "Go to the gym":
            scene Gym
            "You work out for a bit in the team house gym."
            python:
                stamina = stamina + 10
        "Go on a Run":
            scene Run
            "You go on a run around the neighbourhood." #stamina +???
        "Cook a healthy meal":
            scene Cook
            "You buy some fresh ingredients and cook a healthy meal." #health +???
        "Eat McDonalds":
            scene Eat Out
            "You have a cheat day and go buy a Big Mac." #health-???, stamina +????
        "Scrim":
            scene Practice
            "You sit in on a scrim with the current team members." #+gameplay
        "Practice laning":
            scene Practice
            "You practice your laning in game." #+gameplay & tactical corejj
        "Rewatch VOD":
            scene Practice
            "You watch a VOD of the team playing." #+gameplay
        "Practice with Impact":
            scene Practice
            show i smile
            "You duoqueue with Impact." #+gameplay & impact
        "Practice with Broxah":
            scene Practice
            show b smile
            "You duoqueue with Broxah." #+gameplay & broxah
        "Practice with Jensen":
            scene Practice
            show j smile
            "You duoqueue with Jensen." #+gameplay & jensen
        "Practice with Tactical":
            scene Practice
            show t smile
            "You duoqueue with Tactical." #+gameplay & tactical
        "Practice with CoreJJ":
            scene Practice
            show c smile
            "You duoqueue with CoreJJ." #+gameplay & corejj
        "I'm done for the day":
            jump dayEnd


    if stamina == 0:
        jump dayEnd

    label dayEnd:
        n "Whew, what a long day of hard work! Go rest up and come back tomorrow stronger!"
        menu:
            "I think I'll stay up for a bit longer.":
                "You stay up longer and feel worse." #-health
            "Sounds good, thank you Blue!":
                "You go to bed, ready for another day of bootcamp."



    # This ends the game.

    return
