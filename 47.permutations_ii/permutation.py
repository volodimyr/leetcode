# 47. Permutations II
# Topics: 'Array', 'Backtracking', 'Sorting'
# Level: 'Medium'

# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

# Example 1:

# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

# Example 2:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Constraints:

#     1 <= nums.length <= 8
#     -10 <= nums[i] <= 10

from typing import Counter, List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        res = []
        def backtrack(cur):
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            for n in counter.keys():
                if counter[n] > 0:
                    cur.append(n)
                    counter[n]-=1
                    backtrack(cur)
                    counter[n]+=1
                    cur.pop()

        backtrack([])
        return res