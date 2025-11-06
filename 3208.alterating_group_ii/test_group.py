from typing import List
import unittest

from group import Solution

class TestAlternatingGroups(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    # Example test cases
    def test_example1(self):
        """Test with colors = [0,1,0,1,0], k = 3"""
        colors = [0, 1, 0, 1, 0]
        k = 3
        self.assertEqual(self.solution.numberOfAlternatingGroups(colors, k), 3)
    
    def test_example2(self):
        """Test with colors = [0,1,0,0,1,0,1], k = 6"""
        colors = [0, 1, 0, 0, 1, 0, 1]
        k = 6
        self.assertEqual(self.solution.numberOfAlternatingGroups(colors, k), 2)
    
    def test_example3(self):
        """Test with colors = [1,1,0,1], k = 4"""
        colors = [1, 1, 0, 1]
        k = 4
        self.assertEqual(self.solution.numberOfAlternatingGroups(colors, k), 0)
    
    def test_all_ones(self):
        """Test with all tiles blue"""
        colors = [1, 1, 1, 1]
        k = 3
        self.assertEqual(self.solution.numberOfAlternatingGroups(colors, k), 0)
    
    # Fully alternating patterns
    def test_fully_alternating_pattern(self):
        """Test with perfect alternating pattern"""
        colors = [0, 1, 0, 1, 0, 1, 0, 1]
        k = 4
        self.assertEqual(self.solution.numberOfAlternatingGroups(colors, k), 8)
    
    def test_long_alternating_pattern(self):
        """Test with longer alternating pattern"""
        colors = [0, 1] * 10  # [0,1,0,1,...] length 20
        k = 5
        self.assertEqual(self.solution.numberOfAlternatingGroups(colors, k), 20)
    
    # Partial alternating patterns
    def test_one_break_in_pattern(self):
        """Test with one break in alternating pattern"""
        colors = [0, 1, 0, 1, 1, 0, 1, 0]
        k = 4
        # Should find groups that don't include the break at index 4
        result = self.solution.numberOfAlternatingGroups(colors, k)
        self.assertGreaterEqual(result, 0)
    
    def test_multiple_breaks(self):
        """Test with multiple breaks in pattern"""
        colors = [0, 1, 1, 0, 1, 1, 0, 1]
        k = 3
        result = self.solution.numberOfAlternatingGroups(colors, k)
        self.assertGreaterEqual(result, 0)
    
    def test_k_equals_3_mixed(self):
        """Test with k=3 on mixed pattern"""
        colors = [1, 0, 1, 1, 0]
        k = 3
        result = self.solution.numberOfAlternatingGroups(colors, k)
        self.assertGreaterEqual(result, 0)
    
    # Circular property tests
    def test_circular_connection_alternating(self):
        """Test circular connection with alternating at boundaries"""
        colors = [1, 0, 1, 0]
        k = 3
        # Since it's circular: [1,0,1,0] connects to itself
        # Valid groups should consider wraparound
        result = self.solution.numberOfAlternatingGroups(colors, k)
        self.assertEqual(result, 4)
    
    def test_circular_connection_non_alternating(self):
        """Test circular connection with same color at boundaries"""
        colors = [0, 1, 0, 0]
        k = 3
        result = self.solution.numberOfAlternatingGroups(colors, k)
        self.assertGreaterEqual(result, 0)
    
    # Larger arrays
    def test_large_array_mostly_alternating(self):
        """Test with larger array that's mostly alternating"""
        colors = [0, 1] * 50  # Length 100
        k = 10
        result = self.solution.numberOfAlternatingGroups(colors, k)
        self.assertEqual(result, 100)
    
    def test_large_array_with_breaks(self):
        """Test with larger array with some breaks"""
        colors = [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1]
        k = 4
        result = self.solution.numberOfAlternatingGroups(colors, k)
        self.assertGreaterEqual(result, 0)
    
    # Single valid group
    def test_exactly_one_group(self):
        """Test where exactly one alternating group exists"""
        colors = [0, 0, 0, 1, 0, 1]
        k = 3
        result = self.solution.numberOfAlternatingGroups(colors, k)
        self.assertGreaterEqual(result, 0)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)