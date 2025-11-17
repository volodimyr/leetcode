from collections import deque
from typing import List
import unittest
from oranges import Solution

class TestOrangesRotting(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        """Standard case with rotting spreading"""
        grid = [[2,1,1],[1,1,0],[0,1,1]]
        self.assertEqual(self.solution.orangesRotting(grid), 4)
    
    def test_example_2(self):
        """Impossible case - isolated fresh orange"""
        grid = [[2,1,1],[0,1,1],[1,0,1]]
        self.assertEqual(self.solution.orangesRotting(grid), -1)
    
    def test_no_fresh_oranges(self):
        """No fresh oranges to rot"""
        grid = [[0,2]]
        self.assertEqual(self.solution.orangesRotting(grid), 0)
    
    def test_all_fresh_no_rotten(self):
        """All fresh, no rotten oranges"""
        grid = [[1,1,1],[1,1,1]]
        self.assertEqual(self.solution.orangesRotting(grid), -1)
    
    def test_all_rotten(self):
        """All oranges already rotten"""
        grid = [[2,2],[2,2]]
        self.assertEqual(self.solution.orangesRotting(grid), 0)
    
    def test_single_fresh(self):
        """Single fresh orange next to rotten"""
        grid = [[2,1]]
        self.assertEqual(self.solution.orangesRotting(grid), 1)
    
    def test_single_rotten(self):
        """Only one rotten orange, no fresh"""
        grid = [[2]]
        self.assertEqual(self.solution.orangesRotting(grid), 0)
    
    def test_single_fresh_alone(self):
        """Single fresh orange, no rotten"""
        grid = [[1]]
        self.assertEqual(self.solution.orangesRotting(grid), -1)
    
    def test_empty_cells_only(self):
        """Grid with only empty cells"""
        grid = [[0,0],[0,0]]
        self.assertEqual(self.solution.orangesRotting(grid), 0)
    
    def test_multiple_rotten_sources(self):
        """Multiple rotten oranges spreading simultaneously"""
        grid = [[2,1,1],[1,1,1],[1,1,2]]
        self.assertEqual(self.solution.orangesRotting(grid), 2)
    
    def test_long_chain(self):
        """Linear chain of oranges"""
        grid = [[2,1,1,1,1,1]]
        self.assertEqual(self.solution.orangesRotting(grid), 5)
    
    def test_isolated_groups(self):
        """Fresh orange isolated by empty cells"""
        grid = [[2,1,0,1]]
        self.assertEqual(self.solution.orangesRotting(grid), -1)
    
    def test_large_grid(self):
        """Larger grid with complex pattern"""
        grid = [
            [2,1,1,0,0],
            [1,1,0,0,0],
            [0,0,0,1,2],
            [0,0,0,1,1]
        ]
        self.assertEqual(self.solution.orangesRotting(grid), 2)
    
    def test_square_grid(self):
        """Rotten in center spreading outward"""
        grid = [
            [1,1,1],
            [1,2,1],
            [1,1,1]
        ]
        self.assertEqual(self.solution.orangesRotting(grid), 2)
    
    def test_corner_rotten(self):
        """Rotten in corner"""
        grid = [
            [2,1,1],
            [1,1,1],
            [1,1,1]
        ]
        self.assertEqual(self.solution.orangesRotting(grid), 4)


if __name__ == '__main__':
    unittest.main()