import unittest
import io
import contextlib
from print_reverse import Solution


class ImmutableListNode:
    def __init__(self, val: int, next_node: 'ImmutableListNode' = None):
        self._val = val
        self._next = next_node

    def printValue(self) -> None:
        print(self._val)

    def getNext(self) -> 'ImmutableListNode':
        return self._next


def build_immutable_list(vals: list) -> ImmutableListNode:
    if not vals:
        return None
    head = ImmutableListNode(vals[0])
    cur = head
    for v in vals[1:]:
        node = ImmutableListNode(v)
        cur._next = node
        cur = node
    return head


def capture_print(s: Solution, head: ImmutableListNode) -> list:
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        s.printLinkedListInReverse(head)
    return [int(x) for x in buf.getvalue().strip().split('\n') if x]


class TestPrintLinkedListInReverse(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_example1(self):
        head = build_immutable_list([-2, 0, 6, 4, 4, -6])
        self.assertEqual(capture_print(self.s, head), [-6, 4, 4, 6, 0, -2])

    def test_example2(self):
        head = build_immutable_list([0, 10, 4, 5])
        self.assertEqual(capture_print(self.s, head), [5, 4, 10, 0])

    def test_single_element(self):
        head = build_immutable_list([42])
        self.assertEqual(capture_print(self.s, head), [42])

    def test_two_elements(self):
        head = build_immutable_list([1, 2])
        self.assertEqual(capture_print(self.s, head), [2, 1])

    def test_negative_values(self):
        head = build_immutable_list([-1, -2, -3])
        self.assertEqual(capture_print(self.s, head), [-3, -2, -1])

    def test_all_same(self):
        head = build_immutable_list([5, 5, 5, 5])
        self.assertEqual(capture_print(self.s, head), [5, 5, 5, 5])

    def test_boundary_values(self):
        head = build_immutable_list([-1000, 0, 1000])
        self.assertEqual(capture_print(self.s, head), [1000, 0, -1000])

    def test_already_reversed(self):
        head = build_immutable_list([3, 2, 1])
        self.assertEqual(capture_print(self.s, head), [1, 2, 3])

    def test_long_list(self):
        vals = list(range(1, 101))
        head = build_immutable_list(vals)
        self.assertEqual(capture_print(self.s, head), list(range(100, 0, -1)))


if __name__ == "__main__":
    unittest.main()
