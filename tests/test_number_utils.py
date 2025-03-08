import unittest
from coe_number.number_utils import staircase, cat_and_mouse, caesar_cipher

class NumberUtilsTest(unittest.TestCase):
    def test_staircase(self):
        self.assertEqual(staircase(2, "#"), " #\n##")

    def test_cat_and_mouse(self):
        self.assertEqual(cat_and_mouse(2, 5, 4), "Cat B")

    def test_caesar_cipher(self):
        self.assertEqual(caesar_cipher("abc", 3), "def")

if __name__ == '__main__':  # pragma: no cover
    unittest.main()
