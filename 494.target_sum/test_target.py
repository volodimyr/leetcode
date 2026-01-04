import unittest
from target import Solution

class TestFindTargetSumWays(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_basic_example(self):
        self.assertEqual(
            self.sol.findTargetSumWays([1,1,1,1,1], 3),
            5
        )

    def test_single_element_match(self):
        self.assertEqual(
            self.sol.findTargetSumWays([1], 1),
            1
        )

    def test_single_element_no_match(self):
        self.assertEqual(
            self.sol.findTargetSumWays([1], 2),
            0
        )

    def test_all_zeros_target_zero(self):
        # Each zero doubles the number of ways
        self.assertEqual(
            self.sol.findTargetSumWays([0,0,0], 0),
            8
        )

    def test_all_zeros_nonzero_target(self):
        self.assertEqual(
            self.sol.findTargetSumWays([0,0,0], 1),
            0
        )

    def test_negative_target(self):
        self.assertEqual(
            self.sol.findTargetSumWays([1,2,3], -2),
            1  # -1 -2 +3 = 0 ❌, +1 -2 -3 = -4 ❌, -1 +2 -3 = -2 ✅
        )

    def test_empty_nums(self):
        self.assertEqual(
            self.sol.findTargetSumWays([], 0),
            1
        )
        self.assertEqual(
            self.sol.findTargetSumWays([], 1),
            0
        )

    def test_large_values(self):
        self.assertEqual(
            self.sol.findTargetSumWays([1000, 1000], 0),
            2
        )

if __name__ == "__main__":
    unittest.main()
