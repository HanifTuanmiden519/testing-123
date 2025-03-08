import unittest
from coe_number.number_utils import staircase

class StaircaseTest(unittest.TestCase):
    def test_give_2_with_hash_should_be_hh(self):
        n = 2
        pattern = '#'
        expected_output = " #\n##"
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)

    def test_give_4_with_star_should_be_staircase(self):
        n = 4
        pattern = '*'
        expected_output = "   *\n  **\n ***\n****"
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)

    def test_give_3_with_at_should_be_staircase(self):
        n = 3
        pattern = '@'
        expected_output = "  @\n @@\n@@@"
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)

    def test_give_1_should_return_single_symbol(self):
        n = 1
        pattern = '#'
        expected_output = "#"
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)

    def test_give_0_should_return_empty(self):
        n = 0
        pattern = '#'
        expected_output = ""
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)

    def test_give_negative_should_return_empty(self):
        n = -3
        pattern = '#'
        expected_output = ""
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()