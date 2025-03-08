from coe_number.number_utils import staircase
import unittest

class StaircaseTest(unittest.TestCase):
    def test_give_2_with_hash_should_be_hh(self):
        # Arrange
        n = 2
        pattern = '#'
        expected_output = " #\n##"

        # Act
        result = staircase(n, pattern)

        # Assert
        self.assertEqual(result, expected_output, f"Should be:\n{expected_output}")

    def test_give_4_with_star_should_be_staircase(self):
        # Arrange
        n = 4
        pattern = '*'
        expected_output = "   *\n  **\n ***\n****"

        # Act
        result = staircase(n, pattern)

        # Assert
        self.assertEqual(result, expected_output, f"Should be:\n{expected_output}")

    def test_give_3_with_at_should_be_staircase(self):
        # Arrange
        n = 3
        pattern = '@'
        expected_output = "  @\n @@\n@@@"

        # Act
        result = staircase(n, pattern)

        # Assert
        self.assertEqual(result, expected_output, f"Should be:\n{expected_output}")

if __name__ == '__main__':
    unittest.main()
