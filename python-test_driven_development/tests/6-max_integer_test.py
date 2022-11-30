#!/usr/bin/python3
"""max integer-unittest"""


import unittest
max_integer = __import__('6-max_integer').max_integer
class MaxInt(unittest.TestCase):
    def test_multiple_values(self):
        self.assertEqual(max_integer([5, 6, 7, 8, 9]), 9)
        self.assertEqual(max_integer([-5, -6, -7, -8, -9]), -5)
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([7, 8 ,5]), 8)\

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
    
    def test_one_elememt_list(self):
        self.assertEqual(max_integer9[1], 1)

    def test_one_element_list_negative(self):
        self.assertEqual(max_integer([-1]), -1)

if __name__ == '__main__':
    unittest.main()
