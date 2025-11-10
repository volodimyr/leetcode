import unittest
from typing import List

from single import Solution

class TestSingleNonDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    # Example test cases from problem
    def test_example1(self):
        nums = [1,1,2,3,3,4,4,8,8]
        self.assertEqual(self.solution.singleNonDuplicate(nums), 2)
    
    def test_example2(self):
        nums = [3,3,7,7,10,11,11]
        self.assertEqual(self.solution.singleNonDuplicate(nums), 10)
    
    # Edge cases
    def test_single_element(self):
        nums = [1]
        self.assertEqual(self.solution.singleNonDuplicate(nums), 1)
    
    def test_single_at_beginning(self):
        nums = [1,2,2,3,3,4,4]
        self.assertEqual(self.solution.singleNonDuplicate(nums), 1)
    
    def test_single_at_end(self):
        nums = [1,1,2,2,3,3,4]
        self.assertEqual(self.solution.singleNonDuplicate(nums), 4)
    
    def test_three_elements(self):
        nums = [1,1,2]
        self.assertEqual(self.solution.singleNonDuplicate(nums), 2)
    
    def test_three_elements_single_at_start(self):
        nums = [1,2,2]
        self.assertEqual(self.solution.singleNonDuplicate(nums), 1)
    
    # Larger arrays
    def test_larger_array_single_in_middle(self):
        nums = [1,1,2,2,3,4,4,5,5,6,6]
        self.assertEqual(self.solution.singleNonDuplicate(nums), 3)
    
    def test_all_zeros_except_one(self):
        nums = [0,0,0,0,1,0,0]
        self.assertEqual(self.solution.singleNonDuplicate(nums), 1)
    
    def test_large_numbers(self):
        nums = [100000,100000,100001,100002,100002]
        self.assertEqual(self.solution.singleNonDuplicate(nums), 100001)
    
    # Position variations
    def test_single_at_second_position(self):
        nums = [1,1,2,3,3]
        self.assertEqual(self.solution.singleNonDuplicate(nums), 2)
    
    def test_single_at_second_to_last(self):
        nums = [1,1,2,2,3,4,4]
        self.assertEqual(self.solution.singleNonDuplicate(nums), 3)
    
    def test_longer_sequence(self):
        nums = [1,1,2,2,3,3,4,4,5,5,6,6,7,8,8,9,9]
        self.assertEqual(self.solution.singleNonDuplicate(nums), 7)
    
    # Duplicate values at different positions
    def test_same_value_appears_in_pairs(self):
        nums = [1,1,1,1,2,3,3,4,4]
        # This shouldn't happen per problem constraints, but testing robustness
        # Expected behavior may vary
        result = self.solution.singleNonDuplicate(nums)
        self.assertIn(result, [1, 2])  # Either could be valid interpretation


if __name__ == '__main__':
    unittest.main()