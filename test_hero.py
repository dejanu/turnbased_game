import unittest
from Heroes import Hero
from Spells import Spell



class TestHero(unittest.TestCase):

    
    def test_default_health(self):
        """ test init without args"""
        self.assertEqual(Hero("orderus").get_health(),70)

    def test_health_setter(self):
        """test health setter"""
        o = Hero("orderus")
        o.set_health(20)
        self.assertEqual(o.get_health(),95)
        

    # if Hero extends Spell then it must implement at least one spell
    def test_hero_base_class(self):
        """ test if Hero class subclasses Spell"""
        self.assertTrue(issubclass(Hero,Spell))

    def test_hero_rapidstrike(self):
        """ test if Hero class implements rapidstrike method"""
        o = Hero("orderus")
        self.assertTrue(hasattr(o,'rapid_strike')and callable(o.rapid_strike))

    def test_hero_magic_shield(self):
        """ test if Hero class implements magic_shield method"""
        o = Hero("orderus")
        self.assertTrue(hasattr(o,'magic_shield')and callable(o.magic_shield))
         
         


if __name__ == "__main__":

    unittest.main()
