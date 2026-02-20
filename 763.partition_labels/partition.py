# 763. Partition Labels
# Topics: 'Greedy', 'Hash Table', 'Two Pointers', 'String'
# Level: 'Medium'

# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

 

# Example 1:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

# Example 2:

# Input: s = "eccbbbbdec"
# Output: [10]

 

# Constraints:

#     1 <= s.length <= 500
#     s consists of lowercase English letters.

from typing import Counter, List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = {}
        for i in range(len(s)):
            c = s[i]
            m[c] = i
        
        last_index = 0
        j = 0
        res = []
        for i in range(len(s)):
            j+=1
            c = s[i]
            last_index = max(last_index, m[c])
            if last_index == i:
                res.append(j)
                j = 0
        
        return res



# class Solution:
#     def partitionLabels(self, s: str) -> List[int]:
#         counter = Counter(s)

#         arr = [0] * 26
#         ln = 0
#         res = []
#         for c in s:
#             ln += 1
#             arr[ord(c)-97] += 1
#             if counter[c] != arr[ord(c)-97]:
#                 continue

#             uniq = True
#             for i in range(len(arr)):
#                 if arr[i] <= 0:
#                     continue
#                 else:
#                     if counter[chr(i+97)] != arr[i]:
#                         uniq = False
#                         break
#             if uniq:
#                 res.append(ln)
#                 ln = 0
#                 arr = [0] * 26
        
#         return res