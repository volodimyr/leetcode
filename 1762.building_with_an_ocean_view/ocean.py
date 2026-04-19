# 1762. Building With an Ocean View
# Topics: 'Stack', 'Array', 'Monotonic Stack'
# Level: 'Medium'

# You are given an array of integers heights of size n representing a row of buildings, where heights[i] is the height of the ith building.

# There is an ocean located to the far right of the buildings. A building has an ocean view if every building to its right is strictly shorter than it.

# Return a list of indices (0-indexed) of the buildings that have an ocean view, sorted in increasing order.

# Example 1:

# Input: heights = [4,2,3,2,1]

# Output: [0,2,3,4]

# Example 2:

# Input: heights = [1,3,2,4,2,5,1]

# Output: [5,6]

# Example 3:

# Input: heights = [9,8,7,7,6,5,4,3]

# Output: [0,1,3,4,5,6,7]

# Constraints:

#     1 <= heights.length <= 100,000.
#     1 <= heights[i] <= 1,000,000,000


from collections import deque
from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = deque()
        res.append(len(heights)-1)
        tallest = heights[len(heights)-1]
        
        for i in range(len(heights)-2, -1, -1):
            if heights[i] <= tallest:
                continue
            else:
                tallest = heights[i]
                res.appendleft(i)
        
        return list(res)