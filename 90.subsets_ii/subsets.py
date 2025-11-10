# 90. Subsets II
# Topics: 'Array', 'Backtracking', 'Bit Manipulation'
# Level: 'Medium'

# Given an integer array nums that may contain duplicates, return all possible

# (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.


# Example 1:

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# Example 2:

# Input: nums = [0]
# Output: [[],[0]]

# Constraints:

#     1 <= nums.length <= 10
#     -10 <= nums[i] <= 10

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, cur = set(), []
        find(0, nums, subsets, cur)
        return list(subsets)
    
def find(i, nums, subsets, cur):
    if i >= len(nums):
        subsets.add(tuple(cur.copy()))
        return
    cur.append(nums[i])
    find(i+1, nums, subsets, cur)
    cur.pop()
    find(i+1, nums, subsets, cur)