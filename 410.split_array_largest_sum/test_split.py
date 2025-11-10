import unittest
from typing import List
from split import Solution


class TestSplitArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    # Example test cases
    def test_example1(self):
        """[7,2,5,10,8], k=2 -> [7,2,5] and [10,8]"""
        self.assertEqual(self.solution.splitArray([7, 2, 5, 10, 8], 2), 18)
    
    def test_example2(self):
        """[1,2,3,4,5], k=2 -> [1,2,3] and [4,5]"""
        self.assertEqual(self.solution.splitArray([1, 2, 3, 4, 5], 2), 9)
    
    # Edge cases
    def test_k_equals_1(self):
        """When k=1, return sum of entire array"""
        self.assertEqual(self.solution.splitArray([1, 2, 3, 4, 5], 1), 15)
        self.assertEqual(self.solution.splitArray([10, 20, 30], 1), 60)
    
    def test_k_equals_array_length(self):
        """When k=len(nums), each element is its own subarray"""
        self.assertEqual(self.solution.splitArray([7, 2, 5, 10, 8], 5), 10)
        self.assertEqual(self.solution.splitArray([1, 2, 3, 4, 5], 5), 5)
    
    def test_single_element(self):
        """Single element array"""
        self.assertEqual(self.solution.splitArray([100], 1), 100)
    
    def test_two_elements(self):
        """Two elements with different k values"""
        self.assertEqual(self.solution.splitArray([1, 2], 1), 3)
        self.assertEqual(self.solution.splitArray([1, 2], 2), 2)
    
    # All same elements
    def test_all_same_elements(self):
        """All elements are the same"""
        self.assertEqual(self.solution.splitArray([5, 5, 5, 5], 2), 10)
        self.assertEqual(self.solution.splitArray([3, 3, 3, 3, 3, 3], 3), 6)
    
    # Large numbers
    def test_large_numbers(self):
        """Test with large numbers (up to 10^6)"""
        self.assertEqual(self.solution.splitArray([1000000, 1000000], 2), 1000000)
        self.assertEqual(self.solution.splitArray([1000000, 500000, 500000], 2), 1000000)
    
    # Many zeros
    def test_with_zeros(self):
        """Array containing zeros"""
        self.assertEqual(self.solution.splitArray([0, 0, 0], 2), 0)
        self.assertEqual(self.solution.splitArray([1, 0, 0, 1], 2), 1)
    
    # Ascending/descending sequences
    def test_ascending_sequence(self):
        """Strictly ascending sequence"""
        self.assertEqual(self.solution.splitArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 15)
    
    def test_descending_sequence(self):
        """Strictly descending sequence"""
        self.assertEqual(self.solution.splitArray([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 5), 15)
    
    # One large element
    def test_one_large_element(self):
        """One element is much larger than others"""
        self.assertEqual(self.solution.splitArray([100, 1, 1, 1, 1], 2), 100)
        self.assertEqual(self.solution.splitArray([1, 1, 1, 1, 100], 2), 100)
    
    # Realistic scenarios
    def test_realistic_split(self):
        """More realistic splitting scenarios"""
        self.assertEqual(self.solution.splitArray([10, 5, 13, 4, 8, 4, 5, 11, 14, 9, 16, 10, 20, 8], 8), 25)
    
    def test_k_almost_array_length(self):
        """k is close to array length"""
        self.assertEqual(self.solution.splitArray([1, 2, 3, 4, 5, 6], 5), 6)
    
    # Boundary conditions
    def test_minimum_constraints(self):
        """Test minimum constraint values"""
        self.assertEqual(self.solution.splitArray([0], 1), 0)
    
    def test_balanced_split(self):
        """Test where optimal split is balanced"""
        # [1,2,3,4,5,6,7,8,9] with k=3
        # Optimal: [1,2,3,4,5], [6,7], [8,9] -> max = 17
        self.assertEqual(self.solution.splitArray([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), 17)


if __name__ == '__main__':
    unittest.main(verbosity=2)