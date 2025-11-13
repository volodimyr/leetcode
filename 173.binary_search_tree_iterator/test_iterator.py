import unittest
from iterator import TreeNode
from iterator import BSTIterator


class TestTreeNodePostorder(unittest.TestCase):
    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(root.postorder(), [1])

    def test_left_skewed(self):
        #   3
        #  /
        # 2
        #/
        #1
        root = TreeNode(3, TreeNode(2, TreeNode(1)))
        self.assertEqual(root.postorder(), [1, 2, 3])

    def test_right_skewed(self):
        # 1
        #  \
        #   2
        #    \
        #     3
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(root.postorder(), [3, 2, 1])

    def test_balanced_tree(self):
        #   2
        #  / \
        # 1   3
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        self.assertEqual(root.postorder(), [1, 3, 2])

    def test_complex_tree(self):
        #        4
        #      /   \
        #     2     6
        #    / \   /
        #   1   3 5
        root = TreeNode(4,
                        TreeNode(2, TreeNode(1), TreeNode(3)),
                        TreeNode(6, TreeNode(5)))
        self.assertEqual(root.postorder(), [1, 3, 2, 5, 6, 4])


class TestTreeNodePreorder(unittest.TestCase):
    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(root.preorder(), [1])

    def test_left_skewed(self):
        #   3
        #  /
        # 2
        #/
        #1
        root = TreeNode(3, TreeNode(2, TreeNode(1)))
        self.assertEqual(root.preorder(), [3, 2, 1])

    def test_right_skewed(self):
        # 1
        #  \
        #   2
        #    \
        #     3
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(root.preorder(), [1, 2, 3])

    def test_balanced_tree(self):
        #   2
        #  / \
        # 1   3
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        self.assertEqual(root.preorder(), [2, 1, 3])

    def test_complex_tree(self):
        #        4
        #      /   \
        #     2     6
        #    / \   /
        #   1   3 5
        root = TreeNode(4,
                        TreeNode(2, TreeNode(1), TreeNode(3)),
                        TreeNode(6, TreeNode(5)))
        self.assertEqual(root.preorder(), [4, 2, 1, 3, 6, 5])

class TestTreeNode(unittest.TestCase):
    def test_single_node(self):
        root = TreeNode(1, None, None)
        self.assertEqual(root.inorder(), [1])

    def test_left_skewed(self):
        root = TreeNode(3, TreeNode(2, TreeNode(1)))
        self.assertEqual(root.inorder(), [1, 2, 3])

    def test_right_skewed(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(root.inorder(), [1, 2, 3])

    def test_balanced_tree(self):
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        self.assertEqual(root.inorder(), [1, 2, 3])

    def test_complex_tree(self):
        #        4
        #      /   \
        #     2     6
        #    / \   /
        #   1   3 5
        root = TreeNode(4,
                        TreeNode(2, TreeNode(1), TreeNode(3)),
                        TreeNode(6, TreeNode(5)))
        self.assertEqual(root.inorder(), [1, 2, 3, 4, 5, 6])

class TestBSTIterator(unittest.TestCase):
    def build_tree(self):
        # Build a BST:
        #        7
        #      /   \
        #     3     15
        #          /  \
        #         9    20
        n9 = TreeNode(9, None, None)
        n20 = TreeNode(20, None, None)
        n15 = TreeNode(15, n9, n20)
        n3 = TreeNode(3, None, None)
        root = TreeNode(7, n3, n15)
        return root

    def test_inorder_traversal(self):
        root = self.build_tree()
        it = BSTIterator(root)
        result = []
        while it.hasNext():
            result.append(it.next())
        self.assertEqual(result, [3, 7, 9, 15, 20])

    def test_single_node(self):
        root = TreeNode(42, None, None)
        it = BSTIterator(root)
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), 42)
        self.assertFalse(it.hasNext())

    def test_empty_tree(self):
        it = BSTIterator(None)
        self.assertFalse(it.hasNext())

    def test_alternating_next_and_hasNext(self):
        root = self.build_tree()
        it = BSTIterator(root)
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), 3)
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), 7)
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), 9)
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), 15)
        self.assertTrue(it.hasNext())
        self.assertEqual(it.next(), 20)
        self.assertFalse(it.hasNext())


if __name__ == '__main__':
    unittest.main()
