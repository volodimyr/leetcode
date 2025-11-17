# 695. Max area of island
# Topics: 'Array', 'Depth-First Search', 'Breadth-First Search', 'Union Find', 'Matrix'
# Level: 'Medium'

# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

 

# Example 1:

# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.

# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0

 

# Constraints:

#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 50
#     grid[i][j] is either 0 or 1.

from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visits = set()
        def dfs(r: int, c: int) -> int:
            if min(r,c) < 0:
                return 0
            if r == ROWS or c == COLS:
                return 0
            if (r,c) in visits:
                return 0
            if grid[r][c] == 0:
                return 0
            visits.add((r,c))
            return 1+ dfs(r+1, c)+dfs(r-1,c)+dfs(r, c+1)+dfs(r, c-1)
        
        max_area = 0
        for row in range (ROWS):
            for col in range (COLS):
                if grid[row][col] == 1 and (row,col) not in visits:
                    max_area = max(max_area, dfs(row, col))
        return max_area