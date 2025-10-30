from abc import ABC, abstractmethod

class Entity(ABC):
    """Attributes:
    <<get>> _name: string
    <<get>> _hp: int
    _max_hp: int
    """

    def __init__(self, name, max_hp):
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp
    
    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp
    
    def heal(self):
        self._hp = self._max_hp

    def take_damage(self, dmg):
        if(self._hp - dmg <= 0):
            self._hp = 0
        else:
            self._hp -= dmg
    
    def __str__(self):
        return f"{self._name}\nHP: {self._hp}/{self._max_hp}\n" 
    
    @abstractmethod
    def attack(self, entity):
        pass