import unittest
from delete import Solution, ListNode


def build_list(values):
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class TestModifiedList(unittest.TestCase):

    def test_example_1(self):
        nums = [1, 2, 3]
        head = build_list([1, 2, 3, 4, 5])

        result = Solution().modifiedList(nums, head)

        self.assertEqual(list_to_array(result), [4, 5])

    def test_example_2(self):
        nums = [1]
        head = build_list([1, 2, 1, 2, 1, 2])

        result = Solution().modifiedList(nums, head)

        self.assertEqual(list_to_array(result), [2, 2, 2])

    def test_example_3(self):
        nums = [5]
        head = build_list([1, 2, 3, 4])

        result = Solution().modifiedList(nums, head)

        self.assertEqual(list_to_array(result), [1, 2, 3, 4])

    def test_remove_multiple_heads(self):
        nums = [1]
        head = build_list([1, 1, 1, 2, 3])

        result = Solution().modifiedList(nums, head)

        self.assertEqual(list_to_array(result), [2, 3])

    def test_single_node(self):
        nums = [2]
        head = build_list([1])

        result = Solution().modifiedList(nums, head)

        self.assertEqual(list_to_array(result), [1])


if __name__ == "__main__":
    unittest.main()