# 918. Maximum sub circular subarray
# Topics: 'Array', 'Dynamic Programming', 'Queue', 'Monotonic Queue', 'Divide And Conquer'
# Level: 'Medium'

# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

# Example 1:

# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.

# Example 2:

# Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

# Example 3:

# Input: nums = [-3,-2,-3]
# Output: -2
# Explanation: Subarray [-2] has maximum sum -2.

 

# Constraints:

#     n == nums.length
#     1 <= n <= 3 * 104
#     -3 * 104 <= nums[i] <= 3 * 104

from typing import List

# class Solution:
#     def maxSubarraySumCircular(self, nums: List[int]) -> int:
#         total = nums[0]
#         curmax = maxsubarray = nums[0]
#         curmin = minsubarray = nums[0]
        
#         for i in range(1, len(nums)):
#             x = nums[i]
#             curmax = max(x, curmax + x)
#             maxsubarray = max(maxsubarray, curmax)
#             curmin = min(x, curmin + x)
#             minsubarray = min(minsubarray, curmin)
#             total += x
#         if maxsubarray < 0:
#             return maxsubarray
#         return max(maxsubarray, (total - minsubarray))
    

# O(n**2)
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        length = len(nums)
        maxsubarray = 0
        for start in range (length):
            id = start
            curmax = 0
            while True:
                curmax += nums[id]
                curmax = max(curmax, 0)
                maxsubarray = max(maxsubarray, curmax)
                id = (id+1)%length
                if id == start:
                    break
        if maxsubarray == 0:
            maxsubarray = max(nums)
        return maxsubarray