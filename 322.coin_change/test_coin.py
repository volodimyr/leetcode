import unittest
from coin import Solution


class TestCoinChange(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    # --- Given examples ---
    def test_example_1(self):
        self.assertEqual(
            self.solution.coinChange([1, 2, 5], 11),
            3
        )

    def test_example_2(self):
        self.assertEqual(
            self.solution.coinChange([2], 3),
            -1
        )

    def test_example_3(self):
        self.assertEqual(
            self.solution.coinChange([1], 0),
            0
        )

    # --- Edge cases ---
    def test_amount_zero(self):
        self.assertEqual(
            self.solution.coinChange([2, 5, 10], 0),
            0
        )

    def test_single_coin_exact(self):
        self.assertEqual(
            self.solution.coinChange([7], 14),
            2
        )

    def test_single_coin_not_possible(self):
        self.assertEqual(
            self.solution.coinChange([7], 13),
            -1
        )

    # --- General correctness ---
    def test_unsorted_coins(self):
        self.assertEqual(
            self.solution.coinChange([5, 1, 2], 11),
            3
        )

    def test_large_amount(self):
        self.assertEqual(
            self.solution.coinChange([1, 3, 4], 100),
            25
        )

    def test_no_solution(self):
        self.assertEqual(
            self.solution.coinChange([4, 5], 3),
            -1
        )

    def test_multiple_optimal_paths(self):
        self.assertEqual(
            self.solution.coinChange([2, 3, 6], 6),
            1
        )


if __name__ == "__main__":
    unittest.main()
