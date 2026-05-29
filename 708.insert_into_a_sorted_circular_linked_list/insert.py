# 708. Insert into a Sorted Circular Linked List
# Topics: 'Linked List', 'Two Pointers'
# Level: 'Medium'

# Given a Circular Linked List node, which is sorted in non-descending order,
# write a function to insert a value insertVal into the list such that it remains
# a sorted circular list. The given node can be a reference to any single node in
# the list and may not necessarily be the smallest value in the circular list.
#
# If there are multiple suitable places for insertion, you may choose any place to
# insert the new value. After the insertion, the circular list should remain sorted.
#
# If the list is empty (i.e., the given node is null), you should create a new single
# circular list and return the reference to that single node. Otherwise, you should
# return the originally given node.

# Example 1:
# Input: head = [3,4,1], insertVal = 2
# Output: [3,4,1,2]

# Example 2:
# Input: head = [], insertVal = 1
# Output: [1]

# Example 3:
# Input: head = [1], insertVal = 0
# Output: [1,0]

# Constraints:
#     The number of nodes in the list is in the range [0, 5 * 10⁴].
#     -10⁶ <= Node.val, insertVal <= 10⁶

from typing import Optional


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            nNode = Node(insertVal)
            nNode.next = nNode
            return nNode

        biggest = head
        real_head = head
        cur = head
        while True:
            if biggest.val < cur.val:
                biggest = cur
            if real_head.val >= cur.val:
                real_head = cur
            cur = cur.next
            if cur == head:
                break

        real_tail = None
        cur = head
        while True:
            if cur.next == real_head:
                real_tail = cur
                break
            cur = cur.next

        if biggest.val > real_tail.val:
            real_tail = biggest
            real_head = biggest.next

        nNode = Node(insertVal)
        if insertVal < real_head.val or insertVal > real_tail.val:
            real_tail.next, nNode.next = nNode, real_tail.next
        else:
            cur = head
            while True:
                if cur.val <= insertVal <= cur.next.val:
                    cur.next, nNode.next = nNode, cur.next
                    break
                cur = cur.next

        return head
