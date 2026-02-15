import unittest
from closest import Solution, TreeNode


class TestClosestValue(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def build_tree(self, values):
        """
        Build tree from level-order list (LeetCode style).
        None represents missing nodes.
        """
        if not values:
            return None

        nodes = [TreeNode(v) if v is not None else None for v in values]
        kids = nodes[::-1]
        root = kids.pop()

        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root

    def test_example_1(self):
        root = self.build_tree([4, 2, 5, 1, 3])
        self.assertEqual(self.sol.closestValue(root, 3.714286), 4)

    def test_example_2(self):
        root = self.build_tree([1])
        self.assertEqual(self.sol.closestValue(root, 4.428571), 1)

    def test_exact_match(self):
        root = self.build_tree([4, 2, 5, 1, 3])
        self.assertEqual(self.sol.closestValue(root, 3.0), 3)

    def test_target_smaller_than_all(self):
        root = self.build_tree([4, 2, 5, 1, 3])
        self.assertEqual(self.sol.closestValue(root, -10), 1)

    def test_target_larger_than_all(self):
        root = self.build_tree([4, 2, 5, 1, 3])
        self.assertEqual(self.sol.closestValue(root, 100), 5)

    def test_negative_target(self):
        root = self.build_tree([10, 5, 15, 2, 7])
        self.assertEqual(self.sol.closestValue(root, -3.5), 2)

    def test_closest_is_left_subtree(self):
        root = self.build_tree([10, 5, 15, 2, 7])
        self.assertEqual(self.sol.closestValue(root, 6.1), 7)

    def test_closest_is_right_subtree(self):
        root = self.build_tree([10, 5, 15, 2, 7])
        self.assertEqual(self.sol.closestValue(root, 14.9), 15)


if __name__ == "__main__":
    unittest.main()
