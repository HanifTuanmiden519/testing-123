import unittest
from coe_number.number_utils import cat_and_mouse

class CatAndMouseTest(unittest.TestCase):
    def test_cat_b_should_win(self):
        self.assertEqual(cat_and_mouse(2, 5, 4), "Cat B")

    def test_cat_a_should_win(self):
        self.assertEqual(cat_and_mouse(1, 5, 2), "Cat A")

    def test_mouse_should_escape(self):
        self.assertEqual(cat_and_mouse(1, 3, 2), "Mouse C")

    def test_cat_a_should_win_when_closer(self):
        self.assertEqual(cat_and_mouse(10, 20, 12), "Cat A")

    def test_cat_b_should_win_when_closer(self):
        self.assertEqual(cat_and_mouse(30, 25, 28), "Cat B")

if __name__ == '__main__':
    unittest.main()