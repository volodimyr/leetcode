import unittest
from typing import List

# Assuming the Solution class is in solution.py
from sum import Solution

class TestSubarraySum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_case(self):
        self.assertEqual(self.sol.subarraySum([1,1,1], 2), 2)

    def test_single_element_equal_to_k(self):
        self.assertEqual(self.sol.subarraySum([3], 3), 1)

    def test_single_element_not_equal_to_k(self):
        self.assertEqual(self.sol.subarraySum([3], 5), 0)

    def test_negative_numbers(self):
        self.assertEqual(self.sol.subarraySum([1, 2, 3, -2, 5], 6), 2)
        # Explanation: [1,2,3], [3,-2,5]

    def test_all_zeros_k_zero(self):
        self.assertEqual(self.sol.subarraySum([0,0,0], 0), 6)
        # All possible subarrays sum to 0: 3 singles, 2 doubles, 1 triple = 6

    def test_large_input(self):
        nums = [1]*10000
        self.assertEqual(self.sol.subarraySum(nums, 2), 9999)
        # every consecutive pair of 1's gives sum 2

    def test_no_subarray_found(self):
        self.assertEqual(self.sol.subarraySum([2, 4, 6], 5), 0)

if __name__ == "__main__":
    unittest.main()
