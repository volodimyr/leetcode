import unittest
from coins import Solution


class TestArrangeCoins(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        self.assertEqual(self.sol.arrangeCoins(5), 2)

    def test_example_2(self):
        self.assertEqual(self.sol.arrangeCoins(8), 3)

    def test_small_values(self):
        self.assertEqual(self.sol.arrangeCoins(1), 1)
        self.assertEqual(self.sol.arrangeCoins(2), 1)
        self.assertEqual(self.sol.arrangeCoins(3), 2)
        self.assertEqual(self.sol.arrangeCoins(4), 2)

    def test_triangle_numbers(self):
        self.assertEqual(self.sol.arrangeCoins(6), 3)
        self.assertEqual(self.sol.arrangeCoins(10), 4)
        self.assertEqual(self.sol.arrangeCoins(15), 5)

    def test_large_values(self):
        self.assertEqual(self.sol.arrangeCoins(1000), 44)
        self.assertEqual(self.sol.arrangeCoins(2147483647), 65535)


if __name__ == "__main__":
    unittest.main()