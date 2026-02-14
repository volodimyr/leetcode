# 846. Hand of Straights
# Topics: 'Array', 'Hash Table', 'Greedy', 'Sorting'
# Level: 'Medium'

# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

# Example 1:

# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

# Example 2:

# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.

 

# Constraints:

#     1 <= hand.length <= 104
#     0 <= hand[i] <= 109
#     1 <= groupSize <= hand.length

from typing import Counter, List


# O(nlongn) time
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        if N % groupSize:
            return False
        hand.sort()
        counter = Counter(hand)
        for n in hand:
            if not counter:
                break
            if n not in counter:
                continue
            c = 0
            while counter[n] > 0 and c < groupSize:
                counter[n] -= 1
                if counter[n] <= 0:
                    del counter[n]
                c+=1
                n+=1

            if c != groupSize:
                return False

        return len(counter) == 0
    
# O(n**2)
# class Solution:
#     def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
#         N = len(hand)
#         counter = Counter(hand)

#         def helper(start, clean=False):
#             c = 0
#             while start in counter:
#                 if clean:
#                     if counter[start] == 1:
#                         del counter[start]
#                     else:
#                         counter[start] -= 1
#                 start += 1
#                 c += 1
#                 if c == groupSize:
#                     return True
#             return False

#         while counter:
#             start = -1
#             for k in counter:
#                 if helper(k):
#                     start = k
#             if start == -1:
#                 break
#             else:
#                 helper(start, True)
        
#         return len(counter) == 0