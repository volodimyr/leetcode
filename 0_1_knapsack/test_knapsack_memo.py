import unittest
from knapsack_memo import Solution


class TestMaximumProfit(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_basic_case(self):
        profit = [60, 100, 120]
        weight = [10, 20, 30]
        capacity = 50
        self.assertEqual(self.sol.maximumProfit(profit, weight, capacity), 220)

    def test_zero_capacity(self):
        profit = [10, 20, 30]
        weight = [1, 2, 3]
        capacity = 0
        self.assertEqual(self.sol.maximumProfit(profit, weight, capacity), 0)

    def test_single_item_fits(self):
        profit = [100]
        weight = [10]
        capacity = 10
        self.assertEqual(self.sol.maximumProfit(profit, weight, capacity), 100)

    def test_single_item_too_heavy(self):
        profit = [100]
        weight = [20]
        capacity = 10
        self.assertEqual(self.sol.maximumProfit(profit, weight, capacity), 0)

    def test_all_items_fit(self):
        profit = [10, 20, 30]
        weight = [1, 2, 3]
        capacity = 6
        self.assertEqual(self.sol.maximumProfit(profit, weight, capacity), 60)

    def test_some_items_fit(self):
        profit = [10, 40, 50, 70]
        weight = [1, 3, 4, 5]
        capacity = 8
        self.assertEqual(self.sol.maximumProfit(profit, weight, capacity), 110)

    def test_duplicate_weights_profits(self):
        profit = [10, 10, 10]
        weight = [5, 5, 5]
        capacity = 10
        self.assertEqual(self.sol.maximumProfit(profit, weight, capacity), 20)

    def test_large_capacity_small_items(self):
        profit = [1, 2, 3]
        weight = [1, 1, 1]
        capacity = 2
        self.assertEqual(self.sol.maximumProfit(profit, weight, capacity), 5)


if __name__ == "__main__":
    unittest.main()
