# 314. Binary Tree Vertical Order Traversal
# Topics: 'Hash Table', 'Tree', 'Depth-First Search', 'Breadth-First Search', 'Binary Tree'
# Level: 'Medium'

# Given the root of a binary tree, return the vertical order traversal of its nodes' values.
# (i.e., from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]

# Example 2:
# Input: root = [3,9,8,4,0,1,7]
# Output: [[4],[9],[3,0,1],[8],[7]]

# Example 3:
# Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
# Output: [[4],[9,5],[3,0,1],[8,2],[7]]

# Constraints:
#     The number of nodes in the tree is in the range [0, 100].
#     -100 <= Node.val <= 100


from collections import defaultdict, deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        m = defaultdict(list)
        q = deque()
        q.append((root, 0))

        while q:
            pop, group  = q.popleft()
            m[group].append(pop.val)
            if pop.left:
                q.append((pop.left, group-1))
            if pop.right:
                q.append((pop.right, group+1))

        return [m[c] for c in sorted(m)]
