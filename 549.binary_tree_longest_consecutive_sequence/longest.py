# 549. Binary Tree Longest Consecutive Sequence
# Topics: 'Tree', 'Binary Tree', 'Depth-First Search'
# Level: 'Medium'

# Given the root of a binary tree, return the length of the longest consecutive sequence path.

# A consecutive sequence path is a path where the values increase by one along the path.

# Note that the path can start at any node in the tree, and you cannot go from a node to its parent in the path.

# Example 1:

# Input: root = [1,null,3,2,4,null,null,null,5]

# Output: 3

# Explanation: Longest consecutive sequence path is 3-4-5, so return 3.

# Example 2:

# Input: root = [2,null,3,2,null,1]

# Output: 2

# Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.

# Constraints:

#     The number of nodes in the tree is in the range [1, 3 * 10⁴].
#     -3 * 10⁴ <= Node.val <= 3 * 10⁴

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(root, parent, cons):
            res[0] = max(res[0], cons)
            if not root:
                return
            if parent and root.val - parent.val == 1:
                cons += 1
            else:
                cons = 1
            dfs(root.left, root, cons)
            dfs(root.right, root, cons)
        
        dfs(root, None, 1)

        return res[0]