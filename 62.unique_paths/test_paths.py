import unittest
from typing import Dict
from paths import Solution

class TestUniquePaths(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    # Example test cases
    def test_example1(self):
        """Test case from example 1: 3x7 grid"""
        self.assertEqual(self.solution.uniquePaths(3, 7), 28)
    
    def test_example2(self):
        """Test case from example 2: 3x2 grid"""
        self.assertEqual(self.solution.uniquePaths(3, 2), 3)
    
    # Edge cases
    def test_single_cell(self):
        """Test 1x1 grid - robot already at destination"""
        self.assertEqual(self.solution.uniquePaths(1, 1), 1)
    
    def test_single_row(self):
        """Test 1xN grid - only one path (all right moves)"""
        self.assertEqual(self.solution.uniquePaths(1, 5), 1)
        self.assertEqual(self.solution.uniquePaths(1, 10), 1)
    
    def test_single_column(self):
        """Test Mx1 grid - only one path (all down moves)"""
        self.assertEqual(self.solution.uniquePaths(5, 1), 1)
        self.assertEqual(self.solution.uniquePaths(10, 1), 1)
    
    # Small grids
    def test_2x2_grid(self):
        """Test 2x2 grid"""
        self.assertEqual(self.solution.uniquePaths(2, 2), 2)
    
    def test_2x3_grid(self):
        """Test 2x3 grid"""
        self.assertEqual(self.solution.uniquePaths(2, 3), 3)
    
    def test_3x3_grid(self):
        """Test 3x3 grid"""
        self.assertEqual(self.solution.uniquePaths(3, 3), 6)
    
    # Symmetry tests
    def test_symmetry(self):
        """Test that uniquePaths(m, n) == uniquePaths(n, m)"""
        self.assertEqual(
            self.solution.uniquePaths(4, 6),
            self.solution.uniquePaths(6, 4)
        )
        self.assertEqual(
            self.solution.uniquePaths(5, 7),
            self.solution.uniquePaths(7, 5)
        )
    
    # Larger grids
    def test_5x5_grid(self):
        """Test 5x5 grid"""
        self.assertEqual(self.solution.uniquePaths(5, 5), 70)
    
    def test_10x10_grid(self):
        """Test 10x10 grid"""
        self.assertEqual(self.solution.uniquePaths(10, 10), 48620)
    
    # Boundary constraint tests
    def test_max_small_dimension(self):
        """Test with reasonably large dimensions"""
        result = self.solution.uniquePaths(23, 12)
        # Verify it computes without error and returns reasonable value
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)
    
    def test_rectangular_grids(self):
        """Test various rectangular grids"""
        self.assertEqual(self.solution.uniquePaths(4, 5), 35)
        self.assertEqual(self.solution.uniquePaths(5, 4), 35)
        self.assertEqual(self.solution.uniquePaths(2, 10), 10)
    
    # Mathematical verification (using combinatorial formula)
    def test_combinatorial_formula(self):
        """Verify against combinatorial formula: C(m+n-2, m-1)"""
        from math import comb
        
        test_cases = [(2, 3), (3, 3), (4, 4), (5, 5), (3, 7)]
        for m, n in test_cases:
            expected = comb(m + n - 2, m - 1)
            actual = self.solution.uniquePaths(m, n)
            self.assertEqual(actual, expected, 
                           f"Failed for m={m}, n={n}: expected {expected}, got {actual}")
    
    # Performance test
    def test_large_grid_performance(self):
        """Test that larger grids complete in reasonable time"""
        import time
        start = time.time()
        result = self.solution.uniquePaths(50, 50)
        elapsed = time.time() - start
        
        self.assertIsInstance(result, int)
        self.assertGreater(result, 0)
        self.assertLess(elapsed, 1.0, "Should complete within 1 second")


if __name__ == '__main__':
    unittest.main()