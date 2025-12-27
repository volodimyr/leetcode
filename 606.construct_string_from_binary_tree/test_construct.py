import unittest
from construct import Solution,TreeNode

class TestTree2Str(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.tree2str(root), "1")

    def test_example_1(self):
        # Tree: [1,2,3,4]
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(4)),
            TreeNode(3)
        )
        self.assertEqual(self.solution.tree2str(root), "1(2(4))(3)")

    def test_example_2(self):
        # Tree: [1,2,3,null,4]
        root = TreeNode(
            1,
            TreeNode(2, None, TreeNode(4)),
            TreeNode(3)
        )
        self.assertEqual(self.solution.tree2str(root), "1(2()(4))(3)")

    def test_only_left_child(self):
        root = TreeNode(1, TreeNode(2))
        self.assertEqual(self.solution.tree2str(root), "1(2)")

    def test_only_right_child(self):
        root = TreeNode(1, None, TreeNode(2))
        self.assertEqual(self.solution.tree2str(root), "1()(2)")

    def test_deep_tree(self):
        root = TreeNode(
            1,
            TreeNode(
                2,
                TreeNode(
                    3,
                    TreeNode(4)
                )
            )
        )
        self.assertEqual(self.solution.tree2str(root), "1(2(3(4)))")

    def test_negative_values(self):
        root = TreeNode(
            -1,
            TreeNode(-2),
            TreeNode(-3)
        )
        self.assertEqual(self.solution.tree2str(root), "-1(-2)(-3)")

    def test_complex_structure(self):
        root = TreeNode(
            10,
            TreeNode(5, None, TreeNode(7)),
            TreeNode(15, TreeNode(12), None)
        )
        self.assertEqual(
            self.solution.tree2str(root),
            "10(5()(7))(15(12))"
        )


if __name__ == "__main__":
    unittest.main()
