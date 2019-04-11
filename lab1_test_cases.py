import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    # bin_search test cases

    def test0_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 ) # Provided test case

    def test1_bin_search(self):
        tlist1 = [23,45,46,56,68,76,88,90,111,123,435,4355,9009]
        self.assertEqual(bin_search(76,0,len(tlist1)-1,tlist1),5) # Test search with result

    def test2_bin_search(self):
        tlist1 = [23,45,46,56,68,76,88,90,111,123,435,4355,9009]
        self.assertEqual(bin_search(78,0,len(tlist1)-1,tlist1),None) # Test search with no result

    def test3_bin_search(self):
        tlist1 = [23,45,46,56,68,76,88,90,111,123,435,4355,9009]
        self.assertEqual(bin_search(4355,0,len(tlist1)-1,tlist1),11) # Test search with result

    def test4_bin_search(self):
        tlist = [23,45,46,56,68,76,88,90,111,123,435,4355,9009]
        self.assertEqual(bin_search(4355.5,0,len(tlist)-1,tlist),None) # Test search with float

    def test5_bin_search(self):
        tlist = [23,45,46,56,68,76,88,90,111,435,4355,9009]
        self.assertEqual(bin_search(23,0,len(tlist)-1,tlist),0) # Test search for first location

    def test6_bin_search(self):
        with self.assertRaises(ValueError): # Check for none exception
            bin_search(44,0,12,None)   

    def test7_bin_search(self):
        tlist = [23,45,46,56,68,76,88,90,111,None,435,4355,9009]
        with self.assertRaises(ValueError): # Check for none exception
            bin_search(23,0,len(tlist)-1,tlist)  

    def test8_bin_search(self):
        tlist = [23,45,46,56,68,76,88,90,111,435,4355,9009]
        self.assertEqual(bin_search(9009,0,len(tlist)-1,tlist),11) # Test search for last location

    def test9_bin_search(self):
        tlist = [1,2,3,4]
        self.assertEqual(bin_search(1,-12,3,tlist),0)

    def test10_bin_search(self):
        tlist = [1,2,3,4]
        self.assertEqual(bin_search(1,0,5,tlist),0)

    # max_list_iter test cases

    def test0_max_list_iter(self):
        tlist1 = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist1)

    def test1_max_list_iter(self):
        tlist2 = []
        self.assertEqual(max_list_iter(tlist2),None) # Check empty lists

    def test2_max_list_iter(self):
        tlist3 = [0.023,199123,-234233,98.5]
        self.assertEqual(max_list_iter(tlist3),199123) # Check for max value

    def test3_max_list_iter(self):
        tlist4 = [0,-23234,-76,-0.00000001]
        self.assertEqual(max_list_iter(tlist4),0) # Check for max value with 0 and negatives

    # reverse_rec test cases

    def test0_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1]) # Check for reverse list

    def test1_reverse_rec(self):
        tlist1 = None
        with self.assertRaises(ValueError):  # used to check for None exception
            reverse_rec(tlist1)

    def test2_reverse_rec(self):
        self.assertEqual(reverse_rec([]),[]) # Check for empty list functionality

    def test3_reverse_rec(self):
        tlist2 = range(13,21) 
        self.assertEqual(reverse_rec(tlist2),[20,19,18,17,16,15,14,13]) # Check another longer list

 

if __name__ == "__main__":
        unittest.main()

    
