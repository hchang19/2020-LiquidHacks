label end_scene:
    define voucher = ""
    define maxFriendship = 0
    define onTeam = True
    define fail = True
    scene welcome
    show n
    if healh < 1:
        jump death
    python:
        voucher = "corejj"
        health = 40
    jump alternate_ending_corejj
    python:
        for x in friendship:
            if friendship[x] > 0:
                fail = False
            if friendship[x] < 5:
                onTeam = False
            if friendship[x] > maxFriendship:
                voucher = x
    if onTeam == True:
        jump main_ending
    elif fail == False:
        python:
            voucher = "tactical"
        if voucher == "broxah":
            jump alternate_ending_broxah
        elif voucher == "impact":
            jump alternate_ending_impact
        elif voucher == "jensen":
            jump alternate_ending_jensen
        elif voucher == "corejj":
            jump alternate_ending_corejj
        else:
            jump alternate_ending_tactical
    else:
        jump failed_ending

    label main_ending:
        scene welcome
        show i smile2:
            xpos 0
        show b smile2:
            xpos .2
        show j smile2:
            xpos .4
        show t smile2:
            xpos .6
        show c smile2:
            xpos .8
        show n
        show flowers
        n "Congratulations on making it to the team! What are you standing there for?? Let's scrim!"
        jump credits

label alternate_ending_impact:
    scene welcome
    show i smile2:
        xpos 0
    show b smile2:
        xpos .2
    show j smile2:
        xpos .4
    show t smile2:
        xpos .6
    show c smile2:
        xpos .8
    show n
    n "I’m sorry, you weren’t quite what we were looking for-"
    show welcome with vpunch
    hide i
    hide b
    hide j
    hide t
    hide c
    show i talk at left
    show angry at left:
        zoom 1.2
    show n at right
    i "Wait a minute! [name] has so much potential! You have to reconsider this instant!"
    if health >= 30:
        hide angry
        show sparkles at left:
            zoom 1.2
        n "You’re right! How could I have overlooked [name]’s gameplay?! [name], forgive me! Welcome to the team, let’s scrim!"
    else:
        hide angry
        show i upset at left
        show tear at left:
            zoom 1.2
        n "No, I’m sorry, but there it would take too long to refine [name]'s skill. Try again next time and I’m sure you can make it!"
        hide tear
        hide n
        show i at center
        show blush at center:
            zoom 1.2
        i "I'm sorry you didn't make it. If you'd like, I'd love to be your mentor!"
    jump credits

    label alternate_ending_jensen:
        scene welcome
        show i smile2:
            xpos 0
        show b smile2:
            xpos .2
        show j smile2:
            xpos .4
        show t smile2:
            xpos .6
        show c smile2:
            xpos .8
        show n
        n "I’m sorry, you weren’t quite what we were looking for-"
        show welcome with vpunch
        hide i
        hide b
        hide j
        hide t
        hide c
        show j talk at left
        show angry at left:
            zoom 1.2
        show n at right
        j "Wait a minute! [name] has so much potential! You have to reconsider this instant!"
        if health >= 30:
            hide angry
            show sparkles at left:
                zoom 1.2
            n "You’re right! How could I have overlooked [name]’s gameplay?! [name], forgive me! Welcome to the team, let’s scrim!"
        else:
            hide angry
            show j upset at left
            show tear at left:
                zoom 1.2
            n "No, I’m sorry, but there it would take too long to refine [name]'s skill. Try again next time and I’m sure you can make it!"
            hide tear
            hide n
            show j at center
            show blush at center:
                zoom 1.2
            j "I'm sorry you didn't make it. If you'd like, I'd love to be cooking buddies!"
        jump credits

    label alternate_ending_tactical:
        scene welcome
        show i smile2:
            xpos 0
        show b smile2:
            xpos .2
        show j smile2:
            xpos .4
        show t smile2:
            xpos .6
        show c smile2:
            xpos .8
        show n
        n "I’m sorry, you weren’t quite what we were looking for-"
        show welcome with vpunch
        hide i
        hide b
        hide j
        hide t
        hide c
        show t talk at left
        show angry at left:
            zoom 1.2
        show n at right
        t "Wait a minute! [name] has so much potential! You have to reconsider this instant!"
        if health >= 30:
            hide angry
            show sparkles at left:
                zoom 1.2
            n "You’re right! How could I have overlooked [name]’s gameplay?! [name], forgive me! Welcome to the team, let’s scrim!"
        else:
            hide angry
            show t upset at left
            show tear at left:
                zoom 1.2
            n "No, I’m sorry, but there it would take too long to refine [name]'s skill. Try again next time and I’m sure you can make it!"
            hide tear
            hide n
            show t at center
            show blush at center:
                zoom 1.2
            t "I'm sorry you didn't make it. If you'd like, I'd love to be your duo partner!"
        jump credits

    label alternate_ending_corejj:
        scene welcome
        show i smile2:
            xpos 0
        show b smile2:
            xpos .2
        show j smile2:
            xpos .4
        show t smile2:
            xpos .6
        show c smile2:
            xpos .8
        show n
        n "I’m sorry, you weren’t quite what we were looking for-"
        show welcome with vpunch
        hide i
        hide b
        hide j
        hide t
        hide c
        show c talk at left
        show angry at left:
            zoom 1.2
        show n at right
        c "Wait a minute! [name] has so much potential! You have to reconsider this instant!"
        if health >= 30:
            hide angry
            show sparkles at left:
                zoom 1.2
            n "You’re right! How could I have overlooked [name]’s gameplay?! [name], forgive me! Welcome to the team, let’s scrim!"
        else:
            hide angry
            show c upset at left
            show tear at left:
                zoom 1.2
            n "No, I’m sorry, but there it would take too long to refine [name]'s skill. Try again next time and I’m sure you can make it!"
            hide tear
            hide n
            show c at center
            show blush at center:
                zoom 1.2
            c "I'm sorry you didn't make it. If you'd like, I'd love to be your support!"
        jump credits

    label alternate_ending_broxah:
        scene welcome
        show i smile2:
            xpos 0
        show b smile2:
            xpos .2
        show j smile2:
            xpos .4
        show t smile2:
            xpos .6
        show c smile2:
            xpos .8
        show n
        n "I’m sorry, you weren’t quite what we were looking for-"
        show welcome with vpunch
        hide i
        hide b
        hide j
        hide t
        hide c
        show b talk at left
        show angry at left:
            zoom 1.2
        show n at right
        b "Wait a minute! [name] has so much potential! You have to reconsider this instant!"
        if health >= 30:
            hide angry
            show sparkles at left:
                zoom 1.2
            n "You’re right! How could I have overlooked [name]’s gameplay?! [name], forgive me! Welcome to the team, let’s scrim!"
        else:
            hide angry
            show b at left
            show tear at left:
                zoom 1.2
            n "No, I’m sorry, but there it would take too long to refine [name]'s skill. Try again next time and I’m sure you can make it!"
            hide tear
            hide n
            show b at center
            show blush at center:
                zoom 1.2
            b "I'm sorry you didn't make it. If you'd like, I'd love to be your gym buddy!"
        jump credits

    label failed_ending:
        scene welcome
        show n
        n "I'm sorry, you weren’t quite what we were looking for. Why don’t you try again next time?"
        jump credits

    label death:
        show n
        n "You died. Take better care of yourself next time."

    label credits:
        hide t
        hide i
        hide c
        hide j
        hide b
        hide tear
        hide blush
        hide angry
        show n at center
        show flowers at center:
            zoom 1.2
        "The end."
        "This was made by Henry Chang, Long Lin, Kate Land, and Nicole Guan. Art my Nicole Guan. Thank you for playing!"
        return
