# 1288. Remove Covered Intervals
# Topics: 'Array', 'Sorting'
# Level: 'Medium'

# Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

# The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

# Return the number of remaining intervals.


# Example 1:

# Input: intervals = [[1,4],[3,6],[2,8]]
# Output: 2
# Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.

# Example 2:

# Input: intervals = [[1,4],[2,3]]
# Output: 1

 

# Constraints:

#     1 <= intervals.length <= 1000
#     intervals[i].length == 2
#     0 <= li < ri <= 105
#     All the given intervals are unique.

from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        removed = set()
        for i in range(len(intervals)):
            if i in removed:
                continue
            a, b = intervals[i]
            for j in range(len(intervals)):
                if i == j:
                    continue                
                c, d = intervals[j]
                if c <= a and b <= d:
                    removed.add(i)
                    break
        
        return len(intervals) - len(removed)
