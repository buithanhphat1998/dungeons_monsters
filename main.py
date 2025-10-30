"""
CECS 277 – Lab 10 – Singleton
10/29/2025

Group 4
Group members:
Thanh Phat Bui
Ha Gia Bao Hoang

Description: 
Dungeons and Monsters
Create a program that allows the user to wander through a haunted dungeon maze and fight
monsters that they encounter as they explore. The user wins if they reach the dungeon’s exit
alive. Use the following UML diagram and the class descriptions below to create your program
"""

from hero import Hero
from map import Map
from enemy import Enemy
import check_input
import random
def main():
    """
    Main function to run the Dungeons and Monsters game.
    - Prompts the user for their name and creates a Hero.
    - Initializes the dungeon map.
    - Allows the user to navigate the dungeon, encounter monsters, and find items.
    - Handles combat, movement, and win/lose conditions.
    - The game ends when the hero finds the exit or dies.
    """
    # Get user's name
    name = input("What is your name, traverler? ")
    # instantiate a hero object
    hero = Hero(name, 5)
    # instantiate a map
    map = Map()
    # Main game loop: continues until the hero's health points (hp) drop to 0
    while hero.hp > 0:
        # Check if the hero has reached the exit ('f')
        if(map[hero.location[0]][hero.location[1]] == 'f'):
            print("Congratulation! You found the exit.")
            break
        # Display hero info
        print(hero)
        # Reveal the hero's current location on the map
        map.reveal(hero.location)
        print(map.show_map(hero.location))
        # Display movement options 
        print("1. Go North")
        print("2. Go South")
        print("3. Go East")
        print("4. Go West")
        # Get the player's movement choice
        option = check_input.get_int_range("Enter choice: ",1,4)

        letter = ""
        # Handle movement based on the player's choice
        match option:
            case 1: 
                letter = hero.go_north(map)
            case 2: 
                letter = hero.go_south(map)
            case 3: 
                letter = hero.go_east(map)
            case 4: 
                letter = hero.go_west(map)
        # Handle the result of the hero's movement
        match letter:
            case 'm': 
                monster = Enemy() # Create a new monster
                print("You encountered ", end ='')
                print(monster)
                # Combat loop
                while monster.hp > 0 and hero.hp > 0:
                    # Display combat options
                    print(f"1. Attack {monster.name}")
                    print("2. Run away")

                    # Get the player's combat choice
                    choice = check_input.get_int_range("Enter choice: ",1,2)
                    match choice: 
                        case 1: # Attack the monster
                            print(hero.attack(monster))
                            if(monster.hp > 0): # If the monster is still alive, attacks
                                print(monster.attack(hero))
                            if(hero.hp == 0): # If the hero dies
                                print(f"You have been slained by a {monster.name}")
                                break
                            else:  # If the monster dies
                                print(f"You have slain a {monster.name}")
                                map.remove_at_loc(hero.location)
                                break
                        case 2: # Run away from the monster
                            # Randomly move
                            match random.randint(1,4):
                                case 1: 
                                    hero.go_north(map)
                                case 2: 
                                    hero.go_south(map)
                                case 3: 
                                    hero.go_east(map)
                                case 4: 
                                    hero.go_west(map)
                            break

                            

            case 'o': # Invalid movement
                print("You cannot go that way")
            case 'n': # Empty space with no events
                print("There is nothing here")
            case 's': # Starting point
                print("You wound up back at the start of the dungeon")
            case 'i': # Found a health potion
                print("You found a Health Potion! You drink it to restore your health")
                hero.heal()
                map.remove_at_loc(hero.location)
            case 'f': # Found the exit
                print("Congratulation! You found the exit.")
                break
    # End of the game
    print("Game Over.")
    


if __name__ == "__main__":
    main()
