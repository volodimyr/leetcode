import unittest
from range_sum import NumArray


class TestNumArray(unittest.TestCase):

    def test_example_from_prompt(self):
        numArray = NumArray([1, 3, 5])
        self.assertEqual(numArray.sumRange(0, 2), 9)
        numArray.update(1, 2)
        self.assertEqual(numArray.sumRange(0, 2), 8)

    def test_single_element(self):
        numArray = NumArray([10])
        self.assertEqual(numArray.sumRange(0, 0), 10)
        numArray.update(0, -5)
        self.assertEqual(numArray.sumRange(0, 0), -5)

    def test_full_range_query(self):
        nums = [1, 2, 3, 4, 5]
        numArray = NumArray(nums)
        self.assertEqual(numArray.sumRange(0, 4), sum(nums))

    def test_partial_range_query(self):
        nums = [2, 4, 6, 8, 10]
        numArray = NumArray(nums)
        self.assertEqual(numArray.sumRange(1, 3), 4 + 6 + 8)

    def test_update_first_element(self):
        numArray = NumArray([1, 2, 3])
        numArray.update(0, 10)
        self.assertEqual(numArray.sumRange(0, 2), 15)

    def test_update_last_element(self):
        numArray = NumArray([1, 2, 3])
        numArray.update(2, 10)
        self.assertEqual(numArray.sumRange(0, 2), 13)

    def test_multiple_updates(self):
        numArray = NumArray([5, 5, 5, 5])
        numArray.update(1, 1)
        numArray.update(2, 2)
        numArray.update(3, 3)
        self.assertEqual(numArray.sumRange(0, 3), 5 + 1 + 2 + 3)

    def test_negative_numbers(self):
        numArray = NumArray([-1, -2, -3])
        self.assertEqual(numArray.sumRange(0, 2), -6)
        numArray.update(1, 5)
        self.assertEqual(numArray.sumRange(0, 2), 1)

    def test_query_single_index(self):
        numArray = NumArray([7, 8, 9])
        self.assertEqual(numArray.sumRange(1, 1), 8)


if __name__ == "__main__":
    unittest.main()
