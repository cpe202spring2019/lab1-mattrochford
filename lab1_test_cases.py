import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):

        # Test max_list_iter for full functionality

        print('Test #1.1')
        tlist1 = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist1)

        print('Test #1.2')
        tlist2 = []
        self.assertEqual(max_list_iter(tlist2),None) # Check empty lists

        print('Test #1.3')
        tlist3 = [0.023,199123,-234233,98.5]
        self.assertEqual(max_list_iter(tlist3),199123)

        print('Test #1.4')
        tlist4 = [0,-23234,-76,-0.00000001]
        self.assertEqual(max_list_iter(tlist4),0)



    # def test_reverse_rec(self):
    #     self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    # def test_bin_search(self):
    #     list_val =[0,1,2,3,4,7,8,9,10]
    #     low = 0
    #     high = len(list_val)-1
    #     self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

if __name__ == "__main__":
        unittest.main()

    
