# Dungeons & Dragons Python Game

import random

player_alive = True

# initiliaze player stats
# 1: Strength, 2: Speed, 3: Dexterity, 4: Charisma, 5: Endurance, 6: Arcane, 7: Intelligence, 8: Evasiveness, 9: Luck
player_stats = [0, 0, 0, 0 ,0, 0, 0, 0, 0]

knight_stats = [18, 7, 9, 6, 17, 3, 8, 8, 6]
mage_stats = [4, 6, 16, 7, 6, 18, 17, 7, 6]
ninja_stats = [13, 18, 17, 9, 7, 2, 12, 15, 6]
prince_stats = [7, 17, 8, 19, 6, 0, 19, 4, 10]


# initiliaze players currency amount
player_gold = 0

# initiliaze players health amount
player_hp = 100

#player inventory list
player_inventory = []

print()
print("Welcome to the Dungeons & Dragons Python Game! \nA program developed by Ærmin and ReynoBTW.")
print()

# set game difficulty
while True:
    difficulty = input("Enter your difficulty (Easy / Hard): ").upper()
    # if users input meets conditions, loop is exited
    if difficulty == "EASY":
        break
    elif difficulty == "HARD":
        break
    else:
        print("Invalid option. Try again.")

# Display player class and their assigned stats
def player_stat_info_preview(x):
    print("------------------")
    print("       Stats      ")
    print("------------------")
    print(f"Strength: {x[0]}")
    print(f"Speed: {x[1]}")
    print(f"Dexterity: {x[2]}")
    print(f"Charisma: {x[3]}")
    print(f"Endurance: {x[4]}")
    print(f"Arcane: {x[5]}")
    print(f"Intelligence: {x[6]}")
    print(f"Evasiveness: {x[7]}")
    print(f"Luck: {x[8]}")
    print()

# player classes
class_unchosen = True
player_character = ""
while class_unchosen:
    player_character = input("Choose your character type (Knight, Mage, Ninja, Prince): ").upper()
    # Knight is Strong, Endurant, and Evasive.
    if player_character == "KNIGHT":
        while True:
            player_stat_info_preview(knight_stats)
            confirm_pc = input(f"You have selected {player_character}. Do you wish to continue? (Y / N): ").upper()
            if confirm_pc == "Y":
                player_stats[0:] = [18, 7, 9, 6, 17, 3, 8, 8, 6]
                class_unchosen = False
                break
            elif confirm_pc == "N":
                break
            else:
                print("Invalid option. Try again: ")        
    # Mage is intelligent, charismatic, dexteric and skilled in arcane.
    elif player_character == "MAGE":
        while True:
            player_stat_info_preview(mage_stats)
            confirm_pc = input(f"You have selected {player_character}. Do you wish to continue? (Y / N): ").upper()
            if confirm_pc == "Y":
                player_stats[0:] = [4, 6, 16, 7, 6, 18, 17, 7, 6]
                class_unchosen = False
                break
            elif confirm_pc == "N":
                break
            else:
                print("Invalid option. Try again: ")
    # Ninja is fast, dexteric, evasive.
    elif player_character == "NINJA":
        while True:
            player_stat_info_preview(ninja_stats)
            confirm_pc = input(f"You have selected {player_character}. Do you wish to continue? (Y / N): ").upper()
            if confirm_pc == "Y":
                player_stats[0:] = [13, 18, 17, 9, 7, 2, 12, 15, 6]
                class_unchosen = False
                break
            elif confirm_pc == "N":
                break
            else:
                print("Invalid option. Try again: ")
    # Prince is charismatic, intelligent and fast.
    elif player_character == "PRINCE":
        while True:
            player_stat_info_preview(prince_stats)
            confirm_pc = input(f"You have selected {player_character}. Do you wish to continue? (Y / N): ").upper()
            if confirm_pc == "Y":            
                player_stats[0:] = [7, 17, 8, 19, 6, 0, 19, 4, 10]
                player_gold = 350
                class_unchosen = False
                break
            elif confirm_pc == "N":
                break
            else:
                print("Invalid option. Try again: ")
    else:
        print("This is not an available class, please choose again.")

def player_stat_info():    
    print()
    print("Class:", player_character.capitalize())
    print("Health:", player_hp,"/ 100")
    print("Inventory:",player_inventory)
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


while player_alive:
    player_stat_info()

    print(f"You are a {player_character.capitalize()} in the Kingdom of New Ross.")
    print(f"The King's daughter has been kidnapped and it's your job to find her and return her to the kingdom.") 

    while True:
        understand_input = input("Do you understand your job? (Y / N) ").upper()
        if understand_input == "N":
            print()
            print("Too bad, onwards soldier!")
            break
        elif understand_input == "Y":
            print()
            print("Fantastic, onwards soldier!")
            break
        else:
            print()
            understand_input = input("I'm afraid you mispoke... try again. (Y / N) ").upper()

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
                break

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


            while True:
                fr_choice_running = True
                print(f"Black Bear HP: {black_bear_hp}/{black_bear_hpmax}")
                while fr_choice_running:
                    player_stat_info()
                    fr_choice = input("(Attack, Persuade, Run, or.. Seduce?): ").upper()
                    if fr_choice in ("ATTACK", "PERSUADE", "RUN", "SEDUCE"):
                        fr_choice_running = False
                    else:
                        print("Invalid Option. Try again.")
                
                if fr_choice == "ATTACK":
                    if player_stats[0] >= random.randint(0, 20):
                        dmg_bb = random.randint(0, 101)
                        print(f"You dealt {dmg_bb} damage to the bear!")
                        black_bear_hp -= dmg_bb
                        if black_bear_hp <= 0:
                            print("You defeated the Wild Black Bear!")
                            if difficulty == "HARD":
                                player_gold += random.randint(0, 201) * 2
                                print()
                                print(f"You now have {player_gold} gold!")
                                print()
                            else:
                                player_gold += random.randint(0, 201)
                                print()
                                print(f"You now have {player_gold} gold!")
                                print()
                            choice1 = False
                            break

                    else:
                        dmg_player_bb = random.randint(0, 101)
                        print(f"You missed! and the bear dealt {dmg_player_bb} to you!")
                        player_hp -= dmg_player_bb
                        if player_hp <= 0:
                            print("The Wild Black Bear defeated you!")
                            print("Game Over!")
                            player_alive = False
                            choice1 = False
                            break

                elif fr_choice == "PERSUADE":
                    if player_stats[3] >= random.randint(5, 16) and player_stats[6] >= random.randint(5, 16):
                        print("You succesfully communicated with the bear in 'bear' language...")
                        print("the bear understood you were just a mere traveller and let you pass...")
                        player_stat_info()
                        print()
                        choice1 = False
                        break
                elif fr_choice == "RUN":
                    if player_stats[7] >= random.randint(0, 11):
                        choice1 = False
                        print("You successfully evaded the bear and ran away!")
                        player_stat_info()
                        print()
                        break
                    else:
                        print("You tried to evade the Wild Black Bear, instead you jumped right into his mouth..")
                        print("..maybe next time.")
                        print()
                        print("Game Over!")
                        player_stat_info()
                        player_alive = False
                        choice1 = False
                        break
                elif fr_choice == "SEDUCE":
                    print("You attempted to seduce the Wild Black Bear and in return...")
                    print("the Wild Black Bear ate you... nice try... i guess...")
                    print()
                    print("Game Over!")
                    player_stat_info()
                    player_alive = False
                    choice1 = False
                    break
        
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
                    player_alive = False
                    choice1 = False
                    break

            # once fight ends, choice1 loop is exited
        if not choice1:
            break
    if not player_alive:
        break

    while True:
        print("You have arrived at the Merchants!...")
        merchant_input = input("do you wish to see his available items? (Y / N): ").upper 
        while True:
            player_stat_info()
            while True:
                Shop_selection = input("Which item would you like to purchase? \n (Rusty Sword - 100 Gold) " \
                "\n (Health Potion - 150 Gold) \n (Cracked Armour - 100 Gold) \n (Lottery Ticket - 50 Gold) \n").upper()
                if Shop_selection in ("RUSTY SWORD, HEALTH POTION, CRACKED ARMOUR, LOTTERY TICKET"):
                    break 
                else:
                    print("Invalid option, please choose again ")
            if Shop_selection == "RUSTY SWORD":
                player_inventory.append("RUSTY SWORD")
                break

            elif Shop_selection == "HEALTH POTION":
                player_inventory.append("HEALTH POTION")
                break
            
            elif Shop_selection == "CRACKED ARMOUR":
                player_inventory.append("CRACKED ARMOUR")
                break
            elif Shop_selection == "LOTTERY TICKET":
                player_inventory.append("LOTTERY TICKET")
                break

                  

            



               
            
                


# To Do:
# Cave and Swamp
# Shop system after choice1 is exited.