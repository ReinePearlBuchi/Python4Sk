import unittest

from assignment1 import *

class MyTestCase(unittest.TestCase):
    def test_that_this_is_a_list_of_number(self):
        number = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(number,[1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(True, False)



