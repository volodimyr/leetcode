# 234. Palindrome Linked List
# Topics: 'Stack', 'Recursion', 'Linked List', 'Two Pointers'
# Given the head of a singly linked list, return true if it is a or false otherwise.

# Example 1:

# Input: head = [1,2,2,1]
# Output: true

# Example 2:

# Input: head = [1,2]
# Output: false

 

# Constraints:

#     The number of nodes in the list is in the range [1, 105].
#     0 <= Node.val <= 9

 
# Follow up: Could you do it in O(n) time and O(1) space?


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Memory O(n), Time O(n)
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        
        L, R = 0, len(arr)-1
        while L < R:
            if arr[L] != arr[R]:
                return False
            L+=1
            R-=1
        return True