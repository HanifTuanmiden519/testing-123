import unittest
from coe_number.number_utils import funny_string

class FunnyStringTest(unittest.TestCase):
    def test_funny_string_should_return_funny(self):
        self.assertEqual(funny_string("acxz"), "Funny")

    def test_funny_string_should_return_not_funny(self):
        self.assertEqual(funny_string("bcxz"), "Not Funny")

if __name__ == '__main__':
    unittest.main()
