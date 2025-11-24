import unittest
from typing import List
from robber import Solution

class TestHouseRobberII(unittest.TestCase):

    def setUp(self):
        """Set up the Solution instance before each test."""
        self.solution = Solution()

    def test_example_1(self):
        """Test case from Example 1: [2,3,2] -> 3"""
        nums = [2, 3, 2]
        self.assertEqual(self.solution.rob(nums), 3)

    def test_example_2(self):
        """Test case from Example 2: [1,2,3,1] -> 4"""
        nums = [1, 2, 3, 1]
        self.assertEqual(self.solution.rob(nums), 4)

    def test_example_3(self):
        """Test case from Example 3: [1,2,3] -> 3"""
        nums = [1, 2, 3]
        self.assertEqual(self.solution.rob(nums), 3)

    def test_single_house(self):
        """Test case with only one house."""
        nums = [5]
        self.assertEqual(self.solution.rob(nums), 5)

    def test_two_houses(self):
        """Test case with two houses, must rob the max of the two."""
        nums = [5, 8]
        # max(rob([5]), rob([8])) = 8
        self.assertEqual(self.solution.rob(nums), 8)

    def test_three_houses_all_same(self):
        """Test case with three houses of equal value, should rob one."""
        nums = [10, 10, 10]
        # max(rob([10, 10]), rob([10, 10])) = 10
        self.assertEqual(self.solution.rob(nums), 10)

    def test_four_houses_optimal_skips_circular(self):
        """Test case where the circular constraint matters: [10, 5, 2, 7]."""
        nums = [10, 5, 2, 7]
        # Exclude last [10, 5, 2] -> 10 + 2 = 12
        # Exclude first [5, 2, 7] -> 5 + 7 = 12
        self.assertEqual(self.solution.rob(nums), 12)

    def test_five_houses_complex_dp(self):
        """A longer case to test the DP logic."""
        nums = [4, 1, 2, 7, 5]
        # Exclude last [4, 1, 2, 7] -> (4 + 7) = 11
        # Exclude first [1, 2, 7, 5] -> (1 + 7) = 8 OR (2 + 5) = 7. Max 8
        self.assertEqual(self.solution.rob(nums), 11)

if __name__ == '__main__':
    unittest.main()