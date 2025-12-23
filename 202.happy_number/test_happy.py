import unittest
from happy import Solution


class TestHappyNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_happy_number(self):
        self.assertTrue(self.solution.isHappy(19))

    def test_example_unhappy_number(self):
        self.assertFalse(self.solution.isHappy(2))

    def test_single_digit_happy(self):
        self.assertTrue(self.solution.isHappy(1))
        self.assertTrue(self.solution.isHappy(7))

    def test_single_digit_unhappy(self):
        self.assertFalse(self.solution.isHappy(4))
        self.assertFalse(self.solution.isHappy(9))

    def test_known_happy_numbers(self):
        happy_numbers = [10, 13, 19, 23, 28, 31, 32]
        for n in happy_numbers:
            with self.subTest(n=n):
                self.assertTrue(self.solution.isHappy(n))

    def test_known_unhappy_numbers(self):
        unhappy_numbers = [2, 3, 4, 5, 6, 8, 9, 11, 12]
        for n in unhappy_numbers:
            with self.subTest(n=n):
                self.assertFalse(self.solution.isHappy(n))

    def test_large_number(self):
        self.assertFalse(self.solution.isHappy(2**31 - 1))


if __name__ == "__main__":
    unittest.main()
