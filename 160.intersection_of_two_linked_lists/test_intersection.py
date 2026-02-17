import unittest
from intersection import Solution
from intersection import ListNode


def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for v in values[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


class TestIntersectionOfTwoLinkedLists(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_intersection_middle(self):
        # Common part
        common = build_list([8, 4, 5])

        # List A: 4 -> 1 -> 8 -> 4 -> 5
        headA = build_list([4, 1])
        tail = headA
        while tail.next:
            tail = tail.next
        tail.next = common

        # List B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
        headB = build_list([5, 6, 1])
        tail = headB
        while tail.next:
            tail = tail.next
        tail.next = common

        result = self.solution.getIntersectionNode(headA, headB)
        self.assertIs(result, common)

    def test_intersection_at_head(self):
        head = build_list([1, 2, 3])

        result = self.solution.getIntersectionNode(head, head)
        self.assertIs(result, head)

    def test_no_intersection(self):
        headA = build_list([2, 6, 4])
        headB = build_list([1, 5])

        result = self.solution.getIntersectionNode(headA, headB)
        self.assertIsNone(result)

    def test_single_node_intersection(self):
        node = ListNode(1)

        result = self.solution.getIntersectionNode(node, node)
        self.assertIs(result, node)

    def test_single_node_no_intersection(self):
        headA = ListNode(1)
        headB = ListNode(1)

        result = self.solution.getIntersectionNode(headA, headB)
        self.assertIsNone(result)

    def test_different_lengths_intersection(self):
        common = build_list([7, 8])

        headA = build_list([1, 2, 3, 4])
        tail = headA
        while tail.next:
            tail = tail.next
        tail.next = common

        headB = build_list([5])
        headB.next = common

        result = self.solution.getIntersectionNode(headA, headB)
        self.assertIs(result, common)


if __name__ == "__main__":
    unittest.main()
