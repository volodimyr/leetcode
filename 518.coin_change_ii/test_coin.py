import unittest
from coin import Solution


class TestCoinChangeII(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        amount = 5
        coins = [1, 2, 5]
        self.assertEqual(self.solution.change(amount, coins), 4)

    def test_example_2(self):
        amount = 3
        coins = [2]
        self.assertEqual(self.solution.change(amount, coins), 0)

    def test_example_3(self):
        amount = 10
        coins = [10]
        self.assertEqual(self.solution.change(amount, coins), 1)

    def test_zero_amount(self):
        amount = 0
        coins = [1, 2, 5]
        self.assertEqual(self.solution.change(amount, coins), 1)

    def test_no_coins(self):
        amount = 7
        coins = []
        self.assertEqual(self.solution.change(amount, coins), 0)

    def test_single_coin_multiple_ways(self):
        amount = 4
        coins = [1]
        self.assertEqual(self.solution.change(amount, coins), 1)

    def test_unsorted_coins(self):
        amount = 5
        coins = [5, 1, 2]
        self.assertEqual(self.solution.change(amount, coins), 4)

    def test_large_amount(self):
        amount = 100
        coins = [1, 5, 10, 25]
        self.assertEqual(self.solution.change(amount, coins), 242)


if __name__ == "__main__":
    unittest.main()
