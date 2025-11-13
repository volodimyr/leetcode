import unittest
from iterator import TreeNode
from iterator import BSTIterator

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
