import unittest
from stock import Solution


class TestMaxProfitWithCooldown(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        prices = [1, 2, 3, 0, 2]
        self.assertEqual(self.solution.maxProfit(prices), 3)

    def test_example_2(self):
        prices = [1]
        self.assertEqual(self.solution.maxProfit(prices), 0)

    def test_empty_profit(self):
        prices = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.maxProfit(prices), 0)

    def test_single_transaction(self):
        prices = [1, 5]
        self.assertEqual(self.solution.maxProfit(prices), 4)

    def test_alternating_prices(self):
        prices = [1, 2, 1, 2, 1, 2]
        self.assertEqual(self.solution.maxProfit(prices), 2)

    def test_large_profit_with_cooldown(self):
        prices = [6, 1, 3, 2, 4, 7]
        self.assertEqual(self.solution.maxProfit(prices), 6)

    def test_zero_prices(self):
        prices = [0, 0, 0, 0]
        self.assertEqual(self.solution.maxProfit(prices), 0)

    def test_complex_case(self):
        prices = [2, 1, 4]
        self.assertEqual(self.solution.maxProfit(prices), 3)


if __name__ == "__main__":
    unittest.main()