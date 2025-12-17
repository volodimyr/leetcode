# 24. Swap nodes in pairs
# Topics: 'Linked List', 'Recursion'
# Level: 'Medium'

# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

# Example 1:

# Input: head = [1,2,3,4]

# Output: [2,1,4,3]

# Explanation:

# Example 2:

# Input: head = []

# Output: []

# Example 3:

# Input: head = [1]

# Output: [1]

# Example 4:

# Input: head = [1,2,3]

# Output: [2,1,3]

 

# Constraints:

#     The number of nodes in the list is in the range [0, 100].
#     0 <= Node.val <= 100

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur = head
        curnext = head.next
        cur.next = self.swapPairs(curnext.next)
        curnext.next = cur
        return curnext


# wrong solution, violates specification of the task
    # def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head:
    #         return head
        
    #     cur = head
    #     arr = []
    #     while cur:
    #         arr.append(cur.val)
    #         cur = cur.next
        
    #     for i in range(1, len(arr), 2):
    #         arr[i], arr[i-1] = arr[i-1], arr[i]
        
    #     cur = head
    #     i = 0
    #     while cur:
    #         cur.val = arr[i]
    #         i+=1
    #         cur = cur.next
            
    #     return head