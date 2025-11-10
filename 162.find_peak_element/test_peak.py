from typing import List
import unittest

from peak import Solution

class TestFindPeakElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def is_peak(self, nums: List[int], idx: int) -> bool:
        """Helper to verify if an index is a valid peak"""
        n = len(nums)
        left_ok = idx == 0 or nums[idx] > nums[idx - 1]
        right_ok = idx == n - 1 or nums[idx] > nums[idx + 1]
        return left_ok and right_ok
    
    def test_example_1(self):
        """Example 1: [1,2,3,1]"""
        nums = [1, 2, 3, 1]
        result = self.solution.findPeakElement(nums)
        self.assertTrue(self.is_peak(nums, result))
        # Index 2 (value 3) is the only peak
        self.assertEqual(result, 2)
    
    def test_example_2(self):
        """Example 2: [1,2,1,3,5,6,4]"""
        nums = [1, 2, 1, 3, 5, 6, 4]
        result = self.solution.findPeakElement(nums)
        self.assertTrue(self.is_peak(nums, result))
        # Valid peaks are at index 1 (value 2) or index 5 (value 6)
        self.assertIn(result, [1, 5])
    
    def test_single_element(self):
        """Single element is always a peak"""
        nums = [1]
        result = self.solution.findPeakElement(nums)
        self.assertEqual(result, 0)
    
    def test_two_elements_ascending(self):
        """Two elements ascending: [1, 2]"""
        nums = [1, 2]
        result = self.solution.findPeakElement(nums)
        self.assertTrue(self.is_peak(nums, result))
        self.assertEqual(result, 1)
    
    def test_two_elements_descending(self):
        """Two elements descending: [2, 1]"""
        nums = [2, 1]
        result = self.solution.findPeakElement(nums)
        self.assertTrue(self.is_peak(nums, result))
        self.assertEqual(result, 0)
    
    def test_all_ascending(self):
        """Strictly ascending array"""
        nums = [1, 2, 3, 4, 5]
        result = self.solution.findPeakElement(nums)
        self.assertTrue(self.is_peak(nums, result))
        self.assertEqual(result, 4)  # Last element
    
    def test_all_descending(self):
        """Strictly descending array"""
        nums = [5, 4, 3, 2, 1]
        result = self.solution.findPeakElement(nums)
        self.assertTrue(self.is_peak(nums, result))
        self.assertEqual(result, 0)  # First element
    
    def test_peak_at_start(self):
        """Peak at the beginning"""
        nums = [5, 1, 2, 3, 4]
        result = self.solution.findPeakElement(nums)
        self.assertTrue(self.is_peak(nums, result))
        self.assertIn(result, [0, 4])  # Either first or last
    
    def test_peak_at_end(self):
        """Peak at the end"""
        nums = [1, 2, 3, 4, 5]
        result = self.solution.findPeakElement(nums)
        self.assertTrue(self.is_peak(nums, result))
        self.assertEqual(result, 4)
    
    def test_peak_in_middle(self):
        """Peak in the middle"""
        nums = [1, 2, 3, 2, 1]
        result = self.solution.findPeakElement(nums)
        self.assertTrue(self.is_peak(nums, result))
        self.assertEqual(result, 2)
    
    def test_multiple_peaks(self):
        """Multiple peaks exist"""
        nums = [1, 3, 2, 4, 1, 5, 3]
        result = self.solution.findPeakElement(nums)
        self.assertTrue(self.is_peak(nums, result))
        # Valid peaks at indices 1, 3, 5
        self.assertIn(result, [1, 3, 5])
    
    def test_valley_pattern(self):
        """Valley pattern: high-low-high"""
        nums = [5, 1, 5]
        result = self.solution.findPeakElement(nums)
        self.assertTrue(self.is_peak(nums, result))
        self.assertIn(result, [0, 2])
    
    def test_negative_numbers(self):
        """Array with negative numbers"""
        nums = [-1, -2, -3, -2, -1]
        result = self.solution.findPeakElement(nums)
        self.assertTrue(self.is_peak(nums, result))
        self.assertIn(result, [0, 4])
    
    def test_mixed_positive_negative(self):
        """Mixed positive and negative"""
        nums = [-5, -2, 0, -1, -3]
        result = self.solution.findPeakElement(nums)
        self.assertTrue(self.is_peak(nums, result))
        self.assertEqual(result, 2)  # 0 is the peak
    
    def test_large_numbers(self):
        """Large numbers near integer limits"""
        nums = [2**31 - 2, 2**31 - 1, 2**31 - 3]
        result = self.solution.findPeakElement(nums)
        self.assertTrue(self.is_peak(nums, result))
        self.assertEqual(result, 1)
    
    def test_zigzag_pattern(self):
        """Zigzag pattern"""
        nums = [1, 3, 2, 4, 3, 5, 4]
        result = self.solution.findPeakElement(nums)
        self.assertTrue(self.is_peak(nums, result))
        # Peaks at indices 1, 3, 5
        self.assertIn(result, [1, 3, 5])
    
    def test_longer_array(self):
        """Longer array with peak in middle"""
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5]
        result = self.solution.findPeakElement(nums)
        self.assertTrue(self.is_peak(nums, result))
        self.assertEqual(result, 9)  # Value 10 at index 9


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)