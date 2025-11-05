import unittest
from typing import List
from defuse import Solution

class TestDecrypt(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
    
    # Example test cases
    def test_example1(self):
        self.assertEqual(self.s.decrypt([5,7,1,4], 3), [12,10,16,13])
    
    def test_example2(self):
        self.assertEqual(self.s.decrypt([1,2,3,4], 0), [0,0,0,0])
    
    def test_example3(self):
        self.assertEqual(self.s.decrypt([2,4,9,3], -2), [12,5,6,13])
    
    # Edge cases - k = 0
    def test_k_zero_single_element(self):
        self.assertEqual(self.s.decrypt([5], 0), [0])
    
    def test_k_zero_multiple_elements(self):
        self.assertEqual(self.s.decrypt([1,2,3,4,5], 0), [0,0,0,0,0])
    
    # Edge cases - single element array
    def test_single_element_k_positive(self):
        # Note: k can't be >= n, but k=0 is valid
        # Based on constraints: -(n-1) <= k <= n-1
        # For n=1: -0 <= k <= 0, so only k=0 is valid
        pass  # Covered by test_k_zero_single_element
    
    # Positive k cases
    def test_positive_k_no_wrap(self):
        self.assertEqual(self.s.decrypt([1,2,3,4,5], 2), [5,7,9,6,3])
    
    def test_positive_k_full_wrap(self):
        self.assertEqual(self.s.decrypt([1,2,3], 2), [5,4,3])
    
    def test_positive_k_equals_n_minus_1(self):
        self.assertEqual(self.s.decrypt([1,2,3,4], 3), [9,8,7,6])
    
    def test_positive_k_equals_1(self):
        self.assertEqual(self.s.decrypt([5,7,1,4], 1), [7,1,4,5])
    
    def test_negative_k_full_wrap(self):
        self.assertEqual(self.s.decrypt([1,2,3], -2), [5,4,3])
    
    def test_negative_k_equals_minus_n_minus_1(self):
        self.assertEqual(self.s.decrypt([1,2,3,4], -3), [9,8,7,6])
    
    def test_negative_k_equals_minus_1(self):
        self.assertEqual(self.s.decrypt([5,7,1,4], -1), [4,5,7,1])
    
    # Two element array
    def test_two_elements_k_positive(self):
        self.assertEqual(self.s.decrypt([3,5], 1), [5,3])
    
    def test_two_elements_k_negative(self):
        self.assertEqual(self.s.decrypt([3,5], -1), [5,3])
    
    # Large values
    def test_large_values(self):
        self.assertEqual(self.s.decrypt([100,100,100,100], 2), [200,200,200,200])
    
    # All same values
    def test_all_same_values_positive_k(self):
        self.assertEqual(self.s.decrypt([7,7,7,7,7], 2), [14,14,14,14,14])
    
    def test_all_same_values_negative_k(self):
        self.assertEqual(self.s.decrypt([7,7,7,7,7], -2), [14,14,14,14,14])

if __name__ == "__main__":
    unittest.main()