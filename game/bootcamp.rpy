label boot_camp:
    scene map with Fade(1.0, 0, 1.0)
    show n
    n "Welcome to your second day of bootcamp! Here are some things you can choose to do:"

    menu:
        "Go to the gym":
            scene gym
            "You work out for a bit in the team house gym."
            python:
                stamina = stamina + 10
        "Go on a Run":
            scene run
            "You go on a run around the neighbourhood."
            python:
                stamina = stamina + 10  #stamina +???
        "Cook a healthy meal":
            scene cook
            "You buy some fresh ingredients and cook a healthy meal."
            python:
                health = health + 10 #health +???
        "Eat McDonalds":
            scene eat_out
            "You have a cheat day and go buy a Big Mac."
            python:
                health = health - 10 #health-???, stamina +????
        "Scrim":
            scene practice
            "You sit in on a scrim with the current team members."
            python:
                gameplay_level = gameplay_level + 10  #+gameplay
        "Practice laning":
            scene practice
            "You practice your laning in game."
            python:
                gameplay_level = gameplay_level + 10
                friendship["tactical"] = friendship["tactical"] + 10
                friendship["corejj"] = friendship["corejj"] + 10   #+gameplay & tactical corejj
        "Rewatch VOD":
            scene practice
            "You watch a VOD of the team playing."
            python:
                gameplay_level = gameplay_level + 10  #+gameplay
        "Practice with Impact":
            scene practice
            show i smile
            "You duoqueue with Impact."
            python:
                gameplay_level = gameplay_level + 10
                friendship["impact"] = friendship["impact"] + 10   #+gameplay & impact
        "Practice with Broxah":
            scene practice
            show b smile
            "You duoqueue with Broxah."
            python:
                gameplay_level = gameplay_level + 10
                friendship["broxah"] = friendship["broxah"] + 10   #+gameplay & broxah
        "Practice with Jensen":
            scene practice
            show j smile
            "You duoqueue with Jensen."
            python:
                gameplay_level = gameplay_level + 10
                friendship["jensen"] = friendship["jensen"] + 10   #+gameplay & jensen
        "Practice with Tactical":
            scene practice
            show t smile
            "You duoqueue with Tactical."
            python:
                gameplay_level = gameplay_level + 10
                friendship["tactical"] = friendship["tactical"] + 10  #+gameplay & tactical
        "Practice with CoreJJ":
            scene practice
            show c smile
            "You duoqueue with CoreJJ."
            python:
                gameplay_level = gameplay_level + 10
                friendship["corejj"] = friendship["corejj"] + 10 #+gameplay & corejj
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
        python:
            day_num = day_num + 1
        if day_num == 5:
            jump end_scene
        else:
            jump boot_camp
