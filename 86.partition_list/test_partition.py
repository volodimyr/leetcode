import unittest

from partition import ListNode, Solution


def to_list(head: ListNode) -> list:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def to_linked(vals: list) -> ListNode:
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


sol = Solution()


def test_example1():
    assert to_list(sol.partition(to_linked([1, 4, 3, 2, 5, 2]), 3)) == [1, 2, 2, 4, 3, 5]

def test_example2():
    assert to_list(sol.partition(to_linked([2, 1]), 2)) == [1, 2]

def test_empty():
    assert sol.partition(None, 0) is None

def test_single_less():
    assert to_list(sol.partition(to_linked([1]), 3)) == [1]

def test_single_greater():
    assert to_list(sol.partition(to_linked([5]), 3)) == [5]

def test_all_less():
    assert to_list(sol.partition(to_linked([1, 2, 3]), 5)) == [1, 2, 3]

def test_all_greater_or_equal():
    assert to_list(sol.partition(to_linked([5, 6, 7]), 3)) == [5, 6, 7]

def test_equal_to_x_goes_to_bigger():
    assert to_list(sol.partition(to_linked([3, 1]), 3)) == [1, 3]

def test_preserves_relative_order():
    assert to_list(sol.partition(to_linked([1, 4, 3, 2, 5, 2]), 3)) == [1, 2, 2, 4, 3, 5]

def test_negatives():
    assert to_list(sol.partition(to_linked([-1, -3, 0, 2]), 0)) == [-1, -3, 0, 2]

def test_x_below_all():
    assert to_list(sol.partition(to_linked([3, 4, 5]), -10)) == [3, 4, 5]

def test_x_above_all():
    assert to_list(sol.partition(to_linked([1, 2, 3]), 200)) == [1, 2, 3]


if __name__ == "__main__":
    unittest.main()
