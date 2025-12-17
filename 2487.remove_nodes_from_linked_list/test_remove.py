import unittest
from typing import Optional, List
from remove import Solution, ListNode

# ---------- helpers ----------
def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ---------- tests ----------
class TestRemoveNodes(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        head = build_linked_list([5, 2, 13, 3, 8])
        result = self.sol.removeNodes(head)
        self.assertEqual(linked_list_to_list(result), [13, 8])

    def test_example_2_all_equal(self):
        head = build_linked_list([1, 1, 1, 1])
        result = self.sol.removeNodes(head)
        self.assertEqual(linked_list_to_list(result), [1, 1, 1, 1])

    def test_strictly_increasing(self):
        head = build_linked_list([1, 2, 3, 4])
        result = self.sol.removeNodes(head)
        self.assertEqual(linked_list_to_list(result), [4])

    def test_strictly_decreasing(self):
        head = build_linked_list([4, 3, 2, 1])
        result = self.sol.removeNodes(head)
        self.assertEqual(linked_list_to_list(result), [4, 3, 2, 1])

    def test_single_node(self):
        head = build_linked_list([10])
        result = self.sol.removeNodes(head)
        self.assertEqual(linked_list_to_list(result), [10])

    def test_alternating_peaks(self):
        head = build_linked_list([3, 1, 4, 2, 5])
        result = self.sol.removeNodes(head)
        self.assertEqual(linked_list_to_list(result), [5])

    def test_tail_is_max(self):
        head = build_linked_list([2, 2, 1, 3])
        result = self.sol.removeNodes(head)
        self.assertEqual(linked_list_to_list(result), [3])

    def test_large_values(self):
        head = build_linked_list([100000, 1, 99999])
        result = self.sol.removeNodes(head)
        self.assertEqual(linked_list_to_list(result), [100000, 99999])


if __name__ == "__main__":
    unittest.main()
