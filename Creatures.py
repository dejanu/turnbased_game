
class Creature():
    """template class
       to create beasts"""

    def __init__(self, name, health = 60, strength = 60, defence = 40, speed = 40, luck = 25):
        self.name = name
        self._health = health
        self.strength = strength
        self.defence = defence
        self.speed = speed
        self.luck = luck

    def get_health(self):
        """getter for _health"""
        return self._health

    
    def set_health(self, x):
        """damage as setter for health"""
        self._health = self._health +self.defence - x
        
    def attack(self):
        return self.strength
    


if __name__ == "__main__":

    #create Creature objects
    from random import randint
    
    
    beast = Creature("Beast", health = randint(70,100), strength = randint(70,80), defence = randint(45,55), speed = randint(40,50), luck = randint(10,30))
    print(beast.__dict__)

    print(beast.get_health())
    beast.set_health(100)
    print(beast.get_health())
