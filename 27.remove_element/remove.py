import unittest
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:        
        i = 0
        for j in range(0, len(nums)):
            if nums[j] == val:
                continue
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

        
        return i