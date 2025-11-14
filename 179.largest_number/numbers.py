# 179. Largest number
# Topics: 'Array', 'String', 'Greedy', 'Sorting'
# Level: 'Medium'

# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

 

# Example 1:

# Input: nums = [10,2]
# Output: "210"

# Example 2:

# Input: nums = [3,30,34,5,9]
# Output: "9534330"

 

# Constraints:

#     1 <= nums.length <= 100
#     0 <= nums[i] <= 109

from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            return 0
        nums_str.sort(key=cmp_to_key(compare))
        if nums_str[0] == '0':
            return nums_str[0]
        return ''.join(nums_str)