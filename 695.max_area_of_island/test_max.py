import unittest
from typing import List
from max import Solution

class TestMaxAreaOfIsland(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        """Test with example 1 from problem statement"""
        grid = [
            [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]
        ]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 6)
    
    def test_example_2(self):
        """Test with all zeros (no islands)"""
        grid = [[0,0,0,0,0,0,0,0]]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 0)
    
    def test_single_cell_island(self):
        """Test with single cell island"""
        grid = [[1]]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 1)
    
    def test_single_cell_water(self):
        """Test with single cell water"""
        grid = [[0]]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 0)
    
    def test_entire_grid_is_island(self):
        """Test when entire grid is one island"""
        grid = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 9)
    
    def test_multiple_islands_different_sizes(self):
        """Test with multiple islands of different sizes"""
        grid = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]
        ]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 4)
    
    def test_diagonal_not_connected(self):
        """Test that diagonal cells are not considered connected"""
        grid = [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 1)
    
    def test_l_shaped_island(self):
        """Test L-shaped island"""
        grid = [
            [1, 0, 0],
            [1, 0, 0],
            [1, 1, 1]
        ]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 5)
    
    def test_snake_shaped_island(self):
        """Test snake-shaped island"""
        grid = [
            [1, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 1, 1, 0]
        ]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 7)
    
    def test_isolated_single_cells(self):
        """Test multiple isolated single-cell islands"""
        grid = [
            [1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1]
        ]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 1)
    
    def test_vertical_strip(self):
        """Test vertical strip island"""
        grid = [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 4)
    
    def test_horizontal_strip(self):
        """Test horizontal strip island"""
        grid = [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0]
        ]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 4)
    
    def test_complex_shape(self):
        """Test complex island shape"""
        grid = [
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1]
        ]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 14)
    
    def test_max_constraint_size(self):
        """Test with larger grid approaching constraint limits"""
        grid = [[1] * 20 for _ in range(20)]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 400)
    
    def test_checkerboard_pattern(self):
        """Test checkerboard pattern (no connected islands)"""
        grid = [
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1]
        ]
        self.assertEqual(self.solution.maxAreaOfIsland(grid), 1)


if __name__ == '__main__':
    unittest.main()