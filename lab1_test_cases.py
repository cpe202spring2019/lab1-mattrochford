import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_bin_search(self):

        print('\nTest #1.1')
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 ) # Provided test case

        print('Test #1.2')
        tlist1 = [23,45,46,56,68,76,88,90,111,123,435,4355,9009]
        self.assertEqual(bin_search(76,0,len(tlist1)-1,tlist1),5) # Test search with result

        print('Test #1.3')
        self.assertEqual(bin_search(78,0,len(tlist1)-1,tlist1),[]) # Test search with no result

        print('Test #1.4')
        self.assertEqual(bin_search(4355,0,len(tlist1)-1,tlist1),11) # Test search with result

        print('Test #1.5')
        with self.assertRaises(ValueError): # Check for none exception
            bin_search(44,0,12,None)   

    def test_max_list_iter(self):

        # Test max_list_iter for full functionality

        print('\nTest #2.1')
        tlist1 = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist1)

        print('Test #2.2')
        tlist2 = []
        self.assertEqual(max_list_iter(tlist2),None) # Check empty lists

        print('Test #2.3')
        tlist3 = [0.023,199123,-234233,98.5]
        self.assertEqual(max_list_iter(tlist3),199123) # Check for max value

        print('Test #2.4')
        tlist4 = [0,-23234,-76,-0.00000001]
        self.assertEqual(max_list_iter(tlist4),0) # Check for max value with 0 and negatives



    def test_reverse_rec(self):
        print('\nTest #3.1')
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1]) # Check for reverse list

        print('Test #3.2')
        tlist1 = None
        with self.assertRaises(ValueError):  # used to check for None exception
            max_list_iter(tlist1)

        print('Test #3.3')
        self.assertEqual(reverse_rec([]),[]) # Check for empty list functionality

        print('Test #3.4')
        tlist2 = range(13,21) 
        self.assertEqual(reverse_rec(tlist2),[20,19,18,17,16,15,14,13]) # Check another longer list

 

if __name__ == "__main__":
        unittest.main()

    
