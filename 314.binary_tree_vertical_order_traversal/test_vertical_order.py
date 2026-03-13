import unittest

from vertical_order import Solution, TreeNode


def build_tree(vals):
    if not vals:
        return None
    root = TreeNode(vals[0])
    q = [root]
    i = 1
    while q and i < len(vals):
        node = q.pop(0)
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            q.append(node.right)
        i += 1
    return root


class TestVerticalOrder(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        # [3,9,20,null,null,15,7]
        root = build_tree([3, 9, 20, None, None, 15, 7])
        self.assertEqual(self.s.verticalOrder(root), [[9], [3, 15], [20], [7]])

    def test_example2(self):
        # [3,9,8,4,0,1,7]
        root = build_tree([3, 9, 8, 4, 0, 1, 7])
        self.assertEqual(self.s.verticalOrder(root), [[4], [9], [3, 0, 1], [8], [7]])

    def test_example3(self):
        # [3,9,8,4,0,1,7,null,null,null,2,5]
        root = build_tree([3, 9, 8, 4, 0, 1, 7, None, None, None, 2, 5])
        self.assertEqual(self.s.verticalOrder(root), [[4], [9, 5], [3, 0, 1], [8, 2], [7]])

    def test_null_root(self):
        self.assertEqual(self.s.verticalOrder(None), [])

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.s.verticalOrder(root), [[1]])

    def test_left_only(self):
        root = build_tree([1, 2, None, 3])
        self.assertEqual(self.s.verticalOrder(root), [[3], [2], [1]])

    def test_right_only(self):
        root = build_tree([1, None, 2, None, 3])
        self.assertEqual(self.s.verticalOrder(root), [[1], [2], [3]])

    def test_two_nodes_left(self):
        root = TreeNode(1, TreeNode(2))
        self.assertEqual(self.s.verticalOrder(root), [[2], [1]])

    def test_two_nodes_right(self):
        root = TreeNode(1, None, TreeNode(2))
        self.assertEqual(self.s.verticalOrder(root), [[1], [2]])


if __name__ == "__main__":
    unittest.main()
