# 624. Maximum Distance in Arrays
# Topics: 'Array', 'Greedy'
# Level: 'Medium'

# You are given m arrays, where each array is sorted in ascending order.

# You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

# Return the maximum distance.

 

# Example 1:

# Input: arrays = [[1,2,3],[4,5],[1,2,3]]
# Output: 4
# Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.

# Example 2:

# Input: arrays = [[1],[1]]
# Output: 0

 

# Constraints:

#     m == arrays.length
#     2 <= m <= 105
#     1 <= arrays[i].length <= 500
#     -104 <= arrays[i][j] <= 104
#     arrays[i] is sorted in ascending order.
#     There will be at most 105 integers in all the arrays.

from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        res = 0
        for r in range(1, len(arrays)):
            res = max(res, max(abs(arrays[r][0]-max_val), abs(arrays[r][-1]-min_val)))
            min_val = min(min_val, arrays[r][0])
            max_val = max(max_val, arrays[r][-1])
        return res