import unittest
from robber import Solution, TreeNode


def build_tree(values):
    """
    Build a binary tree from a level-order list.
    None represents a missing node.
    """
    if not values:
        return None

    nodes = [None if v is None else TreeNode(v) for v in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


class TestHouseRobberIII(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        root = build_tree([3, 2, 3, None, 3, None, 1])
        self.assertEqual(self.sol.rob(root), 7)

    def test_example_2(self):
        root = build_tree([3, 4, 5, 1, 3, None, 1])
        self.assertEqual(self.sol.rob(root), 9)

    def test_single_node(self):
        root = TreeNode(5)
        self.assertEqual(self.sol.rob(root), 5)

    def test_all_zeros(self):
        root = build_tree([0, 0, 0, 0, 0])
        self.assertEqual(self.sol.rob(root), 0)

    def test_linear_tree(self):
        # 3 -> 2 -> 3 -> 1
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(1)
        self.assertEqual(self.sol.rob(root), 6)  # 3 + 3

    def test_skip_root_better(self):
        #      10
        #     /  \
        #    1    1
        #   / \  / \
        #  10 10 10 10
        root = build_tree([10, 1, 1, 10, 10, 10, 10])
        self.assertEqual(self.sol.rob(root), 50)

    def test_large_values(self):
        root = build_tree([10000, 10000, 10000])
        self.assertEqual(self.sol.rob(root), 20000)


if __name__ == "__main__":
    unittest.main()
