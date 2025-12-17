import unittest
from typing import Optional, List
from swap import ListNode, Solution

# ---------- Helpers ----------
def build_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    cur = head
    while cur:
        result.append(cur.val)
        cur = cur.next
    return result


# ---------- Tests ----------
class TestSwapPairs(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        head = build_linked_list([])
        result = self.solution.swapPairs(head)
        self.assertEqual(linked_list_to_list(result), [])

    def test_single_node(self):
        head = build_linked_list([1])
        result = self.solution.swapPairs(head)
        self.assertEqual(linked_list_to_list(result), [1])

    def test_even_number_of_nodes(self):
        head = build_linked_list([1, 2, 3, 4])
        result = self.solution.swapPairs(head)
        self.assertEqual(linked_list_to_list(result), [2, 1, 4, 3])

    def test_odd_number_of_nodes(self):
        head = build_linked_list([1, 2, 3])
        result = self.solution.swapPairs(head)
        self.assertEqual(linked_list_to_list(result), [2, 1, 3])

    def test_two_nodes(self):
        head = build_linked_list([10, 20])
        result = self.solution.swapPairs(head)
        self.assertEqual(linked_list_to_list(result), [20, 10])

    def test_longer_list(self):
        head = build_linked_list([1, 2, 3, 4, 5, 6])
        result = self.solution.swapPairs(head)
        self.assertEqual(linked_list_to_list(result), [2, 1, 4, 3, 6, 5])


if __name__ == "__main__":
    unittest.main()
