# 41. First Missing Positive
# Topics: 'Array', 'Hash Table',
# Level: 'Hard'

# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

# Example 1:

# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.

# Example 2:

# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.

# Example 3:

# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.

 

# Constraints:

#     1 <= nums.length <= 105
#     -231 <= nums[i] <= 231 - 1

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # crazy solution with O(max(nums)) space complexity :D
        # mx = max(nums)
        # arr = [-1]*(mx+2)
        # for n in nums:
        #     if n < 0:
        #         continue
        #     arr[n] = n
        
        # sm = 1
        # for i in range(1, len(arr)):
        #     if arr[i] == -1:
        #         return i

        # a little better but still not O(1) space
        # ex = set()
        # mx = 1
        # for n in nums:
        #     if n < 1:
        #         continue
        #     mx = max(mx, n)
        #     ex.add(n)
        
        # for n in range(1, mx+2):
        #     if n not in ex:
        #         return n

        size = len(nums)
        for i in range(size):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(size):
            val = abs(nums[i])
            if val >= 1 and val <= size:
                if nums[val-1] > 0:
                    nums[val-1] *= -1
                elif nums[val-1] == 0:
                    nums[val-1] = -1 * (size+1)
        
        for i in range(1, size+1):
            if nums[i-1] >= 0:
                return i
                
        return size+1

            

