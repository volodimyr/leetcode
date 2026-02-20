# 416. Partition Equal Subset Sum
# Topics: 'Array', 'Dynamic Programming'
# Level: 'Medium' 

# Given an integer array nums, return true if you can partition the array
# into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

# Example 1:
#
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
# Example 2:
#
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
#
#
#
# Constraints:
#
#     1 <= nums.length <= 200
#     1 <= nums[i] <= 100

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        N = len(nums)
        memo = {}

        def helper(i, target):
            if i == N:
                return target == 0
            if target < 0:
                return False
            if (i, target) in memo:
                return memo[(i, target)]
            memo[(i, target)] = helper(i + 1, target) or helper(i + 1, target - nums[i])
            return memo[(i, target)]

        return helper(0, total // 2)