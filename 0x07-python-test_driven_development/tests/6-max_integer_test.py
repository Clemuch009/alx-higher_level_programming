#!/usr/bin/python3


import unittest
from max_integer import  max_integer

class TestInteger(unittest.TestCase):
    
    def test_max_integer(self):
        lists = [5, 5, 6,-1, 0, 10, 4]
        result = max_integer(lists)
        self.assertEqual(result, 10)
        
        list_1 = []
        result_2 = max_integer([])
        self.assertEqual(result_2, None)

if __name__ == "__main__":
    unittest.main()
