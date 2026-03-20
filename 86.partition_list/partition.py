# 86. Partition List
# Topics: 'Linked List', 'Two Pointers'
# LeveL: 'Medium'

# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

 

# Example 1:

# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]

# Example 2:

# Input: head = [2,1], x = 2
# Output: [1,2]

 

# Constraints:

#     The number of nodes in the list is in the range [0, 200].
#     -100 <= Node.val <= 100
#     -200 <= x <= 200

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        biggerd, lessd = ListNode(), ListNode()
        bigger, less = biggerd, lessd
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                bigger.next = head
                bigger = bigger.next

            head = head.next

        bigger.next = None
        less.next = biggerd.next

        return lessd.next
    
# class Solution:
#     def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
#         bigger, less = [], []
#         cur = head
#         while cur:
#             if cur.val < x:
#                 less.append(cur.val)
#             else:
#                 bigger.append(cur.val)
#             cur = cur.next

#         cur = head
#         for l in less:
#             cur.val = l
#             cur = cur.next
#         for b in bigger:
#             cur.val = b
#             cur = cur.next

#         return head