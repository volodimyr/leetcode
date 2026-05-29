from typing import List, Optional
import unittest

from insert import Solution, Node


def build_circular(values: List[int]) -> Optional[Node]:
    if not values:
        return None
    head = Node(values[0])
    cur = head
    for v in values[1:]:
        cur.next = Node(v)
        cur = cur.next
    cur.next = head
    return head


def to_list(head: Node, start_val: int = None) -> List[int]:
    """Collect values starting from head, stopping after one full cycle."""
    if not head:
        return []
    result = []
    cur = head
    while True:
        result.append(cur.val)
        cur = cur.next
        if cur == head:
            break
    return result


class TestInsert(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        head = build_circular([3, 4, 1])
        result = self.sol.insert(head, 2)
        values = to_list(result)
        self.assertIn(2, values)
        self.assertEqual(sorted(values), sorted([3, 4, 1, 2]))

    def test_example2_empty_list(self):
        result = self.sol.insert(None, 1)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next, result)

    def test_example3_single_node(self):
        head = build_circular([1])
        result = self.sol.insert(head, 0)
        values = to_list(result)
        self.assertEqual(sorted(values), [0, 1])

    def test_insert_at_wrap_smaller_than_min(self):
        head = build_circular([3, 4, 1])
        result = self.sol.insert(head, 0)
        values = to_list(result)
        self.assertIn(0, values)
        self.assertEqual(sorted(values), [0, 1, 3, 4])

    def test_insert_at_wrap_larger_than_max(self):
        head = build_circular([3, 4, 1])
        result = self.sol.insert(head, 5)
        values = to_list(result)
        self.assertIn(5, values)
        self.assertEqual(sorted(values), [1, 3, 4, 5])

    def test_insert_between_existing_values(self):
        head = build_circular([1, 3, 5])
        result = self.sol.insert(head, 4)
        values = to_list(result)
        self.assertIn(4, values)
        self.assertEqual(sorted(values), [1, 3, 4, 5])

    def test_insert_duplicate_value(self):
        head = build_circular([1, 3, 5])
        result = self.sol.insert(head, 3)
        values = to_list(result)
        self.assertEqual(sorted(values), [1, 3, 3, 5])

    def test_all_same_values(self):
        head = build_circular([3, 3, 3])
        result = self.sol.insert(head, 3)
        values = to_list(result)
        self.assertEqual(values, [3, 3, 3, 3])

    def test_insert_equal_to_min(self):
        head = build_circular([3, 4, 1])
        result = self.sol.insert(head, 1)
        values = to_list(result)
        self.assertEqual(sorted(values), [1, 1, 3, 4])

    def test_insert_equal_to_max(self):
        head = build_circular([3, 4, 1])
        result = self.sol.insert(head, 4)
        values = to_list(result)
        self.assertEqual(sorted(values), [1, 3, 4, 4])

    def test_returns_original_head(self):
        head = build_circular([1, 2, 3])
        result = self.sol.insert(head, 4)
        self.assertIs(result, head)


if __name__ == '__main__':
    unittest.main(verbosity=2)
