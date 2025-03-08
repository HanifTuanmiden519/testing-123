import unittest
from coe_number.number_utils import grid_challenge

class GridChallengeTest(unittest.TestCase):
    def test_should_return_yes(self):
        self.assertEqual(grid_challenge(["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]), "YES")

    def test_should_return_no(self):
        self.assertEqual(grid_challenge(["abc", "lmp", "qrt"]), "NO")

if __name__ == '__main__':
    unittest.main()
