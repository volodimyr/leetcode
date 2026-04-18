# 346. Moving Average from Data Stream
# Topics: 'Design', 'Queue', 'Data Stream'

# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Implement the MovingAverage class:

#     MovingAverage(int size) Initializes the object with the size of the window size.
#     double next(int val) Returns the moving average of the last size values of the stream.

# Example 1:

# Input:
# ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5]]

# Output:
# [null, 1.0, 5.5, 4.66667, 6.0]

# Explanation:
# MovingAverage movingAverage = new MovingAverage(3);
# movingAverage.next(1); // return 1.0 = 1 / 1
# movingAverage.next(10); // return 5.5 = (1 + 10) / 2
# movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
# movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

# Constraints:

#     1 <= size <= 1000
#     -10⁵ <= val <= 10⁵
#     At most 10⁴ calls will be made to next.

from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.q = deque()
        self.sumup = 0
        self.max_size = size
        

    def next(self, val: int) -> float:
        if self.max_size == len(self.q):
            self.sumup -= self.q.popleft()
        self.sumup += val
        self.q.append(val)
        return self.sumup / len(self.q)