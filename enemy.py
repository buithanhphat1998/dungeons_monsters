from entity import Entity
from hero import Hero
import random
class Enemy(Entity):
    def __init__(self):
        names = ["Goblin", "Vampire", "Ghoul", "Skeleton", "Zombie"]
        name = names[random.randint(0, len(names)-1)]
        hp = random.randint(4,8)
        super().__init__(name, hp)
    
    def attack(self, entity: Hero):
        dmg = random.randint(1,4)
        entity.take_damage(dmg)
        return f"{self._name} attacked {entity._name} for {dmg}."
