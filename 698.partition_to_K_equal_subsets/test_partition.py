import unittest
from partition import Solution


class TestCanPartitionKSubsets(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_true(self):
        nums = [4, 3, 2, 3, 5, 2, 1]
        k = 4
        self.assertTrue(self.sol.canPartitionKSubsets(nums, k))

    def test_example_false(self):
        nums = [1, 2, 3, 4]
        k = 3
        self.assertFalse(self.sol.canPartitionKSubsets(nums, k))

    def test_single_bucket(self):
        nums = [1, 2, 3, 4]
        k = 1
        self.assertTrue(self.sol.canPartitionKSubsets(nums, k))

    def test_each_element_bucket(self):
        nums = [1, 1, 1, 1]
        k = 4
        self.assertTrue(self.sol.canPartitionKSubsets(nums, k))

    def test_impossible_large_element(self):
        nums = [10, 1, 1, 1]
        k = 2
        self.assertFalse(self.sol.canPartitionKSubsets(nums, k))

    def test_all_same_elements(self):
        nums = [2, 2, 2, 2, 2, 2]
        k = 3
        self.assertTrue(self.sol.canPartitionKSubsets(nums, k))

    def test_zeroes(self):
        nums = [0, 0, 0, 0]
        k = 2
        self.assertTrue(self.sol.canPartitionKSubsets(nums, k))

    def test_large_k(self):
        nums = [1, 2, 3]
        k = 5
        self.assertFalse(self.sol.canPartitionKSubsets(nums, k))

    def test_complex_false(self):
        nums = [2, 2, 2, 2, 3, 4, 5]
        k = 4
        self.assertFalse(self.sol.canPartitionKSubsets(nums, k))

    def test_complex_true(self):
        nums = [2, 1, 4, 5, 6]
        k = 3
        self.assertTrue(self.sol.canPartitionKSubsets(nums, k))


if __name__ == "__main__":
    unittest.main()
