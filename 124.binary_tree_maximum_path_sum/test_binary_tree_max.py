import unittest
from binary_tree_max import Solution


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TestBinaryTreeMaximumPathSum(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        # [1,2,3]
        root = TreeNode(1,
                        TreeNode(2),
                        TreeNode(3))
        self.assertEqual(self.sol.maxPathSum(root), 6)

    def test_example_2(self):
        # [-10,9,20,null,null,15,7]
        root = TreeNode(-10,
                        TreeNode(9),
                        TreeNode(20,
                                 TreeNode(15),
                                 TreeNode(7)))
        self.assertEqual(self.sol.maxPathSum(root), 42)

    def test_single_node(self):
        root = TreeNode(5)
        self.assertEqual(self.sol.maxPathSum(root), 5)

    def test_all_negative(self):
        #      -3
        #     /  \
        #   -2   -1
        root = TreeNode(-3,
                        TreeNode(-2),
                        TreeNode(-1))
        self.assertEqual(self.sol.maxPathSum(root), -1)

    def test_mixed_values(self):
        #        5
        #       / \
        #      4   8
        #         / \
        #        11  4
        #       /
        #      7
        root = TreeNode(5,
                        TreeNode(4),
                        TreeNode(8,
                                 TreeNode(11,
                                          TreeNode(7)),
                                 TreeNode(4)))
        # Best path: 7 -> 11 -> 8 -> 4 = 30
        self.assertEqual(self.sol.maxPathSum(root), 35)

    def test_left_skewed(self):
        # 1 -> 2 -> 3 -> 4
        root = TreeNode(1,
                        TreeNode(2,
                                 TreeNode(3,
                                          TreeNode(4))))
        self.assertEqual(self.sol.maxPathSum(root), 10)

    def test_right_skewed_with_negative(self):
        # 1 -> -2 -> 3 -> 4
        root = TreeNode(1,
                        None,
                        TreeNode(-2,
                                 None,
                                 TreeNode(3,
                                          None,
                                          TreeNode(4))))
        # Best path: 3 -> 4 = 7
        self.assertEqual(self.sol.maxPathSum(root), 7)


if __name__ == "__main__":
    unittest.main()