# 1523. Count Odd Number in an Interval Range
# Topics: 'Math'

# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

# Example 1:

# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].

# Example 2:

# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].

 

# Constraints:

#     0 <= low <= high <= 10^9

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        length = high - low + 1
        count = length // 2
        if length % 2 and low % 2:
            count += 1
        return count