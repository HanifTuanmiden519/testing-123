from coe_number.number_utils import is_prime_list
import unittest

class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_4_should_not_be_prime(self):
        prime_list = [4]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_5_7_11_should_be_prime(self):
        prime_list = [5, 7, 11]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_6_8_9_should_not_be_prime(self):
        prime_list = [6, 8, 9]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_2_should_be_prime(self):
        prime_list = [2]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

if __name__ == '__main__':
    unittest.main()
