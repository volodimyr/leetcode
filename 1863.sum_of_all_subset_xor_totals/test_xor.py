import unittest
from functools import reduce
from typing import List
from xor import Solution

class TestSubsetXORSum(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        """Test case from problem: [1,3]"""
        # Subsets: [], [1], [3], [1,3]
        # XOR values: 0, 1, 3, 2
        # Sum: 0 + 1 + 3 + 2 = 6
        self.assertEqual(self.solution.subsetXORSum([1, 3]), 6)
    
    def test_example_2(self):
        """Test case from problem: [5,1,6]"""
        # Subsets: [], [5], [1], [6], [5,1], [5,6], [1,6], [5,1,6]
        # XOR values: 0, 5, 1, 6, 4, 3, 7, 2
        # Sum: 0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28
        self.assertEqual(self.solution.subsetXORSum([5, 1, 6]), 28)
    
    def test_example_3(self):
        """Test case from problem: [3,4,5,6,7,8]"""
        self.assertEqual(self.solution.subsetXORSum([3, 4, 5, 6, 7, 8]), 480)
    
    def test_single_element(self):
        """Single element array"""
        # Subsets: [], [5]
        # XOR values: 0, 5
        # Sum: 0 + 5 = 5
        self.assertEqual(self.solution.subsetXORSum([5]), 5)
    
    def test_two_same_elements(self):
        """Two identical elements"""
        # Subsets: [], [2], [2], [2,2]
        # XOR values: 0, 2, 2, 0
        # Sum: 0 + 2 + 2 + 0 = 4
        self.assertEqual(self.solution.subsetXORSum([2, 2]), 4)
    
    def test_all_zeros(self):
        """Array of zeros"""
        # All subsets XOR to 0
        self.assertEqual(self.solution.subsetXORSum([0, 0, 0]), 0)
    
    def test_with_zero(self):
        """Array containing zero"""
        # [0, 1]: Subsets [], [0], [1], [0,1]
        # XOR values: 0, 0, 1, 1
        # Sum: 0 + 0 + 1 + 1 = 2
        self.assertEqual(self.solution.subsetXORSum([0, 1]), 2)
    
    def test_powers_of_two(self):
        """Powers of 2: [1, 2, 4]"""
        # Subsets and their XOR:
        # [] = 0, [1] = 1, [2] = 2, [4] = 4
        # [1,2] = 3, [1,4] = 5, [2,4] = 6, [1,2,4] = 7
        # Sum: 0 + 1 + 2 + 4 + 3 + 5 + 6 + 7 = 28
        self.assertEqual(self.solution.subsetXORSum([1, 2, 4]), 28)
    
    def test_three_elements_simple(self):
        """Simple three element case"""
        # [1, 2, 3]
        # Subsets: [], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]
        # XOR: 0, 1, 2, 3, 3, 2, 1, 0
        # Sum: 0 + 1 + 2 + 3 + 3 + 2 + 1 + 0 = 12
        self.assertEqual(self.solution.subsetXORSum([1, 2, 3]), 12)
    
    def test_max_value(self):
        """Test with maximum allowed value (assuming constraint <= 1000)"""
        self.assertEqual(self.solution.subsetXORSum([1000]), 1000)


if __name__ == '__main__':
    unittest.main()