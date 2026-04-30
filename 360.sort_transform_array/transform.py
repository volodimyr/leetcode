# 360. Sort Trasnform Array
# Topics: 'Two Pointers', 'Array', 'Math', 'Sorting'
# Level: 'Medium'

# Given a sorted integer array nums and three integers a, b and c, apply a quadratic function of the form f(x) = ax² + bx + c to each element nums[i] in the array, and return the array in sorted order.

# Example 1:

# Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5

# Output: [3,9,15,33]

# Example 2:

# Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5

# Output: [-23,-5,1,7]


# Constraints:

#     1 <= nums.length <= 200
#     -100 <= nums[i], a, b, c <= 100
#     nums is sorted in ascending order.


# Follow up: Could you solve it in O(n) time?

from typing import List

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        res = [0] * len(nums)
        L, R = 0, len(nums)-1

        index = 0 if a < 0 else len(nums)-1
        while L <= R:
            x1 = a*(nums[L]*nums[L]) + b*nums[L] + c
            x2 = a*(nums[R]*nums[R]) + b*nums[R] + c
            
            if a < 0:
                if x1 <= x2:
                    res[index] = x1
                    L += 1
                else:
                    res[index] = x2
                    R -= 1
                index += 1
            else:
                if x1 >= x2:
                    res[index] = x1
                    L += 1
                else:
                    res[index] = x2
                    R -= 1
                index -= 1

        return res