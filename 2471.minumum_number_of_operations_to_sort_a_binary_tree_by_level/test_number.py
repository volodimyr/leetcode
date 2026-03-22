import unittest
from number import TreeNode, Solution


def build_tree(values: list) -> TreeNode:
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


class TestMinimumOperations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        root = build_tree([1, 4, 3, 7, 6, 8, 5, None, None, None, None, 9, None, 10])
        self.assertEqual(self.solution.minimumOperations(root), 3)

    def test_example2(self):
        root = build_tree([1, 3, 2, 7, 6, 5, 4])
        self.assertEqual(self.solution.minimumOperations(root), 3)

    def test_example3_already_sorted(self):
        root = build_tree([1, 2, 3, 4, 5, 6])
        self.assertEqual(self.solution.minimumOperations(root), 0)

    def test_single_node(self):
        root = build_tree([1])
        self.assertEqual(self.solution.minimumOperations(root), 0)

    def test_none_root(self):
        self.assertEqual(self.solution.minimumOperations(None), 0)

    def test_two_levels_sorted(self):
        root = build_tree([1, 2, 3])
        self.assertEqual(self.solution.minimumOperations(root), 0)

    def test_two_levels_unsorted(self):
        root = build_tree([1, 3, 2])
        self.assertEqual(self.solution.minimumOperations(root), 1)

    def test_only_left_children(self):
        root = build_tree([1, 2, None, 3])
        self.assertEqual(self.solution.minimumOperations(root), 0)


if __name__ == "__main__":
    unittest.main()
