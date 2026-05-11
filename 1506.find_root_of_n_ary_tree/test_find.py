import unittest
from find import Node, Solution


def build_tree(vals):
    """Build N-ary tree from level-order list with None as group separator."""
    if not vals:
        return [], None
    root = Node(vals[0])
    nodes = {vals[0]: root}
    queue = [root]
    i = 2  # skip root and first null
    while queue and i < len(vals):
        parent = queue.pop(0)
        while i < len(vals) and vals[i] is not None:
            child = Node(vals[i])
            nodes[vals[i]] = child
            parent.children.append(child)
            queue.append(child)
            i += 1
        i += 1  # skip the null separator
    return list(nodes.values()), root


class TestFindRoot(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        # tree = [1,null,3,2,4,null,5,6]
        all_nodes, expected_root = build_tree([1, None, 3, 2, 4, None, 5, 6])
        result = self.sol.findRoot(all_nodes)
        self.assertEqual(result.val, expected_root.val)

    def test_example2(self):
        # tree = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
        serialized = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14]
        all_nodes, expected_root = build_tree(serialized)
        result = self.sol.findRoot(all_nodes)
        self.assertEqual(result.val, expected_root.val)

    def test_single_node(self):
        node = Node(42)
        result = self.sol.findRoot([node])
        self.assertEqual(result.val, 42)

    def test_root_is_in_shuffled_array(self):
        # Verify result is correct regardless of input order
        all_nodes, expected_root = build_tree([1, None, 3, 2, 4, None, 5, 6])
        shuffled = list(reversed(all_nodes))
        result = self.sol.findRoot(shuffled)
        self.assertEqual(result.val, expected_root.val)


if __name__ == '__main__':
    unittest.main()
