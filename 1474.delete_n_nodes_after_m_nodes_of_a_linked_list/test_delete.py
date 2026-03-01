import unittest
from delete import Solution, ListNode


def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class TestDeleteNodes(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = build_linked_list(
            [1,2,3,4,5,6,7,8,9,10,11,12,13]
        )
        result = self.solution.deleteNodes(head, 2, 3)
        self.assertEqual(
            linked_list_to_list(result),
            [1,2,6,7,11,12]
        )

    def test_example_2(self):
        head = build_linked_list(
            [1,2,3,4,5,6,7,8,9,10,11]
        )
        result = self.solution.deleteNodes(head, 1, 3)
        self.assertEqual(
            linked_list_to_list(result),
            [1,5,9]
        )

    def test_keep_all(self):
        head = build_linked_list([1,2,3,4])
        result = self.solution.deleteNodes(head, 10, 1)
        self.assertEqual(
            linked_list_to_list(result),
            [1,2,3,4]
        )

    def test_delete_all_after_first(self):
        head = build_linked_list([1,2,3,4,5])
        result = self.solution.deleteNodes(head, 1, 10)
        self.assertEqual(
            linked_list_to_list(result),
            [1]
        )

    def test_single_node(self):
        head = build_linked_list([1])
        result = self.solution.deleteNodes(head, 1, 1)
        self.assertEqual(
            linked_list_to_list(result),
            [1]
        )

    def test_exact_multiple_pattern(self):
        head = build_linked_list([1,2,3,4,5,6])
        result = self.solution.deleteNodes(head, 2, 2)
        self.assertEqual(
            linked_list_to_list(result),
            [1,2,5,6]
        )

    def test_m_equals_1_n_equals_1(self):
        head = build_linked_list([1,2,3,4,5])
        result = self.solution.deleteNodes(head, 1, 1)
        self.assertEqual(
            linked_list_to_list(result),
            [1,3,5]
        )

    def test_large_n_tail_cut(self):
        head = build_linked_list([1,2,3,4,5,6,7])
        result = self.solution.deleteNodes(head, 3, 100)
        self.assertEqual(
            linked_list_to_list(result),
            [1,2,3]
        )


if __name__ == "__main__":
    unittest.main()