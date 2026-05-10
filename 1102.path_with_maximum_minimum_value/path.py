# 1102. Path With Maximum Minimum Value
# Topics: 'Array', 'Binary Search', 'Depth-First Search', 'Bredth-First Search', 'Union Find', 'Heap (Priroty Queue)', 'Matrix'
# Level: 'Medium'

# Given an m x n integer matrix grid, return the maximum score of a path starting at (0, 0) and ending at (m - 1, n - 1) moving in the 4 cardinal directions.

# The score of a path is the minimum value in that path.

#     For example, the score of the path 8 → 4 → 5 → 9 is 4.


# Example 1:

# Input: grid = [[5,4,5],[1,2,6],[7,4,6]]

# Output: 4

# Explanation: The path with the maximum score is highlighted in yellow.

# Example 2:

# Input: grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]

# Output: 2

# Example 3:

# Input: grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]

# Output: 3


# Constraints:

#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 100
#     0 <= grid[i][j] <= 10⁹


import heapq
from typing import List

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        r, c = 0, 0
        max_heap = [(-grid[r][c], r, c)]

        res = grid[r][c]
        
        visit = set()
        visit.add((r,c))
        while True:
            val, r, c = heapq.heappop(max_heap)
            val = -val
            res = min(res, val)
            if r == ROWS-1 and c == COLS-1:
                break
            
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nr, nc = r+dr, c+dc
                if min(nr,nc) < 0:
                    continue
                if nr == ROWS or nc == COLS:
                    continue
                if (nr,nc) in visit:
                    continue
                visit.add((nr,nc))
                heapq.heappush(max_heap, (-grid[nr][nc], nr, nc))
        
        return res


