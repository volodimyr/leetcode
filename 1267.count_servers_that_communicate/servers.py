# 1267. Count Servers that communicate
# Topics: 'Array', 'Depth-First Search', 'Breadth-First Search', 'Union Find', 'Matrix', 'Counting'
# Level: 'Medium'

# You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

# Return the number of servers that communicate with any other server.

 

# Example 1:

# Input: grid = [[1,0],[0,1]]
# Output: 0
# Explanation: No servers can communicate with others.

# Example 2:

# Input: grid = [[1,0],[1,1]]
# Output: 3
# Explanation: All three servers can communicate with at least one other server.

# Example 3:

# Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# Output: 4
# Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.

 

# Constraints:

#     m == grid.length
#     n == grid[i].length
#     1 <= m <= 250
#     1 <= n <= 250
#     grid[i][j] == 0 or 1

from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        rcnt = [0] * ROWS
        ccnt = [0] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    rcnt[r] +=1
                    ccnt[c] += 1
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] and max(rcnt[r], ccnt[c]) > 1:
                    res+=1

        return res

# crazy...
# class Solution:
#     def countServers(self, grid: List[List[int]]) -> int:
#         ROWS, COLS = len(grid), len(grid[0])
#         ones = [(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 1]
#         visit = set()

#         for r, c in ones:
#             rtop = r-1
#             rbottom = r+1
        
#             while rtop != -1 :
#                 if grid[rtop][c] == 1:
#                     visit.add((rtop,c))
#                 rtop-=1
            
#             while rbottom != ROWS:
#                 if grid[rbottom][c] == 1:
#                     visit.add((rbottom,c))
#                 rbottom+=1
            
#             cright = c+1
#             cleft = c-1

#             while cright != COLS:
#                 if grid[r][cright] == 1:
#                     visit.add((r,cright))
#                 cright+=1

#             while cleft != -1:
#                 if grid[r][cleft] == 1:
#                     visit.add((r,cleft))
#                 cleft-=1
            

#         return len(visit)