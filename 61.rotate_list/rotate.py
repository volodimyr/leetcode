# 61. Rotate List
# Topics: 'Linked List', 'Two Pointers'
# LeveL: 'Medium'

# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:

# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:

# Input: head = [0,1,2], k = 4
# Output: [2,0,1]

 

# Constraints:

#     The number of nodes in the list is in the range [0, 500].
#     -100 <= Node.val <= 100
#     0 <= k <= 2 * 109

from typing import Optional

class ListNode:
  def __init__(self, val=None, next=None):
       self.val = val
       self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        
        def rotate(L, R):
            while L < R:
                arr[L], arr[R] = arr[R], arr[L]
                L += 1
                R -= 1

        if k > len(arr):
            k = k % len(arr)
        rotate(0, len(arr)-1)
        rotate(0, k-1)
        rotate(k, len(arr)-1)

        cur = head
        i = 0
        while cur:
            cur.val = arr[i]
            i+=1
            cur = cur.next

        return head