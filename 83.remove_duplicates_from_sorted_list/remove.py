# 83. Remove Duplicates from Sorted List
# Topics: 'Linked List'
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Example 1:

# Input: head = [1,1,2]
# Output: [1,2]

# Example 2:

# Input: head = [1,1,2,3,3]
# Output: [1,2,3]

 

# Constraints:

#     The number of nodes in the list is in the range [0, 300].
#     -100 <= Node.val <= 100
#     The list is guaranteed to be sorted in ascending order.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Memory O(1), Time O(n)
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        cur = head
        prev = None
        while cur:
            if not prev:
                prev = d
                prev.next= cur
                prev = prev.next
            elif prev.val != cur.val:
                prev.next= cur
                prev = prev.next
            else:
                prev.next = None
            cur = cur.next
        return d.next
    
# Memory O(n), Time O(n)
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         d = ListNode()
#         dup = set()
#         cur = head
#         prev = d
#         while cur:
#             if cur.val not in dup:
#                 prev.next = cur
#                 prev = prev.next
#             else:
#                 prev.next = None
#             dup.add(cur.val)
#             cur = cur.next
#         return d.next