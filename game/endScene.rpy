label end_scene:
    define voucher = ""
    define maxFriendship = 0
    define onTeam = True
    define fail = True
    scene welcome
    show n

    python:
        for x in friendship:
            if friendship[x] > 0:
                fail = False
            if friendship[x] < 5:
                onTeam = False
            if friendship[x] > maxFriendship:
                voucher = x
    if onTeam = True:
        jump main_ending
    elif fail = False:
        jump alternate_ending
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

    label alternate_ending:

    label failed_ending:

    label credits:
        show n
        show flowers
        "This was made by Henry Chang, Long Lin, Kate Land, and Nicole Guan. Art my Nicole Guan. Thank you for playing!"
        return
