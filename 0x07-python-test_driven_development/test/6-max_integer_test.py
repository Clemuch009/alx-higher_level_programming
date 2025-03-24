#!/usr/bin/python3
import unittest
from  6-max_integer import max_integer

class TestMaxinteger(unittest.TestCase):
    def test_positive_number(self):
          """Test case for a list of positive numbers"""
        self.assertEqual(max_integer([1,2,3,4,5,6]),6)
        self.assertEqual(max_integer([10, 40, 50]),50)

    def test_negative_number(self):
        """Test case for a list of negative numbers"""
        self.assertEqual(max_integer([-1,-2,-3]),-1)


    def test_single_number(self):
         """Test case for a list with a single element"""
        self.assertEqual(max_integer([7]),7)

    def test_duplicate_number(self):
         """Test case for a list with duplicate values"""
        self.assertEqual(max_integer([3,3]),3)

if __name__ == "__main__":
    unittest.main()


