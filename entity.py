from abc import ABC, abstractmethod

class Entity(ABC):
    """Attributes:
    Abstract base class representing a generic entity in the game.

    <<get>>_name (str): 
        The name of the entity
    <<get>> _hp:(int):
        The current health points of the entity.
    _max_hp:(int)
        The maximum health points of the entity.
    """

    def __init__(self, name, max_hp):
        """
        Initializes the Entity object.

        Args:
            name (str): The name of the entity.
            max_hp (int): The maximum health points of the entity.
        """
        self._name = name 
        self._max_hp = max_hp
        self._hp = max_hp
    
    @property
    def name(self):
        """
        Returns the name of the entity.

        Returns:
            str: The name of the entity.
        """
        return self._name
    @property
    def hp(self):
        """
        Returns the current health points of the entity.

        Returns:
            int: The current health points of the entity.
        """
        return self._hp
    
    def heal(self):
        """
        Restores the entity's health points to the maximum value.
        """
        self._hp = self._max_hp

    def take_damage(self, dmg):
        """
        Reduces the entity's health points by the specified damage amount.

        Args:
            dmg (int): The amount of damage to inflict.
        """
        if(self._hp - dmg <= 0):  # If damage exceeds or equals current health, set health to 0
            self._hp = 0
        else:
            self._hp -= dmg # Subtract the damage from the current health
    
    def __str__(self):
        """
        Returns a string representation of the entity, including its name and health points.

        Returns:
            str: The string representation of the entity.
        """
        return f"{self._name}\nHP: {self._hp}/{self._max_hp}\n" 
    
    @abstractmethod
    def attack(self, entity):
        pass