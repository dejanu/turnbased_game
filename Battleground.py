from Heroes import Hero, randint
from Creatures import Creature





class Battle():
    """class  that simulates a battle with max 20 turns"""

    def turn_counter(func):
        """decorator for counting function calls as turns """
        def helper(*args):
            helper.calls+=1
            print("Round number {0}".format(helper.calls))
            return func(*args)
    
        helper.calls=0
        return helper

    def __init__ (self, hero, creature):

        #create hero
        hero.charge_attack = False
        self.hero = hero
        

        #create creature
        creature.charge_attack = False
        self.creature = creature

    def __gt__(self,other):
        """ overload greater operator to
            determine which object attacks first
            """
        
        if self.hero.speed > other.creature.speed:
            self.hero.charge_attack = True
            print("{0} has first attack {1}".format(self.hero.name, self.hero.attack()))
           

        elif self.hero.speed == other.creature.speed:
            
            if self.hero.luck > self.creature.luck:
                print("{0} has first attack {1}".format(self.hero.name, self.hero.attack()))
                self.hero.charge_attack = True
               

            elif self.hero.luck ==  self.creature.luck:
                print("Same speed and same luck, what where the chances !!")
                if randint(0,1) == 1:
                    # hero charges
                    print("{0} has first attack {1}".format(self.hero.name, self.hero.attack()))
                    self.hero.charge_attack = True
                else:
                    # creature charges
                    print("{0} has first attack {1}".format(self.creature.name,self.creature.attack()))
                    self.creature.charge_attack = True
            else:
                print("{0} has first attack {1}".format(self.creature.name,self.creature.attack()))
                self.creature.charge_attack = True
                
        else:
                self.creature.charge_attack = True
                print("{0} has first attack {1}".format(self.creature.name,self.creature.attack()))
                
            

    @turn_counter
    def fight(self):
        """simulate fight"""
        
        # hero attacks first
        if self.hero.charge_attack == True:

            # test if creature got lucky and hero missed the attack
            if self.creature.get_lucky() == True:
                print("{0} got lucky and {1} missed his attack".format(self.creature.name, self.hero.name))

            else:
                #verify if hero has acquired rapid_strike
                if self.hero.rapid_strike() == True:
                    print("Hero {0} has acquired rapid_strike and delivered and attack of {1}".format(self.hero.name,self.hero.new_strength)) 
                    self.creature.set_health(self.hero.new_strength)
                
                else:
                    #self.hero.rapid_strike() == False:
                    print("{0} has delivered an attack of {1} ".format(self.hero.name, self.hero.attack()))
                    self.creature.set_health(self.hero.attack())

                
            # hero finished attack
            self.hero.charge_attack = False
            self.creature.charge_attack =  True
            
        # creature attacks first
        else:

            #verify if hero got lucky and creature missed the attack
            if self.hero.get_lucky() == True:
                print("{0} got lucky and {1} missed his attack".format(self.hero.name, self.creature.name))

            else:

                #verify if hero has acquired magic_shield
                if self.hero.magic_shield(self.creature.attack()) == True:
                    print("Hero {0} has acquired magic_shield".format(self.hero.name))
                    print("{0} has delivered an attack of {1}".format(self.creature.name, self.creature.attack()))

                else:
                    print("{0} has delivered an attack of {1}".format(self.creature.name, self.creature.attack()))
                    self.hero.set_health(self.creature.attack())

            # creature finished attack
            self.creature.charge_attack =  False
            self.hero.charge_attack = True

        return [self.hero, self.creature]
        

    @staticmethod
    def print_stats(obj1, obj2, verbose =  True):
        if isinstance(obj1,Hero) and isinstance(obj2, Creature):
            if verbose:
                print("{0} \n {1} \n ".format(obj1.__dict__, obj2.__dict__))
                print("-----------------------------------------------")
                
            else:
                print("{0} has health {1}".format(obj1.name, obj1.get_health()))
                print("{0} has health {1}".format(obj2.name, obj2.get_health()))
                print("-----------------------------------------------")
        else:
            raise TypeError("obj1 must be of type Hero and obj2 must be of type Creature")
        
        
    def check_winner(self):
        """ check who won the fight"""
        
        if self.hero.charge_attack == True and self.creature.charge_attack == False:
            print("Creature {0} has won".format(self.creature.name))
            return "Creature"
        elif self.hero.charge_attack == False and self.creature.charge_attack == True:
            print("Hero {0} has won".format(self.hero.name))
            return "Hero"
        else:
            raise ValueError

            
if __name__ == "__main__":

    # create players
    hero = Hero("Orderus", health = randint(70,100), strength = randint(70,80), defence = randint(45,55), speed = randint(40,50), luck = randint(10,30))
    creature = Creature("Beast", health = randint(60,90), strength = randint(60,90), defence = randint(40,60), speed = randint(40,60), luck = randint(25,40))
    
    
    print("Battle is starting.....\n")
    first_round = Battle(hero,creature)

    # check who attacks first
    first_round > first_round
    
    #battle as long as both obj have positive health
    while all(map(lambda x: x>0, [first_round.hero.get_health(), first_round.creature.get_health()])):
        
            Battle.print_stats(first_round.hero, first_round.creature, verbose=False)
            first_round.fight()

            #check if 20 turns where reached
            if first_round.fight.calls == 20:
                print("Number of max 20 turns has been reached")
                first_round.check_winner()
            
                
            

    first_round.check_winner()

    

    
    

    
    
    

    
