from Heroes import Hero
from Creatures import Creature
from random import randint



class Battle():
    """template to simulate the battle"""



    def __init__ (self, hero, creature):

        #create hero
        hero.charge_attack = False
        self.hero = hero
        

        #create creature
        creature.charge_attack = False
        self.creature = creature

    def __gt__(self,other):
        """determine which object attaks first"""
        
        if self.hero.speed > other.creature.speed:
            self.hero.charge_attack = True
            #print("{0} has first attack {1}".format(self.hero.name, self.hero.attack()))
           

        elif self.hero.speed == other.creature.speed:
            
            if self.hero.luck > self.creature.luck:
                #print("{0} has first attack {1}".format(self.hero.name, self.hero.attack()))
                self.hero.charge_attack = True
               

            elif self.hero.luck ==  self.creature.luck:
                sys.exit("Same speed and same luck, what where the chances !!")
                
            else:
                #print("{0} has first attack {1}".format(self.creature.name,self.creature.attack()))
                self.creature.charge_attack = True
                
        else:
                self.creature.charge_attack = True
                #print("{0} has first attack {1}".format(self.creature.name,self.creature.attack()))
                
            


    def fight(self):
        """simulate fight"""
        
        # hero attacks first
        if self.hero.charge_attack == True:


            if self.hero.rapid_strike() == True:
                print(" Hero {0} has acquired rapid_strike and delivered and attack of {1}".format(self.hero.name,self.hero.new_strength)) 
                self.creature.set_health(self.hero.new_strength)
                
            else:
                #self.hero.rapid_strike() == False:
                print("{0} has delivered an attack of ".format(self.hero.name, self.hero.attack()))
                self.creature.set_health(self.hero.attack())

                
            # hero finished attack
            self.hero.charge_attack = False
            self.creature.charge_attack =  True
            
        # creature attacks first
        else:

            if self.hero.magic_shield(self.creature.attack()) == True:
                print(" Hero {0} has acquired magic_shield".format(self.hero.name))
                print("{0} has delivered an attack of {1}".format(self.creature.name, self.creature.attack()))

            else:
                print("{0} has delivered an attack of {1}".format(self.creature.name, self.creature.attack()))
                self.hero.set_health(self.creature.attack())

            # creature finished attack
            self.creature.charge_attack =  False
            self.hero.charge_attack = True

        return [self.hero, self.creature]
        

    @staticmethod
    def print_stats(obj1, obj2):
        if isinstance(obj1,Hero) and isinstance(obj2, Creature):
            print(obj1.__dict__)
            print(obj2.__dict__)
            print("----------------------------------")
        else:
            raise TypeError("obj1 must be of type Hero and obj2 must be of type Creature")
        

if __name__ == "__main__":

    # create players
    hero = Hero("Orderus", health = randint(70,100), strength = randint(70,80), defence = randint(45,55), speed = randint(40,50), luck = randint(10,30))
    creature = Creature("Beast", health = randint(60,90), strength = randint(60,90), defence = randint(40,60), speed = randint(40,60), luck = randint(25,40))
    
    

    first_round = Battle(hero,creature)

    # check who attacks first
    first_round > first_round
    
    #battle as long as both obj have positive health
    while all(map(lambda x: x>0, [first_round.hero.get_health(), first_round.creature.get_health()])):
            Battle.print_stats(first_round.hero, first_round.creature)
            first_round.fight()


    if first_round.hero.charge_attack == True:
        print("creature {0} has won".format(first_round.creature.name))
    else:
        print("hero {0} has won".format(first_round.hero.name))
    

    
    

    
    
    

    
