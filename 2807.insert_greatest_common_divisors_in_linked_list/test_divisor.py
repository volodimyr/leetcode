import unittest
from divisor import Solution, ListNode


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
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


class TestInsertGreatestCommonDivisors(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        head = build_linked_list([18, 6, 10, 3])
        result = self.sol.insertGreatestCommonDivisors(head)
        self.assertEqual(
            linked_list_to_list(result),
            [18, 6, 6, 2, 10, 1, 3]
        )

    def test_single_node(self):
        head = build_linked_list([7])
        result = self.sol.insertGreatestCommonDivisors(head)
        self.assertEqual(
            linked_list_to_list(result),
            [7]
        )

    def test_two_nodes(self):
        head = build_linked_list([12, 8])
        result = self.sol.insertGreatestCommonDivisors(head)
        self.assertEqual(
            linked_list_to_list(result),
            [12, 4, 8]
        )

    def test_all_ones(self):
        head = build_linked_list([1, 1, 1])
        result = self.sol.insertGreatestCommonDivisors(head)
        self.assertEqual(
            linked_list_to_list(result),
            [1, 1, 1, 1, 1]
        )

    def test_prime_numbers(self):
        head = build_linked_list([7, 11, 13])
        result = self.sol.insertGreatestCommonDivisors(head)
        self.assertEqual(
            linked_list_to_list(result),
            [7, 1, 11, 1, 13]
        )


if __name__ == "__main__":
    unittest.main()
