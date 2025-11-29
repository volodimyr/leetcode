# 101. Symmetric Tree
# Topics: 'Tree', 'Depth-First Search', 'Breadth-First Search', 'Binary Tree'

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:

# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:

# Input: root = [1,2,2,null,3,null,3]
# Output: false

# Constraints:

#     The number of nodes in the tree is in the range [1, 1000].
#     -100 <= Node.val <= 100


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(left, right) -> bool:
            if left and not right:
                return False
            if right and not left:
                return False
            if not right and not left:
                return True
            if right.val != left.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left, root.right)