# 229. Majority element II
# Topics: 'Array', 'Hash Table', 'Sorting', 'Counting'
# Level: 'Medium'

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]

# Example 2:

# Input: nums = [1]
# Output: [1]

# Example 3:

# Input: nums = [1,2]
# Output: [1,2]

 

# Constraints:

#     1 <= nums.length <= 5 * 104
#     -109 <= nums[i] <= 109

from typing import List

# Time: O(n), Space: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        times = len(nums) // 3
        res = set()
        mcount = {}
        for n in nums:
            count = mcount.get(n, 0) + 1
            if count > times:
                res.add(n)
            mcount[n] = count
        return list(res)

# Time: O(nlog(n)), Space: O(1)
# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         times = len(nums) // 3
#         nums.sort()
#         count = 1
#         cur = nums[0]
#         res = []
#         for n in nums[1:]:
#             if cur == n:
#                 count+=1
#             else:
#                 if count > times:
#                     res.append(cur)
#                 cur = n
#                 count = 1
#         if count > times:
#             res.append(cur)
#         return res