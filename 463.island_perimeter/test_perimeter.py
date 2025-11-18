import unittest
from collections import deque
from typing import List
from perimeter import Solution

class TestIslandPerimeter(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_single_cell(self):
        """Test with a single land cell"""
        grid = [[1]]
        self.assertEqual(self.solution.islandPerimeter(grid), 4)
    
    def test_single_cell_with_water(self):
        """Test single land cell surrounded by water"""
        grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        self.assertEqual(self.solution.islandPerimeter(grid), 4)
    
    def test_two_cells_horizontal(self):
        """Test two adjacent cells horizontally"""
        grid = [[1, 1]]
        self.assertEqual(self.solution.islandPerimeter(grid), 6)
    
    def test_two_cells_vertical(self):
        """Test two adjacent cells vertically"""
        grid = [
            [1],
            [1]
        ]
        self.assertEqual(self.solution.islandPerimeter(grid), 6)
    
    def test_example_1(self):
        """Test LeetCode Example 1"""
        grid = [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
        ]
        self.assertEqual(self.solution.islandPerimeter(grid), 16)
    
    def test_example_2(self):
        """Test LeetCode Example 2"""
        grid = [[1]]
        self.assertEqual(self.solution.islandPerimeter(grid), 4)
    
    def test_example_3(self):
        """Test LeetCode Example 3"""
        grid = [[1, 0]]
        self.assertEqual(self.solution.islandPerimeter(grid), 4)
    
    def test_square_island(self):
        """Test 2x2 square island"""
        grid = [
            [1, 1],
            [1, 1]
        ]
        self.assertEqual(self.solution.islandPerimeter(grid), 8)
    
    def test_3x3_square_island(self):
        """Test 3x3 square island"""
        grid = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        self.assertEqual(self.solution.islandPerimeter(grid), 12)
    
    def test_l_shaped_island(self):
        """Test L-shaped island"""
        grid = [
            [1, 0],
            [1, 0],
            [1, 1]
        ]
        self.assertEqual(self.solution.islandPerimeter(grid), 10)
    
    def test_island_at_corner(self):
        """Test island starting at top-left corner"""
        grid = [
            [1, 1, 0],
            [1, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(self.solution.islandPerimeter(grid), 8)
    
    def test_island_at_bottom_right(self):
        """Test island at bottom-right corner"""
        grid = [
            [0, 0, 0],
            [0, 0, 1],
            [0, 1, 1]
        ]
        self.assertEqual(self.solution.islandPerimeter(grid), 8)
    
    def test_long_horizontal_line(self):
        """Test long horizontal line of land"""
        grid = [[1, 1, 1, 1, 1]]
        self.assertEqual(self.solution.islandPerimeter(grid), 12)
    
    def test_long_vertical_line(self):
        """Test long vertical line of land"""
        grid = [
            [1],
            [1],
            [1],
            [1],
            [1]
        ]
        self.assertEqual(self.solution.islandPerimeter(grid), 12)
    
    def test_plus_shaped_island(self):
        """Test plus/cross shaped island"""
        grid = [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]
        ]
        self.assertEqual(self.solution.islandPerimeter(grid), 12)
    
    def test_complex_shape(self):
        """Test complex irregular shape"""
        grid = [
            [1, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1]
        ]
        self.assertEqual(self.solution.islandPerimeter(grid), 16)
    
    def test_snake_shape(self):
        """Test snake-like shape"""
        grid = [
            [1, 1, 0],
            [0, 1, 0],
            [0, 1, 1]
        ]
        self.assertEqual(self.solution.islandPerimeter(grid), 12)
    
    def test_all_water_except_one(self):
        """Test large grid with single land cell"""
        grid = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(self.solution.islandPerimeter(grid), 4)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)