# 1091. Shortest path in binary matrix
# Topics: 'Array', 'Matrix', 'Breadth-First Search'
# Level: 'Medium'

# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

#     All the visited cells of the path are 0.
#     All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

# The length of a clear path is the number of visited cells of this path.

 

# Example 1:

# Input: grid = [[0,1],[1,0]]
# Output: 2

# Example 2:

# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4

# Example 3:

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1

 

# Constraints:

#     n == grid.length
#     n == grid[i].length
#     1 <= n <= 100
#     grid[i][j] is 0 or 1

from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1:
            return -1
        length = 1
        visit = set()
        q = deque()
        q.append((0,0))
        visit.add((0,0))

        while q:
            for i in range (len(q)):
                row, col = q.popleft()
                if row == ROWS-1 and col == COLS-1:
                    return length
                directions = [
                # diagonals
                    [-1,-1], [-1, 1], [1, -1], [1, 1], 
                # straight
                    [0, 1], [0, -1], [1, 0], [-1, 0]
                ]
                for dr, dc in directions:
                    if min(row + dr, col+dc) < 0:
                        continue
                    if row + dr == ROWS or col + dc == COLS:
                        continue
                    if (row+dr, col+dc) in visit:
                        continue
                    if grid[row+dr][col+dc] == 1:
                        continue
                    visit.add((row+dr,col+dc))
                    q.append((row+dr, col+dc))
            length+=1
        return -1
