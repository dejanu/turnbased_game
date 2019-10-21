from abc import ABC, abstractmethod


## Add spells here

class Spell(ABC):
    """ template for creating spells
        each character has to inherit Spells in order to implement their own behaviour of a certain spell
        """


    def __init__(self, skill_name, percentage):
         
        self.skill_name =  skill_name
        self.percentage = percentage
        print("Hero tried to learn {0} the chances where {1}".format(self.skill_name, self.percentage))

    @abstractmethod        
    def rapid_strike(self,*args, **kwargs): pass
        #raise NotImplementedError

    @abstractmethod
    def magic_shield(self,*args, **kwargs):pass
        #raise NotImplementedError

    



    
    

    
