import unittest
from Battleground import Battle
from Heroes import Hero
from Creatures import Creature

class TestBattle(unittest.TestCase):

    def test_max_turns(self):
        """ test if the calls fucntion attr increments corecttly"""
        
        b = Battle(Hero("foo"),Creature("bar"))
        for i in range(20):
            b.fight()

        self.assertEqual(b.fight.calls, 20)

    def test_check_winner_creature(self):
        """ test if the correct obj is declared winner"""
        
        h,c = Hero("foo"),Creature("bar")
        b = Battle(h,c)

        # mock
        h.charge_attack = True
        c.charge_attack = False

        self.assertEqual(b.check_winner(),"Creature")

    def test_check_winner_exception(self):
        """ test if the exception is raised"""

        h,c = Hero("foo"),Creature("bar")
        b = Battle(h,c)

        # mock
        h.charge_attack = False
        c.charge_attack = False

        self.assertRaises(ValueError,b.check_winner)

if __name__ == "__main__":

    unittest.main()
