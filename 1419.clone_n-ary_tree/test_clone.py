import unittest
from clone import Node, Solution


def tree_equal(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    if a.val != b.val or len(a.children) != len(b.children):
        return False
    return all(tree_equal(ac, bc) for ac, bc in zip(a.children, b.children))


def collect_nodes(root):
    if root is None:
        return []
    nodes = [root]
    for ch in root.children:
        nodes.extend(collect_nodes(ch))
    return nodes


class TestCloneTree(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_none(self):
        self.assertIsNone(self.sol.cloneTree(None))

    def test_single_node(self):
        root = Node(1)
        clone = self.sol.cloneTree(root)
        self.assertTrue(tree_equal(root, clone))
        self.assertIsNot(root, clone)

    def test_example1(self):
        # [1,null,3,2,4,null,5,6]
        root = Node(1, [
            Node(3, [Node(5), Node(6)]),
            Node(2),
            Node(4),
        ])
        clone = self.sol.cloneTree(root)
        self.assertTrue(tree_equal(root, clone))

    def test_example2(self):
        # [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
        root = Node(1, [
            Node(2),
            Node(3, [Node(6), Node(7, [Node(11, [Node(14)])])]),
            Node(4, [Node(8, [Node(12)])]),
            Node(5, [Node(9, [Node(13)]), Node(10)]),
        ])
        clone = self.sol.cloneTree(root)
        self.assertTrue(tree_equal(root, clone))

    def test_deep_copy_independence(self):
        root = Node(1, [Node(2, [Node(3)])])
        clone = self.sol.cloneTree(root)
        orig_nodes = collect_nodes(root)
        clone_nodes = collect_nodes(clone)
        for o, c in zip(orig_nodes, clone_nodes):
            self.assertIsNot(o, c)

    def test_mutating_clone_does_not_affect_original(self):
        root = Node(1, [Node(2)])
        clone = self.sol.cloneTree(root)
        clone.children[0].val = 99
        self.assertEqual(root.children[0].val, 2)

    def test_wide_tree(self):
        children = [Node(i) for i in range(2, 102)]
        root = Node(1, children)
        clone = self.sol.cloneTree(root)
        self.assertTrue(tree_equal(root, clone))
        self.assertEqual(len(clone.children), 100)


if __name__ == '__main__':
    unittest.main()
