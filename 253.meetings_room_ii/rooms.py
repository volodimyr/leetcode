# 253. Meetings Room II
# Topics: 'Heap (Priority Queue)', 'Sorting', 'Greedy'
# Level: 'Medium'

# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

# Note: (0,8),(8,10) is not considered a conflict at 8.

# Example 1:

# Input: intervals = [(0,40),(5,10),(15,20)]

# Output: 2

# Explanation:
# day1: (0,40)
# day2: (5,10),(15,20)

# Example 2:

# Input: intervals = [(4,9)]

# Output: 1

# Constraints:

#     0 <= intervals.length <= 500
#     0 <= intervals[i].start < intervals[i].end <= 1,000,000

import heapq
from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        rooms = []
        for i in intervals:
            if rooms and rooms[0] <= i.start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, i.end)
        return len(rooms)

# O(n^2)- bruteforce
# class Solution:
#     def minMeetingRooms(self, intervals: List[Interval]) -> int:
#         if not intervals:
#             return 0
#         intervals.sort(key=lambda x: x.start)
#         res = [[intervals[0]]]
#         for i in range(1, len(intervals)):
#             cur = intervals[i]
#             added = False
#             for rows in res:
#                 rcur = rows[-1]                
#                 if rcur.end <= cur.start:
#                     rows.append(cur)
#                     added = True
#                     break
#             if not added:
#                 res.append([cur])
                
#         return len(res)