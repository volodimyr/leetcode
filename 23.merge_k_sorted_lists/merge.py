import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Node:
    def __init__(self, n):
        self.n = n
    
    def __lt__(self, other):
        return self.n.val < other.n.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for l in lists:
            heapq.heappush(h, Node(l))
        
        res = ListNode()
        cur = res
        while h:
            node = heapq.heappop(h)
            cur.next = ListNode(node.n.val)
            cur = cur.next
            if node.n.next:
                heapq.heappush(h, Node(node.n.next))
        
        return res.next

# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if not lists:
#             return
#         if len(lists) == 1:
#             return lists[0]
        
#         M = len(lists) // 2
#         right = self.mergeKLists(lists[M:])
#         left = self.mergeKLists(lists[:M])
#         return self.merge(left, right)
    
#     def merge(self, l1, l2):
#         res = ListNode()
#         curr = res
#         curl1, curl2 = l1, l2
#         while curl1 and curl2:
#             if curl1.val < curl2.val:
#                 curr.next = curl1
#                 curl1 = curl1.next
#             else:
#                 curr.next = curl2
#                 curl2 = curl2.next
#             curr = curr.next
#         if curl1:
#             curr.next = curl1
#         if curl2:
#             curr.next = curl2
        
#         return res.next