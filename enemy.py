from entity import Entity
from hero import Hero
import random
class Enemy(Entity):
    """
    Represents an enemy entity in the game.

    Attributes:
    _name (str): 
        The name of the enemy, randomly chosen from a predefined list.
    _hp (int): 
        The current health points of the enemy, randomly generated within a range.
    _max_hp (int): 
        The maximum health points of the enemy, set to the same value as _hp.
    """
    def __init__(self):
        """
        Initializes the Enemy object with a random name and health points.
        """
        # List of possible enemy names
        names = ["Goblin", "Vampire", "Ghoul", "Skeleton", "Zombie"]
        # Randomly select a name from the list
        name = names[random.randint(0, len(names)-1)]
        # Randomly generate health points within the range of 4 to 8
        hp = random.randint(4,8)
        # Call the parent constructor to initialize the enemy's attributes
        super().__init__(name, hp)
    
    def attack(self, entity: Hero):
        """
        Attacks a hero entity and deals random damage.

        Args:
            entity (Hero): The hero being attacked.

        Returns:
            str: A message describing the attack and the damage dealt.
        """
        # Generate random damage between 1 and 4
        dmg = random.randint(1,4)
        # Inflict damage on the hero
        entity.take_damage(dmg)
        # Return a message describing the attack
        return f"{self._name} attacked {entity._name} for {dmg} damage."
