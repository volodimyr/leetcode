import unittest
from lca import Solution


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestLowestCommonAncestor(unittest.TestCase):

    def setUp(self):
        """
        Build the tree:
                3
               / \\
              5   1
             / \\ / \\
            6  2 0  8
              / \\
             7   4
        """
        self.root = TreeNode(3)
        self.root.left = TreeNode(5)
        self.root.right = TreeNode(1)

        self.root.left.left = TreeNode(6)
        self.root.left.right = TreeNode(2)
        self.root.right.left = TreeNode(0)
        self.root.right.right = TreeNode(8)

        self.root.left.right.left = TreeNode(7)
        self.root.left.right.right = TreeNode(4)

        self.nodes = {}
        def collect(node):
            if not node:
                return
            self.nodes[node.val] = node
            collect(node.left)
            collect(node.right)

        collect(self.root)

        self.sol = Solution()

    def test_lca_root(self):
        p = self.nodes[5]
        q = self.nodes[1]
        res = self.sol.lowestCommonAncestor(self.root, p, q)
        self.assertEqual(res.val, 3)

    def test_lca_ancestor(self):
        p = self.nodes[5]
        q = self.nodes[4]
        res = self.sol.lowestCommonAncestor(self.root, p, q)
        self.assertEqual(res.val, 5)

    def test_lca_small_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)

        res = self.sol.lowestCommonAncestor(root, root, root.left)
        self.assertEqual(res.val, 1)


if __name__ == "__main__":
    unittest.main()
