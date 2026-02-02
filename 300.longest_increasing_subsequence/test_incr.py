import unittest
from incr import Solution


class TestLongestIncreasingSubsequence(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        self.assertEqual(self.sol.lengthOfLIS(nums), 4)

    def test_example_2(self):
        nums = [0, 1, 0, 3, 2, 3]
        self.assertEqual(self.sol.lengthOfLIS(nums), 4)

    def test_example_3(self):
        nums = [7, 7, 7, 7, 7, 7, 7]
        self.assertEqual(self.sol.lengthOfLIS(nums), 1)

    def test_single_element(self):
        self.assertEqual(self.sol.lengthOfLIS([42]), 1)

    def test_strictly_increasing(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.sol.lengthOfLIS(nums), 5)

    def test_strictly_decreasing(self):
        nums = [5, 4, 3, 2, 1]
        self.assertEqual(self.sol.lengthOfLIS(nums), 1)

    def test_with_negatives(self):
        nums = [-3, -2, -1, 0, 1]
        self.assertEqual(self.sol.lengthOfLIS(nums), 5)

    def test_mixed_values(self):
        nums = [3, 4, -1, 0, 6, 2, 3]
        self.assertEqual(self.sol.lengthOfLIS(nums), 4)

    def test_duplicates_and_growth(self):
        nums = [2, 2, 2, 1, 3, 4, 2, 5]
        self.assertEqual(self.sol.lengthOfLIS(nums), 4)

    def test_large_pattern(self):
        nums = list(range(100)) + list(range(100))
        self.assertEqual(self.sol.lengthOfLIS(nums), 100)


if __name__ == "__main__":
    unittest.main()
