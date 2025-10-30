from entity import Entity
import random
from map import Map
class Hero(Entity):
    """
    Represents the hero character controlled by the player.
    Attributes: 
    <<get>> _loc: int[]
    The current location of the hero on the map, represented as [row, column].
    """
    
    def __init__(self, name, max_hp):
        """
        Initializes the Hero object.

        Args:
            name (str): The name of the hero.
            max_hp (int): The maximum health points of the hero.
        """
        #Call the parent constructor by passing the current Hero's hp
        super().__init__(name, max_hp)
        self._loc = [0,0] # Initialize the hero's starting location at the top-left corner 
    
    @property
    def location(self):
        """
        Returns the current location of the hero.

        Returns:
            list[int]: The hero's location as [row, column].
        """
        return self._loc
    
    def attack(self, entity : Entity):
        """
        Attacks another entity and deals random damage.

        Args:
            entity (Entity): The entity being attacked.

        Returns:
            str: A message describing the attack and the damage dealt.
        """
        dmg = random.randint(2,25) # Generate random damage between 2 and 25
        entity.take_damage(dmg) # Inflict damage on the target entity
        return f"{self._name} attacked {entity._name} for {dmg} damage."
    
    # Movement methods
    #self._loc[0] : Row
    #self._loc[1] : Column 
    def go_north(self, map: Map):
        """
        Moves the hero one tile north if possible.

        Args:
            map (Map): The map object representing the dungeon.

        Returns:
            str: The character at the new location, or 'o' if the move is invalid.
        """
        if(self._loc[0] - 1 < 0): # Check if moving north goes out of bounds
            return 'o' # 'o' indicates an invalid move
        else:
            self._loc[0] -= 1 # Move north by decreasing the row index
            return map[self._loc[0]][self._loc[1]]
    
    def go_south(self, map: Map):
        """
        Moves the hero one tile south if possible.

        Args:
            map (Map): The map object representing the dungeon.

        Returns:
            str: The character at the new location, or 'o' if the move is invalid.
        """
        if(self._loc[0] + 1 >= len(map)): # Check if moving south goes out of bounds
            return 'o' # 'o' indicates an invalid move
        else:
            self._loc[0] += 1  # Move south by increasing the row index
            return map[self._loc[0]][self._loc[1]] 

    def go_east(self, map: Map):
        """
        Moves the hero one tile east if possible.

        Args:
            map (Map): The map object representing the dungeon.
        Returns:
            str: The character at the new location, or 'o' if the move is invalid.
        """
        if(self._loc[1] + 1 >= len(map[0])): # Check if moving east goes out of bounds
            return 'o' # 'o' indicates an invalid move
        else:
            self._loc[1] += 1  # Move east by increasing the column index
            return map[self._loc[0]][self._loc[1]]

    def go_west(self, map: Map):
        """
        Moves the hero one tile west if possible.

        Args:
            map (Map): The map object representing the dungeon.

        Returns:
            str: The character at the new location, or 'o' if the move is invalid.
        """
        if(self._loc[1] - 1 <= 0): # Check if moving west goes out of bounds
            return 'o' # 'o' indicates an invalid move
        else:
            self._loc[1] -= 1 # Move west by decreasing the column index
            return map[self._loc[0]][self._loc[1]]