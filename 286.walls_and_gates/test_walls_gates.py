import unittest
from typing import List
from collections import deque

# --- Your Solution (copied for test execution) ---
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        for row in range (len(grid)):
            for col in range (len(grid[row])):
                if grid[row][col] == 0:
                    q.append((row, col))
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1,0], [0, 1], [0,-1]]
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if min(nr, nc) < 0:
                    continue
                if nr == ROWS or nc == COLS:
                    continue
                if grid[nr][nc] != 2147483647:
                    continue
                grid[nr][nc] = grid[row][col]+1
                q.append((nr,nc))


# --- Test Cases ---
class TestIslandsAndTreasure(unittest.TestCase):

    def test_example1(self):
        grid = [
            [2147483647,-1,0,2147483647],
            [2147483647,2147483647,2147483647,-1],
            [2147483647,-1,2147483647,-1],
            [0,-1,2147483647,2147483647]
        ]
        expected = [
            [3,-1,0,1],
            [2,2,1,-1],
            [1,-1,2,-1],
            [0,-1,3,4]
        ]
        Solution().islandsAndTreasure(grid)
        self.assertEqual(grid, expected)

    def test_example2(self):
        grid = [
            [0,-1],
            [2147483647,2147483647]
        ]
        expected = [
            [0,-1],
            [1,2]
        ]
        Solution().islandsAndTreasure(grid)
        self.assertEqual(grid, expected)

    def test_only_land_no_treasure(self):
        grid = [
            [2147483647,2147483647],
            [2147483647,2147483647]
        ]
        expected = [
            [2147483647,2147483647],
            [2147483647,2147483647]
        ]
        Solution().islandsAndTreasure(grid)
        self.assertEqual(grid, expected)

    def test_single_treasure_center(self):
        grid = [
            [2147483647,2147483647,2147483647],
            [2147483647,0,2147483647],
            [2147483647,2147483647,2147483647]
        ]
        expected = [
            [2,1,2],
            [1,0,1],
            [2,1,2]
        ]
        Solution().islandsAndTreasure(grid)
        self.assertEqual(grid, expected)

    def test_water_blocks(self):
        grid = [
            [0, -1, 2147483647],
            [-1, -1, 2147483647],
            [2147483647, -1, 2147483647]
        ]
        expected = [
            [0, -1, 2147483647],
            [-1, -1, 2147483647],
            [2147483647, -1, 2147483647]
        ]
        Solution().islandsAndTreasure(grid)
        self.assertEqual(grid, expected)

    def test_in_place_modification(self):
        grid = [[0, 2147483647]]
        Solution().islandsAndTreasure(grid)
        self.assertIs(grid, grid)  # Not replaced
        self.assertEqual(grid, [[0,1]])


if __name__ == "__main__":
    unittest.main()
