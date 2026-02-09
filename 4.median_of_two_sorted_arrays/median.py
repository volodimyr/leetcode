# 4. Median of two Sorted Arrays
# Topics: 'Binary Search', 'Array', 'Divide and Conquer'
# Level: 'Hard'

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

 
# Constraints:

#     nums1.length == m
#     nums2.length == n
#     0 <= m <= 1000
#     0 <= n <= 1000
#     1 <= m + n <= 2000
#     -106 <= nums1[i], nums2[i] <= 106

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = [0] * (len(nums1)+len(nums2))
        def merge():
            s = 0
            i = 0
            j = 0

            while i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    arr[s] = nums1[i]
                    i+=1
                else:
                    arr[s] = nums2[j]
                    j+=1
                s+=1
            
            while i < len(nums1):
                arr[s] = nums1[i]
                i+=1
                s+=1
            
            while j < len(nums2):
                arr[s] = nums2[j]
                j+=1
                s+=1
        
        merge()

        if len(arr) % 2 == 1:
            return arr[len(arr)//2]
            
        return (arr[len(arr)//2] + arr[len(arr)//2-1]) / 2
        