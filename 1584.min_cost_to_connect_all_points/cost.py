# 1584. Min cost to connect all points
# Topics: 'Array', 'Union Find', 'Graph', 'Minumum Spanning Tree'
# Level: 'Medium'

# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

# Example 1:

# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation: 

# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.

# Example 2:

# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18

 

# Constraints:

#     1 <= points.length <= 1000
#     -106 <= xi, yi <= 106
#     All pairs (xi, yi) are distinct.


import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minheap = []
        for i in range (1, len(points)):
            dist = distance(points[0][0], points[0][1], points[i][0], points[i][1])
            heapq.heappush(minheap, (dist, points[i][0], points[i][1]))
        
        visit = set()
        total = 0
        visit.add((points[0][0], points[0][1]))
        while minheap:
            d, x, y = heapq.heappop(minheap)
            if (x,y) in visit:
                continue
            visit.add((x,y))
            total += d
            if len(visit) == len(points):
                return total
            for x1, y1 in points:
                if (x1,y1) not in visit:
                    dist = distance(x,y,x1,y1)
                    heapq.heappush(minheap, (dist, x1, y1))
        
        return 0


def distance(x1, y1, x2, y2) -> int:
    return abs(x1-x2) + abs(y1-y2)