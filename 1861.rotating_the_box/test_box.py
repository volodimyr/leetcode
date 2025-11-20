import unittest
from typing import List
from box import Solution


class TestRotateTheBox(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1_single_row(self):
        """Test with single row, basic gravity"""
        grid = [["#", ".", "#"]]
        expected = [
            ["."],
            ["#"],
            ["#"]
        ]
        result = self.solution.rotateTheBox(grid)
        self.assertEqual(result, expected)
    
    def test_example_2_with_obstacles(self):
        """Test with obstacles blocking stones"""
        grid = [
            ["#", ".", "*", "."],
            ["#", "#", "*", "."]
        ]
        expected = [
            ["#", "."],
            ["#", "#"],
            ["*", "*"],
            [".", "."]
        ]
        result = self.solution.rotateTheBox(grid)
        self.assertEqual(result, expected)
    
    def test_example_3_larger_grid(self):
        """Test with larger grid and multiple obstacles"""
        grid = [
            ["#", "#", "*", ".", "*", "."],
            ["#", "#", "#", "*", ".", "."],
            ["#", "#", "#", ".", "#", "."]
        ]
        expected = [
            [".", "#", "#"],
            [".", "#", "#"],
            ["#", "#", "*"],
            ["#", "*", "."],
            ["#", ".", "*"],
            ["#", ".", "."]
        ]
        result = self.solution.rotateTheBox(grid)
        self.assertEqual(result, expected)
    
    def test_all_empty(self):
        """Test with all empty cells"""
        grid = [
            [".", ".", "."],
            [".", ".", "."]
        ]
        expected = [
            [".", "."],
            [".", "."],
            [".", "."]
        ]
        result = self.solution.rotateTheBox(grid)
        self.assertEqual(result, expected)
    
    def test_all_stones(self):
        """Test with all stones"""
        grid = [
            ["#", "#", "#"],
            ["#", "#", "#"]
        ]
        expected = [
            ["#", "#"],
            ["#", "#"],
            ["#", "#"]
        ]
        result = self.solution.rotateTheBox(grid)
        self.assertEqual(result, expected)
    
    def test_all_obstacles(self):
        """Test with all obstacles"""
        grid = [
            ["*", "*", "*"],
            ["*", "*", "*"]
        ]
        expected = [
            ["*", "*"],
            ["*", "*"],
            ["*", "*"]
        ]
        result = self.solution.rotateTheBox(grid)
        self.assertEqual(result, expected)
    
    def test_single_cell_stone(self):
        """Test with single cell containing a stone"""
        grid = [["#"]]
        expected = [["#"]]
        result = self.solution.rotateTheBox(grid)
        self.assertEqual(result, expected)
    
    def test_single_cell_empty(self):
        """Test with single cell that's empty"""
        grid = [["."]]
        expected = [["."]]
        result = self.solution.rotateTheBox(grid)
        self.assertEqual(result, expected)
    
    def test_single_cell_obstacle(self):
        """Test with single cell obstacle"""
        grid = [["*"]]
        expected = [["*"]]
        result = self.solution.rotateTheBox(grid)
        self.assertEqual(result, expected)
    
    def test_stones_already_at_bottom(self):
        """Test where stones are already in final position"""
        grid = [
            [".", ".", "#"],
            [".", ".", "#"]
        ]
        expected = [
            [".", "."],
            [".", "."],
            ["#", "#"]
        ]
        result = self.solution.rotateTheBox(grid)
        self.assertEqual(result, expected)
    
    def test_multiple_obstacles_in_row(self):
        """Test with multiple obstacles creating compartments"""
        grid = [["#", "*", "#", "*", "#"]]
        expected = [
            ["#"],
            ["*"],
            ["#"],
            ["*"],
            ["#"]
        ]
        result = self.solution.rotateTheBox(grid)
        self.assertEqual(result, expected)
    
    def test_stones_separated_by_empty(self):
        """Test stones with empty spaces between them"""
        grid = [["#", ".", ".", "#", ".", "#"]]
        expected = [
            ["."],
            ["."],
            ["."],
            ["#"],
            ["#"],
            ["#"]
        ]
        result = self.solution.rotateTheBox(grid)
        self.assertEqual(result, expected)
    
    def test_tall_narrow_grid(self):
        """Test with many rows, few columns"""
        grid = [
            ["#"],
            ["#"],
            ["#"],
            ["#"]
        ]
        expected = [["#", "#", "#", "#"]]
        result = self.solution.rotateTheBox(grid)
        self.assertEqual(result, expected)
    
    def test_wide_short_grid(self):
        """Test with few rows, many columns"""
        grid = [["#", ".", "#", ".", "#", "."]]
        expected = [
            ["."],
            ["."],
            ["."],
            ["#"],
            ["#"],
            ["#"]
        ]
        result = self.solution.rotateTheBox(grid)
        self.assertEqual(result, expected)
    
    def test_stones_stacking(self):
        """Test multiple stones stacking on obstacle"""
        grid = [["#", "#", "#", "*"]]
        expected = [
            ["#"],
            ["#"],
            ["#"],
            ["*"]
        ]
        result = self.solution.rotateTheBox(grid)
        self.assertEqual(result, expected)
    
    def test_no_gravity_needed(self):
        """Test where no stones need to fall"""
        grid = [
            ["*", "*", "*"],
            ["#", "#", "#"]
        ]
        expected = [
            ["#", "*"],
            ["#", "*"],
            ["#", "*"]
        ]
        result = self.solution.rotateTheBox(grid)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)