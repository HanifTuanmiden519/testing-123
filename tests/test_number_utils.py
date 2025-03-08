import unittest
from coe_number.number_utils import caesar_cipher

class CaesarCipherTest(unittest.TestCase):
    def test_should_shift_abc_by_3(self):
        self.assertEqual(caesar_cipher("abc", 3), "def")

    def test_should_keep_special_chars(self):
        self.assertEqual(caesar_cipher("Hello, World!", 5), "Mjqqt, Btwqi!")

if __name__ == '__main__':
    unittest.main()

