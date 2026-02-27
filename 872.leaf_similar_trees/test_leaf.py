import unittest
from leaf import Solution, TreeNode


def build_tree(values):
    """
    Build binary tree from level-order list representation.
    Example: [3,5,1,6,2,9,8,None,None,7,4]
    """
    if not values:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root


class TestLeafSimilar(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root1 = build_tree([3,5,1,6,2,9,8,None,None,7,4])
        root2 = build_tree([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
        self.assertTrue(self.solution.leafSimilar(root1, root2))

    def test_example_2(self):
        root1 = build_tree([1,2,3])
        root2 = build_tree([1,3,2])
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    def test_single_node_same(self):
        root1 = build_tree([1])
        root2 = build_tree([1])
        self.assertTrue(self.solution.leafSimilar(root1, root2))

    def test_single_node_different(self):
        root1 = build_tree([1])
        root2 = build_tree([2])
        self.assertFalse(self.solution.leafSimilar(root1, root2))

    def test_different_number_of_leaves(self):
        root1 = build_tree([1,2])
        root2 = build_tree([1,None,2])
        self.assertTrue(self.solution.leafSimilar(root1, root2))


if __name__ == "__main__":
    unittest.main()