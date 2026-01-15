import unittest
from choco import Solution

class TestBuyTwoChocolates(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        prices = [1, 2, 2]
        money = 3
        self.assertEqual(self.solution.buyChoco(prices, money), 0)

    def test_example_2(self):
        prices = [3, 2, 3]
        money = 3
        self.assertEqual(self.solution.buyChoco(prices, money), 3)

    def test_exact_money(self):
        prices = [2, 3]
        money = 5
        self.assertEqual(self.solution.buyChoco(prices, money), 0)

    def test_more_than_two_prices(self):
        prices = [5, 1, 4, 2]
        money = 10
        # two cheapest are 1 and 2 → leftover = 7
        self.assertEqual(self.solution.buyChoco(prices, money), 7)

    def test_not_enough_money(self):
        prices = [4, 5, 6]
        money = 8
        self.assertEqual(self.solution.buyChoco(prices, money), 8)

    def test_all_same_prices(self):
        prices = [3, 3, 3]
        money = 6
        self.assertEqual(self.solution.buyChoco(prices, money), 0)

    def test_minimum_constraints(self):
        prices = [1, 1]
        money = 1
        self.assertEqual(self.solution.buyChoco(prices, money), 1)

    def test_large_values(self):
        prices = [100, 100, 100]
        money = 250
        self.assertEqual(self.solution.buyChoco(prices, money), 50)

if __name__ == "__main__":
    unittest.main()
