# 45. Jump Game II
# Topics: 'Array', 'Dynamic Programming', 'Greedy'
# Level: 'Medium'

# You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

#     0 <= j <= nums[i] and
#     i + j < n

# Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2

 

# Constraints:

#     1 <= nums.length <= 104
#     0 <= nums[i] <= 1000
#     It's guaranteed that you can reach nums[n - 1].

from collections import deque
import heapq
import math
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        L, R = 0, 0
        steps = 0

        while R < len(nums)-1:
            farthest = 0
            for i in range(L, R+1):
                farthest = max(farthest, i+nums[i])

            L = R+1
            R = farthest
            steps += 1
        
        return steps


# O(n * M log k) :)
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return 0
#         h = []
#         for i in range(1, nums[0]+1):
#             heapq.heappush(h, (1, -i))
        
#         N = len(nums)-1
#         visited = set()
#         while h:
#             steps, i = heapq.heappop(h)
#             i = -i
#             visited.add(i)
#             if i >= N:
#                 return steps

#             for j in range(1, nums[i]+1):
#                 if (j+i) not in visited:
#                     heapq.heappush(h, (steps+1, -(j+i)))
#         return -1



# O(n^2) time solution
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         if len(nums) == 1:
#             return 0
#         q = deque()
#         for i in range(1, nums[0]+1):
#             q.append((i, 1))
        
#         N = len(nums)-1
#         visited = set()
#         while q:
#             i, steps = q.popleft()
#             visited.add(i)
#             if i >= N:
#                 return steps

#             for j in range(1, nums[i]+1):
#                 if (j+i) not in visited:
#                     q.append((j+i, steps+1))
        
#         return -1



# O(k^n) time solution
# class Solution:
#     def jump(self, nums: List[int]) -> int:
        
#         res = math.inf
#         def dfs(i, count):
#             nonlocal res
#             if i >= len(nums)-1:
#                 res = min(res, count)
#             else:
#                 for j in range(1, nums[i]+1):
#                     dfs(i+j, count+1)

#         dfs(0, 0)
#         return res