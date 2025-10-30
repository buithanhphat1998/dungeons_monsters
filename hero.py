from entity import Entity
import random
from map import Map
class Hero(Entity):
    """Attributes: 
    <<get>> _loc: int[]"""
    
    def __init__(self, name, max_hp):
        #Call the parent constructor by passing the current Hero's hp
        super().__init__(name, max_hp)
        self._loc = [0,0]
    
    @property
    def location(self):
        return self._loc
    
    def attack(self, entity : Entity):
        dmg = random.randint(2,25)
        entity.take_damage(dmg)
        return f"{self._name} attacked {entity._name} for {dmg} damage."
    

    #self._loc[0] : Row
    #self._loc[1] : Column 
    def go_north(self, map: Map):
        if(self._loc[0] - 1 < 0):
            return 'o'
        else:
            self._loc[0] -= 1
            return map[self._loc[0]][self._loc[1]]
    
    def go_south(self, map: Map):
        if(self._loc[0] + 1 >= len(map)):
            return 'o'
        else:
            self._loc[0] += 1
            return map[self._loc[0]][self._loc[1]]

    def go_east(self, map: Map):
        if(self._loc[1] + 1 >= len(map[0])):
            return 'o'
        else:
            self._loc[1] += 1
            return map[self._loc[0]][self._loc[1]]

    def go_west(self, map: Map):
        if(self._loc[1] - 1 <= 0):
            return 'o'
        else:
            self._loc[1] -= 1
            return map[self._loc[0]][self._loc[1]]