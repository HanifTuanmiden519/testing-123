import unittest
from coe_number.number_utils import alternating_characters

class AlternatingCharactersTest(unittest.TestCase):
    def test_should_return_3(self):
        self.assertEqual(alternating_characters("AAAA"), 3)

    def test_should_return_4(self):
        self.assertEqual(alternating_characters("AAABBB"), 4)

if __name__ == '__main__':
    unittest.main()
