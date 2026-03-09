# D&D Game
import random

player_alive = True

while player_alive:
    print("Welcome to the Dungeons & Dragons game!")
    player_character = input("Choose your character type (Knight, Mage, Ninja, Prince): ").upper()
    class_unchosen = True

    # initiliaze player stats
    # 1: Strength, 2: Speed, 3: Dexterity, 4: Charisma, 5: Endurance, 6: Arcane, 7: Intelligence, 8: Evasiveness
    player_stats = [0, 0, 0, 0 ,0, 0, 0, 0]

    # initiliaze players currency amount
    gold = 0

    while class_unchosen:
        # Knight is Strong, Endurant, and Evasive.
        if player_character == "KNIGHT":
            player_stats[0:] = [18, 7, 9, 6, 17, 3, 8, 15]
            class_unchosen = False
        # Mage is intelligent, charismatic, dexteric and skilled in arcane.
        elif player_character == "MAGE":
            player_stats[0:] = [4, 6, 16, 7, 6, 18, 17, 7]
            class_unchosen = False
        # Ninja is fast, dexteric, evasive.
        elif player_character == "NINJA":
            player_stats[0:] = [18, 20, 20, 20, 20, 20, 20, 20]
            class_unchosen = False
        # Prince is charismatic, intelligent and fast.
        elif player_character == "PRINCE":
            player_stats[0:] = [18, 20, 20, 20, 20, 20, 20, 20]
            class_unchosen = False
        else:
            print("This is not an available class, please choose again.")
            player_character = input("Choose your character type (Knight, Mage, Ninja, Prince): ").upper()
        
    # Display player class and their assigned stats    
    print()
    print("Class:", player_character.capitalize())
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
    print()

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
        mk_choice_running = True

        print("Oh no! it seems you've walked right into the Mushroom Kingdom uninvited...")
        print("and your wanted for stealing all of their renowned mushroom bread!")
        print("You encounter King Toadstool and he wants you executed! What will you do?!")
        
        while mk_choice_running:
            mk_choice = input("Attack, Persuade, Run, or.. Seduce? ").upper()
            if mk_choice == "ATTACK" or "PERSUADE" or "RUN" or "SEDUCE":
                mk_choice_running = False
            else:
                print("Invalid Option. Try again.")
                mk_choice = input("Attack, Persuade, Run, or.. Seduce? ").upper()

        if mk_choice == "Attack":
            if player_stats[0] >= random.randint(0, 16):
                print("You killed King Toadstool!.. but his soldiers executed you on the spot.")
                print("Game Over!")
                player_alive = False
            else:
                print("You missed! and died of embarrasment...")
                print("Game Over!")
                player_alive = False
        elif mk_choice == "Persuade":
            if player_stats[3] >= random.randint(0, 10):
                print("You succesfully persuaded the King with your charisma, claiming you'll")
                print("return the bread with a small loan of gold from the King!")
                print(f"The King gives you {random.randint(range(250, 501))} gold and sends you on your way!")
            else:
                print("You stuttered and the King laughed in your face...")
                print("and you died of embarrasment...")
                print("Game Over!")
                player_alive = False
