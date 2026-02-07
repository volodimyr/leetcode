# 236. Lowest Common Ancestor of a Binary Tree
# Topics: 'Tree', 'Depth-First Search', 'Binary Tree'
# Level: 'Medium'

# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

# Example 1:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.

# Example 2:

# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

# Example 3:

# Input: root = [1,2], p = 1, q = 2
# Output: 1

 

# Constraints:

#     The number of nodes in the tree is in the range [2, 105].
#     -109 <= Node.val <= 109
#     All Node.val are unique.
#     p != q
#     p and q will exist in the tree.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root is p or root is q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        
        return left if left else right

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         def path(root, search, p):
#             if not root:
#                 return False
#             p.append(root)
#             if root.val == search:
#                 return True
#             if path(root.left, search, p):
#                 return True
#             if path(root.right, search, p):
#                 return True
#             p.pop()
#             return False
        
#         ppath = []
#         path(root, p.val, ppath)
#         qpath = []
#         path(root, q.val, qpath)

#         i, j = 0, 0
#         parent = None
#         while i < len(ppath) and j < len(qpath) and ppath[i].val == qpath[j].val:
#             parent = ppath[i]
#             i+=1
#             j+=1

#         return parent
