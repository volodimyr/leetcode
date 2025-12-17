# 2487. Remove nodes from linked list
# Topics: 'Linked List', 'Stack', 'Monotonic Stack', 'Recursion'
# LeveL: 'Medium'

# You are given the head of a linked list.

# Remove every node which has a node with a greater value anywhere to the right side of it.

# Return the head of the modified linked list.

 

# Example 1:

# Input: head = [5,2,13,3,8]
# Output: [13,8]
# Explanation: The nodes that should be removed are 5, 2 and 3.
# - Node 13 is to the right of node 5.
# - Node 13 is to the right of node 2.
# - Node 8 is to the right of node 3.

# Example 2:

# Input: head = [1,1,1,1]
# Output: [1,1,1,1]
# Explanation: Every node has value 1, so no nodes are removed.

 

# Constraints:

#     The number of the nodes in the given list is in the range [1, 105].
#     1 <= Node.val <= 105

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        cur = head
        while cur:
            while stack and stack[-1].val < cur.val:
                stack.pop()
            stack.append(cur)
            cur = cur.next
        
        for i in range(1, len(stack)):
            stack[i-1].next = stack[i]
        
        return stack[0]
    
    # def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     stack = []
    #     cur = head
    #     while cur:
    #         shrinked = False
    #         while stack and stack[-1].val < cur.val:
    #             stack.pop()
    #             shrinked = True
            
    #         if shrinked and not stack:
    #             head = cur
    #         elif shrinked and stack:
    #             stack[-1].next = cur
            
    #         stack.append(cur)

    #         cur = cur.next
    #     return head