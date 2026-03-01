import unittest
from rotate import Solution, ListNode


def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head


def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class TestRotateRight(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        head = None
        result = self.solution.rotateRight(head, 5)
        self.assertIsNone(result)

    def test_single_node(self):
        head = build_linked_list([1])
        result = self.solution.rotateRight(head, 10)
        self.assertEqual(linked_list_to_list(result), [1])

    def test_k_zero(self):
        head = build_linked_list([1, 2, 3])
        result = self.solution.rotateRight(head, 0)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3])

    def test_example_1(self):
        head = build_linked_list([1, 2, 3, 4, 5])
        result = self.solution.rotateRight(head, 2)
        self.assertEqual(linked_list_to_list(result), [4, 5, 1, 2, 3])

    def test_example_2(self):
        head = build_linked_list([0, 1, 2])
        result = self.solution.rotateRight(head, 4)
        self.assertEqual(linked_list_to_list(result), [2, 0, 1])

    def test_k_multiple_of_length(self):
        head = build_linked_list([1, 2, 3, 4])
        result = self.solution.rotateRight(head, 8)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 4])

if __name__ == "__main__":
    unittest.main()