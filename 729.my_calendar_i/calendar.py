# 729. My Calendar I
# Topics: 'Array', 'Binary Search', 'Design', 'Segment Tree', 'Ordered Set'
# Level: 'Medium'

# You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

# A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

# The event can be represented as a pair of integers startTime and endTime that represents a booking on the half-open interval [startTime, endTime), the range of real numbers x such that startTime <= x < endTime.

# Implement the MyCalendar class:

#     MyCalendar() Initializes the calendar object.
#     boolean book(int startTime, int endTime) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

 

# Example 1:

# Input
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# Output
# [null, true, false, true]

# Explanation
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
# myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.

 

# Constraints:

#     0 <= start < end <= 109
#     At most 1000 calls will be made to book.

class MyCalendar:
    def __init__(self):
        self.events = []
    def book(self, startTime: int, endTime: int) -> bool:
        L, R = 0, len(self.events)
        while L < R:
            M = (L+R)//2
            if self.events[M][0] < startTime:
                L = M + 1
            else:
                R = M
        idx = L
        if idx > 0 and self.events[idx-1][1] > startTime:
            return False
        if idx < len(self.events) and self.events[idx][0] < endTime:
            return False
        self.events.insert(idx, (startTime, endTime))
        return True

# O(n)
# class MyCalendar:
#     def __init__(self):
#         self.events = []

#     def book(self, startTime: int, endTime: int) -> bool:
#         for s, e in self.events:
#             if max(s, startTime) < min(e, endTime):
#                 return False
#         self.events.append((startTime, endTime))
#         return True
        
