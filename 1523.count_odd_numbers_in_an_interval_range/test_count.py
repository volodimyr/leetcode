import unittest
from count import Solution


class TestCountOdds(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.countOdds(3, 7), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.countOdds(8, 10), 1)

    def test_single_even_number(self):
        self.assertEqual(self.solution.countOdds(4, 4), 0)

    def test_single_odd_number(self):
        self.assertEqual(self.solution.countOdds(5, 5), 1)

    def test_low_even_high_odd(self):
        self.assertEqual(self.solution.countOdds(2, 9), 4)  # 3,5,7,9

    def test_low_odd_high_even(self):
        self.assertEqual(self.solution.countOdds(3, 8), 3)  # 3,5,7

    def test_zero_range(self):
        self.assertEqual(self.solution.countOdds(0, 0), 0)

    def test_large_range(self):
        self.assertEqual(self.solution.countOdds(0, 10**9), 500_000_000)


if __name__ == "__main__":
    unittest.main()
