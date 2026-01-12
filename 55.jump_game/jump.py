# 55. Jump Game
# Topics: 'Array', 'Dynamic Programming', 'Greedy'
# Level: 'Medium'

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

 

# Constraints:

#     1 <= nums.length <= 104
#     0 <= nums[i] <= 105

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            j = nums[i]
            if i+j >= goal:
                goal = i
        
        return goal == 0

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         N = len(nums)
#         memo = {}
#         def jump(i):
#             if i >= N-1:
#                 return True
#             if i in memo:
#                 return memo[i]
            
#             if nums[i] == 0:
#                 memo[i] = False
#                 return memo[i]
            
#             j = nums[i]
#             while j > 0:
#                 if jump(i + j):
#                     memo[i] = True
#                     return True
#                 j-=1

#             memo[i] = False

#             return memo[i]
        
#         return jump(0)