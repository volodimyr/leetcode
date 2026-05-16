# 1228. Missing Number In Arithmetic Progression
# Topics: 'Array', 'Math'

# In some array arr, the values were in arithmetic progression: the values arr[i + 1] - arr[i] are all equal for every 0 <= i < arr.length - 1.

# A value from arr was removed that was not the first or last value in the array.

# Given arr, return the removed value.

# Example 1:

# Input: arr = [5,7,11,13]

# Output: 9

# Explanation: The previous array was [5,7,9,11,13].

# Example 2:

# Input: arr = [15,13,12]

# Output: 14

# Explanation: The previous array was [15,14,13,12].

# Constraints:

#     3 <= arr.length <= 1000
#     0 <= arr[i] <= 10⁵
#     The given array is guaranteed to be a valid array.

from typing import List

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        N = len(arr)
        first, last = arr[0], arr[N-1]
        prg = (last - first) // N
        if prg == 0:
            return arr[0]
        i = 1
        pred = arr[0] + prg
        while arr[i] == pred:
            pred = arr[i] + prg
            i += 1

        return pred