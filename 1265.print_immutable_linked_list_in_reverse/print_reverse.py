# 1265. Print Immutable Linked List in Reverse
# Topics: 'Linked List', 'Two Pointers', 'Stack', 'Recursion'

# You are given an immutable linked list, print out all values of each node in reverse
# with the first node's value last.
# You must use printValue() to print the value of a node and getNext() to get the next node.

# Example 1:
# Input: head = [-2,0,6,4,4,-6]
# Output: -6,4,4,6,0,-2

# Example 2:
# Input: head = [0,10,4,5]
# Output: 5,4,10,0

# Constraints:
#     The length of the linked list is between [1, 1000].
#     The value of each node in the linked list is between [-1000, 1000].
#     1 <= n <= 1000


# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
    #  def printValue(self) -> None: # print the value of this node.
    #  def getNext(self) -> 'ImmutableListNode': # return the next node.


class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        res = []

        nxt = head
        while nxt:
            res.append(nxt)
            nxt = nxt.getNext()

        while res:
            res.pop().printValue()
