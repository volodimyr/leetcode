# 1094. Car pooling
# Topics: 'Sorting', 'Array', 'Simulation', 'Prefix Sum', 'Heap (Pririty Queue)'
# Level: 'Medium'

# There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

# You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

# Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 

# Example 1:

# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false

# Example 2:

# Input: trips = [[2,1,5],[3,3,7]], capacity = 5
# Output: true

 

# Constraints:

#     1 <= trips.length <= 1000
#     trips[i].length == 3
#     1 <= numPassengersi <= 100
#     0 <= fromi < toi <= 1000
#     1 <= capacity <= 105

import heapq
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        group = []
        cur_cap = 0
        for num, pickup, dropoff in trips:
            while group and group[0].dropoff <= pickup:    
                dropped_group = heapq.heappop(group)
                cur_cap -= dropped_group.num
            
            cur_cap += num
            heapq.heappush(group, Group(num, dropoff))
            
            if cur_cap > capacity:
                return False
        return True

class Group:
    def __init__(self, num, dropoff):
        self.num = num
        self.dropoff = dropoff
    
    def __lt__(self, other):
        return self.dropoff < other.dropoff