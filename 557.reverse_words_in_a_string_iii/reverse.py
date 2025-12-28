# 557. Reverse Workds in a String III
# Topics: 'Two Pointers', 'String'

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# Example 2:

# Input: s = "Mr Ding"
# Output: "rM gniD"

 

# Constraints:

#     1 <= s.length <= 5 * 104
#     s contains printable ASCII characters.
#     s does not contain any leading or trailing spaces.
#     There is at least one word in s.
#     All the words in s are separated by a single space.

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(word[::-1] for word in s.split())

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         split = s.split()
#         res = []
#         for sp in split:
#             arr = list(sp)
#             L, R = 0, len(arr)-1
#             while L < R:
#                 arr[L], arr[R] = arr[R], arr[L]
#                 L+=1
#                 R-=1
#             res.append(''.join(arr))
        
#         return ' '.join(res)

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         arr = list(s)

#         tmp = 0
#         L, R = 0, 0

#         while tmp < len(arr):
#             R = tmp
#             while R+1 < len(arr) and arr[R+1] != ' ':
#                 R+=1
        
#             if L > 0:
#                 L = tmp+1
#             tmp = R+1

#             while L <= R:
#                 arr[L], arr[R] = arr[R], arr[L]
#                 L+=1
#                 R-=1
                
#         return ''.join(arr)
