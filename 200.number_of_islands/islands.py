# 200. Number of islands
# Topics: 'Array', 'Depth-First Search', 'Breadth-First Search', 'Union Find', 'Matrix'
# Level: 'Medium'

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

# Constraints:

#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 300
#     grid[i][j] is '0' or '1'.

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
    
        def complete_island(r: int, c: int):
            if r < 0 or c < 0:
                return
            if r == ROWS or c == COLS:
                return
            if (r, c) in visited:
                return
            if grid[r][c] == '0':
                return
            
            visited.add((r,c))
            complete_island(r+1, c)
            complete_island(r-1, c)
            complete_island(r, c+1)
            complete_island(r, c-1)
            

        count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1' and (i,j) not in visited:
                    count += 1
                    complete_island(i, j)


        return count