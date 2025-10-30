"""
CECS 277 – Lab 10 – Singleton

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
    # Get user's name
    name = input("What is your name, traverler? ")
    # instantiate a hero object
    hero = Hero(name, 5)
    # instantiate a map
    map = Map()
    
    while hero.hp > 0:

        if(map[hero.location[0]][hero.location[1]] == 'f'):
            print("Congratulation! You found the exit.")
            break
        # Display hero info
        print(hero)
        
        map.reveal(hero.location)
        print(map.show_map(hero.location))

        print("1. Go North")
        print("2. Go South")
        print("3. Go East")
        print("4. Go West")
        option = check_input.get_int_range("Enter choice: ",1,4)

        letter = ""
        match option:
            case 1: 
                letter = hero.go_north(map)
            case 2: 
                letter = hero.go_south(map)
            case 3: 
                letter = hero.go_east(map)
            case 4: 
                letter = hero.go_west(map)
        
        match letter:
            case 'm': 
                monster = Enemy()
                print("You encountered ", end ='')
                print(monster)

                while monster.hp > 0 and hero.hp > 0:
                    print(f"1. Attack {monster.name}")
                    print("2. Run away")

                    choice = check_input.get_int_range("Enter choice: ",1,2)
                    match choice: 
                        case 1:
                            print(hero.attack(monster))
                            if(monster.hp > 0):
                                print(monster.attack(hero))
                            if(hero.hp == 0):
                                print(f"You have been slained by a {monster.name}")
                                break
                            else: 
                                print(f"You have slain a {monster.name}")
                                map.remove_at_loc(hero.location)
                                break
                        case 2: 
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

                            

            case 'o':
                print("You cannot go that way")
            case 'n': 
                print("There is nothing here")
            case 's': 
                print("You wound up back at the start of the dungeon")
            case 'i':
                print("You found a Health Potion! You drink it to restore your health")
                hero.heal()
                map.remove_at_loc(hero.location)
            case 'f':
                print("Congratulation! You found the exit.")
                break
    print("Game Over.")
    


if __name__ == "__main__":
    main()
