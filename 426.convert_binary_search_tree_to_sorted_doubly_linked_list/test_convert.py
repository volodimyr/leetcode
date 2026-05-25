from typing import Optional, List
import unittest

from convert import Solution
from convert import Node


class TestTreeToDoublyList(unittest.TestCase):

    def build_bst(self, values: List[Optional[int]]) -> Optional[Node]:
        if not values or values[0] is None:
            return None

        root = Node(values[0])
        queue = [root]
        i = 1

        while queue and i < len(values):
            node = queue.pop(0)

            if i < len(values) and values[i] is not None:
                node.left = Node(values[i])
                queue.append(node.left)
            i += 1

            if i < len(values) and values[i] is not None:
                node.right = Node(values[i])
                queue.append(node.right)
            i += 1

        return root

    def dll_to_list(self, head: Optional[Node]) -> List[int]:
        if not head:
            return []
        result = [head.val]
        cur = head.right
        while cur != head:
            result.append(cur.val)
            cur = cur.right
        return result

    def test_example1(self):
        """Test Example 1: BST [4,2,5,1,3] -> [1,2,3,4,5]"""
        sol = Solution()
        root = self.build_bst([4, 2, 5, 1, 3])
        head = sol.treeToDoublyList(root)
        self.assertEqual(self.dll_to_list(head), [1, 2, 3, 4, 5])

    def test_example2(self):
        """Test Example 2: BST [2,1,3] -> [1,2,3]"""
        sol = Solution()
        root = self.build_bst([2, 1, 3])
        head = sol.treeToDoublyList(root)
        self.assertEqual(self.dll_to_list(head), [1, 2, 3])

    def test_empty(self):
        """Test empty tree returns None"""
        sol = Solution()
        self.assertIsNone(sol.treeToDoublyList(None))

    def test_single_node(self):
        """Test single node forms a self-referencing circular list"""
        sol = Solution()
        root = Node(1)
        head = sol.treeToDoublyList(root)
        self.assertEqual(head.val, 1)
        self.assertIs(head.left, head)
        self.assertIs(head.right, head)

    def test_circular_forward(self):
        """Test that traversing right from last node wraps to first"""
        sol = Solution()
        root = self.build_bst([2, 1, 3])
        head = sol.treeToDoublyList(root)
        # head should be node with val=1
        self.assertEqual(head.val, 1)
        # traverse forward: 1 -> 2 -> 3 -> back to 1
        self.assertEqual(head.right.val, 2)
        self.assertEqual(head.right.right.val, 3)
        self.assertIs(head.right.right.right, head)

    def test_circular_backward(self):
        """Test that traversing left from first node wraps to last"""
        sol = Solution()
        root = self.build_bst([2, 1, 3])
        head = sol.treeToDoublyList(root)
        # head.left should be the last node (val=3)
        self.assertEqual(head.left.val, 3)
        self.assertIs(head.left.right, head)

    def test_left_skewed(self):
        """Test left-skewed BST (all nodes go left)"""
        sol = Solution()
        root = Node(3, Node(2, Node(1)))
        head = sol.treeToDoublyList(root)
        self.assertEqual(self.dll_to_list(head), [1, 2, 3])

    def test_right_skewed(self):
        """Test right-skewed BST (all nodes go right)"""
        sol = Solution()
        root = Node(1, None, Node(2, None, Node(3)))
        head = sol.treeToDoublyList(root)
        self.assertEqual(self.dll_to_list(head), [1, 2, 3])

    def test_negative_values(self):
        """Test BST with negative values"""
        sol = Solution()
        root = self.build_bst([0, -2, 2, -3, -1, 1, 3])
        head = sol.treeToDoublyList(root)
        self.assertEqual(self.dll_to_list(head), [-3, -2, -1, 0, 1, 2, 3])

    def test_returns_smallest(self):
        """Test that returned node is the smallest element"""
        sol = Solution()
        root = self.build_bst([4, 2, 5, 1, 3])
        head = sol.treeToDoublyList(root)
        self.assertEqual(head.val, 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
