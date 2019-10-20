from abc import ABC, abstractmethod

class Spell(ABC):
    """ template for creating spells"""


    def __init__(self, skill_name, percentage):
         
        self.skill_name =  skill_name
        self.percentage = percentage
        print("Hero tried acquired {0} the chances where {1}".format(self.skill_name, self.percentage))

    @abstractmethod        
    def rapid_strike(self,*args, **kwargs): pass
        #raise NotImplementedError

    @abstractmethod
    def magic_shield(self,*args, **kwargs):pass
        #raise NotImplementedError

    



    
    

    
