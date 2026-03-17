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

# initiliaze player companions list
player_companions = []

# initiliaze player damage
plaer_damage = 0

# initiliaze players currency amount
player_gold = 0

# initiliaze players health amount
player_hp = 100
player_hp_max = player_hp

# player inventory list
player_inventory = []

# boss health options
boss_health_hard = [500, 600, 700]
boss_health_easy = [200, 300, 400]

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
    print("Health:", player_hp,"/", player_hp_max)
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
    print("------------------")
    print("     Companions   ")
    print("------------------")
    print(":", player_companions)


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
    choice1_environments = ["Forest", "Desert", "Mushroom Kingdom", "Forest", "Desert", "Cave"]

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
            
            while True:
                player_stat_info()
                mk_choice = input("(Attack, Persuade, Run, or.. Seduce?) ").upper()
                if mk_choice in ("ATTACK", "PERSUADE", "RUN", "SEDUCE"):
                    break
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
                    choice1_environments.pop("Mushroom Kingdom")

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

        elif environment1 == "Cave":
            print()
            print("While walking down the path, you see an interesting looking cave...")
            cave_input = input("do you enter? (Y / N): ").upper()

            cave_decision = True

            while cave_decision:
                if cave_input == "Y":

                    # determine cave boss health
                    if difficulty == "HARD":    
                        cave_boss_health = random.choice(boss_health_hard)
                        cave_boss_health_max = cave_boss_health
                    else:
                        cave_boss_health = random.choice(boss_health_easy)
                        cave_boss_health_max = cave_boss_health   

                    cave_active = True

                    print()
                    print("You enter the cave and you see a Shiny Item on the floor.." \
                    "\nonly it's being guarded by a Giant Spider! What do you do?")

                    while cave_active:
                        while True:
                            print(f"Boss Health: {cave_boss_health} / {cave_boss_health_max}")
                            player_stat_info()
                            cv_choice = input("Attack, Persuade, Run, or.. Seduce?: ").upper()
                            if cv_choice in ("ATTACK", "PERSUADE", "RUN", "SEDUCE"):
                                break
                            else:
                                print("Invalid option. Try again.")

                        if cv_choice == "ATTACK":
                            if player_stats[0] >= random.randint(0, 16):
                                pl_dmg_cave = random.randint(0, 101)
                                cave_boss_health -= pl_dmg_cave
                                print()
                                print(f"You dealt {pl_dmg_cave} damage!")
                                if cave_boss_health <= 0:
                                    if difficulty == "HARD":
                                        goldgiven_cave = random.randint(0, 201) * 2
                                        player_gold += goldgiven_cave
                                    else:
                                        goldgiven_cave = random.randint(0, 201)
                                        player_gold += goldgiven_cave
                                        print()
                                    print("You defeated the Giant Spider! and under it was a Mysterious Key! \nIt's been added to your inventory!")
                                    print(f"You earned {goldgiven_cave} gold from defeating the Giant Spider!")
                                    print(f"You now have {player_gold} gold!")
                                    player_inventory.append("Mysterious Key")
                                    choice1 = False
                                    cave_decision = False
                                    cave_active = False
                                else:
                                    pass              
                            else:
                                cave_dmg_pl = random.randint(0, 51)
                                player_hp -= cave_dmg_pl
                                print()
                                print(f"You missed! The boss dealt {cave_dmg_pl} damage to you!")
                                if player_hp <= 0:
                                    print("The Giant Spider defeated you!")
                                    print()
                                    print("Game over!")
                                    player_alive = False
                                    choice1 = False
                                    cave_decision = False
                                    cave_active = False

                        elif cv_choice == "PERSUADE":
                            # awards less gold (100 max, x2 if difficulty = hard) due to non-attack
                            if player_stats[3] >= random.randint(0, 11) and player_stats[6] >= random.randint(0, 11):
                                if difficulty == "HARD":
                                    goldgiven_cave = random.randint(0, 101) * 2
                                    player_gold += goldgiven_cave
                                else:
                                    goldgiven_cave = random.randint(0, 101)
                                    player_gold += goldgiven_cave
                                print()
                                print("You successfully managed to persuade the Giant Spider by distracting it...")
                                print("with your horrific attempt to communicate with it, thus confusing it...")
                                print()
                                print("You successfully distracted the Giant Spider! and under it was a Mysterious Key! /nIt's been added to your inventory!")
                                player_inventory.append("Mysterious Key")
                            else:
                                cave_dmg_pl = random.randint(0, 51)
                                player_hp -= cave_dmg_pl
                                print()
                                print("You failed to persuade the Giant Spider, while trying to communicate with it, the Giant Spider attackd you!")
                                print(f"The Giant Spider dealt {cave_dmg_pl} damage to you!")
                                if player_hp <= 0:
                                    print("The Giant Spider defeated you!")
                                    print()
                                    print("Game over!")
                                    player_alive = False
                                    choice1 = False
                                    cave_decision = False
                                    cave_active = False

                        elif cv_choice == "RUN":
                            if player_stats[1] >= random.randint(0, 21):
                                print()
                                print("You were successfully able to run away!")
                                choice1_environments.pop("Cave")
                                cave_decision = False
                                cave_active = False
                            else:
                                print()
                                print("You tried to run but instead you slip and fell!")
                                cave_dmg_pl = random.randint(0, 51)
                                player_hp -= cave_dmg_pl
                                print(f"The Giant Spider dealt {cave_dmg_pl} damage to you!")
                                if player_hp <= 0:
                                    print("The Giant Spider defeated you!")
                                    print()
                                    print("Game over!")
                                    player_alive = False
                                    choice1 = False
                                    cave_decision = False
                                    cave_active = False


                        elif cv_choice == "SEDUCE":
                            pass

                elif cave_input == "N":
                    choice1_environments.pop("Cave")
                    break
                else:
                    cave_input = input("Invalid option. Try again: ")

        elif environment1 == "Forest":
            print()
            print("You took a cut in the path and have gotten lost in the forest...")
            print("while trying to find a way out.. you encounter a Wild Black Bear! What will you do?")
            print()

            if difficulty == "HARD":
                black_bear_hp = random.choice(boss_health_hard)
                black_bear_hpmax = black_bear_hp
            else:
                black_bear_hp = random.choice(boss_health_easy)
                black_bear_hpmax = black_bear_hp


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
                                goldgiven_forest = random.randint(0, 201) * 2
                                player_gold += goldgiven_forest
                                print()
                                print(f"You earned {goldgiven_forest} gold from defeating the Wild Black Bear!")
                                print(f"You now have {player_gold} gold!")
                                print()
                            else:
                                goldgiven_forest = random.randint(0, 201)
                                player_gold += goldgiven_forest
                                print()
                                print(f"You earned {goldgiven_forest} gold from defeating the Wild Black Bear!")
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

            if difficulty == "HARD":
                desert_boss_hp = random.choice(boss_health_hard)
                desert_boss_hpmax = desert_boss_hp
            else:
                desert_boss_hp = random.choice(boss_health_easy)
                desert_boss_hpmax = desert_boss_hp

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
                        choice1 = False 
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

    print()
    print("You have arrived at the Merchants!...")
    merchant_input = input("do you wish to see his available items? (Y / N): ").upper()

    merchant_active = True

    while merchant_active:
        while True:
        # get users input for shop
            if merchant_input == "Y":
                break
            elif merchant_input == "N":
                merchant_active = False
                break
            else:
                merchant_input = input("Invalid option. Try again: ").upper()

        player_stat_info()
        while True:

            shop_items = {"RUSTY SWORD": 100, "HEALTH POTION": 150, "CRACKED ARMOUR": 100, "LOTTERY TICKET": 50}

            # get users input for shop
            Shop_selection = input("Which item would you like to purchase? \n- [Rusty Sword - 100 Gold] " \
            "\n- (Health Potion - 150 Gold) \n- (Cracked Armour - 100 Gold) \n- [Lottery Ticket - 50 Gold] \n").upper()

            if Shop_selection in shop_items:
                break 
            else:
                print("Invalid option")

        if Shop_selection == "RUSTY SWORD":
            if player_gold >= shop_items["RUSTY SWORD"]:
                player_gold -= shop_items["RUSTY SWORD"]
                player_inventory.append("RUSTY SWORD")
                print("You purchased the Rusty Sword! It has been added to your inventory!")
                merchant_active = False
                break
            else:
                print("You don't have enough gold to purchase this item.")
                merchant_input = input("Do you wish to see the shop items again? (Y / N): ").upper()
                while True:
                    if merchant_input == "Y":
                        break
                    elif merchant_input == "N":
                        merchant_active = False
                        break
                    else:
                        merchant_input = input("Invalid option. Try again: ").upper()

        elif Shop_selection == "HEALTH POTION":
            if player_gold >= shop_items["HEALTH POTION"]:
                player_gold -= shop_items["HEALTH POTION"]
                player_inventory.append("HEALTH POTION")
                print("You purchased the Health Potion! It has been added to your inventory!")
                merchant_active = False
                break
            else:
                print("You don't have enough gold to purchase this item.")
                merchant_input = input("Do you wish to see the shop items again? (Y / N): ").upper()
                while True:
                    if merchant_input == "Y":
                        break
                    elif merchant_input == "N":
                        merchant_active = False
                        break
                    else:
                        merchant_input = input("Invalid option. Try again: ").upper()

        elif Shop_selection == "CRACKED ARMOUR":
            if player_gold >= shop_items["CRACKED ARMOUR"]:
                player_gold -= shop_items["CRACKED ARMOUR"]
                player_inventory.append("CRACKED ARMOUR")
                print("You purchased the Cracked Armour! It has been added to your inventory!")
                merchant_active = False
                break
            else:
                print("You don't have enough gold to purchase this item.")
                merchant_input = input("Do you wish to see the shop items again? (Y / N): ").upper()
                while True:
                    if merchant_input == "Y":
                        break
                    elif merchant_input == "N":
                        merchant_active = False
                        break
                    else:
                        merchant_input = input("Invalid option. Try again: ").upper()
                    
        elif Shop_selection == "LOTTERY TICKET":
            if player_gold >= shop_items["LOTTERY TICKET"]:
                player_gold -= shop_items["LOTTERY TICKET"]
                player_inventory.append("LOTTERY TICKET")
                print("You purchased the Lottery Ticket! It has been added to your inventory!")
                merchant_active = False
                break
            else:
                print("You don't have enough gold to purchase this item.")
                merchant_input = input("Do you wish to see the shop items again? (Y / N): ").upper()
                while True:
                    if merchant_input == "Y":
                        break
                    elif merchant_input == "N":
                        merchant_active = False
                        break
                    else:
                        merchant_input = input("Invalid option. Try again: ").upper()
    

    stage2 = True 
    stage2_scenario = True

    while stage2:
        print()
        print("You have exited the shop and continue on your journey to save the King's daughter...")
        print("After walking for what feels like years in the scorching sun, you decide to take shelter in a local building..")
        print()
        print("you see 2 buildings, one is a run down cabin and the other is an ominous looking castle... which do you choose?")

        stage2_input = input("(Cabin or Castle): ").upper()
        while stage2_scenario:
            if stage2_input == "CABIN":

                # introduce user to the level
                print()
                print("You enter the cabin and find a friendly old man who offers you a place to rest for the night...")
                cabin_input = input("do you stay the night? (Y / N): ").upper()
                while True:
                    if cabin_input == "Y":
                        print()
                        print("You stay the night and wake up to find out, that the old man had stolen half of your gold!")
                        goldStolen_cabin = player_gold = player_gold // 2
                        print(f"The old man stole {goldStolen_cabin} gold!")
                        # player has seen the old man, and has opportunity to regain their gold.
                        old_man_seen = True
                        stage2 = False
                        stage2_scenario = False
                        break 

                    elif cabin_input == "N":
                        stage2_scenario = False
                    else:
                        cabin_input = input("Invalid option. Try again: ").upper()

            elif stage2_input == "CASTLE":
                
                # determine castle boss health
                if difficulty == "HARD":
                    castle_boss_health = random.choice(boss_health_hard)
                    castle_boss_health_max = castle_boss_health
                else:
                    castle_boss_health = random.choice(boss_health_easy)
                    castle_boss_health_max = castle_boss_health

                print()
                print("You enter the castle and find the place to be abandoned and very dark...")
                print("While exploring the castle, you encounter a ghost! What do you do?")
                while True:
                    player_stat_info()
                    castle_choice = input("(Attack, Persuade, Run, or.. Seduce?): ").upper()
                    if castle_choice in ("ATTACK", "PERSUADE", "RUN", "SEDUCE"):
                        break
                    else:
                        print("Invalid option. Try again.")
                
                if castle_choice == "ATTACK":
                    if player_stats[0] >= random.randint(0, 16):

                        pl_dmg_castle = random.randint(0, 101)
                        castle_boss_health -= pl_dmg_castle

                        print(f"You dealt {pl_dmg_castle} damage to the ghost!")
                        if castle_boss_health <= 0:
                            # determine gold given to player
                            if difficulty == "HARD":
                                goldgiven_castle = random.randint(0, 201) * 2
                                player_gold += goldgiven_castle
                            else:
                                goldgiven_castle = random.randint(0, 201)
                                player_gold += goldgiven_castle

                            print()
                            print("You defeated the ghost! and found a secret passage leading you to the next area!")
                            stage2 = False
                            secret_passage = True 
                            break   
                        elif player_hp <= 0:
                            print()
                            print("The ghost defeated you!")
                            print()
                            print("Game Over!")
                            player_alive = False
                            stage2 = False
                            break  
                        else:
                            pass    
                        
                    else:
                        castle_dmg_pl = random.randint(0, 51)
                        player_hp -= castle_dmg_pl
                        print()
                        print(f"You missed! and the ghost dealt {castle_dmg_pl} damage to you!")
                        if player_hp <= 0:
                            print("The ghost defeated you!")
                            print()
                            print("Game Over!")
                            player_alive = False
                            stage2 = False
                            break
                        else:
                            pass 
                elif castle_choice == "PERSUADE":
                    if player_stats[3] >= random.randint(0, 11) and player_stats[6] >= random.randint(0, 11):
                        print()
                        print("You successfully persuaded the ghost to let you pass through the castle unharmed!")
                        stage2 = False
                        stage2_scenario = False
                        secret_passage = True 
                        break
                    else:
                        castle_dmg_pl = random.randint(0, 51)
                        player_hp -= castle_dmg_pl
                        print()
                        print("You failed to persuade the ghost, while trying to communicate with it, the ghost attackd you!")
                        print(f"The ghost dealt {castle_dmg_pl} damage to you!")
                        if player_hp <= 0:
                            print()
                            print("The ghost defeated you!")
                            print()
                            print("Game over!")
                            player_alive = False
                            stage2 = False
                            break
                elif castle_choice == "RUN":
                    if player_stats[7] >= random.randint(0, 11) and player_stats[8] >= random.randint(0, 11):
                        print("You successfully ran away!")
                        stage2 = False 
                        stage2_scenario = False
                        break
                    else:
                        castle_dmg_pl = random.randint(0, 51)
                        print()
                        print("You tried to run away but failed!")
                        print(f"The ghost dealt {castle_dmg_pl} damage to you!")
                        player_hp -= castle_dmg_pl
                        if player_hp <= 0:
                            print()
                            print("The ghost defeated you!")
                            print()
                            print("Game Over!")
                            player_alive = False
                            stage2 = False
                            break
                elif castle_choice == "SEDUCE":
                    print()
                    print("why even choose this action...")
                    print("The ghost mistook your seduction as an opportunity to damage you!")
                    ghost_dmg_pl = random.randint(0, 51)
                    player_php -= ghost_dmg_pl
                    print(f"The ghost dealt {ghost_dmg_pl} damage to you!")
                    if player_hp <= 0:
                        print()
                        print("The ghost defeated you!")
                        print()
                        print("Game Over!")
                        player_alive = False
                        stage2 = False
                        break
    
    while secret_passage:
        print()
        print("You have entered the secret passage and find yourself in a new area...")
        print("you go downstairs and find a locked chest!...")
        if "Mysterious Key" in player_inventory:
            print()
            print("You have the Mysterious Key in your inventory...")
            key_input = input("would you like to use it to open the chest? (Y / N): ").upper()
            while True:
                if key_input == "Y":
                    # 1. Legenedary Sword - increases attack by 50
                    # 2. Legendary Armour - increases health by 50
                    # 3. Legendary Potion - fully restores health + 50 permanent health increase
                    # 4. Legendary Ring - increases arcane & intelligence by 6
        
                    chest_loot = {"Legendary Sword": 50, "Legendary Armour": 50, "Legendary Potion": 50, "Legendary Ring": 6}
                    print()
                    print("You used the Mysterious Key to open the chest and found a powerful item inside!...")
                    chestLoot_chosen = random.choice(chest_loot)

                    if chestLoot_chosen == "Legendary Sword":

                        # if difficulty is hard, full 50 attack increase, if difficulty is easy, 25 attack increase
                        if difficulty == "HARD":
                            player_damage += chest_loot["Legendary Sword"]
                        else:
                            player_damage += chest_loot["Legendary Sword"] // 2
                        player_inventory.append("Legendary Sword")

                        print()
                        print(f"You found the Legendary Sword! Your attack has permanently increased by {chest_loot['Legendary Sword']}!")
                        print("You continue on your journey and head to Njyurhavn, a nearby city...")

                        secret_passage = False
                        break

                    elif chestLoot_chosen == "Legendary Armour":

                        # if difficulty is hard, full 50 health increase, if difficulty is easy, 25 health increase
                        if difficulty == "HARD":
                            player_hp += chest_loot['Legendary Armour']
                        else:
                            player_hp += chest_loot['Legendary Armour'] // 2
                        player_inventory.append("Legendary Armour")

                        print()
                        print(f"You found the Legendary Armour! Your health has permanently increased by {chest_loot['Legendary Armour']}!")
                        print("You continue on your journey and head to Njyurhavn, a nearby city...")

                        secret_passage = False
                        break

                    elif chestLoot_chosen == "Legendary Potion":

                        # if difficulty is hard, full 50 health increase, if difficulty is easy, 25 health increase
                        if difficulty == "HARD":
                            player_hp_max += chest_loot['Legendary Potion']
                        else:
                            player_hp_max += chest_loot['Legendary Potion'] // 2
                        player_hp = player_hp_max

                        print()
                        print(f"You found the Legendary Potion! Your health has been fully restored and permanently increased by {chest_loot['Legendary Potion']}!")
                        print("You continue on your journey and head to Njyurhavn, a nearby city...") 
                                          
                        secret_passage = False
                        break

                    elif chestLoot_chosen == "Legendary Ring":

                        # if difficulty is hard, full 6 arcane and intelligence increase, if difficulty is easy, 3 arcane and intelligence increase
                        if difficulty == "HARD":
                            player_stats[6] += chest_loot[chestLoot_chosen]
                            player_stats[3] += chest_loot[chestLoot_chosen]
                        else:
                            player_stats[6] += chest_loot[chestLoot_chosen] // 2
                            player_stats[3] += chest_loot[chestLoot_chosen] // 2
                        player_inventory.append("Legendary Ring")

                        print()
                        print(f"You found the Legendary Ring! Your arcane and intelligence have both increased by {chest_loot['Legendary Ring']}!")
                        print("You continue on your journey and head to Njyurhavn, a nearby city...")       

                        secret_passage = False
                        break

                elif key_input == "N":
                    print()
                    print("You decided not to use the Mysterious Key and left the chest unopened...")
                    print("You continue on your journey and head to Njyurhavn, a nearby city...")
                    secret_passage = False
                    break 
                else:
                    key_input = input("Invalid option. Try again: ").upper()
        else:
            print()
            print("You don't have the Mysterious Key in your inventory, so you can't open the chest...")
            print("You continue on your journey and head to Njyurhavn, a nearby city...")
            break

    stage3 = True
    while stage3:
        print()
        print("You have arrived at Njyurhavn, a city that is said to be the home of the most powerful sorcerer in the world...")
        print("You have heard that the sorcerer has a powerful item that can help you in your quest to save the King's daughter, but you also heard that the sorcerer is very dangerous and has a powerful army of minions protecting him...")
        print()
        print("You have two options, you can either try to sneak into the sorcerer's tower and steal the item, or you can try to fight the sorcerer and his minions head on... which do you choose?")
        stage3_input = input("(Sneak or Fight): ").upper()
        while True:
            if stage3_input in ("SNEAK", "FIGHT"):
                break
            else:
                stage3_input = input("Invalid option. Try again: ").upper()
        if stage3_input == "SNEAK":
            if player_stats[1] >= random.randint(0, 16) and player_stats[9] >= random.randint(0, 16):
                print()
                print("You decided to sneak into the sorcerer's tower and try to steal the item...")
                print("You successfully snuck into the tower and found the Book of Knowledge, a powerful item that can help you in your quest to save the King's daughter!")
                player_inventory.append("Book of Knowledge")
                print()
                print("You quickly left the tower and continue on your journey to save the King's daughter...")
                stage3 = False
            else:
                print()
                print("You tried to sneak into the sorcerer's tower but got caught by the sorcerer's minions...")
                print("The sorcerer is very angry and decides to fight you himself...")

                # To DO List:
                # - create a fight sequence for the sorcerer and his minions, with different stats and abilities for each enemy.
                # - create a way for the player to escape the tower after defeating the sorcerer and his minions.
        elif stage3_input == "FIGHT":

            # determine sorcerer health
            if difficulty == "HARD":
                sorcerer_hp = random.choice(boss_health_hard)
                sorcerer_hpmax = sorcerer_hp
            else:
                sorcerer_hp = random.choice(boss_health_easy)
                sorcerer_hpmax = sorcerer_hp

            player_stat_info()
            print("You decided to fight the sorcerer and his minions head on...")
            print("the sorcerer steps forward to fight...")
            print()
            stage3Fight_input = input("(Attack, Persuade, Run, or.. Seduce?): ").upper()
            while True:
                if stage3Fight_input in ("ATTACK", "PERSUADE", "RUN", "SEDUCE"):
                    break
                else:
                    stage3Fight_input = input("Invalid option. Try again: ").upper()

            while player_alive and sorcerer_hp > 0:
                if stage3Fight_input == "ATTACK":
                    
                    if player_stats[0] >= random.randint(0, 16):
                        pl_dmg_sorcerer = random.randint(0, 101)
                        print()
                        print(f"You dealt {pl_dmg_sorcerer} damage to the sorcerer!")
                        sorcerer_hp -= pl_dmg_sorcerer
                        if sorcerer_hp <= 0:

                            if difficulty == "HARD":
                                goldgiven_sorcerer = random.randint(0, 201) * 2
                                player_gold += goldgiven_sorcerer
                            else:
                                goldgiven_sorcerer = random.randint(0, 201)
                                player_gold += goldgiven_sorcerer

                            print()
                            print("You defeated the sorcerer and his minions, and retrieved the Book of Knowledge from the sorcerer's chamber!")
                            player_inventory.append("Book of Knowledge")
                            print(f"You now have {player_gold} gold!")
                            stage3 = False
                            break   
                        elif player_hp <= 0:
                            print()
                            print("The sorcerer defeated you!")
                            print()
                            print("Game Over!")
                            player_alive = False
                            stage3 = False
                            break  

                    else:
                        sorcerer_dmg_pl = random.randint(0, 51)
                        player_hp -= sorcerer_dmg_pl
                        print(f"You missed! and the sorcerer dealt {sorcerer_dmg_pl} damage to you!")
                        if player_hp <= 0:
                            print("The sorcerer defeated you!")
                            print("Game Over!")
                            player_alive = False
                            stage3 = False
                            break

                elif stage3Fight_input == "PERSUADE":   
                    if player_stats[3] >= random.randint(0, 11) and player_stats[6] >= random.randint(0, 11):
                        print("You successfully persuaded the sorcerer to let you pass through his tower unharmed!")
                        print("and he even gave you the Book of Knowledge, a powerful item that can help you in your quest to save the King's daughter!")
                        player_inventory.append("Book of Knowledge")
                        stage3 = False
                        break
                    else:
                        sorcerer_dmg_pl = random.randint(0, 51)
                        player_hp -= sorcerer_dmg_pl
                        print("You failed to persuade the sorcerer, while trying to communicate with him, the sorcerer attackd you!")
                        print(f"The sorcerer dealt {sorcerer_dmg_pl} damage to you!")
                        if player_hp <= 0:
                            print("The sorcerer defeated you!")
                            print()
                            print("Game Over!")
                            player_alive = False
                            stage3 = False
                            break     
                        
                elif stage3Fight_input == "RUN":
                    if player_stats[7] >= random.randint(0, 11) and player_stats[8] >= random.randint(0, 11):
                        print("You successfully ran away from the sorcerer and his minions!")
                        stage3 = False 
                        break
                    else:
                        sorcerer_dmg_pl = random.randint(0, 51)
                        print("You tried to run away but failed!")
                        print(f"The sorcerer dealt {sorcerer_dmg_pl} damage to you!")
                        player_hp -= sorcerer_dmg_pl
                        if player_hp <= 0:
                            print("The sorcerer defeated you!")
                            print()
                            print("Game Over!")
                            player_alive = False
                            stage3 = False
                            break

                elif stage3Fight_input == "SEDUCE":
                    print("You attempted to seduce the sorcerer and his minions, but they were not interested in your advances...")
                    print("The sorcerer and his minions attack you while you're vulnerable!")
                    sorcerer_dmg_pl = random.randint(0, 51)
                    player_hp -= sorcerer_dmg_pl
                    print(f"The sorcerer and his minions dealt {sorcerer_dmg_pl} damage to you!")
                    if player_hp <= 0:
                        print("The sorcerer defeated you!")
                        print()
                        print("Game Over!")
                        player_alive = False
                        stage3 = False
                        break

    while True:
        if "Book of Knowledge" in player_inventory:
            print("You have the Book of Knowledge in your inventory, which can help you in your quest to save the King's daughter...")
            print("You continue on your journey and head to the final area, where the King's daughter is being held captive by a powerful dragon...")
            break
        else:
            print("You don't have the Book of Knowledge in your inventory, the key item to finding the King's daughter...")
            print("You return to the King empty handed and fail in your quest to save his daughter...")
            print()
            print("Game Over!")
            player_alive = False
            break

    merchantActive_2 = True
    while merchantActive_2:
        print()
        print("On your way to the final area, you encounter another merchant...")
        merchant_input_2 = input("do you wish to see his available items? (Y / N): ").upper()

        while True:
            if merchant_input_2 == "Y":
                break
            elif merchant_input_2 == "N":
                merchantActive_2 = False
                break
            else:
                merchant_input_2 = input("Invalid option. Try again: ").upper()

        player_stat_info()
        while True:

            shop_items_2 = {"EXCALIBUR": 500, "ELIXIR OF LIFE": 750, "DRAGON ARMOUR": 1000, "MAP TO DRAGON'S LAIR": 250}

            Shop_selection_2 = input("Which item would you like to purchase? \n- [Excalibur - 500 Gold] "\
            "\n- (Elixir of Life - 750 Gold) \n- (Dragon Armour - 1000 Gold) \n- [Map to Dragon's Lair - 250 Gold] \n").upper()
            if Shop_selection_2 == "EXCALIBUR":
                if player_gold >= shop_items_2["EXCALIBUR"]:
                    player_gold -= shop_items_2["EXCALIBUR"]
                    player_inventory.append("EXCALIBUR")
                    print("You purchased Excalibur! It has been added to your inventory!")
                    merchantActive_2 = False
                    break
                else:
                    print("You don't have enough gold to purchase this item.")
                    merchant_input_2 = input("Do you wish to see the shop items again? (Y / N): ").upper()
                    while True:
                        if merchant_input_2 == "Y":
                            break
                        elif merchant_input_2 == "N":
                            merchantActive_2 = False
                            break
                        else:
                            merchant_input_2 = input("Invalid option. Try again: ").upper()
            elif Shop_selection_2 == "ELIXIR OF LIFE":
                if player_gold >= shop_items_2["ELIXIR OF LIFE"]:
                    player_gold -= shop_items_2["ELIXIR OF LIFE"]
                    player_inventory.append("ELIXIR OF LIFE")
                    print("You purchased the Elixir of Life! It has been added to your inventory!")
                    merchantActive_2 = False
                    break
                else:
                    print("You don't have enough gold to purchase this item.")
                    merchant_input_2 = input("Do you wish to see the shop items again? (Y / N): ").upper()
                    while True:
                        if merchant_input_2 == "Y":
                            break
                        elif merchant_input_2 == "N":
                            merchantActive_2 = False
                            break
                        else:
                            merchant_input_2 = input("Invalid option. Try again: ").upper()
            elif Shop_selection_2 == "DRAGON ARMOUR":
                if player_gold >= shop_items_2["DRAGON ARMOUR"]:
                    player_gold -= shop_items_2["DRAGON ARMOUR"]
                    player_inventory.append("DRAGON ARMOUR")
                    print("You purchased the Dragon Armour! It has been added to your inventory!")
                    merchantActive_2 = False
                    break
                else:
                    print("You don't have enough gold to purchase this item.")
                    merchant_input_2 = input("Do you wish to see the shop items again? (Y / N): ").upper()
                    while True:
                        if merchant_input_2 == "Y":
                            break
                        elif merchant_input_2 == "N":
                            merchantActive_2 = False
                            break
                        else:
                            merchant_input_2 = input("Invalid option. Try again: ").upper()
            elif Shop_selection_2 == "MAP TO DRAGON'S LAIR":
                if player_gold >= shop_items_2["MAP TO DRAGON'S LAIR"]:
                    player_gold -= shop_items_2["MAP TO DRAGON'S LAIR"]
                    player_inventory.append("MAP TO DRAGON'S LAIR")
                    print("You purchased the Map to Dragon's Lair! It has been added to your inventory!")
                    dragonLair = True
                    merchantActive_2 = False
                    break
                else:
                    print("You don't have enough gold to purchase this item.")
                    merchant_input_2 = input("Do you wish to see the shop items again? (Y / N): ").upper()
                    while True:
                        if merchant_input_2 == "Y":
                            break
                        elif merchant_input_2 == "N":
                            merchantActive_2 = False
                            break
                        else:
                            merchant_input_2 = input("Invalid option. Try again: ").upper()
            else:
                print("Invalid option. Try again.")
    
    while dragonLair:
        print()
        print("You have the Map to the Dragon's Lair in your inventory!...")
        print("using this information, you follow the map to find this lair, travelling through dangerous terrain and overcoming various obstacles along the way...")
        print("until finally, you arrive at the entrance to the Dragon's Lair, where a powerful dragon is said to reside...")
        print()
        print("You enter the lair, and find the dragon sleeping on a pile of gold and treasure...")
        print("What do you do?")
        while True:
            player_stat_info()
            dragonLair_input = input("(Attack, Persuade, Run, or.. Tame?): ").upper()
            if dragonLair_input in ("ATTACK", "PERSUADE", "RUN", "TAME"):
                break
            else:
                print("Invalid option. Try again.")
        
        if dragonLair_input == "ATTACK":
            print("You decided to attack the dragon while it's sleeping...")
            print("The dragon wakes up and is very angry that you disturbed its sleep, and it attacks you with its fiery breath!")
            dragon_dmg_pl = random.randint(0, 101)
            player_hp -= dragon_dmg_pl
            print(f"The dragon dealt {dragon_dmg_pl} damage to you!")
            if player_hp <= 0:
                print("The dragon defeated you!")
                print()
                print("Game Over!")
                player_alive = False
                dragonLair = False
            else:
                pass

        elif dragonLair_input == "PERSUADE":
            print("You decided to try to persuade the dragon to let you pass through its lair unharmed...")
            if player_stats[3] >= random.randint(0, 11) and player_stats[6] >= random.randint(0, 11):
                print("You successfully persuaded the dragon to let you pass through its lair unharmed!")
                print("and it even gave you a powerful item, the Dragon's Scale, which can help you in your quest to save the King's daughter!")
                player_inventory.append("Dragon's Scale")
                dragonLair = False
            else:
                print("You failed to persuade the dragon, while trying to communicate with it, the dragon attackd you with its fiery breath!")
                dragon_dmg_pl = random.randint(0, 101)
                player_hp -= dragon_dmg_pl
                print(f"The dragon dealt {dragon_dmg_pl} damage to you!")
                if player_hp <= 0:
                    print("The dragon defeated you!")
                    print()
                    print("Game Over!")
                    player_alive = False
                    dragonLair = False

        elif dragonLair_input == "RUN":
            print("You decided to try to run away from the dragon...")
            if player_stats[7] >= random.randint(0, 11) and player_stats[8] >= random.randint(0, 11):
                print("You successfully ran away from the dragon!")
                dragonLair = False 
            else:
                print("You tried to run away but failed!")
                print("The dragon attackd you with its fiery breath as you were trying to escape!")
                dragon_dmg_pl = random.randint(0, 101)
                player_hp -= dragon_dmg_pl
                print(f"The dragon dealt {dragon_dmg_pl} damage to you!")
                if player_hp <= 0:
                    print("The dragon defeated you!")
                    print()
                    print("Game Over!")
                    player_alive = False
                    dragonLair = False
        
        elif dragonLair_input == "TAME":
            print()
            print("You decided to try to tame the dragon and make it your ally...")
            if player_stats[5] >= random.randint(0, 11) and player_stats[6] >= random.randint(0, 11):
                print()
                print("You successfully tamed the dragon and made it your ally!")
                print("The dragon is very grateful that you showed it kindness and respect, and it decides to help you in your quest to save the King's daughter!")
                print()

                # determine gold given to player
                if difficulty == "HARD":
                    goldgiven_dragon = random.randint(0, 201) * 2
                    player_gold += goldgiven_dragon
                else:
                    goldgiven_dragon = random.randint(0, 201)
                    player_gold += goldgiven_dragon

                print(f"The dragon also gave you {goldgiven_dragon} gold as a token of its gratitude!")
                player_inventory.append("Tamed Dragon")
                dragonLair = False
            else:
                print("You failed to tame the dragon, while trying to communicate with it, the dragon attackd you with its fiery breath!")
                dragon_dmg_pl = random.randint(0, 101)
                player_hp -= dragon_dmg_pl
                print(f"The dragon dealt {dragon_dmg_pl} damage to you!")
                if player_hp <= 0:
                    print("The dragon defeated you!")
                    print()
                    print("Game Over!")
                    player_alive = False
                    dragonLair = False

    # To be continued...

