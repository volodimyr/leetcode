# 1229. Meeting Scheduler
# Topics: 'Array', 'Two Pointers', 'Sorting'

# Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration,
# return the earliest time slot that works for both of them and is of duration duration.

# If there is no common time slot that satisfies the requirements, return an empty array.

# The format of a time slot is an array of two elements [start, end] representing
# an inclusive time range from start to end.

# It is guaranteed that no two availability slots of the same person intersect with each other.
# That is, for any two time slots [s1, e1] and [s2, e2] of the same person,
# either s1 > e2 or s2 > e1.

# Example 1:

# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8

# Output: [60,68]

# Example 2:

# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12

# Output: []

# Constraints:

#     1 <= slots1.length, slots2.length <= 10⁴
#     slots1[i].length, slots2[i].length == 2
#     slots1[i][0] < slots1[i][1]
#     slots2[i][0] < slots2[i][1]
#     0 <= slots1[i][j], slots2[i][j] <= 10⁹
#     1 <= duration <= 10⁶

from typing import List

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        N = len(slots1)
        M = len(slots2)

        slots1.sort()
        slots2.sort()

        i = 0
        j = 0
        while i < N and j < M:
            i1, j2 = slots1[i], slots2[j]
            s = max(i1[0], j2[0])
            e = min(i1[1], j2[1])
            if s <= e and e - s >= duration:
                return [s, s + duration]
            if i1[1] < j2[1]:
                i += 1
            else:
                j += 1

        return []
