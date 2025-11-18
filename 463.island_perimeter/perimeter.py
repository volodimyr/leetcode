# 463. Island perimeter
# Topics: 'Matrix', 'Array', 'Depth-First Search', 'Breadth-First Search'

# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

# Example 1:

# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.

# Example 2:

# Input: grid = [[1]]
# Output: 4

# Example 3:

# Input: grid = [[1,0]]
# Output: 4

 

# Constraints:

#     row == grid.length
#     col == grid[i].length
#     1 <= row, col <= 100
#     grid[i][j] is 0 or 1.
#     There is exactly one island in grid.

from collections import deque
from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        perm = 0
        q = deque()
        visit = set()
        for i in range (len(grid)):
            for j in range (len(grid[i])):
                if grid[i][j] == 1:
                    q.append((i,j))
                    break
        
        while q:
            row, col = q.popleft()
            if min(row, col) < 0:
                continue
            if row == ROWS or col == COLS:
                continue
            if (row,col) in visit:
                continue
            if grid[row][col] != 1:
                continue
            visit.add((row,col))
            perm += self.calculate(grid, row, col)
            q.append((row+1, col))
            q.append((row-1, col))
            q.append((row, col+1))
            q.append((row, col-1))

        return perm
    
    def calculate(self, grid: List[List[int]], row: int, col: int) -> int:
        p = 4
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        for dr, dc in directions:
            if min(row+dr,col+dc) < 0:
                continue
            if row+dr == ROWS or col+dc == COLS:
                continue
            if grid[row+dr][col+dc] == 1:
                p-=1
        return p
