import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self): # Test representation function
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    def test_eq1(self): # Test equal locations
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertTrue(loc1==loc2)

    def test_eq2(self): # Test equal locations differently
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc1,loc2)

    def test_not_eq1(self): # Test not equal locations
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Not_SLO", 36.0, 123)
        self.assertNotEqual(loc1,loc2)

    def test_not_eq2(self): # Test not equal locations, different names
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("San Luis Obispo", 35.3, -120.7)
        self.assertNotEqual(loc1,loc2)    
    
    def test_not_eq3(self): # Test not equal locations, different lons
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.2, -120.7)
        self.assertNotEqual(loc1,loc2)  

    def test_not_eq4(self): # Test not equal locations, different lats
        loc1 = Location("SLO", 35.3, -120.6)
        loc2 = Location("SLO", 35.2, -120.7)
        self.assertNotEqual(loc1,loc2)  

if __name__ == "__main__":
        unittest.main()
