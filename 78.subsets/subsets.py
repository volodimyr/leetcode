# 78. Subsets
# Topics: 'Array', 'Backtracking', 'Bit Manipulation'
# Level: 'Medium'

# Given an integer array nums of unique elements, return all possible

# (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

# Constraints:

#     1 <= nums.length <= 10
#     -10 <= nums[i] <= 10
#     All the numbers of nums are unique.

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, cur = [], []
        find(0, nums, subsets, cur)
        return subsets
    
def find(i, nums, subsets, cur):
    if i >= len(nums):
        subsets.append(cur.copy())
        return
    cur.append(nums[i])
    find(i+1, nums, subsets, cur)
    cur.pop()
    find(i+1, nums, subsets, cur)