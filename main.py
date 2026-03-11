# D&D Game

import random

player_alive = True

while player_alive:
    print("Welcome to the Dungeons & Dragons game!")
    # set game difficulty
    while True:
        difficulty = input("Enter your difficulty (Easy / Hard): ").upper()
        if difficulty == "EASY":
            break
        elif difficulty == "HARD":
            break
        else:
            print("Invalid option. Try again.")

    # player chooses their class
    player_character = input("Choose your character type (Knight, Mage, Ninja, Prince): ").upper()

    # initiliaze player stats
    # 1: Strength, 2: Speed, 3: Dexterity, 4: Charisma, 5: Endurance, 6: Arcane, 7: Intelligence, 8: Evasiveness, 9: Luck
    player_stats = [0, 0, 0, 0 ,0, 0, 0, 0, 0]

    # initiliaze players currency amount
    player_gold = 0

    # initiliaze players health amount
    player_hp = 100

    # player classes
    class_unchosen = True
    while class_unchosen:
        # Knight is Strong, Endurant, and Evasive.
        if player_character == "KNIGHT":
            player_stats[0:] = [18, 7, 9, 6, 17, 3, 8, 8, 6]
            class_unchosen = False
        # Mage is intelligent, charismatic, dexteric and skilled in arcane.
        elif player_character == "MAGE":
            player_stats[0:] = [4, 6, 16, 7, 6, 18, 17, 7, 6]
            class_unchosen = False
        # Ninja is fast, dexteric, evasive.
        elif player_character == "NINJA":
            player_stats[0:] = [13, 18, 17, 9, 7, 2, 12, 15, 6]
            class_unchosen = False
        # Prince is charismatic, intelligent and fast.
        elif player_character == "PRINCE":
            player_stats[0:] = [7, 17, 8, 19, 6, 0, 19, 4, 10]
            player_gold = 350
            class_unchosen = False
        else:
            print("This is not an available class, please choose again.")
            player_character = input("Choose your character type (Knight, Mage, Ninja, Prince): ").upper()
        
    # Display player class and their assigned stats
    def player_stat_info():    
        print()
        print("Class:", player_character.capitalize())
        print("Health:", player_hp,"/ 100")
        print("Gold:", player_gold)
        print("------------------")
        print("       Stats      ")
        print("------------------")
        print(f"Strength: {player_stats[0]}")
        print(f"Speed: {player_stats[1]}")
        print(f"Dexterity: {player_stats[2]}")
        print(f"Charisma: {player_stats[3]}")
        print(f"Endurance: {player_stats[4]}")
        print(f"Arcane: {player_stats[5]}")
        print(f"Intelligence: {player_stats[6]}")
        print(f"Evasiveness: {player_stats[7]}")
        print(f"Luck: {player_stats[8]}")
        print()
    player_stat_info()

    # initiliaze the players first confirmation
    confirm1 = True

    print(f"You are a {player_character.capitalize()} in the Kingdom of New Ross.")
    print(f"The King's daughter has been kidnapped and it's your job to find her and return her to the kingdom.") 

    # runs while players choice hasn't been selected or correctly input
    while confirm1:
        confirm1_input = input("Do you understand your job? (Y / N) ").upper()
        if confirm1_input == "N":
            print("Too bad, onwards soldier!")
            break
        elif confirm1_input == "Y":
            print("Fantastic, onwards soldier!")
            break
        else:
            confirm1_input = input("I'm afraid you mispoke... try again. (Y / N)").upper()

    # initiliaze availabe environments for choice one
    choice1_environments = ["Forest", "Desert", "Mushroom Kingdom", "Forest", "Desert", "Swamp", "Cave"]

    print()
    print("On your voluntary journey to save the King's daughter, you encounter a split in the roads...")

    # initiliaze players first impactful game choice
    choice1 = True

    while choice1:
        while True:
            choice1_input = input("Which way do you go? (L / R): ").upper()
            if choice1_input == "L":
                environment1 = random.choice(choice1_environments[0:2])
                print(f"You take the left path and enter: {environment1}")
                break
            elif choice1_input == "R":
                environment1 = random.choice(choice1_environments[2:])
                print(f"You take the right path and enter: {environment1}")
                break
        
        if environment1 == "Mushroom Kingdom":
            print()
            print("Oh no! it seems you've walked right into the Mushroom Kingdom uninvited...")
            print("and your wanted for stealing all of their renowned mushroom bread!")
            print("You encounter King Toadstool and he wants you executed! What will you do?!")
            
            mk_choice_running = True
            while mk_choice_running:
                player_stat_info()
                mk_choice = input("(Attack, Persuade, Run, or.. Seduce?) ").upper()
                if mk_choice in ("ATTACK", "PERSUADE", "RUN", "SEDUCE"):
                    mk_choice_running = False
                else:
                    print("Invalid Option. Try again.")

            if mk_choice == "ATTACK":
                if player_stats[0] >= random.randint(0, 16):
                    print("You killed King Toadstool!.. but his soldiers executed you on the spot.")
                    print("Game Over!")
                    player_alive = False
                    choice1 = False
                else:
                    print("You missed! and died of embarrasment...")
                    print("Game Over!")
                    player_alive = False
                    choice1 = False
            elif mk_choice == "PERSUADE":
                if player_stats[3] >= random.randint(0, 10):
                    if difficulty == "HARD":
                        goldgiven_mk = random.randint(250, 501) * 2
                    else:
                        goldgiven_mk = random.randint(250, 501)
                    player_gold += goldgiven_mk
                    choice1_environments.pop(2)

                    print("You succesfully persuaded the King with your charisma, claiming you'll")
                    print("return the bread with a small loan of gold from the King!")
                    print()
                    print(f"The King gives you {goldgiven_mk} gold and sends you on your way!")
                    print(f"You now have {player_gold} gold!")
                else:
                    print("You stuttered and the King laughed in your face...")
                    print("and you died of embarrasment...")
                    print()
                    print("Game Over!")
                    player_alive = False
                    choice1 = False 
            elif mk_choice == "RUN":
                if player_stats[7] >= random.randint(5, 16):
                    print("You succesfully run away and escape the Kingdom!...")
                    print("leaving the King embarrased and ashamed for his lack of containment... ")
                    print()
                    print("You return to the split in the path...")
                else:
                    print("You trip and fall while trying to run...")
                    print("The King's guards arrest you and you spend the rest of your life in a cell... embarrasing.")
                    print()
                    print("Game Over!")
                    player_alive = False
                    choice1 = False
            elif mk_choice == "SEDUCE":
                print("You attempt to seduce the King... ")
                print("and it works! You spend the rest of your life as the King's servant, happily ever after!")
                print()
                print("Game Over!")
                player_alive = False
                choice1 = False

            else:
                print("Not a valid choice. Try again.")

        elif environment1 == "Forest":
            print()
            print("You took a cut in the path and have gotten lost in the forest...")
            print("while trying to find a way out.. you encounter a Wild Black Bear! What will you do?")
            print()

            if difficulty == "HARD":
                black_bear_hp = 400
                black_bear_hpmax = 400
            else:
                black_bear_hp = 200
                black_bear_hpmax = 200

            black_bear_fight = True

            while black_bear_fight:

                fr_choice_running = True
                print(f"Black Bear HP: {black_bear_hp}/{black_bear_hpmax}")
                while fr_choice_running:
                    player_stat_info()
                    fr_choice = input("(Attack, Persuade, Run, or.. Seduce?): ").upper()
                    if fr_choice in ("ATTACK", "PERSUADE", "RUN", "SEDUCE"):
                        fr_choice_running = False
                    else:
                        print("Invalid Option. Try again.")
                        pass
                
                if fr_choice == "ATTACK":
                    if player_stats[0] >= random.randint(5,15):
                        dmg_bb = random.randint(0, 101)
                        print(f"You dealt {dmg_bb} damage to the bear!")
                        black_bear_hp -= dmg_bb
                        if black_bear_hp <= 0:
                            print("You defeated the Wild Black Bear!")
                            black_bear_fight = False
                            choice1 = False
                            if difficulty == "HARD":
                                player_gold += random.randint(0, 201) * 2
                            else:
                                player_gold += random.randint(0, 201)
                            print(f"You now have {player_gold} gold!")

                    else:
                        dmg_player_bb = random.randint(0, 101)
                        print(f"You missed! and the bear dealt {dmg_player_bb} to you!")
                        player_hp -= dmg_player_bb
                        if player_hp <= 0:
                            print("The Wild Black Bear defeated you!")
                            print("Game Over!")
                            black_bear_fight = False
                            choice1 = False
                            player_alive = False
                elif fr_choice == "PERSUADE":
                    if player_stats[3] >= random.randint(5, 16) and player_stats[6] >= random.randint(5, 16):
                        print("You succesfully communicated with the bear in 'bear' language...")
                        print("the bear understood you were just a mere traveller and let you pass...")
                        player_stat_info()
                        print()
                        black_bear_fight = False
                        choice1 = False
                elif fr_choice == "RUN":
                    if player_stats[7] >= random.randint(0, 11):
                        black_bear_fight = False
                        choice1 = False
                        print("You successfully evaded the bear and ran away!")
                        player_stat_info()
                        print()
                    else:
                        print("You tried to evade the Wild Black Bear, instead you jumped right into his mouth..")
                        print("..maybe next time.")
                        print()
                        print("Game Over!")
                        player_stat_info()
                        black_bear_fight = False
                        choice1 = False
                        player_alive = False
                elif fr_choice == "SEDUCE":
                    print("You attempted to seduce the Wild Black Bear and in return...")
                    print("the Wild Black Bear ate you... nice try... i guess...")
                    print()
                    print("Game Over!")
                    player_stat_info()
                    black_bear_fight = False
                    choice1 = False
                    player_alive = False
        
        elif environment1 == "Desert":
            print()
            print("You crossed a hill, and proceeded to swim an ocean, now you're in the middle of the desert...")
            print("while in the desert, you encounter a Lion! What do you do?")

            boss_health = [400, 500, 600, 700]

            if difficulty == "HARD":
                desert_boss_hp = random.choice(boss_health)
                desert_boss_hpmax = desert_boss_hp
            else:
                desert_boss_hp = 200
                desert_boss_hpmax = 200

            while True:
                print()
                print(f"Lion's Health: {desert_boss_hp}/{desert_boss_hpmax}")
                while True:
                    player_stat_info()
                    dr_choice = input("(Attack, Persuade, Run, or.. Seduce?): ").upper()
                    if dr_choice in ("ATTACK, PERSUADE, RUN, SEDUCE"):
                        break
                    else:
                        print("Invalid option. Try again.")

                if dr_choice == "ATTACK":
                    if player_stats[0] >= random.randint(0,15) and player_stats[2] >= random.randint(0,15):
                        dmg_dl = random.randint(0, 101)
                        print(f"You dealt {dmg_dl} damage to the Lion!")
                        desert_boss_hp -= dmg_dl
                    else:
                        dl_dmg_pl = random.randint(0,51)
                        print(f"You failed to hit! Lion dealt {dl_dmg_pl} damange to you!")
                        player_hp -= dl_dmg_pl
                elif dr_choice == "PERSUADE":
                    dl_dmg_pl = random.randint(0,51)
                    print("While attempting to persuade the lion for some reason...")
                    print(f"the lion lunges and deals {dl_dmg_pl} damage to you!")
                    player_hp -= dl_dmg_pl
                elif dr_choice == "RUN":
                    if player_stats[7] >= random.randint(0,11) and player_stats[8] >= random.randint(0,11):
                        print("You successfully ran away!")
                        break
                    else:
                        dl_dmg_pl = random.randint(0,51)
                        print("You tried to run away but failed!")
                        print(f"The lion dealt {dl_dmg_pl} damage to you!")
                        player_hp -= dl_dmg_pl

                if desert_boss_hp <= 0:
                    if difficulty == "HARD":
                        player_gold += random.randint(0, 201) * 2
                    else:
                        player_gold += random.randint(0, 201)

                    player_stat_info()

                    print("You defeated the desert's lion!")
                    print(f"You now have {player_gold} gold.")
                    choice1 = False
                    break

                elif player_hp <= 0:
                    player_stat_info()

                    print("The lion defeated you!")
                    print()
                    print("Game Over!")
                    choice1 = False
                    player_alive = False
                    break

            # once fight ends, choice1 loop is exited
        if not choice1:
            break

    while True:
        print("You have arrived at the Merchants!...")
        merchant_input = input("do you wish to see his available items? (Y / N): ").upper 
        while True:
            pass

# To Do:
# Cave and Swamp
# Shop system after choice1 is exited.