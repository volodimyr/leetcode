# 64. Minimum Path Sum
# Topics: 'Dynamic Programming', 'Array', 'Matrix'
# Level: 'Medium'

# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

 

# Example 1:

# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

# Example 2:

# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12

# Constraints:

#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 200
#     0 <= grid[i][j] <= 200

import math
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        from functools import lru_cache
        @lru_cache(None)
        def dfs(r, c):
            if min(r, c) < 0:
                return math.inf
            if r == ROWS or c == COLS:
                return math.inf
            if r == ROWS-1 and c == COLS-1:
                return grid[r][c]
            return grid[r][c] + min(dfs(r+1,c), dfs(r, c+1))
        
        return dfs(0,0)