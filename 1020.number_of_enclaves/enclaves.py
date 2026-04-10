# 1020. Number of Enclaves
# Topics: 'Array', 'Depth-First Search', 'Breadth-First Search', 'Union-Find', 'Matrix'
# Level: 'Medim'

# You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

# A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

# Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

# Example 1:

# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

# Example 2:

# Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Output: 0
# Explanation: All 1s are either on the boundary or can reach the boundary.

 

# Constraints:

#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 500
#     grid[i][j] is either 0 or 1.

from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        def can(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return (True, 0)  
            if grid[r][c] == 0 or (r, c) in visit:
                return (False, 0)

            visit.add((r, c))

            touches = False
            size = 1
            for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS:
                    touches = True
                    continue
                if grid[nr][nc] == 0 or (nr, nc) in visit:
                    continue

                t, s = can(nr, nc)
                if t:
                    touches = True
                size += s
            
            return (touches, size)
        
        visit = set()
        enclave = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    continue
                if (r,c) in visit:
                    continue
                t, s = can(r, c)
                if not t:
                    enclave += s

        return enclave

