# 1272. Remove Interval
# Topics: 'Array'
# Level: 'Medium'

# A set of real numbers can be represented as the union of several disjoint intervals, where each interval is in the form [a, b). A real number x is in the set if one of its intervals [a, b) contains x (i.e. a <= x < b).

# You are given a sorted list of disjoint intervals intervals representing a set of real numbers as described above, where intervals[i] = [aᵢ, bᵢ] represents the interval [aᵢ, bᵢ). You are also given another interval toBeRemoved.

# Return the set of real numbers with the interval toBeRemoved removed from intervals. In other words, return the set of real numbers such that every x in the set is in intervals but not in toBeRemoved. Your answer should be a sorted list of disjoint intervals as described above.

# Example 1:

# Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]

# Output: [[0,1],[6,7]]

# Example 2:

# Input: intervals = [[0,5]], toBeRemoved = [2,3]

# Output: [[0,2],[3,5]]

# Example 3:

# Input: intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4]

# Output: [[-5,-4],[-3,-2],[4,5],[8,9]]

# Constraints:

#     1 <= intervals.length <= 10⁴
#     -10⁹ <= aᵢ < bᵢ <= 10⁹

from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        rem_start, rem_end = toBeRemoved[0], toBeRemoved[1]
        for i in range(len(intervals)):
            start, end = intervals[i]
            if end <= rem_start or start >= rem_end:
                res.append([start,end])
            else:
                if start < rem_start:
                    res.append([start, rem_start])
                if end > rem_end:
                    res.append([rem_end, end])
        return res