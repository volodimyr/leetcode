import unittest
from sum_leaf import Solution, TreeNode


class TestSumRootToLeafNumbers(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_single_node(self):
        root = TreeNode(5)
        self.assertEqual(self.solution.sumNumbers(root), 5)

    def test_example_1(self):
        # Tree: [1,2,3]
        #      1
        #     / \
        #    2   3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        self.assertEqual(self.solution.sumNumbers(root), 25)

    def test_example_2(self):
        # Tree: [4,9,0,5,1]
        #         4
        #        / \
        #       9   0
        #      / \
        #     5   1
        root = TreeNode(4)
        root.left = TreeNode(9)
        root.right = TreeNode(0)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(1)

        self.assertEqual(self.solution.sumNumbers(root), 1026)

    def test_left_skewed_tree(self):
        # 1 -> 2 -> 3 -> 4
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)

        # Number = 1234
        self.assertEqual(self.solution.sumNumbers(root), 1234)

    def test_right_skewed_tree(self):
        # 1 -> 2 -> 3 -> 4 (right only)
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)

        # Number = 1234
        self.assertEqual(self.solution.sumNumbers(root), 1234)

    def test_tree_with_zeroes(self):
        #       0
        #      / \
        #     1   0
        #        /
        #       5
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.right = TreeNode(0)
        root.right.left = TreeNode(5)

        # Paths:
        # 0->1 = 1
        # 0->0->5 = 5
        # Total = 6
        self.assertEqual(self.solution.sumNumbers(root), 6)

    def test_complex_tree(self):
        #         2
        #        / \
        #       3   1
        #      /   / \
        #     4   5   6
        root = TreeNode(2)
        root.left = TreeNode(3)
        root.right = TreeNode(1)
        root.left.left = TreeNode(4)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(6)

        # Paths:
        # 2->3->4 = 234
        # 2->1->5 = 215
        # 2->1->6 = 216
        # Total = 665
        self.assertEqual(self.solution.sumNumbers(root), 665)


if __name__ == "__main__":
    unittest.main()
