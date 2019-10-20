from functools import wraps
from Spells import Spell
from random import random


class Hero(Spell):
    """ template class to create heroes
        if subclass Spell means that hero can acquire spells and must implement them"""

    def __init__(self,name ,health = 70 ,strength = 70 ,defence = 45 ,speed = 40, luck = 10):
        self.name = name
        self._health = health
        self.strength = strength
        self.defence = defence
        self.speed = speed
        self.luck = luck

        #verify if hero has the posbility to implement spells
        self.blessed = issubclass(Hero,Spell)
        
    
    def damage(x):
        def deco(f):
            @wraps(f)
            def wrapper(self,*args):
                return  f(self,*args) - int(x)
            return wrapper
        return deco

    def get_health(self):
        """getter for _health"""
        return self._health

    
    def set_health(self, x):
        """damage as setter for _health"""  
        self._health = self._health + self.defence - x

    
    def attack(self):
       return self.strength
    
    def rapid_strike(self):
        # strike twice in his turn aka strength doubles
        
        super(Hero,self).__init__("rapidstrike",0.1)
        if random() <= self.percentage:
            self.new_strength = self.strength * 2
            return True
        else:
            return False

    def magic_shield(self,x):
        # takes half the damage 
        super(Hero,self).__init__("magicshield",0.2)
        if random() <= self.percentage:
            self._health = self._health + ((self.defence - x)//2)
            return True
        else:
            return False


    
    



if __name__ == "__main__":

    #create Hero objects with random values within the range

    from random import randint
    
    
    orderus = Hero("Orderus", health = randint(70,100), strength = randint(70,80), defence = randint(45,55), speed = randint(40,50), luck = randint(10,30))
    print(orderus.__dict__)
    
