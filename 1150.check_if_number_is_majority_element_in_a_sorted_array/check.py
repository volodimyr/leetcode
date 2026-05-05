# 1150. Check If a Number Is Majority Element in a Sorted Array
# Topics: 'Array', 'Binary Search'

# Given an integer array nums sorted in non-decreasing order and an integer target, return true if target is a majority element, or false otherwise.

# A majority element in an array nums is an element that appears more than nums.length / 2 times in the array.

# Example 1:

# Input: nums = [2,4,5,5,5,5,5,6,6], target = 5

# Output: true

# Explanation: The value 5 appears 5 times and the length of the array is 9. Thus, 5 is a majority element because 5 > 9/2 is true.

# Example 2:

# Input: nums = [10,100,101,101], target = 101

# Output: false

# Explanation: The value 101 appears 2 times and the length of the array is 4. Thus, 101 is not a majority element because 2 > 4/2 is false.

# Constraints:

#     1 <= nums.length <= 1000
#     1 <= nums[i], target <= 10⁹
#     nums is sorted in non-decreasing order.

from typing import List

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:   
        L, R = 0, len(nums)-1
        index = -1
        while L <= R:
            mid = (L+R) // 2
            if nums[mid] >= target:
                R = mid - 1
                index = mid
            else:
                L = mid + 1
        
        half = len(nums) // 2
        if index == -1:
            return False
        
        if index + half >= len(nums):
            return False
        
        return nums[index+half] == target
