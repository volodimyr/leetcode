# 1765. Map of Highers Peak
# Topics: 'Array', 'Matrix', 'Breadth-First Search'
# Level: 'Medium'

# You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

#     If isWater[i][j] == 0, cell (i, j) is a land cell.
#     If isWater[i][j] == 1, cell (i, j) is a water cell.

# You must assign each cell a height in a way that follows these rules:

#     The height of each cell must be non-negative.
#     If the cell is a water cell, its height must be 0.
#     Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).

# Find an assignment of heights such that the maximum height in the matrix is maximized.

# Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.

 

# Example 1:

# Input: isWater = [[0,1],[0,0]]
# Output: [[1,0],[2,1]]
# Explanation: The image shows the assigned heights of each cell.
# The blue cell is the water cell, and the green cells are the land cells.

# Example 2:

# Input: isWater = [[0,0,1],[1,0,0],[0,0,0]]
# Output: [[1,1,0],[0,1,1],[1,2,2]]
# Explanation: A height of 2 is the maximum possible height of any assignment.
# Any height assignment that has a maximum height of 2 while still meeting the rules will also be accepted.

 

# Constraints:

#     m == isWater.length
#     n == isWater[i].length
#     1 <= m, n <= 1000
#     isWater[i][j] is 0 or 1.
#     There is at least one water cell.


from collections import deque
from typing import List

class Solution:
    def highestPeak(self, w: List[List[int]]) -> List[List[int]]:
        if not w:
            return w
        ROWS, COLS = len(w), len(w[0])
        q = deque()
        visit = set()
        for r in range(ROWS):
            for c in range(COLS):
                if w[r][c] == 1:
                    visit.add((r,c))
                    q.append((r,c,0))
        
        while q:
            r,c,d = q.popleft()
            w[r][c] = d
            for dr,dc in ((1,0),(0,1),(-1,0),(0,-1)):
                ndr,ndc = dr+r,dc+c
                if min(ndr,ndc) < 0:
                    continue
                if ndr >= ROWS or ndc >= COLS:
                    continue
                if (ndr,ndc) in visit:
                    continue
                visit.add((ndr,ndc))
                q.append((ndr,ndc,d+1))
        return w