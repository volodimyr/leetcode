# 1405. Longest happy string
# Topics: 'String', 'Greedy', 'Heap (Priority Queue)'
# Level: 'Medium'

# A string s is called happy if it satisfies the following conditions:

#     s only contains the letters 'a', 'b', and 'c'.
#     s does not contain any of "aaa", "bbb", or "ccc" as a substring.
#     s contains at most a occurrences of the letter 'a'.
#     s contains at most b occurrences of the letter 'b'.
#     s contains at most c occurrences of the letter 'c'.

# Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.

# Example 2:

# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It is the only correct answer in this case.

 

# Constraints:

#     0 <= a, b, c <= 100
#     a + b + c > 0

import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a:
            heapq.heappush(max_heap, Letter('a', a))
        if b:
            heapq.heappush(max_heap, Letter('b', b))
        if c:
            heapq.heappush(max_heap, Letter('c', c))
        
        s = ''
        while max_heap:
            next = heapq.heappop(max_heap)
            if len(s) > 1 and s[-1] == next.letter and s[-2] == next.letter:
                if not max_heap:
                    break
                delim = heapq.heappop(max_heap)
                s += delim.letter
                delim.times-=1
                if delim.times:
                    heapq.heappush(max_heap, delim)
                heapq.heappush(max_heap, next)
                continue
            s += next.letter
            next.times-=1
            if next.times:
                heapq.heappush(max_heap, next)
    
        return s

class Letter:
    def __init__(self, letter, times):
        self.letter = letter
        self.times = times

    def __lt__(self, other):
        return self.times > other.times

