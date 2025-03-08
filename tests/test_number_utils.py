import unittest
from coe_number.number_utils import two_characters

class TwoCharactersTest(unittest.TestCase):
    def test_should_return_5(self):
        self.assertEqual(two_characters("beabeefeab"), 5)

    def test_should_return_2(self):
        self.assertEqual(two_characters("abcd"), 2)

if __name__ == '__main__':
    unittest.main()
