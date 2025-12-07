# 286. Walls and Gates (Islands and Treasure)
# Topics: 'Breadh-First Search', 'Matrix'
# Level: 'Medium'

# You are given a m×nm×n 2D grid initialized with these three possible values:

#     -1 - A water cell that can not be traversed.
#     0 - A treasure chest.
#     INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.

# Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

# Assume the grid can only be traversed up, down, left, or right.

# Modify the grid in-place.

# Example 1:

# Input: [
#   [2147483647,-1,0,2147483647],
#   [2147483647,2147483647,2147483647,-1],
#   [2147483647,-1,2147483647,-1],
#   [0,-1,2147483647,2147483647]
# ]

# Output: [
#   [3,-1,0,1],
#   [2,2,1,-1],
#   [1,-1,2,-1],
#   [0,-1,3,4]
# ]

# Example 2:

# Input: [
#   [0,-1],
#   [2147483647,2147483647]
# ]

# Output: [
#   [0,-1],
#   [1,2]
# ]

# Constraints:

#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 100
#     grid[i][j] is one of {-1, 0, 2147483647}

from collections import deque
from typing import List

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
        
