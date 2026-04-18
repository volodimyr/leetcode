import unittest
from transactions import Solution


class TestInvalidTransactions(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        result = self.sol.invalidTransactions(["alice,20,800,mtv", "alice,50,100,beijing"])
        self.assertCountEqual(result, ["alice,20,800,mtv", "alice,50,100,beijing"])

    def test_example2(self):
        result = self.sol.invalidTransactions(["alice,20,800,mtv", "alice,50,1200,mtv"])
        self.assertCountEqual(result, ["alice,50,1200,mtv"])

    def test_example3(self):
        result = self.sol.invalidTransactions(["alice,20,800,mtv", "bob,50,1200,mtv"])
        self.assertCountEqual(result, ["bob,50,1200,mtv"])

    def test_amount_over_1000(self):
        result = self.sol.invalidTransactions(["alice,20,1001,mtv"])
        self.assertCountEqual(result, ["alice,20,1001,mtv"])

    def test_exactly_1000_valid(self):
        result = self.sol.invalidTransactions(["alice,20,1000,mtv"])
        self.assertCountEqual(result, [])

    def test_exactly_60_min_diff_different_city(self):
        result = self.sol.invalidTransactions(["alice,0,500,mtv", "alice,60,500,beijing"])
        self.assertCountEqual(result, ["alice,0,500,mtv", "alice,60,500,beijing"])

    def test_61_min_diff_different_city(self):
        result = self.sol.invalidTransactions(["alice,0,500,mtv", "alice,61,500,beijing"])
        self.assertCountEqual(result, [])

    def test_same_city_within_60_min(self):
        result = self.sol.invalidTransactions(["alice,0,500,mtv", "alice,30,500,mtv"])
        self.assertCountEqual(result, [])

    def test_no_invalid(self):
        result = self.sol.invalidTransactions(["alice,20,500,mtv", "bob,50,300,nyc"])
        self.assertCountEqual(result, [])

    def test_multiple_names(self):
        result = self.sol.invalidTransactions(["alice,20,800,mtv", "alice,50,100,beijing", "bob,20,900,mtv", "bob,30,200,mtv"])
        self.assertCountEqual(result, ["alice,20,800,mtv", "alice,50,100,beijing"])


if __name__ == "__main__":
    unittest.main()
