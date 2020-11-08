label day_start:
    scene map with Fade(1.0, 0, 1.0)
    show n
    $ day_start = True
    if health <= 0:
        jump end_scene
    $ curr_stamina = max_stamina - (sleep_late * 5)
    $ sleep_late = 0
    n "Welcome to your [day_num] day of bootcamp! Here are some things you can choose to do:"
    if curr_stamina != max_stamina or sleep_late != 0:
        n "Looks like someone went to bed late and isn't fully energized!"

label boot_camp:
    if not day_start:
        scene map
        show n
    else:
        $ day_start = False

    if health <= 0:
        jump end_scene
    if curr_stamina <= 0:
        jump dayEnd

    n "Current stats: "
    n " Gameplay: [gameplay_level] \n
           Health: [health] \n
           Stamina: [curr_stamina]/[max_stamina]"
    menu:

        "Go to the gym (15)" if curr_stamina >= 15:
            scene gym
            if health >= 10 and max_stamina >= 30:
                pov "I can see my muscles swell! I am strong!"
            else:
                pov "Lets try to bench a plate today! {i} struggle {/i} Actually, let's just try the bar ..."

            show b smile
            b "Keep up the good work!"
            b "You will be strong like me in no time!"
            b "{i} Flexes muscles and leaves {/i}"
            hide b

            "You hanged out with Broxah! Looks like your friendship increased a little."
            $ friendship["broxah"] = friendship["broxah"] + 1


            "Working out increased your total stamina by 10 and health by 5! Keep it up!"
            $ max_stamina += 10
            $ health += 5

            $ curr_stamina -= 15
            jump boot_camp


        "Cook a healthy meal (5)" if curr_stamina >= 5:
            scene cook
            pov "Mmmmmh, my spaghetti smells sooooo good!"

            show j smile
            j "That looks so good! Mind if I try some? "
            pov "Of course! Lets eat together!"
            j "Wow! I love your cooking. I will be back for more!"
            hide j

            "You fed Jensen some food! He seems to admire you a little now."
            $ friendship["jensen"] = friendship["jensen"] + 1

            "You are what you eat! Your health increases by 10."
            $ health = health + 10
            $ curr_stamina -= 5

            jump boot_camp

        "Eat McDonalds (5) " if curr_stamina >= 5:
            scene eat_out
            pov "Um, I will like to order 2 Big Macs, 30 Chicken nuggets, and one large icecream please."

            "Yuck! All those greasy fast food in your stomach. That can not be good for you! Your health decrease by 5."
            $ health = health - 10

            pov "Oh no, I think I want to throw up..."
            pov "At least I got the new happy meal toy..."
            jump boot_camp

        "Training Tool (10) " if curr_stamina >= 10:
            scene practice
            if gameplay_level < 20:
                pov "Yep, just practicing some of my garen mechanics."
            else:
                pov "Okay, how exactly do I do the Shy combo?"

            show i smile
            i "Look at you go! Practicing the fundamentals..."
            i "I like those top lane picks! Let me give you some tips ..."
            pov "Whoa thanks a lot dude!"

            hide i
            "You learn alot and increased your friendship with Impact."
            "Gameplay went up by a 10 points!"
            $ gameplay_level += 10
            $ friendship["impact"] = friendship["impact"] + 1
            $ curr_stamina -= 10
            jump boot_camp

        "Duo with Tactical (10)" if curr_stamina >= 10:
            scene practice
            pov "Tactical can you show me the rope please?"
            show t smile
            t "Of course! I will show you some neat tricks bot lane"
            t "Remember to ward dragon!"
            hide t
            "You learned a lot and hanging out with tactical incrases your relationship with him!"
            $ gameplay_level = gameplay_level + 10
            $friendship["tactical"] = friendship["tactical"] + 1
            $curr_stamina -= 10
            jump boot_camp

        "Rewatch VOD (10)" if curr_stamina >= 10:
            scene practice
            pov "Watching gameplay review myself in the end isn't too bad ..."
            $ gameplay_level = gameplay_level + 1
            $ curr_stamina -= 10
            jump boot_camp

        "Duo with CoreJJ (10) " if curr_stamina >= 10:
            scene practice
            pov "CoreJJ can you show me the rope please?"
            show c smile
            c "Of course! I will show you some neat tricks bot lane."
            c "Remember to ward dragon!"
            hide c
            "You learned a lot and hanging out with tactical incrases your relationship with him!"
            $ gameplay_level = gameplay_level + 10
            $ friendship["corejj"] = friendship["corejj"] + 1
            $ curr_stamina -= 10
            jump boot_camp

        "I'm done for the day":
            if curr_stamina > 5:
                pov "I just want to be lazy for a day..."
            else:
                pov "Today was a really productive day!"
            jump dayEnd




    label dayEnd:
        n "Whew, what a long day of hard work! You are all out of juice! Go rest up and come back tomorrow stronger!"
        menu:
            "I think I'll stay up for a bit longer.":
                pov "Hell yes! I love watching random youtube videos!"
                $ sleep_late += 1

            "Sounds good, thank you Blue!":
                pov "ZZZ ZZZ ZZZ"

        $ day_num = day_num + 1
        if day_num == 5:
            jump end_scene
        else:
            jump day_start
