import unittest
from knapsack import Solution

class TestMaximumProfit(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_case(self):
        profit = [60, 100, 120]
        weight = [10, 20, 30]
        capacity = 50
        expected = 220
        self.assertEqual(self.sol.maximumProfit(profit, weight, capacity), expected)

    def test_zero_capacity(self):
        profit = [10, 20, 30]
        weight = [1, 2, 3]
        capacity = 0
        expected = 0
        self.assertEqual(self.sol.maximumProfit(profit, weight, capacity), expected)

    def test_single_item_fits(self):
        profit = [50]
        weight = [5]
        capacity = 5
        expected = 50
        self.assertEqual(self.sol.maximumProfit(profit, weight, capacity), expected)

    def test_single_item_too_heavy(self):
        profit = [50]
        weight = [10]
        capacity = 5
        expected = 0
        self.assertEqual(self.sol.maximumProfit(profit, weight, capacity), expected)

    def test_all_items_fit(self):
        profit = [10, 20, 30]
        weight = [1, 2, 3]
        capacity = 6
        expected = 60
        self.assertEqual(self.sol.maximumProfit(profit, weight, capacity), expected)

    def test_no_items(self):
        profit = []
        weight = []
        capacity = 10
        expected = 0
        self.assertEqual(self.sol.maximumProfit(profit, weight, capacity), expected)

if __name__ == '__main__':
    unittest.main()