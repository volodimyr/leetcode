import unittest
from typing import List
from islands import Solution

class TestNumIslands(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_basic_multiple_islands(self):
        """Test case with multiple distinct islands"""
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 1)
    
    def test_separate_islands(self):
        """Test case with clearly separated islands"""
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 3)
    
    def test_single_cell_island(self):
        """Test with single cell island"""
        grid = [["1"]]
        self.assertEqual(self.solution.numIslands(grid), 1)
    
    def test_single_cell_water(self):
        """Test with single cell of water"""
        grid = [["0"]]
        self.assertEqual(self.solution.numIslands(grid), 0)
    
    def test_all_water(self):
        """Test grid with only water"""
        grid = [
            ["0","0","0"],
            ["0","0","0"],
            ["0","0","0"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 0)
    
    def test_all_land(self):
        """Test grid with only land (one big island)"""
        grid = [
            ["1","1","1"],
            ["1","1","1"],
            ["1","1","1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 1)
    
    def test_diagonal_not_connected(self):
        """Test that diagonal cells are not considered connected"""
        grid = [
            ["1","0","1"],
            ["0","1","0"],
            ["1","0","1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 5)
    
    def test_complex_shape(self):
        """Test with complex island shapes"""
        grid = [
            ["1","1","0","0","1"],
            ["1","0","0","1","1"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 4)
    
    def test_snake_island(self):
        """Test with a snake-like connected island"""
        grid = [
            ["1","0","0","0"],
            ["1","1","0","0"],
            ["0","1","1","0"],
            ["0","0","1","1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 1)
    
    def test_vertical_line(self):
        """Test with vertical line island"""
        grid = [
            ["1"],
            ["1"],
            ["1"],
            ["1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 1)
    
    def test_horizontal_line(self):
        """Test with horizontal line island"""
        grid = [["1","1","1","1"]]
        self.assertEqual(self.solution.numIslands(grid), 1)
    
    def test_checkerboard_pattern(self):
        """Test with alternating pattern"""
        grid = [
            ["1","0","1","0"],
            ["0","1","0","1"],
            ["1","0","1","0"],
            ["0","1","0","1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 8)
    
    def test_large_grid_one_island(self):
        """Test with larger grid containing one island"""
        grid = [
            ["1","1","1","1","1"],
            ["1","0","0","0","1"],
            ["1","0","0","0","1"],
            ["1","0","0","0","1"],
            ["1","1","1","1","1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 1)
    
    def test_surrounded_water(self):
        """Test island surrounded by water"""
        grid = [
            ["0","0","0","0","0"],
            ["0","1","1","1","0"],
            ["0","1","0","1","0"],
            ["0","1","1","1","0"],
            ["0","0","0","0","0"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)