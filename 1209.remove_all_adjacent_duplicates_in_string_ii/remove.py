# 1209. Remove All Adjacent Duplicates in String II
# Topics: 'String', 'Stack'
# Level: 'Medium'

# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

# Example 1:

# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.

# Example 2:

# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"

# Example 3:

# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"

 

# Constraints:

#     1 <= s.length <= 105
#     2 <= k <= 104
#     s only contains lowercase English letters.

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        arr = []
        for c in s:
            if not arr:
                arr.append((c, 1))
            else:
                endc, count = arr[-1]
                if endc != c:
                    arr.append((c, 1))
                else:
                    if count + 1 == k:
                        arr.pop()
                    else:
                        arr[-1] = (c, count+1)
        
        return "".join(c * count for c, count in arr)