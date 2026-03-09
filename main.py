# D&D Game

print("Welcome to the Dungeons & Dragons game!")
player_character = input("Choose your character type (Knight, Mage, Ninja, Prince): ").upper()
class_unchosen = True

# 1: Strength, 2: Speed, 3: Dexterity, 4: Charisma, 5: Endurance, 6: Arcane, 7: Intelligence, 8: Evasiveness
player_stats = [0, 0, 0, 0 ,0, 0, 0, 0]

while class_unchosen:
    if player_character == "KNIGHT":
        player_stats[0:] = [18, 20, 20, 20, 20, 20, 20, 20]
        class_unchosen = False
    elif player_character == "MAGE":
        player_stats[0:] = [18, 20, 20, 20, 20, 20, 20, 20]
        class_unchosen = False
    elif player_character == "NINJA":
        player_stats[0:] = [18, 20, 20, 20, 20, 20, 20, 20]
        class_unchosen = False
    elif player_character == "PRINCE":
        player_stats[0:] = [18, 20, 20, 20, 20, 20, 20, 20]
        class_unchosen = False
    else:
        print("This is not an available class, please choose again.")
        player_character = input("Choose your character type (Knight, Mage, Ninja, Prince): ").upper()
    
print("Class:", player_character.capitalize())
print(f"Stats: {player_stats}")