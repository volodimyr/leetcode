# 46. Permutations
# Topics: 'Backtrating', 'Array'
# Level: 'Medium'

# Given an array nums of distinct integers, return all the possible

# . You can return the answer in any order.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:

# Input: nums = [1]
# Output: [[1]]

 

# Constraints:

#     1 <= nums.length <= 6
#     -10 <= nums[i] <= 10
#     All the integers of nums are unique.

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(used, cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            else:
                for n in nums:
                    if n not in used:
                        cur.append(n)
                        used.add(n)
                    else:
                        continue
                    backtrack(used, cur)
                    cur.pop()
                    used.remove(n)
        backtrack(set(), [])
        return res